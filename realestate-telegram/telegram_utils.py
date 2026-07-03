# -*- coding: utf-8 -*-
"""
텔레그램 전송 공용 함수 모음. (send_presale.py 전용)
"""

import json
import urllib.request

TELEGRAM = "https://api.telegram.org/bot{token}/{method}"


def escape_html(text):
    """텔레그램 HTML 모드에서 문제가 되는 문자를 이스케이프합니다."""
    return (
        str(text)
        .replace("&", "&amp;")
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
