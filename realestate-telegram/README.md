# 🏠 부동산 분양정보 자동 알림 (텔레그램)

**서울·경기** 지역의 아파트 **분양정보**(공공분양 + 민간분양 모두)를 매일 텔레그램으로 받아보는 자동화입니다.

- 데이터 출처: [한국부동산원 청약Home 분양정보 조회 서비스](https://www.data.go.kr/data/15098547/openapi.do) (공공데이터포털, 무료)
- 아파트 분양공고는 공공분양이든 민간분양이든 모두 청약홈을 통해 접수되므로, API 하나로 **공공 + 민간을 함께** 받아볼 수 있어요.
- **새로 올라온 공고만** 보냅니다 (청약접수가 아직 끝나지 않은 공고 중, 한 번도 알려주지 않은 것만). 매일 같은 공고를 반복해서 보내지 않아요.
- 보낸 공고 목록은 `state/notified.json`에 저장되어 다음 실행 때도 중복 발송을 막습니다.
- **비용**: 공공데이터포털, 텔레그램 봇 API, GitHub Actions 모두 무료입니다.

---

## ⚙️ 처음 한 번만 설정하면 됩니다

### 1단계. 공공데이터포털 API 키 발급

1. [data.go.kr](https://www.data.go.kr) 에서 회원가입 후 로그인합니다.
2. [한국부동산원_청약Home 분양정보 조회 서비스](https://www.data.go.kr/data/15098547/openapi.do) 페이지에서 **활용신청** 버튼을 누릅니다.
   - 활용 목적 등은 자유롭게 작성하면 됩니다 (개인 알림용 등).
3. 승인되면(보통 몇 시간 이내) **마이페이지 → 데이터 활용 → Open API → 개발계정**에서 **일반 인증키(Decoding)** 값을 확인해 복사합니다.
   - 이 값이 `APPLYHOME_API_KEY` 입니다.

### 2단계. 텔레그램 봇 준비

`english-telegram`에서 이미 봇을 만들어 두었다면 같은 `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID`를 그대로 써도 됩니다. 처음이라면:

1. 텔레그램에서 **@BotFather** 검색 → `/newbot` → 봇 이름/사용자명 설정 → **토큰** 복사.
2. 만든 봇과 대화창을 열고 아무 메시지나 보냅니다(예: `hi`). (봇이 먼저 말을 걸 수 없어서 필요한 단계입니다.)
3. **@userinfobot** 검색 → `/start` → 알려주는 숫자 **ID**가 `TELEGRAM_CHAT_ID` 입니다.

### 3단계. GitHub에 비밀값(Secrets) 등록

이 저장소의 **Settings → Secrets and variables → Actions → New repository secret** 에서 3개를 등록합니다.

| Name | 값 |
|------|------|
| `APPLYHOME_API_KEY` | 1단계에서 받은 공공데이터포털 인증키 (Decoding 값) |
| `TELEGRAM_BOT_TOKEN` | 2단계에서 받은 봇 토큰 |
| `TELEGRAM_CHAT_ID` | 2단계에서 받은 숫자 ID |

### 4단계. 스케줄 활성화 (중요)

GitHub Actions의 **정기 실행(cron)은 기본 브랜치(main)에 있는 워크플로우만 작동**합니다. 이 브랜치를 **`main`에 병합**해야 매일 자동 발송이 시작됩니다.

---

## ▶️ 바로 테스트해 보기

- **GitHub에서:** 저장소의 **Actions** 탭 → **Daily Real Estate Presale Alerts (Telegram)** 선택 → **Run workflow**.
  (이 버튼은 워크플로우가 `main` 브랜치에 있을 때 보입니다.)
- **내 컴퓨터에서:**
  ```bash
  cd realestate-telegram
  APPLYHOME_API_KEY=내키 TELEGRAM_BOT_TOKEN=내토큰 TELEGRAM_CHAT_ID=내아이디 python3 send_presale.py
  ```
- **전송 없이 미리보기만** (텔레그램 키 불필요, 현재 진행중인 공고 전체를 콘솔에 출력):
  ```bash
  APPLYHOME_API_KEY=내키 python3 send_presale.py --preview
  ```
  ⚠️ 처음 API 키를 등록했다면 **`--preview`로 먼저 정상 동작(에러 없이 목록이 출력되는지)을 확인**해 보는 걸 추천합니다.

---

## 🔧 자주 바꾸는 설정

### 보내는 시간 바꾸기
`.github/workflows/daily-presale.yml`의 `cron` 값을 수정하세요. **UTC 기준**이라 한국 시간 − 9시간입니다. (기본값: 매일 08:00 KST)

### 지역 바꾸기
`applyhome_api.py`의 `TARGET_REGIONS = ("서울", "경기")` 를 원하는 시/도 이름으로 바꾸면 됩니다. (청약홈에서 쓰는 축약 표기: 서울/부산/대구/인천/광주/대전/울산/세종/경기/강원/충북/충남/전북/전남/경북/경남/제주)

### 공공/민간 분류 기준
`applyhome_api.py`의 `PUBLIC_HINTS` 목록(주택상세구분에 포함되면 공공분양으로 표시)에 단어를 추가/삭제해 조정할 수 있습니다. 분류가 애매할 수 있어 메시지에는 원본 구분값(예: 민영/국민/공공 등)도 항상 함께 표시됩니다.

### 발송 이력 보관 기간
`send_presale.py`의 `STATE_TTL_DAYS`(기본 180일) — 이보다 오래된 기록은 자동 정리됩니다.

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `applyhome_api.py` | 청약홈 공공데이터 API 호출, 서울·경기 필터링, 공공/민간 분류 |
| `send_presale.py` | 신규 공고 판별 + 메시지 작성 + 텔레그램 전송 |
| `telegram_utils.py` | 텔레그램 메시지 전송 공용 함수 |
| `state/notified.json` | 이미 보낸 공고 기록 — 자동 갱신 (중복 발송 방지) |
| `../.github/workflows/daily-presale.yml` | 매일 자동 발송 워크플로우 |

---

## ❓ 문제 해결

- **메시지가 안 와요**: ① `--preview`로 먼저 콘솔 출력이 되는지 확인하세요. ② Secret 이름이 정확한지(`APPLYHOME_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`) 확인하세요. ③ 봇에게 먼저 메시지를 보냈는지 확인하세요.
- **"인증키가 유효하지 않습니다" 같은 오류**: 공공데이터포털 활용신청이 아직 승인되지 않았거나, 인증키를 **Encoding** 값으로 잘못 넣은 경우가 많습니다. 마이페이지에서 **Decoding** 값을 다시 복사해 보세요.
- **신규 공고가 계속 0건이에요**: 정상입니다. 새로 올라온 서울·경기 아파트 분양공고가 없으면 조용히 넘어가고(메시지 발송 안 함) 로그에만 "신규 0건"으로 표시됩니다.
- **정해진 시간에 안 와요**: 워크플로우가 `main` 브랜치에 있는지 확인하세요(4단계). GitHub 정기 실행은 부하에 따라 몇 분 늦어질 수 있습니다.
- **API 응답 형식이 문서와 달라진 것 같아요**: 이 API 필드는 공공데이터포털 공식 문서를 기준으로 작성했지만, 만약 오류가 발생하면 `--preview` 실행 시 나오는 오류 메시지(원본 응답 일부 포함)를 알려주세요.
