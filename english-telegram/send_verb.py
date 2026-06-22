#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
오늘의 동사 한 개를 골라 텔레그램으로 보냅니다.

기초 코스(send_lesson.py)처럼 START_DATE 부터 '순서대로' 하루 하나씩 진행하고,
전체를 한 바퀴 끝내면 처음부터 다시 복습합니다.

필요한 환경 변수: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

미리보기 (전송 없이):
  python3 send_verb.py --preview 0
  python3 send_verb.py --preview-all
"""

import os
import sys
import tempfile
from datetime import date

from telegram_utils import escape_html, make_tts_mp3, send_audio, send_message
from verbs import VERBS

# 코스 시작일. 이 날 첫 동사(Day 1)가 나갑니다.
START_DATE = date(2026, 6, 22)
DIVIDER = "━━━━━━━━━━━━━━━━━━"


def pick_for_today(total, today=None):
    """오늘이 며칠째인지 계산해 (동사 인덱스, 복습 회차)를 돌려줍니다."""
    if today is None:
        today = date.today()
    days = (today - START_DATE).days
    if days < 0:
        days = 0
    return days % total, days // total


def build_message(verb, day_number, total, cycle):
    """동사 하나를 텔레그램용 HTML 메시지로 만듭니다."""
    review = " · 복습 {0}회차".format(cycle) if cycle >= 1 else ""
    lines = []
    lines.append(
        "🔤 <b>오늘의 동사</b>  (Day {n}/{t}){r}".format(n=day_number, t=total, r=review)
    )
    lines.append(
        "👉 <b>{verb}</b> — {ko}".format(
            verb=escape_html(verb["verb"]), ko=escape_html(verb["ko"])
        )
    )
    lines.append("")
    lines.append(
        "📐 <b>변화형</b>: {forms}  ({reg})".format(
            forms=escape_html(verb["forms"]), reg=escape_html(verb["reg"])
        )
    )
    lines.append("")
    lines.append(DIVIDER)
    lines.append("💬 <b>예문</b>")
    for i, example in enumerate(verb["examples"], 1):
        lines.append("{i}. {en}".format(i=i, en=escape_html(example["en"])))
        lines.append("   <i>{ko}</i>".format(ko=escape_html(example["ko"])))

    if verb.get("phrases"):
        lines.append("")
        lines.append("🔁 <b>자주 쓰는 표현</b>")
        for phrase in verb["phrases"]:
            lines.append(
                "• <b>{en}</b> — {ko}".format(
                    en=escape_html(phrase["en"]), ko=escape_html(phrase["ko"])
                )
            )

    lines.append("")
    lines.append("🔊 동사와 예문 음성 — 큰 소리로 따라 읽으며 외워보세요!")
    return "\n".join(lines)


def build_audio_text(verb):
    """음성으로 읽어줄 영어 텍스트(변화형 + 예문)를 만듭니다."""
    forms = verb["forms"].replace(" → ", ", ").replace("/", " or ")
    parts = [forms]
    parts.extend(example["en"] for example in verb["examples"])
    return "\n".join(parts)


def main():
    args = sys.argv[1:]
    total = len(VERBS)

    if args and args[0] == "--preview-all":
        for i, verb in enumerate(VERBS):
            print("=" * 60)
            print(build_message(verb, i + 1, total, 0))
            print()
        return 0

    if args and args[0] == "--preview":
        if len(args) > 1:
            index, cycle = int(args[1]) % total, 0
        else:
            index, cycle = pick_for_today(total)
        print(build_message(VERBS[index], index + 1, total, cycle))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write(
            "오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n"
        )
        return 1

    index, cycle = pick_for_today(total)
    verb = VERBS[index]
    message = build_message(verb, index + 1, total, cycle)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    # 동사·예문 음성(TTS)도 함께 전송 (실패해도 텍스트는 이미 전송됨).
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(verb), mp3_path)
        caption = "🔊 오늘의 동사 '{verb}' — 발음 듣기".format(verb=verb["verb"])
        send_audio(
            token, chat_id, mp3_path, "오늘의 동사: {0}".format(verb["verb"]), caption
        )
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    print(
        "전송 완료: Day {n}/{t} - {verb}".format(
            n=index + 1, t=total, verb=verb["verb"]
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
