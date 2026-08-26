#!/usr/bin/env python3
"""웹 배포본(index.html) 생성 — 단일파일 + 모바일/PWA 셋업.

build_single_file.py 가 만든 POSITION_v5_9_single.html(이미지 인라인 완료)에
모바일 최적화 메타 + PWA(매니페스트·아이콘·서비스워커 등록)를 입혀
GitHub Pages 로 서비스할 index.html 을 만든다.

배경: 기존 배포본(v5.8 "Mobile Build")에는 PWA가 있었지만 튜토리얼이 없었고,
      개발본(v5.9 "Tutorial Build")에는 튜토리얼이 있었지만 PWA가 없었다.
      이 스크립트가 둘을 합친다.

PWA 자산(매니페스트·아이콘)은 tools/pwa_assets.html 에서 읽는다.

사용:
  python3 tools/build_single_file.py   # 1) 이미지 인라인 단일파일
  python3 tools/build_deploy.py        # 2) index.html (배포본) 생성
"""
import os
import re

SRC = "POSITION_v5_9_single.html"          # 이미지 인라인된 단일파일
OUT = "index.html"                          # GitHub Pages 진입점
PWA_ASSETS = "tools/pwa_assets.html"        # <link rel=manifest> + <link rel=apple-touch-icon>

# 모바일 최적화 메타 (기존 v5.8 배포본과 동일)
MOBILE_META = """<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#0d1117">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">"""

# 서비스워커 등록 (file:// 로 열면 조용히 무시 → 다운로드본에서도 안전)
SW_REGISTER = """<script>
/* (PWA) 서비스워커 등록 — https/호스팅 환경에서만 동작, file://에서는 무시 */
if('serviceWorker' in navigator && (location.protocol==='https:' || location.protocol==='http:')){
  window.addEventListener('load', function(){
    navigator.serviceWorker.register('sw.js').catch(function(){ /* sw.js 없으면 조용히 무시 */ });
  });
}
</script>
</body>"""


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"[!] {SRC} 없음 — 먼저 python3 tools/build_single_file.py 를 실행하세요.")
    with open(SRC, "r", encoding="utf-8") as f:
        html = f.read()

    # 1) 모바일 메타 주입 (charset 바로 뒤)
    if 'name="viewport"' not in html:
        html = html.replace('<meta charset="UTF-8">',
                            '<meta charset="UTF-8">\n' + MOBILE_META, 1)

    # 2) PWA 매니페스트 + 아이콘 주입 (</head> 직전)
    pwa = ""
    if os.path.exists(PWA_ASSETS):
        with open(PWA_ASSETS, "r", encoding="utf-8") as f:
            pwa = f.read().strip()
        if pwa and 'rel="manifest"' not in html:
            html = html.replace("</head>", pwa + "\n</head>", 1)
    else:
        print(f"  (주의: {PWA_ASSETS} 없음 — 매니페스트·아이콘 없이 빌드)")

    # 3) 서비스워커 등록 (</body> 직전)
    if "serviceWorker" not in html:
        html = html.replace("</body>", SW_REGISTER, 1)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    build = re.search(r'<meta name="position-build" content="([^"]*)"', html)
    mb = os.path.getsize(OUT) / 1024 / 1024
    ok = lambda cond: "✓" if cond else "✗"
    has_viewport = 'name="viewport"' in html
    has_manifest = 'rel="manifest"' in html
    print(f"배포본 생성: {OUT} [{mb:.1f}MB] · 빌드 {build.group(1) if build else '?'}")
    print(f"  모바일 메타 {ok(has_viewport)}"
          f" · 매니페스트 {ok(has_manifest)}"
          f" · 서비스워커 {ok('serviceWorker' in html)}"
          f" · 튜토리얼 {ok('startTutorial' in html)}")


if __name__ == "__main__":
    main()
