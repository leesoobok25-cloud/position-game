# -*- coding: utf-8 -*-
"""
텔레그램 전송 & 음성(TTS) 공용 함수 모음.

send_daily.py(여행 회화) 와 send_lesson.py(기초 영어 코스) 가 함께 사용합니다.
"""

import json
import urllib.request

TELEGRAM = "https://api.telegram.org/bot{token}/{method}"


def escape_html(text):
    """텔레그램 HTML 모드에서 문제가 되는 문자를 이스케이프합니다."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def send_message(token, chat_id, text):
    """텔레그램으로 HTML 형식 텍스트 메시지를 전송합니다."""
    url = TELEGRAM.format(token=token, method="sendMessage")
    payload = json.dumps(
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
        result = json.loads(body)
        if not result.get("ok"):
            raise RuntimeError("Telegram sendMessage 오류: {0}".format(body))
        return result


def make_tts_mp3(text, path):
    """영어 텍스트를 MP3 음성 파일로 변환합니다 (gTTS 사용)."""
    from gtts import gTTS  # 음성 생성이 필요할 때만 불러옵니다.

    gTTS(text=text, lang="en", slow=False).save(path)


def send_audio(token, chat_id, mp3_path, title, caption):
    """텔레그램으로 발음 듣기용 음성(오디오) 파일을 전송합니다."""
    import requests  # gtts 설치 시 함께 설치됩니다.

    url = TELEGRAM.format(token=token, method="sendAudio")
    with open(mp3_path, "rb") as audio_file:
        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "title": title,
                "performer": "Daily English",
                "caption": caption,
            },
            files={"audio": ("audio.mp3", audio_file, "audio/mpeg")},
            timeout=60,
        )
    result = response.json()
    if not result.get("ok"):
        raise RuntimeError("Telegram sendAudio 오류: {0}".format(response.text))
    return result
