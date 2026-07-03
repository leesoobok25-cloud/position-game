# -*- coding: utf-8 -*-
"""
텔레그램 전송 공용 함수 모음. (send_presale.py 전용)
"""

import json
import time
import urllib.error
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


def send_message(token, chat_id, text, max_retries=3):
    """텔레그램으로 HTML 형식 텍스트 메시지를 전송합니다. (429 속도 제한 시 자동 재시도)"""
    url = TELEGRAM.format(token=token, method="sendMessage")
    payload = json.dumps(
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        }
    ).encode("utf-8")

    for attempt in range(max_retries + 1):
        request = urllib.request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            if exc.code == 401:
                raise RuntimeError(
                    "텔레그램 봇 토큰이 유효하지 않습니다(401 Unauthorized). "
                    "Secret에 등록한 토큰 값을 다시 확인하세요 "
                    "(BotFather에서 /revoke 했다면 새 토큰으로 교체 필요)."
                ) from exc
            if exc.code == 429 and attempt < max_retries:
                # 속도 제한: 텔레그램이 알려준 대기 시간만큼 쉬었다가 재시도합니다.
                try:
                    retry_after = json.loads(body)["parameters"]["retry_after"]
                except (ValueError, KeyError, TypeError):
                    retry_after = 5
                time.sleep(retry_after + 1)
                continue
            raise RuntimeError(
                "Telegram sendMessage HTTP {0}: {1}".format(exc.code, body[:300])
            ) from exc

        result = json.loads(body)
        if not result.get("ok"):
            raise RuntimeError("Telegram sendMessage 오류: {0}".format(body))
        return result
