#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
오늘의 여행 영어 회화 스크립트를 골라 텔레그램으로 보냅니다.

필요한 환경 변수 (GitHub Secrets):
  - TELEGRAM_BOT_TOKEN : @BotFather에서 발급받은 봇 토큰
  - TELEGRAM_CHAT_ID    : 메시지를 받을 채팅 ID (본인 계정 ID)

로컬에서 테스트하려면:
  TELEGRAM_BOT_TOKEN=xxx TELEGRAM_CHAT_ID=yyy python3 send_daily.py

특정 시나리오를 미리 보고 싶으면 (전송 없이 출력만):
  python3 send_daily.py --preview 0      # 0번 시나리오 미리보기
  python3 send_daily.py --preview-all    # 전체 미리보기

텍스트와 함께 발음 듣기용 음성(MP3)도 전송합니다.
이를 위해 gtts 패키지가 필요합니다:  pip install gtts requests
"""

import os
import sys
import tempfile
from datetime import date

from scenarios import SCENARIOS
from telegram_utils import escape_html, make_tts_mp3, send_audio, send_message

# 순환 기준 날짜. 이 날짜로부터 며칠 지났는지로 오늘의 시나리오를 정합니다.
EPOCH = date(2026, 1, 1)
DIVIDER = "━━━━━━━━━━━━━━━━━━"


def pick_index_for_today(total, today=None):
    """오늘 날짜에 해당하는 시나리오 인덱스를 결정적으로 계산합니다."""
    if today is None:
        today = date.today()
    return (today - EPOCH).days % total


def build_message(scenario, day_number, total):
    """시나리오 하나를 텔레그램용 HTML 메시지로 만듭니다."""
    lines = []
    lines.append(
        "🌍 <b>오늘의 여행 영어</b>  "
        "(Day {n}/{t})".format(n=day_number, t=total)
    )
    lines.append(
        "{emoji} <b>{en}</b> — {ko}".format(
            emoji=scenario["emoji"],
            en=escape_html(scenario["title_en"]),
            ko=escape_html(scenario["title_ko"]),
        )
    )
    lines.append("")
    lines.append(DIVIDER)
    lines.append("💬 <b>대화 (Dialogue)</b>")
    lines.append("")

    for turn in scenario["dialogue"]:
        speaker = escape_html(turn["speaker"])
        en = escape_html(turn["en"])
        ko = escape_html(turn["ko"])
        lines.append("<b>{speaker}:</b> {en}".format(speaker=speaker, en=en))
        lines.append("<i>{ko}</i>".format(ko=ko))
        lines.append("")

    lines.append(DIVIDER)
    lines.append("🔑 <b>핵심 표현 (Key Phrases)</b>")
    for phrase in scenario["key_phrases"]:
        lines.append(
            "• <b>{en}</b> — {ko}".format(
                en=escape_html(phrase["en"]),
                ko=escape_html(phrase["ko"]),
            )
        )

    lines.append("")
    lines.append("💡 <b>팁:</b> {tip}".format(tip=escape_html(scenario["tip"])))
    lines.append("")
    lines.append("오늘도 한 문장씩! 소리 내어 읽어보세요 🗣️")

    return "\n".join(lines)


def build_audio_text(scenario):
    """음성으로 읽어줄 영어 텍스트(대화문)를 만듭니다. 빈칸(___)이 없는 자연스러운 문장만 사용합니다."""
    return "\n".join(turn["en"] for turn in scenario["dialogue"])


def main():
    args = sys.argv[1:]
    total = len(SCENARIOS)

    # 미리보기 모드 (전송하지 않음)
    if args and args[0] == "--preview-all":
        for i, scenario in enumerate(SCENARIOS):
            print("=" * 60)
            print(build_message(scenario, i + 1, total))
            print()
        return 0

    if args and args[0] == "--preview":
        index = int(args[1]) if len(args) > 1 else pick_index_for_today(total)
        index %= total
        print(build_message(SCENARIOS[index], index + 1, total))
        return 0

    # 실제 전송 모드
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        sys.stderr.write(
            "오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n"
            "GitHub 저장소 Settings > Secrets and variables > Actions 에 등록하세요.\n"
        )
        return 1

    index = pick_index_for_today(total)
    scenario = SCENARIOS[index]
    message = build_message(scenario, index + 1, total)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    # 발음 듣기용 음성(TTS)도 함께 전송합니다.
    # (음성 생성/전송이 실패해도 텍스트는 이미 전송됐으므로 작업을 실패 처리하지 않습니다.)
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(scenario), mp3_path)
        caption = "🔊 {emoji} {title} — 발음 듣기 (탭하면 재생)".format(
            emoji=scenario["emoji"], title=scenario["title_en"]
        )
        send_audio(token, chat_id, mp3_path, scenario["title_en"], caption)
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    print(
        "전송 완료: Day {n}/{t} - {title}".format(
            n=index + 1, t=total, title=scenario["title_en"]
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
