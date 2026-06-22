# -*- coding: utf-8 -*-
"""
단계별(학년별) 영어 회화 — 중학 1학년 → 고등 3학년 (6단계).

레벨이 올라갈수록 문장이 길어지고 시제·표현·뉘앙스가 어려워집니다.
사용자가 봇에게 'up'이라고 답하면 한 학년씩 올라가고, 'down'이면 내려갑니다.
(현재 학년은 state/conversation_state.json 에 저장되어 매일 이어집니다.)

각 학년(grade):
{
    "grade": "학년 이름",
    "focus": "이 단계에서 익히는 것",
    "dialogues": [
        {"title": "주제", "turns": [{"s": "A/B", "en": "영어", "ko": "한국어"}]},
    ],
}
"""

GRADES = [
    {
        "grade": "중학 1학년",
        "focus": "일상 대화 (현재·과거·미래 기본), 짧고 완결된 문장",
        "dialogues": [
            {
                "title": "오늘 하루",
                "turns": [
                    {"s": "A", "en": "How was your day?", "ko": "오늘 하루 어땠어?"},
                    {"s": "B", "en": "It was busy. I had a lot of meetings.", "ko": "바빴어. 회의가 많았어."},
                    {"s": "A", "en": "That sounds tiring.", "ko": "피곤했겠다."},
                    {"s": "B", "en": "Yeah, but it's over now.", "ko": "응, 근데 이제 끝났어."},
                ],
            },
            {
                "title": "주말 계획",
                "turns": [
                    {"s": "A", "en": "Do you have any plans this weekend?", "ko": "이번 주말에 계획 있어?"},
                    {"s": "B", "en": "I'm going to meet some friends. How about you?", "ko": "친구들 만날 거야. 너는?"},
                    {"s": "A", "en": "I'll probably just stay home and relax.", "ko": "난 그냥 집에서 쉴 것 같아."},
                    {"s": "B", "en": "That sounds nice, too.", "ko": "그것도 좋네."},
                ],
            },
        ],
    },
    {
        "grade": "중학 2학년",
        "focus": "조언·이유·의견 (should / because), 자연스러운 맞장구",
        "dialogues": [
            {
                "title": "조언하기",
                "turns": [
                    {"s": "A", "en": "I'm really stressed about my exam.", "ko": "시험 때문에 너무 스트레스 받아."},
                    {"s": "B", "en": "You should take a short break and study again.", "ko": "잠깐 쉬었다가 다시 공부해."},
                    {"s": "A", "en": "You're right. I've been studying all day.", "ko": "맞아. 하루 종일 공부했어."},
                    {"s": "B", "en": "Don't worry, you've prepared a lot.", "ko": "걱정 마, 너 많이 준비했잖아."},
                ],
            },
            {
                "title": "이유 말하기",
                "turns": [
                    {"s": "A", "en": "Why do you like this cafe so much?", "ko": "왜 이 카페를 그렇게 좋아해?"},
                    {"s": "B", "en": "Because it's quiet, and the coffee is great.", "ko": "조용하고 커피가 맛있거든."},
                    {"s": "A", "en": "I agree. It's a good place to work.", "ko": "맞아. 일하기 좋은 곳이야."},
                    {"s": "B", "en": "Exactly. I come here almost every day.", "ko": "그러니까. 거의 매일 와."},
                ],
            },
        ],
    },
    {
        "grade": "중학 3학년",
        "focus": "경험·비교 (현재완료, 비교급), 약속 조율",
        "dialogues": [
            {
                "title": "경험 묻기",
                "turns": [
                    {"s": "A", "en": "Have you ever been to Japan?", "ko": "일본 가본 적 있어?"},
                    {"s": "B", "en": "Yes, I've been there twice.", "ko": "응, 두 번 가봤어."},
                    {"s": "A", "en": "Which city did you like the most?", "ko": "어느 도시가 제일 좋았어?"},
                    {"s": "B", "en": "Kyoto, probably. It's more peaceful than Tokyo.", "ko": "아마 교토. 도쿄보다 더 평화로워."},
                ],
            },
            {
                "title": "약속 변경",
                "turns": [
                    {"s": "A", "en": "I'm sorry, but can we move our plan to Friday?", "ko": "미안한데, 약속 금요일로 옮길 수 있을까?"},
                    {"s": "B", "en": "Sure, Friday actually works better for me.", "ko": "그럼, 나도 사실 금요일이 더 나아."},
                    {"s": "A", "en": "Great. Let's meet at the same place.", "ko": "좋아. 같은 곳에서 만나자."},
                    {"s": "B", "en": "Sounds good. See you then.", "ko": "좋아. 그때 봐."},
                ],
            },
        ],
    },
    {
        "grade": "고등 1학년",
        "focus": "가정·선호 (would / I'd rather), 정중한 반대",
        "dialogues": [
            {
                "title": "만약에",
                "turns": [
                    {"s": "A", "en": "What would you do if you won the lottery?", "ko": "복권에 당첨되면 뭐 할 거야?"},
                    {"s": "B", "en": "I'd travel the world and help my family.", "ko": "세계 여행 하고 가족을 도울 거야."},
                    {"s": "A", "en": "Would you keep working?", "ko": "계속 일은 할 거야?"},
                    {"s": "B", "en": "Honestly, I'm not sure I would.", "ko": "솔직히, 안 할 것 같아."},
                ],
            },
            {
                "title": "정중하게 반대하기",
                "turns": [
                    {"s": "A", "en": "I think we should leave early to avoid traffic.", "ko": "차 막히니까 일찍 출발하는 게 좋겠어."},
                    {"s": "B", "en": "That makes sense, but I'd rather not rush.", "ko": "일리 있는데, 난 서두르고 싶진 않아."},
                    {"s": "A", "en": "Fair enough. Let's leave at noon, then.", "ko": "그래. 그럼 정오에 출발하자."},
                    {"s": "B", "en": "Perfect. That gives us enough time.", "ko": "완벽해. 시간 충분하겠다."},
                ],
            },
        ],
    },
    {
        "grade": "고등 2학년",
        "focus": "추상적 주제 토론 (의견·균형), 더 긴 호흡",
        "dialogues": [
            {
                "title": "기술과 행복",
                "turns": [
                    {"s": "A", "en": "Do you think technology makes us happier?", "ko": "기술이 우리를 더 행복하게 한다고 생각해?"},
                    {"s": "B", "en": "In some ways, yes, but it can also be stressful.", "ko": "어떤 면에선 그렇지만, 스트레스가 되기도 해."},
                    {"s": "A", "en": "I feel the same. It's hard to disconnect these days.", "ko": "나도 그래. 요즘은 (기기에서) 떨어지기가 어려워."},
                    {"s": "B", "en": "True. Balance is the key, I guess.", "ko": "맞아. 균형이 중요한 것 같아."},
                ],
            },
            {
                "title": "일과 삶의 균형",
                "turns": [
                    {"s": "A", "en": "How do you manage work and personal life?", "ko": "일이랑 개인 생활을 어떻게 관리해?"},
                    {"s": "B", "en": "I try to set clear boundaries, though it's not easy.", "ko": "명확한 경계를 두려고 해, 쉽진 않지만."},
                    {"s": "A", "en": "I struggle with that, too.", "ko": "나도 그게 힘들어."},
                    {"s": "B", "en": "The trick is to take it one day at a time.", "ko": "하루하루 차근차근 하는 게 비결이야."},
                ],
            },
        ],
    },
    {
        "grade": "고등 3학년",
        "focus": "미묘한 뉘앙스·관용 표현, 거의 원어민 같은 자연스러움",
        "dialogues": [
            {
                "title": "어려운 결정",
                "turns": [
                    {"s": "A", "en": "I heard you turned down the new job offer.", "ko": "새 일자리 제안 거절했다며."},
                    {"s": "B", "en": "I did. The pay was great, but it wasn't the right fit.", "ko": "응. 보수는 좋았는데, 잘 안 맞았어."},
                    {"s": "A", "en": "That takes courage. Most people would jump at it.", "ko": "용기 있다. 대부분은 덥석 잡을 텐데."},
                    {"s": "B", "en": "Maybe, but I'd rather do something I believe in.", "ko": "그럴 수도. 근데 난 진짜 믿는 일을 하고 싶어."},
                ],
            },
            {
                "title": "돌아보며",
                "turns": [
                    {"s": "A", "en": "Looking back, is there anything you'd do differently?", "ko": "돌아보면, 다르게 하고 싶은 게 있어?"},
                    {"s": "B", "en": "Honestly, I try not to dwell on the past too much.", "ko": "솔직히, 과거에 너무 얽매이지 않으려고 해."},
                    {"s": "A", "en": "That's a healthy way to look at it.", "ko": "건강한 시각이네."},
                    {"s": "B", "en": "I've learned that mistakes are part of growing.", "ko": "실수도 성장의 일부라는 걸 배웠어."},
                ],
            },
        ],
    },
]
