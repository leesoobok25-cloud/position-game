#!/usr/bin/env python3
"""단일 파일로 재통합 (분리의 역작업).

분리된 assets/cards/*.jpg 들을 base64 로 HTML 안에 인라인해
완전히 자체 포함된 한 개의 파일 POSITION_v5_9_single.html 을 만든다.

(v5.12) 웹 단일파일 경량화:
 - Pillow가 있으면, 큰 이미지(>MAX_DIM)는 인라인 시 MAX_DIM 으로 다운스케일 + 재압축.
   → 레포의 원본 .jpg(640px)는 그대로 두고(앱 이식용 마스터), 단일파일만 가벼워진다.
 - Pillow가 없거나 이미 작은 이미지는 원본 바이트 그대로 인라인.
 - 이미지 파일이 아직 없으면 빈 값("") → 게임에서 자동 🗳️ 아이콘 폴백.

분리본(POSITION_v5_9_dashboard_tutorial.html)은 그대로 두고 결과만 새로 만든다.
사용:  python3 tools/build_single_file.py
"""
import re
import base64
import os
import io

try:
    from PIL import Image
    _HAS_PIL = True
except ImportError:
    _HAS_PIL = False

SRC = "POSITION_v5_9_dashboard_tutorial.html"
OUT = "POSITION_v5_9_single.html"

MAX_DIM = 400   # 웹 인라인 최대 변(픽셀) — 카드 표시 크기에 충분
JPEG_Q = 85

# "카드ID":"assets/cards/<파일>.jpg"
PATTERN = re.compile(r'"(?P<key>[^"]+)"\s*:\s*"(?P<path>assets/cards/[^"]+\.jpg)"')


def _b64_inline(path):
    """큰 이미지는 다운스케일+재압축해서 base64 반환. 작거나 Pillow 없으면 원본 그대로."""
    if _HAS_PIL:
        try:
            im = Image.open(path)
            if max(im.size) > MAX_DIM:
                im = im.convert("RGB")
                im.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)
                buf = io.BytesIO()
                im.save(buf, "JPEG", quality=JPEG_Q, optimize=True)
                return base64.b64encode(buf.getvalue()).decode("ascii")
        except Exception:
            pass
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        html = f.read()

    stats = {"inlined": 0, "missing": []}

    def repl(m):
        path = m.group("path")
        if os.path.exists(path):
            b64 = _b64_inline(path)
            stats["inlined"] += 1
            return f'"{m.group("key")}":"data:image/jpeg;base64,{b64}"'
        stats["missing"].append(m.group("key"))
        return f'"{m.group("key")}":""'

    single, n = PATTERN.subn(repl, html)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(single)

    mb = os.path.getsize(OUT) / 1024 / 1024
    note = f"(다운스케일 {MAX_DIM}px q{JPEG_Q})" if _HAS_PIL else "(Pillow 없음 — 원본 크기 인라인)"
    print(f"통합 완료: 이미지 {stats['inlined']}장 인라인 {note} -> {OUT}  [{mb:.1f}MB]")
    if stats["missing"]:
        print(f"  (이미지 없는 카드 {len(stats['missing'])}장은 아이콘 폴백: {', '.join(stats['missing'][:6])}{' …' if len(stats['missing'])>6 else ''})")


if __name__ == "__main__":
    main()
