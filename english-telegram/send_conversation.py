#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
오늘의 '단계별 회화'를 텔레그램으로 보냅니다. (중1 → 고3, 6단계)

매일:
  1) 봇이 받은 새 메시지(getUpdates)를 읽어 사용자의 'up/down' 응답을 확인하고 학년을 조정합니다.
  2) 현재 학년에 맞는 회화를 보내고, 끝에 "다음 학년으로 올릴까요?"라고 물어봅니다.
  3) 바뀐 학년(상태)을 state/conversation_state.json 에 저장합니다.
     (GitHub Actions 워크플로우가 이 파일을 커밋해 다음 날로 이어집니다.)

필요한 환경 변수: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

미리보기 (전송/상태변경 없이):
  python3 send_conversation.py --preview 0     # 0번 학년 미리보기
  python3 send_conversation.py --preview-all
"""

import json
import os
import sys
import tempfile
from datetime import date

from conversation_levels import GRADES
from telegram_utils import (
    escape_html,
    get_updates,
    make_tts_mp3,
    send_audio,
    send_message,
)

STATE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "state", "conversation_state.json"
)
# 회화 안 다이얼로그를 날짜로 돌리기 위한 기준일.
START_DATE = date(2026, 6, 22)
DIVIDER = "━━━━━━━━━━━━━━━━━━"

# 사용자가 봇에게 보내면 학년을 올리는/내리는 키워드 (소문자 비교).
LEVEL_UP_WORDS = {"up", "업", "올려", "올리기", "레벨업", "레벨 업", "👍", "⬆️"}
LEVEL_DOWN_WORDS = {"down", "다운", "내려", "내리기", "쉽게", "⬇️"}


def load_state():
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            state = json.load(f)
    except (OSError, ValueError):
        state = {}
    state.setdefault("grade_index", 0)
    state.setdefault("last_update_id", 0)
    return state


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")


def apply_user_replies(token, state):
    """getUpdates로 사용자의 up/down 응답을 읽어 학년을 조정합니다. 바뀐 칸 수(net)를 반환."""
    max_index = len(GRADES) - 1
    try:
        updates = get_updates(token, state["last_update_id"] + 1)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("getUpdates 실패(레벨 변경 건너뜀): {0}\n".format(exc))
        return 0

    direction = 0
    highest = state["last_update_id"]
    for update in updates:
        highest = max(highest, update.get("update_id", 0))
        message = update.get("message") or update.get("edited_message") or {}
        text = (message.get("text") or "").strip().lower()
        callback = update.get("callback_query") or {}
        if callback.get("data"):
            text = callback["data"].strip().lower()
        if not text:
            continue
        if text in LEVEL_UP_WORDS:
            direction = 1
        elif text in LEVEL_DOWN_WORDS:
            direction = -1

    state["last_update_id"] = highest

    old = state["grade_index"]
    if direction > 0:
        state["grade_index"] = min(old + 1, max_index)
    elif direction < 0:
        state["grade_index"] = max(old - 1, 0)
    return state["grade_index"] - old


def pick_dialogue(grade, today=None):
    if today is None:
        today = date.today()
    pool = grade["dialogues"]
    return pool[(today - START_DATE).days % len(pool)]


def build_message(grade_index, dialogue, moved):
    grade = GRADES[grade_index]
    total = len(GRADES)
    lines = []
    lines.append(
        "🗣️ <b>오늘의 회화</b>  ·  레벨 {n}/{t} · <b>{g}</b>".format(
            n=grade_index + 1, t=total, g=escape_html(grade["grade"])
        )
    )
    if moved > 0:
        lines.append("🎉 <b>축하해요! {g}(으)로 올라갔어요!</b>".format(g=escape_html(grade["grade"])))
    elif moved < 0:
        lines.append("🔽 <b>{g}(으)로 한 단계 내렸어요.</b>".format(g=escape_html(grade["grade"])))
    lines.append("📝 주제: {title}".format(title=escape_html(dialogue["title"])))
    lines.append("")
    lines.append(DIVIDER)
    for turn in dialogue["turns"]:
        lines.append(
            "<b>{s}:</b> {en}".format(s=escape_html(turn["s"]), en=escape_html(turn["en"]))
        )
        lines.append("<i>{ko}</i>".format(ko=escape_html(turn["ko"])))
    lines.append(DIVIDER)
    lines.append("")
    lines.append("📈 <b>오늘 회화 끝!</b>")
    lines.append("다음 학년으로 <b>올리려면</b> 이 봇에게 <b>up</b> 이라고 보내주세요.")
    lines.append("(너무 어려우면 <b>down</b>, 그대로면 그냥 두면 돼요 · 다음 발송 때 반영)")
    lines.append("")
    lines.append("🔊 음성도 같이 보낼게요. 큰 소리로 따라 읽어보세요!")
    return "\n".join(lines)


def build_audio_text(dialogue):
    return "\n".join(turn["en"] for turn in dialogue["turns"])


def main():
    args = sys.argv[1:]
    total = len(GRADES)

    if args and args[0] == "--preview-all":
        for i, grade in enumerate(GRADES):
            for dialogue in grade["dialogues"]:
                print("=" * 60)
                print(build_message(i, dialogue, 0))
                print()
        return 0

    if args and args[0] == "--preview":
        index = (int(args[1]) if len(args) > 1 else 0) % total
        print(build_message(index, GRADES[index]["dialogues"][0], 0))
        return 0

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        sys.stderr.write(
            "오류: TELEGRAM_BOT_TOKEN 과 TELEGRAM_CHAT_ID 환경 변수가 필요합니다.\n"
        )
        return 1

    state = load_state()
    moved = apply_user_replies(token, state)  # up/down 반영 (학년 변경)
    grade_index = state["grade_index"]
    dialogue = pick_dialogue(GRADES[grade_index])
    message = build_message(grade_index, dialogue, moved)

    try:
        send_message(token, chat_id, message)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("텍스트 전송 실패: {0}\n".format(exc))
        return 1

    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            mp3_path = tmp.name
        make_tts_mp3(build_audio_text(dialogue), mp3_path)
        caption = "🔊 오늘의 회화 ({0}) — 발음 듣기".format(GRADES[grade_index]["grade"])
        send_audio(token, chat_id, mp3_path, "오늘의 회화", caption)
        os.remove(mp3_path)
        print("음성 전송 완료")
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("음성 전송은 건너뜀(텍스트는 정상 전송됨): {0}\n".format(exc))

    save_state(state)
    print(
        "전송 완료: 레벨 {n}/{t} ({g}), 학년변동 {m}".format(
            n=grade_index + 1, t=total, g=GRADES[grade_index]["grade"], m=moved
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
