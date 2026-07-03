#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
서울·경기 지역의 분양정보를 매일 텔레그램으로 보냅니다.
  - APT (공공분양 + 민간분양)
  - 오피스텔 / 도시형생활주택 / 민간임대 / 생활숙박시설
  - APT 무순위·잔여세대
  - 공공지원 민간임대
  - 임의공급

데이터 출처: 한국부동산원_청약홈 분양정보 조회 서비스 (공공데이터포털 #15098547)
https://www.data.go.kr/data/15098547/openapi.do

동작 방식:
  1) 청약홈 API의 주택유형별 엔드포인트에서 서울·경기 분양정보를 모두 가져옵니다.
  2) 청약접수가 아직 끝나지 않은(접수종료일이 오늘 이후이거나 비어있는) 공고만 추립니다.
  3) 그중 한 번도 보낸 적 없는(state/notified.json에 없는) 공고만 텔레그램으로 보냅니다.
  4) 보낸 공고는 state/notified.json에 기록합니다.
     (GitHub Actions 워크플로우가 이 파일을 커밋해 다음 실행으로 이어집니다.)

필요한 환경 변수:
  APPLYHOME_API_KEY   공공데이터포털에서 발급받은 서비스키
  TELEGRAM_BOT_TOKEN
  TELEGRAM_CHAT_ID

미리보기 (전송/상태변경 없이 현재 진행중인 공고 전체를 출력, 텔레그램 키 불필요):
  APPLYHOME_API_KEY=내키 python3 send_presale.py --preview
"""

import json
import os
import sys
import time
from datetime import date, timedelta

from applyhome_api import (
    detail_url,
    fetch_seoul_gyeonggi,
    group_label,
    house_type,
    listing_key,
    rcept_dates,
)
from telegram_utils import escape_html, send_message

STATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state", "notified.json")
STATE_TTL_DAYS = 180  # 상태 파일이 무한정 커지지 않도록 오래된 기록은 정리합니다.
TELEGRAM_LIMIT = 3500  # 텔레그램 메시지 최대 길이(4096) 대비 여유를 둔 값.

# 메시지 그룹 표시 순서와 아이콘.
GROUP_ORDER = [
    ("공공분양", "🏛"),
    ("민간분양", "🏙"),
    ("오피스텔·도시형·민간임대·생활숙박", "🏬"),
    ("APT 무순위·잔여세대", "🎯"),
    ("공공지원 민간임대", "🏘"),
    ("임의공급", "📦"),
]


def load_state():
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


def prune_state(state, today):
    cutoff = (today - timedelta(days=STATE_TTL_DAYS)).isoformat()
    for key in list(state.keys()):
        if state[key] < cutoff:
            del state[key]


def is_active(row, today_str):
    """청약접수 종료일이 지나지 않았으면(또는 비어있으면) 진행중/예정 공고로 봅니다."""
    _, end = rcept_dates(row)
    end = end.strip().replace(".", "-").replace("/", "-")
    return (not end) or end[:10] >= today_str


def format_entry(row):
    name = escape_html(row.get("HOUSE_NM") or "(단지명 미상)")
    area = escape_html(row.get("SUBSCRPT_AREA_CODE_NM") or "-")
    addr = escape_html(row.get("HSSPLY_ADRES") or "-")
    detail_type = escape_html(house_type(row))
    scale = escape_html(row.get("TOT_SUPLY_HSHLDCO") or "-")
    builder = escape_html(row.get("BSNS_MBY_NM") or "-")
    announce = escape_html(row.get("RCRIT_PBLANC_DE") or "-")
    begin, end = rcept_dates(row)
    tel = escape_html(row.get("MDHS_TELNO") or "-")
    url = detail_url(row)

    lines = [
        "🏢 <b>{0}</b>  [{1}]".format(name, detail_type),
        "📍 {0} ({1})".format(area, addr),
        "🏗 공급규모: {0}세대/실  ·  사업주체: {1}".format(scale, builder),
        "📢 모집공고일: {0}".format(announce),
        "🗓 청약접수: {0} ~ {1}".format(escape_html(begin or "-"), escape_html(end or "-")),
        "☎️ 문의처: {0}".format(tel),
        '🔗 <a href="{0}">청약홈에서 자세히 보기</a>'.format(url),
    ]
    return "\n".join(lines)


def chunk_messages(header, entries):
    """
    텔레그램 길이 제한을 넘기지 않도록 항목들을 여러 메시지로 나눕니다.
    entries는 (본문, row) 쌍의 목록이며, (메시지, [포함된 row들]) 쌍의 목록을 반환합니다.
    """
    chunks = []
    current = [header]
    current_rows = []
    current_len = len(header)
    for entry, row in entries:
        entry_len = len(entry) + 2
        if current_len + entry_len > TELEGRAM_LIMIT and len(current) > 1:
            chunks.append(("\n\n".join(current), current_rows))
            current = [header]
            current_rows = []
            current_len = len(header)
        current.append(entry)
        current_rows.append(row)
        current_len += entry_len
    if len(current) > 1:
        chunks.append(("\n\n".join(current), current_rows))
    return chunks


def main():
    args = sys.argv[1:]
    preview = "--preview" in args

    api_key = os.environ.get("APPLYHOME_API_KEY")
    if not api_key:
        sys.stderr.write("오류: APPLYHOME_API_KEY 환경 변수가 필요합니다.\n")
        return 1

    today = date.today()
    today_str = today.isoformat()

    try:
        rows = fetch_seoul_gyeonggi(api_key)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("청약홈 API 호출 실패: {0}\n".format(exc))
        return 1

    active = [row for row in rows if is_active(row, today_str)]
    active.sort(key=lambda row: (rcept_dates(row)[0], row.get("HOUSE_NM") or ""))

    state = {} if preview else load_state()
    targets = active if preview else [row for row in active if listing_key(row) not in state]

    print(
        "서울·경기 진행중/예정 공고 {0}건 중 신규 {1}건".format(len(active), len(targets))
    )

    if not targets:
        if not preview:
            prune_state(state, today)
            save_state(state)
        print("신규 분양공고가 없어 메시지를 보내지 않습니다.")
        return 0

    grouped = {}
    for row in targets:
        grouped.setdefault(group_label(row), []).append((format_entry(row), row))

    known_labels = [label for label, _ in GROUP_ORDER]
    ordered_labels = known_labels + sorted(set(grouped) - set(known_labels))
    icons = dict(GROUP_ORDER)

    messages = []
    for label in ordered_labels:
        entries = grouped.get(label)
        if not entries:
            continue
        header = "{0} <b>{1} 신규 공고</b> (서울·경기)".format(icons.get(label, "🏢"), label)
        messages.extend(chunk_messages(header, entries))

    if preview:
        print(("\n\n" + "=" * 40 + "\n\n").join(message for message, _ in messages))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write("오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n")
        return 1

    # 메시지마다 보낸 공고를 즉시 상태에 기록해, 중간에 실패해도
    # 이미 보낸 공고가 다음 실행 때 중복 발송되지 않도록 합니다.
    sent = 0
    for i, (message, message_rows) in enumerate(messages):
        if i > 0:
            time.sleep(1.5)  # 텔레그램 속도 제한(같은 채팅에 초당 약 1건) 예방.
        try:
            send_message(token, chat_id, message)
        except Exception as exc:  # noqa: BLE001
            sys.stderr.write(
                "메시지 {0}/{1} 전송 실패: {2}\n".format(i + 1, len(messages), exc)
            )
            prune_state(state, today)
            save_state(state)
            return 1
        for row in message_rows:
            state[listing_key(row)] = today_str
        save_state(state)
        sent += len(message_rows)

    prune_state(state, today)
    save_state(state)

    counts = {label: len(entries) for label, entries in grouped.items()}
    print("전송 완료: 신규 {0}건 — {1}".format(sent, counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
