# 📚 매일 영어 학습 (텔레그램 자동 발송)

매일 텔레그램으로 **말하기 중심** 영어 훈련을 자동으로 보내주는 자동화입니다. "읽기"가 아니라 **입으로 말하게** 만드는 게 목표예요. 하루 세 번:

- 🗣️ **오늘의 말하기** (아침 9시) — **30초 질문**에 직접 답하고, 모범답안을 소리 내어 따라 말해요(섀도잉). **중1 → 고3 6단계**, 봇에게 **`up`/`down`** 을 보내면 한 학년씩 오르내려요. (학년 자동 저장)
- ☀️ **오늘의 패턴** (낮 1시) — 회화 핵심 문장 패턴 1개를 **내 주제(일상·투자)로 바꿔 5번씩** 말해요 (문장 자동화).
- 🇰🇷➡️🇬🇧 **한→영 말하기** (저녁 8시) — 한국어 문장을 보고 **먼저 직접 영어로 말한 뒤** 정답을 확인해요 (한국어→영어 출력 훈련).

공통:
- 주제는 **일상 + 투자/시장** 으로 맞췄어요.
- 각 메시지에 **음성(MP3)** 첨부 — 따라 말하기(섀도잉)용. 무료(`gtts`).
- 원칙: **짧게, 틀려도, 바로, 소리 내어.** (완성도보다 반응속도)
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
- 오늘의 말하기(아침): `.github/workflows/daily-english.yml`
- 오늘의 패턴(낮): `.github/workflows/daily-verb.yml`
- 한→영 말하기(저녁): `.github/workflows/daily-lesson.yml`

각 파일의 `cron` 값을 수정하세요. **UTC 기준**이라 한국 시간 − 9시간입니다.

| 받고 싶은 시간 (KST) | cron 값 |
|------|------|
| 오전 9시 (말하기 기본) | `0 0 * * *` |
| 낮 1시 (패턴 기본) | `0 4 * * *` |
| 저녁 8시 (한→영 기본) | `0 11 * * *` |
| 밤 10시 | `0 13 * * *` |

### 콘텐츠 추가·수정하기
- 오늘의 말하기: `conversation_levels.py` 의 `GRADES` (학년별 `dialogues`)
- 오늘의 패턴: `patterns.py` 의 `PATTERNS`
- 한→영 말하기: `ke_drills.py` 의 `KE_SETS`

같은 형식으로 항목을 추가하면 자동으로 포함됩니다.

### 회화 레벨(학년) 관련
- 봇에게 **`up`** 보내기 → 다음 발송 때 한 학년 ⬆️ / **`down`** → 한 학년 ⬇️
- 현재 학년은 `state/conversation_state.json` 의 `grade_index`(0=중1 … 5=고3)에 저장돼요. 직접 숫자를 바꿔 원하는 학년에서 시작할 수도 있어요.
- ⚠️ 레벨 저장이 안 되면(항상 같은 학년) 저장소 **Settings → Actions → General → Workflow permissions** 를 **"Read and write"** 로 설정하세요.

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `conversation_levels.py` | 오늘의 말하기 6단계 중1~고3 (콘텐츠) |
| `patterns.py` | 오늘의 패턴 29개 (콘텐츠) |
| `ke_drills.py` | 한→영 말하기 24세트 (콘텐츠) |
| `telegram_utils.py` | 텔레그램 전송·음성(TTS)·응답읽기 공용 함수 |
| `send_conversation.py` | 오늘의 말하기 전송 + up/down 레벨 조정 |
| `send_pattern.py` | 오늘의 패턴 전송 |
| `send_ke.py` | 한→영 말하기 전송 (정답 스포일러) |
| `state/conversation_state.json` | 현재 말하기 학년(레벨) 저장 — 자동 갱신 |
| `scenarios.py` · `verbs.py` · `lessons.py` 등 | (예전) 여행·동사·기초 콘텐츠 — 지금은 미사용, 보관용 |
| `../.github/workflows/daily-english.yml` | 오늘의 말하기 자동 발송 (아침) |
| `../.github/workflows/daily-verb.yml` | 오늘의 패턴 자동 발송 (낮) |
| `../.github/workflows/daily-lesson.yml` | 한→영 말하기 자동 발송 (저녁) |

---

## ❓ 문제 해결

- **메시지가 안 와요**: ① 2단계에서 내 봇에게 메시지를 먼저 보냈는지, ② Secret 이름이 정확한지(`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`), ③ Actions 탭의 실행 로그에 오류가 없는지 확인하세요.
- **정해진 시간에 안 와요**: 워크플로우가 `main` 브랜치에 있는지 확인하세요 (4단계). GitHub의 정기 실행은 부하에 따라 몇 분 늦어질 수 있습니다.
- **`chat not found` 오류**: 봇에게 먼저 말을 걸지 않았거나 `TELEGRAM_CHAT_ID`가 틀린 경우입니다.
