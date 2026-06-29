# -*- coding: utf-8 -*-
"""
한→영 말하기 — 한국어 문장을 보고 '직접 영어로 말한 뒤' 모범답안을 확인하는 훈련.

회화에서 가장 중요한 '한국어 생각 → 영어 출력' 능력을 기릅니다.
주제는 일상 + 투자/시장. 매일 한 세트(4문장)씩 순서대로.

각 세트:
{
    "theme": "주제",
    "items": [{"ko": "한국어 문장", "en": "영어 모범답안"}],   # 4개
}
"""

KE_SETS = [
    {
        "theme": "자기소개",
        "items": [
            {"ko": "저는 투자에 관심이 있어요.", "en": "I'm interested in investing."},
            {"ko": "저는 아침에 시장 뉴스를 읽어요.", "en": "I read market news in the morning."},
            {"ko": "저는 영어를 배우고 있어요.", "en": "I'm learning English."},
            {"ko": "만나서 반가워요.", "en": "Nice to meet you."},
        ],
    },
    {
        "theme": "오늘 한 일",
        "items": [
            {"ko": "오늘 시장 뉴스를 읽었어요.", "en": "I read market news today."},
            {"ko": "반도체 주식을 확인했어요.", "en": "I checked semiconductor stocks."},
            {"ko": "영어를 30분 공부했어요.", "en": "I studied English for thirty minutes."},
            {"ko": "산책도 했어요.", "en": "I also took a walk."},
        ],
    },
    {
        "theme": "오늘의 시장",
        "items": [
            {"ko": "오늘 시장이 강했어요.", "en": "The market was strong today."},
            {"ko": "반도체 주식이 올랐어요.", "en": "Semiconductor stocks went up."},
            {"ko": "투자자들이 낙관적인 것 같아요.", "en": "I think investors are optimistic."},
            {"ko": "하지만 단기적으로는 변동성이 클 수 있어요.", "en": "But it may be volatile in the short term."},
        ],
    },
    {
        "theme": "내 관심사",
        "items": [
            {"ko": "저는 AI 인프라에 관심이 있어요.", "en": "I'm interested in AI infrastructure."},
            {"ko": "저는 한국 반도체를 좋아해요.", "en": "I like Korean semiconductors."},
            {"ko": "저는 거시 지표를 자주 봐요.", "en": "I often check macro indicators."},
            {"ko": "저는 장기 투자를 선호해요.", "en": "I prefer long-term investing."},
        ],
    },
    {
        "theme": "의견 말하기",
        "items": [
            {"ko": "제 생각엔 시장이 너무 낙관적이에요.", "en": "I think the market is too optimistic."},
            {"ko": "이유는 간단해요.", "en": "The reason is simple."},
            {"ko": "AI 수요가 여전히 강해요.", "en": "AI demand is still strong."},
            {"ko": "예를 들어, 빅테크가 많이 투자하고 있어요.", "en": "For example, big tech is investing a lot."},
        ],
    },
    {
        "theme": "질문하기",
        "items": [
            {"ko": "다시 설명해 주실 수 있나요?", "en": "Could you explain that again?"},
            {"ko": "그게 무슨 뜻이에요?", "en": "What do you mean by that?"},
            {"ko": "예를 하나 들어 주실래요?", "en": "Can you give me an example?"},
            {"ko": "당신은 어떻게 생각해요?", "en": "What do you think?"},
        ],
    },
    {
        "theme": "카페에서",
        "items": [
            {"ko": "아이스 아메리카노 하나 주세요.", "en": "Could I get an iced Americano?"},
            {"ko": "여기서 마실게요.", "en": "For here, please."},
            {"ko": "카드로 계산해도 되나요?", "en": "Can I pay by card?"},
            {"ko": "고맙습니다.", "en": "Thank you."},
        ],
    },
    {
        "theme": "약속 잡기",
        "items": [
            {"ko": "내일 시간 있어요?", "en": "Are you free tomorrow?"},
            {"ko": "오후에 만날 수 있어요.", "en": "I can meet in the afternoon."},
            {"ko": "어디서 만날까요?", "en": "Where should we meet?"},
            {"ko": "2시에 만나요.", "en": "Let's meet at two."},
        ],
    },
    {
        "theme": "기분·상태",
        "items": [
            {"ko": "오늘 기분이 좋아요.", "en": "I feel good today."},
            {"ko": "좀 피곤해요.", "en": "I'm a little tired."},
            {"ko": "시장 때문에 좀 긴장돼요.", "en": "I'm a little nervous about the market."},
            {"ko": "하지만 괜찮아요.", "en": "But I'm okay."},
        ],
    },
    {
        "theme": "주가 움직임",
        "items": [
            {"ko": "하이닉스 주가가 올랐어요.", "en": "SK Hynix went up."},
            {"ko": "삼성전자는 약했어요.", "en": "Samsung Electronics was weak."},
            {"ko": "그 주식은 가이던스 때문에 떨어졌어요.", "en": "The stock fell because of the guidance."},
            {"ko": "전체적으로 시장은 보합이었어요.", "en": "Overall, the market was flat."},
        ],
    },
    {
        "theme": "투자 이유",
        "items": [
            {"ko": "저는 AI 수요가 중요하다고 생각해요.", "en": "I think AI demand is important."},
            {"ko": "기업들이 더 많은 칩이 필요해요.", "en": "Companies need more chips."},
            {"ko": "그래서 메모리 수요가 늘고 있어요.", "en": "So memory demand is increasing."},
            {"ko": "장기 추세는 탄탄해 보여요.", "en": "The long-term trend looks solid."},
        ],
    },
    {
        "theme": "계획 말하기",
        "items": [
            {"ko": "오늘 밤에 실적 보고서를 읽을 거예요.", "en": "I'm going to read the earnings report tonight."},
            {"ko": "이 주식을 계속 들고 있을 거예요.", "en": "I'm going to hold this stock."},
            {"ko": "매일 영어를 연습할 계획이에요.", "en": "I'm planning to practice English every day."},
            {"ko": "조금 더 저축하려고 해요.", "en": "I'm trying to save a little more."},
        ],
    },
    {
        "theme": "걱정·우려",
        "items": [
            {"ko": "금리가 걱정돼요.", "en": "I'm worried about interest rates."},
            {"ko": "시장이 과열된 것 같아요.", "en": "I feel like the market is overheated."},
            {"ko": "조정이 올 수도 있어요.", "en": "There's a chance of a correction."},
            {"ko": "그래서 조심하고 있어요.", "en": "So I'm being careful."},
        ],
    },
    {
        "theme": "비교하기",
        "items": [
            {"ko": "작년과 비교하면 더 나아요.", "en": "Compared to last year, it's better."},
            {"ko": "채권보다 주식이 더 위험해요.", "en": "Stocks are riskier than bonds."},
            {"ko": "이게 저것보다 싸요.", "en": "This is cheaper than that."},
            {"ko": "전보다 영어를 더 많이 말해요.", "en": "I speak more English than before."},
        ],
    },
    {
        "theme": "만약에 (가정)",
        "items": [
            {"ko": "시장이 떨어지면 더 살 거예요.", "en": "If the market drops, I'll buy more."},
            {"ko": "시간이 있으면 책을 읽을 거예요.", "en": "If I have time, I'll read a book."},
            {"ko": "확실하지 않으면 기다리겠어요.", "en": "If I'm not sure, I'll wait."},
            {"ko": "복권에 당첨되면 여행할 거예요.", "en": "If I won the lottery, I'd travel."},
        ],
    },
    {
        "theme": "회사·실적",
        "items": [
            {"ko": "그 회사는 실적이 좋았어요.", "en": "The company had good earnings."},
            {"ko": "매출이 작년보다 늘었어요.", "en": "Revenue grew from last year."},
            {"ko": "시장은 실적보다 가이던스에 더 반응했어요.", "en": "The market reacted more to the guidance than the earnings."},
            {"ko": "저는 이 회사를 더 이해하고 싶어요.", "en": "I want to understand this company better."},
        ],
    },
    {
        "theme": "금리·경제",
        "items": [
            {"ko": "금리가 오르면 주식시장에 부담이 돼요.", "en": "When rates go up, it pressures the stock market."},
            {"ko": "경제가 천천히 식고 있어요.", "en": "The economy is slowing down."},
            {"ko": "인플레이션이 걱정돼요.", "en": "I'm worried about inflation."},
            {"ko": "그래도 장기적으로는 낙관적이에요.", "en": "But I'm optimistic in the long run."},
        ],
    },
    {
        "theme": "추천·제안",
        "items": [
            {"ko": "커피 한잔 어때요?", "en": "How about a coffee?"},
            {"ko": "이 주식 한번 보는 게 어때요?", "en": "How about looking at this stock?"},
            {"ko": "같이 공부합시다.", "en": "Let's study together."},
            {"ko": "지켜봅시다.", "en": "Let's wait and see."},
        ],
    },
    {
        "theme": "동의·반대",
        "items": [
            {"ko": "동의해요.", "en": "I agree."},
            {"ko": "전적으로 동의해요.", "en": "I couldn't agree more."},
            {"ko": "그건 잘 모르겠어요.", "en": "I'm not so sure about that."},
            {"ko": "일리 있는 말이에요.", "en": "That's a fair point."},
        ],
    },
    {
        "theme": "시간·일정",
        "items": [
            {"ko": "지금 몇 시예요?", "en": "What time is it now?"},
            {"ko": "시장은 9시에 열어요.", "en": "The market opens at nine."},
            {"ko": "얼마나 걸려요?", "en": "How long does it take?"},
            {"ko": "곧 끝나요.", "en": "It'll be over soon."},
        ],
    },
    {
        "theme": "여행",
        "items": [
            {"ko": "거기 어떻게 가요?", "en": "How do I get there?"},
            {"ko": "거기까지 얼마나 걸려요?", "en": "How long does it take to get there?"},
            {"ko": "이 근처에 좋은 식당 있어요?", "en": "Is there a good restaurant near here?"},
            {"ko": "도와주셔서 감사해요.", "en": "Thank you for your help."},
        ],
    },
    {
        "theme": "식당",
        "items": [
            {"ko": "두 명 자리 주세요.", "en": "A table for two, please."},
            {"ko": "뭘 추천하세요?", "en": "What do you recommend?"},
            {"ko": "이걸로 할게요.", "en": "I'll have this one."},
            {"ko": "계산서 좀 주시겠어요?", "en": "Could we get the check, please?"},
        ],
    },
    {
        "theme": "결정하기",
        "items": [
            {"ko": "결정을 내려야 해요.", "en": "I need to make a decision."},
            {"ko": "차라리 기다리겠어요.", "en": "I'd rather wait."},
            {"ko": "상황에 달렸어요.", "en": "It depends on the situation."},
            {"ko": "생각 좀 해볼게요.", "en": "Let me think about it."},
        ],
    },
    {
        "theme": "마무리·다짐",
        "items": [
            {"ko": "저는 영어 말하기를 늘리고 싶어요.", "en": "I want to improve my English speaking."},
            {"ko": "매일 조금씩 연습할 거예요.", "en": "I'll practice a little every day."},
            {"ko": "꾸준함이 핵심이에요.", "en": "Consistency is the key."},
            {"ko": "포기하지 않을 거예요.", "en": "I won't give up."},
        ],
    },
]
