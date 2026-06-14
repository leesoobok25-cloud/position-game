#!/usr/bin/env python3
"""카드 이미지 분리 (1회성).

POSITION_v5_9_dashboard_tutorial.html 의 CARD_IMAGES 객체에 인라인(base64)으로
박혀 있는 카드 이미지들을 assets/cards/<카드ID>.jpg 파일로 빼내고,
HTML 안의 data: URI 는 그 파일 경로로 바꾼다.

렌더러(line ~4243)는 CARD_IMAGES[c.id] 값을 그대로 <img src> 에 넣으므로
data: URI 든 파일 경로든 동작이 동일하다. 따라서 안전하다.

되돌리기(단일 파일로 통합): tools/build_single_file.py
"""
import re
import base64
import os

HTML = "POSITION_v5_9_dashboard_tutorial.html"
OUTDIR = "assets/cards"

# "카드ID":"data:image/jpeg;base64,<DATA>"
PATTERN = re.compile(
    r'"(?P<key>[^"]+)"\s*:\s*"data:image/jpeg;base64,(?P<data>[A-Za-z0-9+/=]+)"'
)


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    with open(HTML, "r", encoding="utf-8") as f:
        html = f.read()

    used = {}

    def repl(m):
        key = m.group("key")
        safe = re.sub(r"[^A-Za-z0-9_-]", "_", key)
        path = f"{OUTDIR}/{safe}.jpg"
        if path in used and used[path] != key:
            raise SystemExit(f"파일명 충돌: {path} ({used[path]} vs {key})")
        used[path] = key
        with open(path, "wb") as out:
            out.write(base64.b64decode(m.group("data")))
        return f'"{key}":"{path}"'

    new_html, n = PATTERN.subn(repl, html)
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"분리 완료: 이미지 {n}장 -> {OUTDIR}/")


if __name__ == "__main__":
    main()
