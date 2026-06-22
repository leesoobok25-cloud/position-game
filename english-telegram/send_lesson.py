#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
기초 영어 코스의 '오늘의 과'를 골라 텔레그램으로 보냅니다.

회화 스크립트(send_daily.py)와 달리, START_DATE 부터 '순서대로' 하루에 한 과씩 진행합니다.
전체 과를 한 바퀴 끝내면 처음부터 다시 복습합니다.

필요한 환경 변수 (GitHub Secrets):
  - TELEGRAM_BOT_TOKEN
  - TELEGRAM_CHAT_ID

미리보기 (전송 없이 출력만):
  python3 send_lesson.py --preview 0     # 0번 과 미리보기
  python3 send_lesson.py --preview-all   # 전체 미리보기

텍스트와 함께 예문 음성(MP3)도 전송합니다 (pip install gtts requests).
"""

import os
import sys
import tempfile
from datetime import date

from lessons import LESSONS
from telegram_utils import escape_html, make_tts_mp3, send_audio, send_message

# 코스 시작일. 이 날 첫 과(Day 1)가 나갑니다.
START_DATE = date(2026, 6, 22)
DIVIDER = "━━━━━━━━━━━━━━━━━━"


def pick_for_today(total, today=None):
    """오늘이 코스 며칠째인지 계산해 (과 번호 인덱스, 복습 회차)를 돌려줍니다."""
    if today is None:
        today = date.today()
    days = (today - START_DATE).days
    if days < 0:
        days = 0
    return days % total, days // total


def build_message(lesson, day_number, total, cycle):
    """기초 영어 한 과를 텔레그램용 HTML 메시지로 만듭니다."""
    review = " · 복습 {0}회차".format(cycle) if cycle >= 1 else ""
    lines = []
    lines.append(
        "📘 <b>기초 영어</b>  (Day {n}/{t}){r}".format(n=day_number, t=total, r=review)
    )
    lines.append(
        "📗 {unit} · <b>{en}</b> — {ko}".format(
            unit=escape_html(lesson["unit"]),
            en=escape_html(lesson["title_en"]),
            ko=escape_html(lesson["title_ko"]),
        )
    )
    lines.append("")
    lines.append(DIVIDER)
    lines.append("📖 <b>오늘 배울 것</b>")
    lines.append(escape_html(lesson["explain"]))
    lines.append("")

    lines.append("✏️ <b>핵심 패턴</b>")
    for point in lesson["points"]:
        lines.append(
            "• <b>{en}</b> — {ko}".format(
                en=escape_html(point["en"]), ko=escape_html(point["ko"])
            )
        )
    lines.append("")

    lines.append("💬 <b>예문</b>")
    for i, example in enumerate(lesson["examples"], 1):
        lines.append("{i}. {en}".format(i=i, en=escape_html(example["en"])))
        lines.append("   <i>{ko}</i>".format(ko=escape_html(example["ko"])))
    lines.append("")

    lines.append(DIVIDER)
    lines.append("📝 <b>연습</b> (정답은 가려놨어요 — 먼저 풀고 탭해서 확인!)")
    for i, item in enumerate(lesson["practice"], 1):
        lines.append("Q{i}. {q}".format(i=i, q=escape_html(item["q"])))
        lines.append(
            "    👉 <tg-spoiler>{a}</tg-spoiler>".format(a=escape_html(item["a"]))
        )
    lines.append("")
    lines.append("🔊 예문 음성도 같이 보낼게요. 큰 소리로 따라 읽어보세요!")

    return "\n".join(lines)


def build_audio_text(lesson):
    """음성으로 읽어줄 영어 텍스트(예문)를 만듭니다."""
    return "\n".join(example["en"] for example in lesson["examples"])


def main():
    args = sys.argv[1:]
    total = len(LESSONS)

    if args and args[0] == "--preview-all":
        for i, lesson in enumerate(LESSONS):
            print("=" * 60)
            print(build_message(lesson, i + 1, total, 0))
            print()
        return 0

    if args and args[0] == "--preview":
        if len(args) > 1:
            index, cycle = int(args[1]) % total, 0
        else:
            index, cycle = pick_for_today(total)
        print(build_message(LESSONS[index], index + 1, total, cycle))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write(
            "오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n"
        )
        return 1

    index, cycle = pick_for_today(total)
    lesson = LESSONS[index]
    message = build_message(lesson, index + 1, total, cycle)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    # 예문 음성(TTS)도 함께 전송 (실패해도 텍스트는 이미 전송됨).
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(lesson), mp3_path)
        caption = "🔊 기초 영어 Day {n} — {title} 예문 듣기".format(
            n=index + 1, title=lesson["title_en"]
        )
        send_audio(
            token, chat_id, mp3_path, "기초 영어 Day {0}".format(index + 1), caption
        )
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    print(
        "전송 완료: Day {n}/{t} - {title}".format(
            n=index + 1, t=total, title=lesson["title_en"]
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
