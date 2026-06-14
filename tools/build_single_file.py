#!/usr/bin/env python3
"""단일 파일로 재통합 (분리의 역작업).

분리된 assets/cards/*.jpg 들을 다시 base64 로 읽어 HTML 안에 인라인으로 박아
완전히 자체 포함된 한 개의 파일 POSITION_v5_9_single.html 을 만든다.
(원본과 바이트 단위로 동일하게 복원되는 무손실 작업.)

분리본(POSITION_v5_9_dashboard_tutorial.html)은 그대로 두고 결과만 새로 만든다.
사용:  python3 tools/build_single_file.py
"""
import re
import base64

SRC = "POSITION_v5_9_dashboard_tutorial.html"
OUT = "POSITION_v5_9_single.html"

# "카드ID":"assets/cards/<파일>.jpg"
PATTERN = re.compile(r'"(?P<key>[^"]+)"\s*:\s*"(?P<path>assets/cards/[^"]+\.jpg)"')


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        html = f.read()

    def repl(m):
        with open(m.group("path"), "rb") as img:
            b64 = base64.b64encode(img.read()).decode("ascii")
        return f'"{m.group("key")}":"data:image/jpeg;base64,{b64}"'

    single, n = PATTERN.subn(repl, html)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(single)
    print(f"통합 완료: 이미지 {n}장 인라인 -> {OUT}")


if __name__ == "__main__":
    main()
