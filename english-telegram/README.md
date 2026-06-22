# 📚 매일 여행 영어 회화 (텔레그램 자동 발송)

매일 텔레그램으로 영어 공부거리를 자동으로 보내주는 자동화입니다. 두 가지를 보냅니다:

- 🌍 **여행 영어 회화** (아침 9시) — 공항·호텔·식당·길찾기 등 30개 여행 시나리오. `대화 → 핵심 표현 → 팁`. 한 달 주기로 순환.
- 📘 **기초 영어 코스** (저녁 8시) — 인사부터 시제까지 45과를 **순서대로** 하루 한 과씩. `설명 → 핵심 패턴 → 예문 → 연습문제(정답 가림)`. 완전 초보용.

공통 특징:
- **발음 듣기**: 텍스트와 함께 영어를 읽어주는 **음성(MP3)** 도 보내드려요. 탭하면 재생됩니다. (무료 TTS `gtts` 사용)
- **비용**: 텔레그램 봇 API, GitHub Actions 모두 무료입니다.

---

## ⚙️ 처음 한 번만 설정하면 됩니다 (약 5분)

### 1단계. 텔레그램 봇 만들기 (봇 토큰 받기)

1. 텔레그램에서 **@BotFather** 를 검색해 대화를 시작합니다.
2. `/newbot` 입력 → 봇 이름과 사용자명(`...bot`으로 끝나야 함)을 정합니다.
3. 그러면 아래처럼 생긴 **토큰**을 줍니다. 복사해 두세요.
   ```
   123456789:AAEexampleexampleexampleexampleexample
   ```

### 2단계. 내 채팅 ID 알아내기

1. 방금 만든 **내 봇**과의 대화창을 열고 아무 메시지나 하나 보냅니다 (예: `hi`).
   - ⚠️ 이 단계를 안 하면 봇이 나에게 먼저 말을 걸 수 없습니다.
2. 텔레그램에서 **@userinfobot** 을 검색해 `/start` 를 누르면 내 **숫자 ID**(예: `987654321`)를 알려줍니다.
   - 이 숫자가 `TELEGRAM_CHAT_ID` 입니다.

### 3단계. GitHub에 비밀값(Secrets) 등록

이 저장소(GitHub) 페이지에서:

1. **Settings** 탭 → 왼쪽 메뉴 **Secrets and variables** → **Actions** 로 이동
2. **New repository secret** 버튼을 눌러 아래 두 개를 등록합니다.

   | Name | Secret (값) |
   |------|------|
   | `TELEGRAM_BOT_TOKEN` | 1단계에서 받은 봇 토큰 |
   | `TELEGRAM_CHAT_ID` | 2단계에서 받은 숫자 ID |

### 4단계. 스케줄 활성화 (중요)

GitHub Actions의 **정기 실행(cron)은 기본 브랜치(main)에 있는 워크플로우만 작동**합니다.
지금 이 파일들은 작업 브랜치에 있으므로, **`main` 브랜치에 병합(merge)** 해야 매일 자동 발송이 시작됩니다.

> 병합 전이라도 아래 "바로 테스트해 보기"로 동작을 확인할 수 있습니다.

---

## ▶️ 바로 테스트해 보기

설정이 끝났으면 기다리지 않고 바로 한 통 받아볼 수 있습니다.

- **방법 A (GitHub에서):** 저장소의 **Actions** 탭 → 왼쪽에서 **Daily English (Telegram)** 선택
  → 오른쪽 **Run workflow** 버튼 클릭. 잠시 후 텔레그램으로 메시지가 옵니다.
  - (이 버튼은 워크플로우가 `main` 브랜치에 있을 때 보입니다.)

- **방법 B (내 컴퓨터에서):**
  ```bash
  cd english-telegram
  TELEGRAM_BOT_TOKEN=내토큰 TELEGRAM_CHAT_ID=내아이디 python3 send_daily.py
  ```

전송 없이 내용만 미리 보고 싶다면:
```bash
python3 send_daily.py --preview 0     # 0번 시나리오 미리보기
python3 send_daily.py --preview-all   # 30개 전체 미리보기
```

---

## 🔧 자주 바꾸는 설정

### 보내는 시간 바꾸기
- 회화(아침): `.github/workflows/daily-english.yml`
- 기초 코스(저녁): `.github/workflows/daily-lesson.yml`

각 파일의 `cron` 값을 수정하세요. **UTC 기준**이라 한국 시간 − 9시간입니다.

| 받고 싶은 시간 (KST) | cron 값 |
|------|------|
| 오전 7시 | `0 22 * * *` |
| 오전 9시 (회화 기본) | `0 0 * * *` |
| 저녁 8시 (기초 기본) | `0 11 * * *` |
| 밤 10시 | `0 13 * * *` |

### 콘텐츠 추가·수정하기
- 회화: `scenarios.py` 의 `SCENARIOS`
- 기초 코스: `lessons.py` 의 `LESSONS`

같은 형식으로 항목을 추가하면 자동으로 포함됩니다.

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `scenarios.py` | 여행 영어 회화 30개 (콘텐츠) |
| `lessons.py` | 기초 영어 코스 45과 (콘텐츠) |
| `telegram_utils.py` | 텔레그램 전송·음성(TTS) 공용 함수 |
| `send_daily.py` | 오늘의 회화를 골라 전송 |
| `send_lesson.py` | 오늘의 기초 과를 골라 전송 |
| `../.github/workflows/daily-english.yml` | 회화 자동 발송 (아침) |
| `../.github/workflows/daily-lesson.yml` | 기초 코스 자동 발송 (저녁) |

---

## ❓ 문제 해결

- **메시지가 안 와요**: ① 2단계에서 내 봇에게 메시지를 먼저 보냈는지, ② Secret 이름이 정확한지(`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`), ③ Actions 탭의 실행 로그에 오류가 없는지 확인하세요.
- **정해진 시간에 안 와요**: 워크플로우가 `main` 브랜치에 있는지 확인하세요 (4단계). GitHub의 정기 실행은 부하에 따라 몇 분 늦어질 수 있습니다.
- **`chat not found` 오류**: 봇에게 먼저 말을 걸지 않았거나 `TELEGRAM_CHAT_ID`가 틀린 경우입니다.
