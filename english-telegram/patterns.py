# -*- coding: utf-8 -*-
"""
오늘의 패턴 — 회화에서 바로 쓰는 문장 패턴 30개 (문장 자동화 훈련).

한 패턴을 '내 주제(일상 + 투자/시장)'로 바꿔 입으로 5번씩 말하는 게 목적입니다.
매일 하나씩 순서대로 진행합니다.

각 패턴:
{
    "pattern": "패턴",
    "ko": "뜻",
    "examples": [{"en": "예문", "ko": "뜻"}],   # 내 주제로 바꾼 5문장
}
"""

PATTERNS = [
    {
        "pattern": "I want to ~", "ko": "나는 ~하고 싶다",
        "examples": [
            {"en": "I want to improve my English.", "ko": "영어를 늘리고 싶어요."},
            {"en": "I want to check the market.", "ko": "시장을 확인하고 싶어요."},
            {"en": "I want to learn about investing.", "ko": "투자에 대해 배우고 싶어요."},
            {"en": "I want to take a break.", "ko": "좀 쉬고 싶어요."},
            {"en": "I want to understand this company.", "ko": "이 회사를 이해하고 싶어요."},
        ],
    },
    {
        "pattern": "I'm interested in ~", "ko": "나는 ~에 관심이 있다",
        "examples": [
            {"en": "I'm interested in stocks.", "ko": "주식에 관심이 있어요."},
            {"en": "I'm interested in semiconductors.", "ko": "반도체에 관심이 있어요."},
            {"en": "I'm interested in AI companies.", "ko": "AI 기업에 관심이 있어요."},
            {"en": "I'm interested in market trends.", "ko": "시장 흐름에 관심이 있어요."},
            {"en": "I'm interested in learning English.", "ko": "영어 배우는 데 관심이 있어요."},
        ],
    },
    {
        "pattern": "I think (that) ~", "ko": "나는 ~라고 생각한다",
        "examples": [
            {"en": "I think the market is too optimistic.", "ko": "시장이 너무 낙관적인 것 같아요."},
            {"en": "I think AI demand is still strong.", "ko": "AI 수요가 여전히 강한 것 같아요."},
            {"en": "I think this stock is expensive.", "ko": "이 주식은 비싼 것 같아요."},
            {"en": "I think I need more practice.", "ko": "연습이 더 필요한 것 같아요."},
            {"en": "I think it's a good time to wait.", "ko": "기다리기 좋은 때인 것 같아요."},
        ],
    },
    {
        "pattern": "I'm going to ~", "ko": "나는 ~할 것이다 (계획)",
        "examples": [
            {"en": "I'm going to study English tonight.", "ko": "오늘 밤 영어 공부할 거예요."},
            {"en": "I'm going to check the earnings report.", "ko": "실적 보고서를 볼 거예요."},
            {"en": "I'm going to hold this stock.", "ko": "이 주식을 계속 들고 있을 거예요."},
            {"en": "I'm going to take a walk.", "ko": "산책할 거예요."},
            {"en": "I'm going to read some news.", "ko": "뉴스 좀 읽을 거예요."},
        ],
    },
    {
        "pattern": "I'm trying to ~", "ko": "나는 ~하려고 (노력)하는 중이다",
        "examples": [
            {"en": "I'm trying to speak more English.", "ko": "영어를 더 말하려고 해요."},
            {"en": "I'm trying to understand the market.", "ko": "시장을 이해하려고 해요."},
            {"en": "I'm trying to save more money.", "ko": "돈을 더 모으려고 해요."},
            {"en": "I'm trying to stay calm.", "ko": "침착하려고 해요."},
            {"en": "I'm trying to make a habit of it.", "ko": "그걸 습관으로 만들려고 해요."},
        ],
    },
    {
        "pattern": "I need to ~", "ko": "나는 ~해야 한다",
        "examples": [
            {"en": "I need to practice speaking.", "ko": "말하기 연습을 해야 해요."},
            {"en": "I need to check the price.", "ko": "가격을 확인해야 해요."},
            {"en": "I need to do more research.", "ko": "조사를 더 해야 해요."},
            {"en": "I need to get some rest.", "ko": "좀 쉬어야 해요."},
            {"en": "I need to make a decision.", "ko": "결정을 내려야 해요."},
        ],
    },
    {
        "pattern": "Could you ~?", "ko": "~해 주실 수 있나요? (정중한 부탁)",
        "examples": [
            {"en": "Could you say that again?", "ko": "다시 말씀해 주실래요?"},
            {"en": "Could you speak more slowly?", "ko": "조금 천천히 말해 주실래요?"},
            {"en": "Could you help me with this?", "ko": "이것 좀 도와주실래요?"},
            {"en": "Could you explain that?", "ko": "그거 설명해 주실래요?"},
            {"en": "Could you recommend a stock?", "ko": "주식 하나 추천해 주실래요?"},
        ],
    },
    {
        "pattern": "Can I ~?", "ko": "~해도 될까요?",
        "examples": [
            {"en": "Can I ask you a question?", "ko": "질문 하나 해도 될까요?"},
            {"en": "Can I get an iced Americano?", "ko": "아이스 아메리카노 하나 주실래요?"},
            {"en": "Can I think about it?", "ko": "생각 좀 해봐도 될까요?"},
            {"en": "Can I join you?", "ko": "같이 해도 될까요?"},
            {"en": "Can I see the chart?", "ko": "차트 좀 봐도 될까요?"},
        ],
    },
    {
        "pattern": "I'd like to ~", "ko": "~하고 싶어요 (정중)",
        "examples": [
            {"en": "I'd like to learn more.", "ko": "더 배우고 싶어요."},
            {"en": "I'd like to open an account.", "ko": "계좌를 열고 싶어요."},
            {"en": "I'd like to ask about the fees.", "ko": "수수료에 대해 물어보고 싶어요."},
            {"en": "I'd like to introduce myself.", "ko": "제 소개를 하고 싶어요."},
            {"en": "I'd like to try again.", "ko": "다시 해보고 싶어요."},
        ],
    },
    {
        "pattern": "I have to ~", "ko": "나는 ~해야만 한다",
        "examples": [
            {"en": "I have to work tomorrow.", "ko": "내일 일해야 해요."},
            {"en": "I have to check the market first.", "ko": "먼저 시장을 확인해야 해요."},
            {"en": "I have to be careful with money.", "ko": "돈에 신중해야 해요."},
            {"en": "I have to leave now.", "ko": "지금 가봐야 해요."},
            {"en": "I have to finish this today.", "ko": "오늘 이걸 끝내야 해요."},
        ],
    },
    {
        "pattern": "It depends on ~", "ko": "~에 달려 있어요",
        "examples": [
            {"en": "It depends on the situation.", "ko": "상황에 달렸어요."},
            {"en": "It depends on the price.", "ko": "가격에 달렸어요."},
            {"en": "It depends on the earnings.", "ko": "실적에 달렸어요."},
            {"en": "It depends on the interest rate.", "ko": "금리에 달렸어요."},
            {"en": "It depends on how you feel.", "ko": "당신 기분에 달렸어요."},
        ],
    },
    {
        "pattern": "I'm not sure if ~", "ko": "~인지 잘 모르겠어요",
        "examples": [
            {"en": "I'm not sure if it's a good idea.", "ko": "좋은 생각인지 잘 모르겠어요."},
            {"en": "I'm not sure if the market will rise.", "ko": "시장이 오를지 잘 모르겠어요."},
            {"en": "I'm not sure if I'm right.", "ko": "내가 맞는지 잘 모르겠어요."},
            {"en": "I'm not sure if I can make it.", "ko": "갈 수 있을지 잘 모르겠어요."},
            {"en": "I'm not sure if it's worth it.", "ko": "그럴 가치가 있는지 잘 모르겠어요."},
        ],
    },
    {
        "pattern": "I'm worried about ~", "ko": "나는 ~이 걱정돼요",
        "examples": [
            {"en": "I'm worried about the market.", "ko": "시장이 걱정돼요."},
            {"en": "I'm worried about interest rates.", "ko": "금리가 걱정돼요."},
            {"en": "I'm worried about my English.", "ko": "내 영어가 걱정돼요."},
            {"en": "I'm worried about the economy.", "ko": "경제가 걱정돼요."},
            {"en": "I'm worried about losing money.", "ko": "돈을 잃을까 걱정돼요."},
        ],
    },
    {
        "pattern": "The reason is ~", "ko": "이유는 ~예요",
        "examples": [
            {"en": "The reason is simple.", "ko": "이유는 간단해요."},
            {"en": "The reason is strong AI demand.", "ko": "이유는 강한 AI 수요예요."},
            {"en": "The reason is the weak guidance.", "ko": "이유는 약한 가이던스예요."},
            {"en": "The reason is high interest rates.", "ko": "이유는 높은 금리예요."},
            {"en": "The reason is I didn't practice.", "ko": "이유는 제가 연습을 안 해서예요."},
        ],
    },
    {
        "pattern": "How about ~?", "ko": "~는 어때요? (제안)",
        "examples": [
            {"en": "How about a coffee?", "ko": "커피 한잔 어때요?"},
            {"en": "How about meeting at two?", "ko": "2시에 만나는 거 어때요?"},
            {"en": "How about this stock?", "ko": "이 주식은 어때요?"},
            {"en": "How about studying together?", "ko": "같이 공부하는 거 어때요?"},
            {"en": "How about you?", "ko": "당신은 어때요?"},
        ],
    },
    {
        "pattern": "Let me ~", "ko": "제가 ~할게요 / ~하게 해주세요",
        "examples": [
            {"en": "Let me check.", "ko": "제가 확인해 볼게요."},
            {"en": "Let me think about it.", "ko": "생각 좀 해볼게요."},
            {"en": "Let me explain.", "ko": "제가 설명할게요."},
            {"en": "Let me look at the chart.", "ko": "차트 좀 볼게요."},
            {"en": "Let me know what you think.", "ko": "어떻게 생각하는지 알려줘요."},
        ],
    },
    {
        "pattern": "I used to ~", "ko": "예전엔 ~했었어요 (지금은 아님)",
        "examples": [
            {"en": "I used to trade every day.", "ko": "예전엔 매일 매매했어요."},
            {"en": "I used to be afraid of speaking.", "ko": "예전엔 말하기가 무서웠어요."},
            {"en": "I used to invest in only one stock.", "ko": "예전엔 한 종목만 투자했어요."},
            {"en": "I used to skip breakfast.", "ko": "예전엔 아침을 걸렀어요."},
            {"en": "I used to study late at night.", "ko": "예전엔 밤늦게 공부했어요."},
        ],
    },
    {
        "pattern": "I feel like ~", "ko": "~인 것 같아요 / ~하고 싶어요",
        "examples": [
            {"en": "I feel like the market is overheated.", "ko": "시장이 과열된 것 같아요."},
            {"en": "I feel like I'm improving.", "ko": "내가 늘고 있는 것 같아요."},
            {"en": "I feel like taking a rest.", "ko": "좀 쉬고 싶어요."},
            {"en": "I feel like something will change.", "ko": "뭔가 바뀔 것 같아요."},
            {"en": "I feel like I need more time.", "ko": "시간이 더 필요한 것 같아요."},
        ],
    },
    {
        "pattern": "What do you think about ~?", "ko": "~에 대해 어떻게 생각해요?",
        "examples": [
            {"en": "What do you think about this stock?", "ko": "이 주식 어떻게 생각해요?"},
            {"en": "What do you think about AI?", "ko": "AI에 대해 어떻게 생각해요?"},
            {"en": "What do you think about the economy?", "ko": "경제에 대해 어떻게 생각해요?"},
            {"en": "What do you think about my plan?", "ko": "제 계획 어떻게 생각해요?"},
            {"en": "What do you think about working from home?", "ko": "재택근무 어떻게 생각해요?"},
        ],
    },
    {
        "pattern": "It seems like ~", "ko": "~인 것 같아요 (보아하니)",
        "examples": [
            {"en": "It seems like a good deal.", "ko": "좋은 거래 같아요."},
            {"en": "It seems like the market is calm.", "ko": "시장이 잠잠한 것 같아요."},
            {"en": "It seems like he's busy.", "ko": "그는 바쁜 것 같아요."},
            {"en": "It seems like demand is growing.", "ko": "수요가 커지는 것 같아요."},
            {"en": "It seems like it'll rain.", "ko": "비가 올 것 같아요."},
        ],
    },
    {
        "pattern": "I'm planning to ~", "ko": "나는 ~할 계획이에요",
        "examples": [
            {"en": "I'm planning to study every day.", "ko": "매일 공부할 계획이에요."},
            {"en": "I'm planning to buy more shares.", "ko": "주식을 더 살 계획이에요."},
            {"en": "I'm planning to travel next month.", "ko": "다음 달에 여행할 계획이에요."},
            {"en": "I'm planning to read the report.", "ko": "그 보고서를 읽을 계획이에요."},
            {"en": "I'm planning to save more.", "ko": "더 저축할 계획이에요."},
        ],
    },
    {
        "pattern": "There's a chance (that) ~", "ko": "~할 가능성이 있어요",
        "examples": [
            {"en": "There's a chance the stock will recover.", "ko": "주가가 회복할 가능성이 있어요."},
            {"en": "There's a chance rates will go down.", "ko": "금리가 내릴 가능성이 있어요."},
            {"en": "There's a chance I'm wrong.", "ko": "제가 틀렸을 가능성이 있어요."},
            {"en": "There's a chance it will rain.", "ko": "비가 올 가능성이 있어요."},
            {"en": "There's a chance we can meet.", "ko": "우리가 만날 가능성이 있어요."},
        ],
    },
    {
        "pattern": "Compared to ~", "ko": "~와 비교하면",
        "examples": [
            {"en": "Compared to last year, it's better.", "ko": "작년과 비교하면 더 나아요."},
            {"en": "Compared to Samsung, it's cheaper.", "ko": "삼성과 비교하면 더 싸요."},
            {"en": "Compared to before, I speak more.", "ko": "전과 비교하면 더 많이 말해요."},
            {"en": "Compared to bonds, stocks are risky.", "ko": "채권과 비교하면 주식은 위험해요."},
            {"en": "Compared to yesterday, it's calm.", "ko": "어제와 비교하면 잠잠해요."},
        ],
    },
    {
        "pattern": "Because of ~", "ko": "~ 때문에",
        "examples": [
            {"en": "Because of strong earnings, the stock rose.", "ko": "강한 실적 때문에 주가가 올랐어요."},
            {"en": "Because of high rates, the market fell.", "ko": "높은 금리 때문에 시장이 떨어졌어요."},
            {"en": "Because of the rain, I stayed home.", "ko": "비 때문에 집에 있었어요."},
            {"en": "Because of AI, chip demand is rising.", "ko": "AI 때문에 칩 수요가 늘어요."},
            {"en": "Because of work, I was busy.", "ko": "일 때문에 바빴어요."},
        ],
    },
    {
        "pattern": "As far as I know, ~", "ko": "내가 아는 한 ~",
        "examples": [
            {"en": "As far as I know, it's safe.", "ko": "내가 아는 한 안전해요."},
            {"en": "As far as I know, earnings are next week.", "ko": "내가 아는 한 실적은 다음 주예요."},
            {"en": "As far as I know, the market is closed.", "ko": "내가 아는 한 시장은 닫았어요."},
            {"en": "As far as I know, he agrees.", "ko": "내가 아는 한 그는 동의해요."},
            {"en": "As far as I know, it's free.", "ko": "내가 아는 한 무료예요."},
        ],
    },
    {
        "pattern": "I'd rather ~ (than ...)", "ko": "차라리 ~하겠어요 (…보다)",
        "examples": [
            {"en": "I'd rather wait.", "ko": "차라리 기다리겠어요."},
            {"en": "I'd rather buy low than chase it.", "ko": "쫓아가느니 차라리 싸게 사겠어요."},
            {"en": "I'd rather stay home tonight.", "ko": "오늘 밤은 차라리 집에 있겠어요."},
            {"en": "I'd rather learn slowly than quit.", "ko": "그만두느니 천천히 배우겠어요."},
            {"en": "I'd rather be safe than sorry.", "ko": "후회하느니 안전한 게 낫죠."},
        ],
    },
    {
        "pattern": "I'm sure (that) ~", "ko": "~라고 확신해요",
        "examples": [
            {"en": "I'm sure it'll be fine.", "ko": "괜찮을 거라고 확신해요."},
            {"en": "I'm sure you can do it.", "ko": "당신은 할 수 있다고 확신해요."},
            {"en": "I'm sure the trend will continue.", "ko": "추세가 이어질 거라고 확신해요."},
            {"en": "I'm sure I locked the door.", "ko": "문 잠근 거 확실해요."},
            {"en": "I'm sure we'll meet again.", "ko": "또 만날 거라고 확신해요."},
        ],
    },
    {
        "pattern": "Let's ~", "ko": "~합시다 (같이 하자)",
        "examples": [
            {"en": "Let's start.", "ko": "시작합시다."},
            {"en": "Let's talk about it.", "ko": "그것에 대해 얘기합시다."},
            {"en": "Let's wait and see.", "ko": "지켜봅시다."},
            {"en": "Let's keep it simple.", "ko": "간단하게 갑시다."},
            {"en": "Let's meet next week.", "ko": "다음 주에 만납시다."},
        ],
    },
    {
        "pattern": "I'm looking for ~", "ko": "나는 ~을 찾고 있어요",
        "examples": [
            {"en": "I'm looking for a good entry point.", "ko": "좋은 매수 시점을 찾고 있어요."},
            {"en": "I'm looking for a safe investment.", "ko": "안전한 투자를 찾고 있어요."},
            {"en": "I'm looking for the station.", "ko": "역을 찾고 있어요."},
            {"en": "I'm looking for a way to practice.", "ko": "연습할 방법을 찾고 있어요."},
            {"en": "I'm looking for more information.", "ko": "더 많은 정보를 찾고 있어요."},
        ],
    },
]
