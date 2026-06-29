#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
오늘의 패턴 하나를 텔레그램으로 보냅니다 (문장 자동화 훈련).

START_DATE 기준으로 매일 하나씩 순서대로 진행하고, 한 바퀴 끝나면 복습합니다.

필요한 환경 변수: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
미리보기: python3 send_pattern.py --preview 0 / --preview-all
"""

import os
import sys
import tempfile
from datetime import date

from patterns import PATTERNS
from telegram_utils import escape_html, make_tts_mp3, send_audio, send_message

START_DATE = date(2026, 6, 22)
DIVIDER = "━━━━━━━━━━━━━━━━━━"


def pick_for_today(total, today=None):
    if today is None:
        today = date.today()
    days = (today - START_DATE).days
    if days < 0:
        days = 0
    return days % total, days // total


def build_message(item, day_number, total, cycle):
    review = " · 복습 {0}회차".format(cycle) if cycle >= 1 else ""
    lines = []
    lines.append("☀️ <b>오늘의 패턴</b>  (Day {n}/{t}){r}".format(n=day_number, t=total, r=review))
    lines.append("👉 <b>{p}</b> — {ko}".format(p=escape_html(item["pattern"]), ko=escape_html(item["ko"])))
    lines.append("")
    lines.append(DIVIDER)
    lines.append("🔁 <b>내 주제로 바꿔 말하기</b> (각 문장 5번씩 입으로!)")
    for i, ex in enumerate(item["examples"], 1):
        lines.append("{i}. {en}".format(i=i, en=escape_html(ex["en"])))
        lines.append("   <i>{ko}</i>".format(ko=escape_html(ex["ko"])))
    lines.append(DIVIDER)
    lines.append("")
    lines.append("🗣️ 마지막에 <b>나만의 문장 1개</b>를 이 패턴으로 만들어 말해보세요!")
    lines.append("🔊 음성으로 따라 말하기(섀도잉) 하세요.")
    return "\n".join(lines)


def build_audio_text(item):
    return "\n".join(ex["en"] for ex in item["examples"])


def main():
    args = sys.argv[1:]
    total = len(PATTERNS)

    if args and args[0] == "--preview-all":
        for i, item in enumerate(PATTERNS):
            print("=" * 60)
            print(build_message(item, i + 1, total, 0))
            print()
        return 0
    if args and args[0] == "--preview":
        if len(args) > 1:
            index, cycle = int(args[1]) % total, 0
        else:
            index, cycle = pick_for_today(total)
        print(build_message(PATTERNS[index], index + 1, total, cycle))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write("오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n")
        return 1

    index, cycle = pick_for_today(total)
    item = PATTERNS[index]
    message = build_message(item, index + 1, total, cycle)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(item), mp3_path)
        caption = "🔊 오늘의 패턴 '{0}' — 따라 말하기".format(item["pattern"])
        send_audio(token, chat_id, mp3_path, "오늘의 패턴", caption)
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    print("전송 완료: Day {n}/{t} - {p}".format(n=index + 1, t=total, p=item["pattern"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
