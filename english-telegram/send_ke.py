#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
한→영 말하기 한 세트를 텔레그램으로 보냅니다.

한국어 문장을 보고 '직접 영어로 말한 뒤', 가려진 정답을 탭해서 확인합니다.
START_DATE 기준으로 매일 한 세트씩 순서대로.

필요한 환경 변수: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
미리보기: python3 send_ke.py --preview 0 / --preview-all
"""

import os
import sys
import tempfile
from datetime import date

from ke_drills import KE_SETS
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


def build_message(drill, day_number, total, cycle):
    review = " · 복습 {0}회차".format(cycle) if cycle >= 1 else ""
    lines = []
    lines.append("🇰🇷➡️🇬🇧 <b>한→영 말하기</b>  (Day {n}/{t}){r}".format(n=day_number, t=total, r=review))
    lines.append("📝 주제: {th}".format(th=escape_html(drill["theme"])))
    lines.append("")
    lines.append("아래 한국어를 보고 <b>먼저 직접 영어로 말해보세요.</b> 그다음 정답을 탭해서 확인!")
    lines.append(DIVIDER)
    for i, item in enumerate(drill["items"], 1):
        lines.append("{i}. {ko}".format(i=i, ko=escape_html(item["ko"])))
        lines.append("    👉 <tg-spoiler>{en}</tg-spoiler>".format(en=escape_html(item["en"])))
    lines.append(DIVIDER)
    lines.append("")
    lines.append("✅ 정답을 보고 <b>3번 소리 내어</b> 따라 말하세요.")
    lines.append("🔊 음성으로 발음도 확인하세요!")
    return "\n".join(lines)


def build_audio_text(drill):
    return "\n".join(item["en"] for item in drill["items"])


def main():
    args = sys.argv[1:]
    total = len(KE_SETS)

    if args and args[0] == "--preview-all":
        for i, drill in enumerate(KE_SETS):
            print("=" * 60)
            print(build_message(drill, i + 1, total, 0))
            print()
        return 0
    if args and args[0] == "--preview":
        if len(args) > 1:
            index, cycle = int(args[1]) % total, 0
        else:
            index, cycle = pick_for_today(total)
        print(build_message(KE_SETS[index], index + 1, total, cycle))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write("오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n")
        return 1

    index, cycle = pick_for_today(total)
    drill = KE_SETS[index]
    message = build_message(drill, index + 1, total, cycle)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(drill), mp3_path)
        caption = "🔊 한→영 말하기 ({0}) — 정답 발음".format(drill["theme"])
        send_audio(token, chat_id, mp3_path, "한→영 말하기", caption)
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    print("전송 완료: Day {n}/{t} - {th}".format(n=index + 1, t=total, th=drill["theme"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
