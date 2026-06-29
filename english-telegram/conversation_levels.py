# -*- coding: utf-8 -*-
"""
오늘의 말하기 (단계별) — 중1 → 고3 (6단계). 말하기(output) 훈련용.

각 카드 = 30초 말하기 질문(speak_q) + 따라 말할 모범 대화(turns).
주제는 '일상 + 투자/시장'으로 회원님 생활에 맞췄습니다.
레벨이 오를수록 문장·표현이 어려워집니다. (봇에게 up/down으로 학년 조정)
"""

GRADES = [
    {
        "grade": "중학 1학년",
        "focus": "짧은 일상·시장 한마디 (현재/과거 기본)",
        "dialogues": [
            {
                "title": "오늘 하루",
                "speak_q": {"en": "What did you do today?", "ko": "오늘 뭐 했어요?"},
                "turns": [
                    {"s": "A", "en": "What did you do today?", "ko": "오늘 뭐 했어?"},
                    {"s": "B", "en": "I read some news and studied English.", "ko": "뉴스 좀 읽고 영어 공부했어."},
                    {"s": "A", "en": "That sounds productive.", "ko": "알차게 보냈네."},
                    {"s": "B", "en": "Yeah, it was a good day.", "ko": "응, 괜찮은 하루였어."},
                ],
            },
            {
                "title": "오늘의 시장",
                "speak_q": {"en": "How was the stock market today?", "ko": "오늘 주식 시장 어땠어요?"},
                "turns": [
                    {"s": "A", "en": "Did you check the market today?", "ko": "오늘 시장 봤어?"},
                    {"s": "B", "en": "Yes, stocks went up.", "ko": "응, 주가 올랐어."},
                    {"s": "A", "en": "That's good news.", "ko": "좋은 소식이네."},
                    {"s": "B", "en": "Yeah, I'm happy about it.", "ko": "응, 기분 좋아."},
                ],
            },
        ],
    },
    {
        "grade": "중학 2학년",
        "focus": "이유·의견 (because / I think)",
        "dialogues": [
            {
                "title": "스트레스 풀기",
                "speak_q": {"en": "What do you do when you feel stressed?", "ko": "스트레스 받으면 뭐 해요?"},
                "turns": [
                    {"s": "A", "en": "You look tired today.", "ko": "오늘 피곤해 보여."},
                    {"s": "B", "en": "I am. I take a walk when I'm stressed.", "ko": "응. 스트레스 받으면 산책해."},
                    {"s": "A", "en": "That's a good habit.", "ko": "좋은 습관이네."},
                    {"s": "B", "en": "It really helps me relax.", "ko": "진짜 마음이 편해져."},
                ],
            },
            {
                "title": "주가가 오른 이유",
                "speak_q": {"en": "Why do you think the market moved today?", "ko": "오늘 시장이 왜 움직였다고 생각해요?"},
                "turns": [
                    {"s": "A", "en": "Why did the stock go up?", "ko": "주가가 왜 올랐어?"},
                    {"s": "B", "en": "Because the earnings were good.", "ko": "실적이 좋았거든."},
                    {"s": "A", "en": "That makes sense.", "ko": "그럴 만하네."},
                    {"s": "B", "en": "I think investors are happy.", "ko": "투자자들이 만족한 것 같아."},
                ],
            },
        ],
    },
    {
        "grade": "중학 3학년",
        "focus": "경험·비교 (현재완료, 비교급)",
        "dialogues": [
            {
                "title": "해본 적 있어?",
                "speak_q": {"en": "Have you ever traveled abroad?", "ko": "해외여행 가본 적 있어요?"},
                "turns": [
                    {"s": "A", "en": "Have you ever traveled abroad?", "ko": "해외여행 가본 적 있어?"},
                    {"s": "B", "en": "Yes, I've been to Japan twice.", "ko": "응, 일본 두 번 가봤어."},
                    {"s": "A", "en": "Which trip was better?", "ko": "어느 쪽이 더 좋았어?"},
                    {"s": "B", "en": "The second one was more relaxing.", "ko": "두 번째가 더 편안했어."},
                ],
            },
            {
                "title": "내 투자 이야기",
                "speak_q": {"en": "What are you interested in investing in?", "ko": "어떤 투자에 관심 있어요?"},
                "turns": [
                    {"s": "A", "en": "Have you invested in semiconductors?", "ko": "반도체에 투자해 봤어?"},
                    {"s": "B", "en": "Yes, I've held them for about a year.", "ko": "응, 1년쯤 들고 있어."},
                    {"s": "A", "en": "How is it going?", "ko": "어떻게 돼 가?"},
                    {"s": "B", "en": "Better than I expected.", "ko": "예상보다 좋아."},
                ],
            },
        ],
    },
    {
        "grade": "고등 1학년",
        "focus": "가정·선호 (would / I'd rather)",
        "dialogues": [
            {
                "title": "만약에",
                "speak_q": {"en": "What would you do if you had a free week?", "ko": "일주일 자유 시간이 생기면 뭐 할래요?"},
                "turns": [
                    {"s": "A", "en": "What would you do if you had a free week?", "ko": "일주일 자유 시간이 생기면 뭐 할 거야?"},
                    {"s": "B", "en": "I'd travel somewhere quiet and read.", "ko": "조용한 데 가서 책 읽을 거야."},
                    {"s": "A", "en": "That sounds nice.", "ko": "좋겠다."},
                    {"s": "B", "en": "I'd rather rest than work, honestly.", "ko": "솔직히 일보다 쉬는 게 낫지."},
                ],
            },
            {
                "title": "시장이 떨어지면",
                "speak_q": {"en": "What would you do if the market dropped 10%?", "ko": "시장이 10% 떨어지면 어떻게 할래요?"},
                "turns": [
                    {"s": "A", "en": "What would you do if the market dropped 10%?", "ko": "시장이 10% 떨어지면 어떻게 할 거야?"},
                    {"s": "B", "en": "I'd probably buy more, honestly.", "ko": "솔직히 더 살 것 같아."},
                    {"s": "A", "en": "That takes nerve.", "ko": "배짱 있네."},
                    {"s": "B", "en": "I'd rather buy low than panic.", "ko": "패닉보다 싸게 사는 게 낫지."},
                ],
            },
        ],
    },
    {
        "grade": "고등 2학년",
        "focus": "추상적 토론 (의견·균형, 더 긴 호흡)",
        "dialogues": [
            {
                "title": "일과 휴식",
                "speak_q": {"en": "How do you balance work and rest?", "ko": "일과 휴식을 어떻게 균형 맞춰요?"},
                "turns": [
                    {"s": "A", "en": "How do you balance work and rest?", "ko": "일과 휴식 균형을 어떻게 맞춰?"},
                    {"s": "B", "en": "I try to set limits, though it's hard.", "ko": "한계를 두려고 해, 어렵긴 하지만."},
                    {"s": "A", "en": "I struggle with that, too.", "ko": "나도 그게 힘들어."},
                    {"s": "B", "en": "The key is taking it one day at a time.", "ko": "하루하루 차근차근 하는 게 비결이야."},
                ],
            },
            {
                "title": "AI 투자는 거품일까",
                "speak_q": {"en": "Do you think AI investment is a bubble? Why?", "ko": "AI 투자가 거품이라고 생각해요? 왜요?"},
                "turns": [
                    {"s": "A", "en": "Do you think AI demand is a bubble?", "ko": "AI 수요가 거품이라고 생각해?"},
                    {"s": "B", "en": "In some ways, but the spending is real.", "ko": "어떤 면에선 그렇지만, 지출은 진짜야."},
                    {"s": "A", "en": "That's a fair point.", "ko": "일리 있는 말이야."},
                    {"s": "B", "en": "I think the long-term trend is solid.", "ko": "장기 추세는 탄탄하다고 봐."},
                ],
            },
        ],
    },
    {
        "grade": "고등 3학년",
        "focus": "미묘한 뉘앙스·관용 표현 (거의 원어민)",
        "dialogues": [
            {
                "title": "올해의 목표",
                "speak_q": {"en": "What's one thing you want to improve this year?", "ko": "올해 개선하고 싶은 것 하나는?"},
                "turns": [
                    {"s": "A", "en": "What's one thing you want to improve this year?", "ko": "올해 개선하고 싶은 거 하나 있어?"},
                    {"s": "B", "en": "Honestly, I want to be more consistent.", "ko": "솔직히, 더 꾸준해지고 싶어."},
                    {"s": "A", "en": "That's a goal I respect.", "ko": "존경스러운 목표네."},
                    {"s": "B", "en": "Small habits add up over time.", "ko": "작은 습관이 쌓이면 커지니까."},
                ],
            },
            {
                "title": "언제 파느냐",
                "speak_q": {"en": "How do you decide when to sell a stock?", "ko": "주식을 언제 팔지 어떻게 정해요?"},
                "turns": [
                    {"s": "A", "en": "I heard you trimmed your tech position.", "ko": "테크 비중 줄였다며."},
                    {"s": "B", "en": "I did. The valuations were getting stretched.", "ko": "응. 밸류에이션이 좀 과해지고 있었어."},
                    {"s": "A", "en": "So you're playing it safe?", "ko": "그럼 안전하게 가는 거야?"},
                    {"s": "B", "en": "I'd rather lock in gains than chase the top.", "ko": "꼭대기 좇느니 수익을 확정하는 게 낫지."},
                ],
            },
        ],
    },
]
