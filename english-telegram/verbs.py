# -*- coding: utf-8 -*-
"""
오늘의 동사 — 회화에 자주 쓰이는 핵심 동사 60개 (빈도순).

매일 하나씩 순서대로 외웁니다. 각 동사:
{
    "verb": "동사 원형",
    "ko": "뜻",
    "forms": "원형 → 과거 → 과거분사",
    "reg": "규칙(-ed) 또는 불규칙",
    "examples": [{"en": "예문", "ko": "뜻"}],   # 2개
    "phrases": [{"en": "자주 쓰는 표현", "ko": "뜻"}],  # 0~2개
}
"""

VERBS = [
    {
        "verb": "be", "ko": "~이다 · ~에 있다", "forms": "be → was/were → been", "reg": "불규칙",
        "examples": [
            {"en": "I am happy.", "ko": "나는 행복해요."},
            {"en": "Where were you?", "ko": "어디 있었어요?"},
        ],
        "phrases": [{"en": "be careful", "ko": "조심하다"}],
    },
    {
        "verb": "have", "ko": "가지다 · 먹다", "forms": "have → had → had", "reg": "불규칙",
        "examples": [
            {"en": "Do you have time?", "ko": "시간 있어요?"},
            {"en": "I have a question.", "ko": "질문이 있어요."},
        ],
        "phrases": [{"en": "have to", "ko": "~해야 한다"}, {"en": "have lunch", "ko": "점심을 먹다"}],
    },
    {
        "verb": "do", "ko": "하다", "forms": "do → did → done", "reg": "불규칙",
        "examples": [
            {"en": "What do you do?", "ko": "무슨 일 하세요?"},
            {"en": "I did my best.", "ko": "최선을 다했어요."},
        ],
        "phrases": [{"en": "do the dishes", "ko": "설거지를 하다"}],
    },
    {
        "verb": "go", "ko": "가다", "forms": "go → went → gone", "reg": "불규칙",
        "examples": [
            {"en": "Let's go home.", "ko": "집에 가요."},
            {"en": "I went to school.", "ko": "나는 학교에 갔어요."},
        ],
        "phrases": [{"en": "go out", "ko": "외출하다"}, {"en": "go back", "ko": "돌아가다"}],
    },
    {
        "verb": "get", "ko": "얻다 · 받다 · 도착하다", "forms": "get → got → gotten", "reg": "불규칙",
        "examples": [
            {"en": "I got your message.", "ko": "네 메시지 받았어요."},
            {"en": "How can I get there?", "ko": "거기 어떻게 가요?"},
        ],
        "phrases": [{"en": "get up", "ko": "(잠자리에서) 일어나다"}, {"en": "get a taxi", "ko": "택시를 잡다"}],
    },
    {
        "verb": "make", "ko": "만들다 · ~하게 하다", "forms": "make → made → made", "reg": "불규칙",
        "examples": [
            {"en": "I made dinner.", "ko": "내가 저녁을 만들었어요."},
            {"en": "You make me happy.", "ko": "당신은 나를 행복하게 해요."},
        ],
        "phrases": [{"en": "make a mistake", "ko": "실수하다"}, {"en": "make a decision", "ko": "결정하다"}],
    },
    {
        "verb": "take", "ko": "가지고 가다 · (교통수단을) 타다 · (시간이) 걸리다", "forms": "take → took → taken", "reg": "불규칙",
        "examples": [
            {"en": "Take this, please.", "ko": "이거 가져가세요."},
            {"en": "I took the bus.", "ko": "나는 버스를 탔어요."},
        ],
        "phrases": [{"en": "take a break", "ko": "쉬다"}, {"en": "take a photo", "ko": "사진을 찍다"}],
    },
    {
        "verb": "come", "ko": "오다", "forms": "come → came → come", "reg": "불규칙",
        "examples": [
            {"en": "Come here, please.", "ko": "이리 와요."},
            {"en": "She came late.", "ko": "그녀는 늦게 왔어요."},
        ],
        "phrases": [{"en": "come back", "ko": "돌아오다"}, {"en": "come in", "ko": "들어오다"}],
    },
    {
        "verb": "see", "ko": "보다 · 알다", "forms": "see → saw → seen", "reg": "불규칙",
        "examples": [
            {"en": "I see.", "ko": "알겠어요 / 그렇군요."},
            {"en": "I saw him yesterday.", "ko": "어제 그를 봤어요."},
        ],
        "phrases": [{"en": "See you later.", "ko": "나중에 봐요."}],
    },
    {
        "verb": "want", "ko": "원하다", "forms": "want → wanted → wanted", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I want some water.", "ko": "물 좀 주세요(원해요)."},
            {"en": "Do you want to go?", "ko": "갈래요?"},
        ],
        "phrases": [{"en": "want to", "ko": "~하고 싶다"}],
    },
    {
        "verb": "know", "ko": "알다", "forms": "know → knew → known", "reg": "불규칙",
        "examples": [
            {"en": "I don't know.", "ko": "몰라요."},
            {"en": "I know him well.", "ko": "그를 잘 알아요."},
        ],
        "phrases": [{"en": "I know what you mean.", "ko": "무슨 말인지 알아요."}],
    },
    {
        "verb": "think", "ko": "생각하다", "forms": "think → thought → thought", "reg": "불규칙",
        "examples": [
            {"en": "I think so.", "ko": "그런 것 같아요."},
            {"en": "Let me think.", "ko": "생각 좀 해볼게요."},
        ],
        "phrases": [{"en": "think about", "ko": "~에 대해 생각하다"}],
    },
    {
        "verb": "like", "ko": "좋아하다", "forms": "like → liked → liked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I like it.", "ko": "마음에 들어요."},
            {"en": "Do you like coffee?", "ko": "커피 좋아해요?"},
        ],
        "phrases": [{"en": "would like", "ko": "~을 원하다 (정중)"}],
    },
    {
        "verb": "need", "ko": "필요하다", "forms": "need → needed → needed", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I need help.", "ko": "도움이 필요해요."},
            {"en": "You need to rest.", "ko": "당신은 쉬어야 해요."},
        ],
        "phrases": [{"en": "need to", "ko": "~할 필요가 있다"}],
    },
    {
        "verb": "say", "ko": "말하다", "forms": "say → said → said", "reg": "불규칙",
        "examples": [
            {"en": "What did you say?", "ko": "뭐라고 했어요?"},
            {"en": "She said yes.", "ko": "그녀는 그렇다고 했어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "tell", "ko": "말해 주다 · 알려 주다", "forms": "tell → told → told", "reg": "불규칙",
        "examples": [
            {"en": "Tell me, please.", "ko": "말해 주세요."},
            {"en": "I told you.", "ko": "내가 말했잖아요."},
        ],
        "phrases": [{"en": "tell the truth", "ko": "사실을 말하다"}],
    },
    {
        "verb": "give", "ko": "주다", "forms": "give → gave → given", "reg": "불규칙",
        "examples": [
            {"en": "Give me a minute.", "ko": "잠깐만요."},
            {"en": "He gave me a gift.", "ko": "그가 선물을 줬어요."},
        ],
        "phrases": [{"en": "give up", "ko": "포기하다"}],
    },
    {
        "verb": "ask", "ko": "묻다 · 부탁하다", "forms": "ask → asked → asked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Can I ask you something?", "ko": "뭐 좀 물어봐도 돼요?"},
            {"en": "She asked a question.", "ko": "그녀가 질문을 했어요."},
        ],
        "phrases": [{"en": "ask for", "ko": "~을 요청하다"}],
    },
    {
        "verb": "look", "ko": "보다 · ~해 보이다", "forms": "look → looked → looked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Look at this!", "ko": "이것 좀 봐요!"},
            {"en": "You look great.", "ko": "좋아 보여요."},
        ],
        "phrases": [{"en": "look for", "ko": "~을 찾다"}, {"en": "look at", "ko": "~을 보다"}],
    },
    {
        "verb": "find", "ko": "찾다 · 알아내다", "forms": "find → found → found", "reg": "불규칙",
        "examples": [
            {"en": "I can't find my keys.", "ko": "열쇠를 못 찾겠어요."},
            {"en": "Did you find it?", "ko": "찾았어요?"},
        ],
        "phrases": [{"en": "find out", "ko": "알아내다"}],
    },
    {
        "verb": "use", "ko": "사용하다", "forms": "use → used → used", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Can I use your phone?", "ko": "전화 좀 써도 돼요?"},
            {"en": "I used it once.", "ko": "한 번 써봤어요."},
        ],
        "phrases": [{"en": "used to", "ko": "예전에 ~하곤 했다"}],
    },
    {
        "verb": "work", "ko": "일하다 · 작동하다", "forms": "work → worked → worked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I work in Seoul.", "ko": "나는 서울에서 일해요."},
            {"en": "It doesn't work.", "ko": "그거 작동이 안 돼요."},
        ],
        "phrases": [{"en": "work out", "ko": "운동하다 · 잘 풀리다"}],
    },
    {
        "verb": "call", "ko": "전화하다 · 부르다", "forms": "call → called → called", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Call me later.", "ko": "나중에 전화해요."},
            {"en": "I called you twice.", "ko": "두 번 전화했어요."},
        ],
        "phrases": [{"en": "call back", "ko": "다시 전화하다"}],
    },
    {
        "verb": "try", "ko": "시도하다 · 노력하다", "forms": "try → tried → tried", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Try again.", "ko": "다시 해봐요."},
            {"en": "I tried my best.", "ko": "최선을 다했어요."},
        ],
        "phrases": [{"en": "try on", "ko": "(옷을) 입어 보다"}],
    },
    {
        "verb": "feel", "ko": "느끼다 · 기분이 ~하다", "forms": "feel → felt → felt", "reg": "불규칙",
        "examples": [
            {"en": "I feel good today.", "ko": "오늘 기분이 좋아요."},
            {"en": "How do you feel?", "ko": "기분이 어때요?"},
        ],
        "phrases": [{"en": "feel like", "ko": "~하고 싶다 · ~인 것 같다"}],
    },
    {
        "verb": "help", "ko": "돕다", "forms": "help → helped → helped", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Can you help me?", "ko": "도와줄 수 있어요?"},
            {"en": "He helped a lot.", "ko": "그가 많이 도와줬어요."},
        ],
        "phrases": [{"en": "help out", "ko": "거들다 · 도와주다"}],
    },
    {
        "verb": "talk", "ko": "이야기하다", "forms": "talk → talked → talked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Let's talk.", "ko": "얘기 좀 해요."},
            {"en": "We talked for hours.", "ko": "우리는 몇 시간 동안 얘기했어요."},
        ],
        "phrases": [{"en": "talk about", "ko": "~에 대해 이야기하다"}],
    },
    {
        "verb": "speak", "ko": "말하다 · (언어를) 구사하다", "forms": "speak → spoke → spoken", "reg": "불규칙",
        "examples": [
            {"en": "Do you speak English?", "ko": "영어 할 줄 아세요?"},
            {"en": "Please speak slowly.", "ko": "천천히 말해 주세요."},
        ],
        "phrases": [{"en": "speak up", "ko": "더 크게 말하다"}],
    },
    {
        "verb": "start", "ko": "시작하다", "forms": "start → started → started", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Let's start.", "ko": "시작합시다."},
            {"en": "It started to rain.", "ko": "비가 오기 시작했어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "stop", "ko": "멈추다 · 그만두다", "forms": "stop → stopped → stopped", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Stop, please.", "ko": "멈춰 주세요."},
            {"en": "The bus stopped.", "ko": "버스가 멈췄어요."},
        ],
        "phrases": [{"en": "stop by", "ko": "잠깐 들르다"}],
    },
    {
        "verb": "eat", "ko": "먹다", "forms": "eat → ate → eaten", "reg": "불규칙",
        "examples": [
            {"en": "Let's eat.", "ko": "먹읍시다."},
            {"en": "Did you eat?", "ko": "밥 먹었어요?"},
        ],
        "phrases": [{"en": "eat out", "ko": "외식하다"}],
    },
    {
        "verb": "drink", "ko": "마시다", "forms": "drink → drank → drunk", "reg": "불규칙",
        "examples": [
            {"en": "Drink some water.", "ko": "물 좀 마셔요."},
            {"en": "I drank too much coffee.", "ko": "커피를 너무 많이 마셨어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "buy", "ko": "사다", "forms": "buy → bought → bought", "reg": "불규칙",
        "examples": [
            {"en": "I want to buy this.", "ko": "이거 사고 싶어요."},
            {"en": "She bought a car.", "ko": "그녀는 차를 샀어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "pay", "ko": "지불하다", "forms": "pay → paid → paid", "reg": "불규칙",
        "examples": [
            {"en": "Can I pay by card?", "ko": "카드로 계산해도 돼요?"},
            {"en": "I already paid.", "ko": "이미 계산했어요."},
        ],
        "phrases": [{"en": "pay for", "ko": "~의 값을 치르다"}],
    },
    {
        "verb": "meet", "ko": "만나다", "forms": "meet → met → met", "reg": "불규칙",
        "examples": [
            {"en": "Nice to meet you.", "ko": "만나서 반가워요."},
            {"en": "We met yesterday.", "ko": "우리는 어제 만났어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "wait", "ko": "기다리다", "forms": "wait → waited → waited", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Wait a moment, please.", "ko": "잠시만 기다려 주세요."},
            {"en": "I waited an hour.", "ko": "한 시간 기다렸어요."},
        ],
        "phrases": [{"en": "wait for", "ko": "~을 기다리다"}],
    },
    {
        "verb": "open", "ko": "열다 · 열리다", "forms": "open → opened → opened", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Open the door, please.", "ko": "문 좀 열어 주세요."},
            {"en": "The store opens at nine.", "ko": "가게는 9시에 열어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "close", "ko": "닫다 · 닫히다", "forms": "close → closed → closed", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Please close the window.", "ko": "창문 좀 닫아 주세요."},
            {"en": "The shop is closed.", "ko": "가게가 닫혔어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "walk", "ko": "걷다", "forms": "walk → walked → walked", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Let's walk.", "ko": "걸어가요."},
            {"en": "I walked home.", "ko": "나는 집에 걸어갔어요."},
        ],
        "phrases": [{"en": "go for a walk", "ko": "산책하러 가다"}],
    },
    {
        "verb": "run", "ko": "달리다 · 운영하다", "forms": "run → ran → run", "reg": "불규칙",
        "examples": [
            {"en": "I run every morning.", "ko": "나는 매일 아침 달려요."},
            {"en": "She ran very fast.", "ko": "그녀는 아주 빨리 달렸어요."},
        ],
        "phrases": [{"en": "run out of", "ko": "~이 다 떨어지다"}],
    },
    {
        "verb": "put", "ko": "놓다 · 두다", "forms": "put → put → put", "reg": "불규칙",
        "examples": [
            {"en": "Put it here, please.", "ko": "여기 놓아 주세요."},
            {"en": "I put it on the table.", "ko": "탁자 위에 뒀어요."},
        ],
        "phrases": [{"en": "put on", "ko": "(옷을) 입다 · 착용하다"}],
    },
    {
        "verb": "keep", "ko": "계속 ~하다 · 유지하다", "forms": "keep → kept → kept", "reg": "불규칙",
        "examples": [
            {"en": "Keep the change.", "ko": "잔돈은 가지세요."},
            {"en": "Keep trying.", "ko": "계속 시도해 봐요."},
        ],
        "phrases": [{"en": "keep going", "ko": "계속 나아가다"}],
    },
    {
        "verb": "let", "ko": "~하게 하다 · 허락하다", "forms": "let → let → let", "reg": "불규칙",
        "examples": [
            {"en": "Let me see.", "ko": "어디 봐요 / 생각 좀."},
            {"en": "Let me know.", "ko": "알려 주세요."},
        ],
        "phrases": [{"en": "Let's ~", "ko": "~하자"}],
    },
    {
        "verb": "leave", "ko": "떠나다 · 두고 가다", "forms": "leave → left → left", "reg": "불규칙",
        "examples": [
            {"en": "I have to leave now.", "ko": "이제 가봐야 해요."},
            {"en": "She left early.", "ko": "그녀는 일찍 떠났어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "bring", "ko": "가져오다 · 데려오다", "forms": "bring → brought → brought", "reg": "불규칙",
        "examples": [
            {"en": "Bring your friend.", "ko": "친구 데려와요."},
            {"en": "I brought lunch.", "ko": "점심 가져왔어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "send", "ko": "보내다", "forms": "send → sent → sent", "reg": "불규칙",
        "examples": [
            {"en": "Send me the file, please.", "ko": "파일 좀 보내 주세요."},
            {"en": "I sent it already.", "ko": "이미 보냈어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "read", "ko": "읽다", "forms": "read → read → read", "reg": "불규칙 (발음: 리드 → 레드)",
        "examples": [
            {"en": "I read books every day.", "ko": "나는 매일 책을 읽어요."},
            {"en": "I read it yesterday.", "ko": "어제 그걸 읽었어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "write", "ko": "쓰다", "forms": "write → wrote → written", "reg": "불규칙",
        "examples": [
            {"en": "Write your name here.", "ko": "여기에 이름을 쓰세요."},
            {"en": "She wrote a letter.", "ko": "그녀는 편지를 썼어요."},
        ],
        "phrases": [{"en": "write down", "ko": "받아 적다"}],
    },
    {
        "verb": "learn", "ko": "배우다", "forms": "learn → learned → learned", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I want to learn English.", "ko": "영어를 배우고 싶어요."},
            {"en": "I learned a lot.", "ko": "많이 배웠어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "understand", "ko": "이해하다", "forms": "understand → understood → understood", "reg": "불규칙",
        "examples": [
            {"en": "I understand.", "ko": "이해했어요."},
            {"en": "I don't understand.", "ko": "이해가 안 돼요."},
        ],
        "phrases": [],
    },
    {
        "verb": "remember", "ko": "기억하다", "forms": "remember → remembered → remembered", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I remember you.", "ko": "당신을 기억해요."},
            {"en": "Remember to call me.", "ko": "잊지 말고 전화해요."},
        ],
        "phrases": [],
    },
    {
        "verb": "forget", "ko": "잊다", "forms": "forget → forgot → forgotten", "reg": "불규칙",
        "examples": [
            {"en": "Don't forget.", "ko": "잊지 마세요."},
            {"en": "I forgot my password.", "ko": "비밀번호를 잊어버렸어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "love", "ko": "사랑하다 · 정말 좋아하다", "forms": "love → loved → loved", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I love this place.", "ko": "이곳이 정말 좋아요."},
            {"en": "She loves music.", "ko": "그녀는 음악을 사랑해요."},
        ],
        "phrases": [],
    },
    {
        "verb": "enjoy", "ko": "즐기다", "forms": "enjoy → enjoyed → enjoyed", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Enjoy your meal.", "ko": "맛있게 드세요."},
            {"en": "I enjoyed the trip.", "ko": "여행이 즐거웠어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "live", "ko": "살다", "forms": "live → lived → lived", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I live in Seoul.", "ko": "나는 서울에 살아요."},
            {"en": "They lived in Busan.", "ko": "그들은 부산에 살았어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "play", "ko": "놀다 · (운동·악기를) 하다", "forms": "play → played → played", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Let's play soccer.", "ko": "축구 하자."},
            {"en": "She plays the piano.", "ko": "그녀는 피아노를 쳐요."},
        ],
        "phrases": [],
    },
    {
        "verb": "watch", "ko": "보다 · 지켜보다", "forms": "watch → watched → watched", "reg": "규칙(-ed)",
        "examples": [
            {"en": "I watch TV at night.", "ko": "나는 밤에 TV를 봐요."},
            {"en": "We watched a movie.", "ko": "우리는 영화를 봤어요."},
        ],
        "phrases": [{"en": "watch out", "ko": "조심하다"}],
    },
    {
        "verb": "listen", "ko": "듣다", "forms": "listen → listened → listened", "reg": "규칙(-ed)",
        "examples": [
            {"en": "Listen to me, please.", "ko": "제 말 좀 들어 보세요."},
            {"en": "I listened carefully.", "ko": "주의 깊게 들었어요."},
        ],
        "phrases": [{"en": "listen to", "ko": "~을 듣다"}],
    },
    {
        "verb": "sleep", "ko": "자다", "forms": "sleep → slept → slept", "reg": "불규칙",
        "examples": [
            {"en": "I need to sleep.", "ko": "자야 해요."},
            {"en": "I slept well.", "ko": "잘 잤어요."},
        ],
        "phrases": [],
    },
    {
        "verb": "happen", "ko": "일어나다 · 생기다", "forms": "happen → happened → happened", "reg": "규칙(-ed)",
        "examples": [
            {"en": "What happened?", "ko": "무슨 일이에요?"},
            {"en": "It happened so fast.", "ko": "너무 빨리 일어났어요."},
        ],
        "phrases": [],
    },
]
