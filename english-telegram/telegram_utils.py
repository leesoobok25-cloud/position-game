# -*- coding: utf-8 -*-
"""
텔레그램 전송 & 음성(TTS) 공용 함수 모음.

send_daily.py(여행 회화) 와 send_lesson.py(기초 영어 코스) 가 함께 사용합니다.
"""

import json
import urllib.parse
import urllib.request

TELEGRAM = "https://api.telegram.org/bot{token}/{method}"


def get_updates(token, offset=None, timeout=25):
    """getUpdates로 봇이 받은 새 메시지를 가져옵니다. (사용자의 레벨 조정 응답 'up/down' 읽기용)"""
    params = {}
    if offset is not None:
        params["offset"] = offset
    url = TELEGRAM.format(token=token, method="getUpdates")
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not data.get("ok"):
        raise RuntimeError("getUpdates 오류: {0}".format(data))
    return data.get("result", [])


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


# 음성 속도. 1.0 = 원래 속도, 낮출수록 느려짐 (학습용으로 약간 느리게).
#   더 느리게: 0.8 / 0.75  ·  조금 빠르게: 0.9 / 1.0
TTS_SPEED = 0.85


def make_tts_mp3(text, path):
    """영어 텍스트를 MP3 음성 파일로 변환합니다.

    gTTS로 만든 뒤 ffmpeg로 약간 느리게(TTS_SPEED) 처리합니다.
    ffmpeg가 없거나 실패하면 gTTS 자체 느린 모드로 대체합니다.
    """
    import os
    import subprocess

    from gtts import gTTS  # 음성 생성이 필요할 때만 불러옵니다.

    raw_path = path + ".raw.mp3"
    gTTS(text=text, lang="en", slow=False).save(raw_path)
    try:
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", raw_path,
                "-filter:a", "atempo={0}".format(TTS_SPEED),
                "-vn", path,
            ],
            check=True,
            capture_output=True,
        )
        os.remove(raw_path)
    except Exception:  # noqa: BLE001  # ffmpeg 없음/실패 → gTTS 느린 모드로 대체
        gTTS(text=text, lang="en", slow=True).save(path)
        if os.path.exists(raw_path):
            os.remove(raw_path)


def send_audio(token, chat_id, mp3_path, title, caption):
    """발음 mp3를 텔레그램으로 전송합니다.

    '오디오'가 아니라 '문서(document)'로 보냅니다. 오디오로 보내면 재생이 끝났을 때
    텔레그램이 채팅 내 다음 오디오를 자동 재생(재생목록)하는데, 문서로 보내면 그 자동
    넘김이 없습니다. (탭하면 재생되는 것은 그대로예요.)
    """
    import requests  # gtts 설치 시 함께 설치됩니다.

    url = TELEGRAM.format(token=token, method="sendDocument")
    filename = "{0}.mp3".format(title).replace(" ", "_").replace("/", "-")
    with open(mp3_path, "rb") as audio_file:
        response = requests.post(
            url,
            data={"chat_id": chat_id, "caption": caption},
            files={"document": (filename, audio_file, "audio/mpeg")},
            timeout=60,
        )
    result = response.json()
    if not result.get("ok"):
        raise RuntimeError("Telegram sendDocument 오류: {0}".format(response.text))
    return result
