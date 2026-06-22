# -*- coding: utf-8 -*-
"""
기초 영어 학습 코스 (완전 초보 → 기초, 45일 커리큘럼)

매일 한 과씩 '순서대로' 진행됩니다 (회화 스크립트와 달리 단계별 진행).
인사 → 인칭대명사 → be동사 → 일반동사 → 의문사 → 시제(현재/과거/미래) 순으로 쌓아갑니다.

각 과 형식:
{
    "unit": "단원 이름",
    "emoji": "이모지",
    "title_en": "영어 제목",
    "title_ko": "한국어 제목",
    "explain": "오늘 배울 것 (쉬운 한국어 설명)",
    "points": [{"en": "핵심 패턴", "ko": "뜻"}],
    "examples": [{"en": "예문", "ko": "뜻"}],
    "practice": [{"q": "문제", "a": "정답"}],
}
"""

LESSONS = [
    # ===== Unit 1. 첫걸음 =====
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "👋",
        "title_en": "Greetings",
        "title_ko": "인사하기",
        "explain": "만나고 헤어질 때 쓰는 가장 기본 인사예요. 시간대에 따라 인사가 조금 달라져요.",
        "points": [
            {"en": "Hello. / Hi.", "ko": "안녕하세요. / 안녕. (아무 때나)"},
            {"en": "Good morning.", "ko": "좋은 아침이에요. (아침 인사)"},
            {"en": "Goodbye. / Bye.", "ko": "안녕히 가세요. / 잘 가."},
        ],
        "examples": [
            {"en": "Hi, Tom!", "ko": "안녕, Tom!"},
            {"en": "Good morning, everyone.", "ko": "모두 좋은 아침이에요."},
            {"en": "Good night.", "ko": "잘 자요. (밤에 헤어질 때)"},
            {"en": "See you tomorrow.", "ko": "내일 봐요."},
        ],
        "practice": [
            {"q": "'아침'에 하는 인사는?", "a": "Good morning."},
            {"q": "헤어질 때 '잘 가'는?", "a": "Goodbye. (또는 Bye.)"},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "🙏",
        "title_en": "Essential Phrases",
        "title_ko": "필수 기본 표현",
        "explain": "외국에서 가장 자주 쓰는 필수 표현이에요. 이것만 알아도 예의 바르게 소통할 수 있어요.",
        "points": [
            {"en": "Thank you.", "ko": "고맙습니다."},
            {"en": "Sorry. / Excuse me.", "ko": "미안합니다. / 실례합니다."},
            {"en": "Please.", "ko": "부탁합니다 (정중하게)"},
        ],
        "examples": [
            {"en": "Thank you very much.", "ko": "정말 고맙습니다."},
            {"en": "I'm sorry.", "ko": "죄송합니다."},
            {"en": "Excuse me, where is the bathroom?", "ko": "실례합니다, 화장실이 어디예요?"},
            {"en": "Water, please.", "ko": "물 주세요."},
        ],
        "practice": [
            {"q": "누군가 도와줬을 때 한마디는?", "a": "Thank you."},
            {"q": "지나가게 비켜달라고 할 때 시작하는 말은?", "a": "Excuse me."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "✅",
        "title_en": "Yes / No & Replies",
        "title_ko": "대답하기",
        "explain": "대답할 때 자주 쓰는 짧은 표현들이에요.",
        "points": [
            {"en": "Yes. / No.", "ko": "네. / 아니요."},
            {"en": "Okay. / Sure.", "ko": "알겠어요. / 그럼요."},
            {"en": "I don't know.", "ko": "잘 모르겠어요."},
        ],
        "examples": [
            {"en": "Yes, please.", "ko": "네, 부탁해요."},
            {"en": "No, thank you.", "ko": "아니요, 괜찮아요."},
            {"en": "Sure, no problem.", "ko": "그럼요, 문제없어요."},
            {"en": "I think so.", "ko": "그런 것 같아요."},
        ],
        "practice": [
            {"q": "정중한 거절 '아니요, 괜찮아요.'", "a": "No, thank you."},
            {"q": "'그럼요, 문제없어요.'", "a": "Sure, no problem."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "🧑",
        "title_en": "Pronouns",
        "title_ko": "인칭대명사",
        "explain": "사람이나 사물을 가리키는 말이에요. 영어 문장은 보통 이 말(주어)로 시작해요.",
        "points": [
            {"en": "I / you", "ko": "나 / 너, 당신"},
            {"en": "he / she / it", "ko": "그(남) / 그녀(여) / 그것"},
            {"en": "we / they", "ko": "우리 / 그들, 그것들"},
        ],
        "examples": [
            {"en": "I am Korean.", "ko": "나는 한국인이에요."},
            {"en": "You are kind.", "ko": "당신은 친절해요."},
            {"en": "She is my friend.", "ko": "그녀는 내 친구예요."},
            {"en": "They are students.", "ko": "그들은 학생이에요."},
        ],
        "practice": [
            {"q": "'우리'를 뜻하는 단어는?", "a": "we"},
            {"q": "여자 한 명을 가리키는 말은?", "a": "she"},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "🟰",
        "title_en": "The verb BE (am/is/are)",
        "title_ko": "be동사 (긍정)",
        "explain": "be동사는 '~이다, ~에 있다'라는 뜻이에요. 주어에 따라 모양이 달라져요: I=am, he/she/it=is, you/we/they=are.",
        "points": [
            {"en": "I am ~", "ko": "나는 ~이다"},
            {"en": "He / She / It is ~", "ko": "그/그녀/그것은 ~이다"},
            {"en": "You / We / They are ~", "ko": "너/우리/그들은 ~이다"},
        ],
        "examples": [
            {"en": "I am a teacher.", "ko": "나는 선생님이에요."},
            {"en": "He is tall.", "ko": "그는 키가 커요."},
            {"en": "We are happy.", "ko": "우리는 행복해요."},
            {"en": "It is cold today.", "ko": "오늘 추워요."},
        ],
        "practice": [
            {"q": "She ___ pretty. (be동사 넣기)", "a": "She is pretty."},
            {"q": "They ___ my friends.", "a": "They are my friends."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "❌",
        "title_en": "BE negative",
        "title_ko": "be동사 부정",
        "explain": "'~이 아니다'는 be동사 뒤에 not을 붙여요. 줄여서 isn't, aren't로 자주 써요.",
        "points": [
            {"en": "I am not ~ (I'm not)", "ko": "나는 ~이 아니다"},
            {"en": "He is not ~ (isn't)", "ko": "그는 ~이 아니다"},
            {"en": "They are not ~ (aren't)", "ko": "그들은 ~이 아니다"},
        ],
        "examples": [
            {"en": "I'm not tired.", "ko": "나는 안 피곤해요."},
            {"en": "She isn't here.", "ko": "그녀는 여기 없어요."},
            {"en": "We aren't ready.", "ko": "우리는 준비가 안 됐어요."},
            {"en": "It isn't expensive.", "ko": "그건 안 비싸요."},
        ],
        "practice": [
            {"q": "'그는 학생이 아니에요.'", "a": "He isn't a student."},
            {"q": "'나는 배고프지 않아요.'", "a": "I'm not hungry."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "❓",
        "title_en": "BE questions",
        "title_ko": "be동사 의문문",
        "explain": "be동사를 문장 맨 앞으로 보내면 질문이 돼요. 대답은 Yes, I am. / No, I'm not. 처럼 해요.",
        "points": [
            {"en": "Are you ~?", "ko": "너는 ~이니? → Yes, I am. / No, I'm not."},
            {"en": "Is he ~?", "ko": "그는 ~이니? → Yes, he is. / No, he isn't."},
        ],
        "examples": [
            {"en": "Are you okay?", "ko": "괜찮아요?"},
            {"en": "Is she a doctor?", "ko": "그녀는 의사예요?"},
            {"en": "Are they at home?", "ko": "그들은 집에 있어요?"},
            {"en": "Yes, I am.", "ko": "네, 그래요."},
        ],
        "practice": [
            {"q": "'당신은 한국인인가요?'", "a": "Are you Korean?"},
            {"q": "'Is he busy?'에 긍정으로 답하면?", "a": "Yes, he is."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "📦",
        "title_en": "Articles a / an",
        "title_ko": "관사 a / an",
        "explain": "하나의(특정하지 않은) 사물 앞에 a를 붙여요. 단어가 모음 소리(a,e,i,o,u)로 시작하면 an을 써요.",
        "points": [
            {"en": "a + 자음 소리", "ko": "a book, a car, a dog"},
            {"en": "an + 모음 소리", "ko": "an apple, an egg, an hour"},
        ],
        "examples": [
            {"en": "I have a pen.", "ko": "나는 펜이 하나 있어요."},
            {"en": "She is a nurse.", "ko": "그녀는 간호사예요."},
            {"en": "It is an old house.", "ko": "그건 오래된 집이에요."},
            {"en": "I want an orange.", "ko": "나는 오렌지 하나를 원해요."},
        ],
        "practice": [
            {"q": "___ apple (a 또는 an?)", "a": "an apple"},
            {"q": "___ teacher (a 또는 an?)", "a": "a teacher"},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "👉",
        "title_en": "this / that / these / those",
        "title_ko": "이것 / 저것",
        "explain": "가까운 건 this(이것), 먼 건 that(저것). 여러 개면 these(이것들), those(저것들).",
        "points": [
            {"en": "this / these", "ko": "이것 / 이것들 (가까움)"},
            {"en": "that / those", "ko": "저것 / 저것들 (멀리)"},
        ],
        "examples": [
            {"en": "This is my bag.", "ko": "이건 내 가방이에요."},
            {"en": "That is your seat.", "ko": "저건 당신 자리예요."},
            {"en": "These are my shoes.", "ko": "이건 내 신발이에요."},
            {"en": "Those are nice.", "ko": "저것들 멋지네요."},
        ],
        "practice": [
            {"q": "멀리 있는 하나를 가리키며 '저것'", "a": "that"},
            {"q": "'이것들은 사과예요.'", "a": "These are apples."},
        ],
    },
    {
        "unit": "Unit 1. 첫걸음",
        "emoji": "🔢",
        "title_en": "Plural nouns",
        "title_ko": "명사 복수형",
        "explain": "둘 이상이면 보통 단어 끝에 -s를 붙여요. -s, -x, -ch, -sh로 끝나면 -es. 불규칙도 있어요.",
        "points": [
            {"en": "보통: book→books", "ko": "그냥 -s"},
            {"en": "-es: box→boxes, watch→watches", "ko": "-s/-x/-ch/-sh 끝"},
            {"en": "불규칙: man→men, child→children", "ko": "모양이 바뀜"},
        ],
        "examples": [
            {"en": "I have two cats.", "ko": "나는 고양이가 두 마리 있어요."},
            {"en": "There are three boxes.", "ko": "상자가 세 개 있어요."},
            {"en": "The children are playing.", "ko": "아이들이 놀고 있어요."},
            {"en": "I need new shoes.", "ko": "새 신발이 필요해요."},
        ],
        "practice": [
            {"q": "'box'의 복수형은?", "a": "boxes"},
            {"q": "'child'의 복수형은?", "a": "children"},
        ],
    },
    # ===== Unit 2. 문장 만들기 =====
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🔢",
        "title_en": "Numbers 0-20",
        "title_ko": "숫자 0~20",
        "explain": "기본 숫자예요. 가격, 나이, 시간 등 어디에나 쓰여요.",
        "points": [
            {"en": "1 one, 2 two, 3 three, 4 four, 5 five", "ko": "1~5"},
            {"en": "6 six, 7 seven, 8 eight, 9 nine, 10 ten", "ko": "6~10"},
            {"en": "11 eleven, 12 twelve, 13 thirteen, 20 twenty", "ko": "11~20"},
        ],
        "examples": [
            {"en": "I have five dollars.", "ko": "나는 5달러 있어요."},
            {"en": "There are twelve months.", "ko": "열두 달이 있어요."},
            {"en": "Room number eight, please.", "ko": "8호실이요."},
            {"en": "I am twenty years old.", "ko": "나는 스무 살이에요."},
        ],
        "practice": [
            {"q": "숫자 7은 영어로?", "a": "seven"},
            {"q": "숫자 13은 영어로?", "a": "thirteen"},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "💯",
        "title_en": "Big Numbers",
        "title_ko": "숫자 (10단위~큰 수)",
        "explain": "30은 thirty처럼 -ty가 붙어요. 21은 twenty-one처럼 이어서 써요.",
        "points": [
            {"en": "20 twenty, 30 thirty, 40 forty, 50 fifty", "ko": "10단위"},
            {"en": "21 twenty-one, 35 thirty-five", "ko": "이어 쓰기"},
            {"en": "100 a hundred, 1000 a thousand", "ko": "큰 수"},
        ],
        "examples": [
            {"en": "I am thirty-five years old.", "ko": "나는 35살이에요."},
            {"en": "It is fifty dollars.", "ko": "50달러예요."},
            {"en": "There are a hundred people.", "ko": "백 명이 있어요."},
            {"en": "Forty minutes, please.", "ko": "40분이요."},
        ],
        "practice": [
            {"q": "숫자 40은 영어로?", "a": "forty"},
            {"q": "'스물둘'은 영어로?", "a": "twenty-two"},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "📅",
        "title_en": "Days of the Week",
        "title_ko": "요일",
        "explain": "일주일의 요일이에요. 요일 앞에는 보통 on을 써요 (on Monday).",
        "points": [
            {"en": "Sunday, Monday, Tuesday, Wednesday", "ko": "일,월,화,수"},
            {"en": "Thursday, Friday, Saturday", "ko": "목,금,토"},
            {"en": "on Monday", "ko": "월요일에"},
        ],
        "examples": [
            {"en": "Today is Friday.", "ko": "오늘은 금요일이에요."},
            {"en": "See you on Sunday.", "ko": "일요일에 봐요."},
            {"en": "I work on Tuesday.", "ko": "나는 화요일에 일해요."},
            {"en": "The meeting is on Wednesday.", "ko": "회의는 수요일이에요."},
        ],
        "practice": [
            {"q": "'월요일'은 영어로?", "a": "Monday"},
            {"q": "'토요일에 봐요.'", "a": "See you on Saturday."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🗓️",
        "title_en": "Months",
        "title_ko": "월(月)",
        "explain": "열두 달의 이름이에요. 월 앞에는 in을 써요 (in May).",
        "points": [
            {"en": "January, February, March, April", "ko": "1~4월"},
            {"en": "May, June, July, August", "ko": "5~8월"},
            {"en": "September, October, November, December", "ko": "9~12월"},
        ],
        "examples": [
            {"en": "My birthday is in June.", "ko": "내 생일은 6월이에요."},
            {"en": "It is December now.", "ko": "지금은 12월이에요."},
            {"en": "School starts in March.", "ko": "학교는 3월에 시작해요."},
            {"en": "See you in April.", "ko": "4월에 봐요."},
        ],
        "practice": [
            {"q": "'7월'은 영어로?", "a": "July"},
            {"q": "'내 생일은 9월이에요.'", "a": "My birthday is in September."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🕒",
        "title_en": "Telling Time",
        "title_ko": "시간 말하기",
        "explain": "몇 시인지 말할 때 It's ~ 로 시작해요. 정각은 o'clock, 분은 숫자만 붙여 읽어요.",
        "points": [
            {"en": "What time is it?", "ko": "몇 시예요?"},
            {"en": "It's three o'clock.", "ko": "3시예요. (정각)"},
            {"en": "It's seven thirty.", "ko": "7시 30분이에요."},
        ],
        "examples": [
            {"en": "It's nine o'clock.", "ko": "9시예요."},
            {"en": "It's ten fifteen.", "ko": "10시 15분이에요."},
            {"en": "The bus is at eight.", "ko": "버스는 8시예요."},
            {"en": "It's noon.", "ko": "정오예요."},
        ],
        "practice": [
            {"q": "'몇 시예요?'", "a": "What time is it?"},
            {"q": "'5시예요.' (정각)", "a": "It's five o'clock."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🔑",
        "title_en": "Possessives (my, your...)",
        "title_ko": "소유격",
        "explain": "'누구의'를 나타내요. 명사 앞에 붙여요. (my book = 내 책)",
        "points": [
            {"en": "my / your / his / her", "ko": "나의 / 너의 / 그의 / 그녀의"},
            {"en": "its / our / their", "ko": "그것의 / 우리의 / 그들의"},
        ],
        "examples": [
            {"en": "This is my phone.", "ko": "이건 내 전화기예요."},
            {"en": "What is your name?", "ko": "이름이 뭐예요?"},
            {"en": "Her bag is red.", "ko": "그녀의 가방은 빨간색이에요."},
            {"en": "Our house is small.", "ko": "우리 집은 작아요."},
        ],
        "practice": [
            {"q": "'그의'는 영어로?", "a": "his"},
            {"q": "'이건 우리 차예요.'", "a": "This is our car."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🏃",
        "title_en": "Present Simple",
        "title_ko": "일반동사 현재 (긍정)",
        "explain": "be동사가 아닌 '행동'을 나타내는 동사예요. 보통 주어 뒤에 그대로 써요.",
        "points": [
            {"en": "I like ~", "ko": "나는 ~을 좋아해요"},
            {"en": "I have ~", "ko": "나는 ~을 가지고 있어요"},
            {"en": "I want ~", "ko": "나는 ~을 원해요"},
        ],
        "examples": [
            {"en": "I like coffee.", "ko": "나는 커피를 좋아해요."},
            {"en": "We have a dog.", "ko": "우리는 개가 있어요."},
            {"en": "They live in Seoul.", "ko": "그들은 서울에 살아요."},
            {"en": "I want some water.", "ko": "물 좀 주세요."},
        ],
        "practice": [
            {"q": "'나는 음악을 좋아해요.'", "a": "I like music."},
            {"q": "'우리는 시간이 있어요.'", "a": "We have time."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "👤",
        "title_en": "Third Person -s",
        "title_ko": "3인칭 단수 -s",
        "explain": "주어가 he, she, it (한 사람/한 개)이면 동사 끝에 -s를 붙여요. have는 has로 바뀌어요.",
        "points": [
            {"en": "He likes / She wants / It works", "ko": "동사 + s"},
            {"en": "have → has", "ko": "She has a car."},
            {"en": "go→goes, study→studies", "ko": "약간 변하는 것"},
        ],
        "examples": [
            {"en": "She likes tea.", "ko": "그녀는 차를 좋아해요."},
            {"en": "He works in a bank.", "ko": "그는 은행에서 일해요."},
            {"en": "My sister has two kids.", "ko": "내 여동생은 아이가 둘 있어요."},
            {"en": "He goes to school.", "ko": "그는 학교에 가요."},
        ],
        "practice": [
            {"q": "He ___ (like) pizza.", "a": "He likes pizza."},
            {"q": "She ___ (have) a cat.", "a": "She has a cat."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "🚫",
        "title_en": "Negative (don't / doesn't)",
        "title_ko": "일반동사 부정",
        "explain": "일반동사를 부정할 때 동사 앞에 don't를 써요. 주어가 he/she/it이면 doesn't (이때 동사는 원형!).",
        "points": [
            {"en": "I/You/We/They don't ~", "ko": "~하지 않아요"},
            {"en": "He/She/It doesn't ~", "ko": "~하지 않아요 (동사 원형)"},
        ],
        "examples": [
            {"en": "I don't like onions.", "ko": "나는 양파를 안 좋아해요."},
            {"en": "She doesn't eat meat.", "ko": "그녀는 고기를 안 먹어요."},
            {"en": "We don't have time.", "ko": "우리는 시간이 없어요."},
            {"en": "He doesn't know.", "ko": "그는 몰라요."},
        ],
        "practice": [
            {"q": "'나는 커피를 안 마셔요.'", "a": "I don't drink coffee."},
            {"q": "He ___ (not like) it.", "a": "He doesn't like it."},
        ],
    },
    {
        "unit": "Unit 2. 문장 만들기",
        "emoji": "❓",
        "title_en": "Questions (Do / Does)",
        "title_ko": "일반동사 의문문",
        "explain": "일반동사로 질문할 때 문장 앞에 Do를 써요. 주어가 he/she/it이면 Does (동사는 원형).",
        "points": [
            {"en": "Do you ~?", "ko": "→ Yes, I do. / No, I don't."},
            {"en": "Does he ~?", "ko": "→ Yes, he does. / No, he doesn't."},
        ],
        "examples": [
            {"en": "Do you like sports?", "ko": "운동 좋아해요?"},
            {"en": "Does she speak English?", "ko": "그녀는 영어를 해요?"},
            {"en": "Do they live here?", "ko": "그들은 여기 살아요?"},
            {"en": "Yes, I do.", "ko": "네, 그래요."},
        ],
        "practice": [
            {"q": "'당신은 김치를 좋아해요?'", "a": "Do you like kimchi?"},
            {"q": "'Does he work here?'에 부정으로 답하면?", "a": "No, he doesn't."},
        ],
    },
    # ===== Unit 3. 넓혀가기 =====
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "🔍",
        "title_en": "what / who",
        "title_ko": "의문사 (무엇/누구)",
        "explain": "'무엇'은 what, '누구'는 who. 질문을 구체적으로 만들어요.",
        "points": [
            {"en": "What is ~?", "ko": "~은 무엇이에요?"},
            {"en": "Who is ~?", "ko": "~은 누구예요?"},
            {"en": "What do you ~?", "ko": "무엇을 ~해요?"},
        ],
        "examples": [
            {"en": "What is this?", "ko": "이게 뭐예요?"},
            {"en": "What is your job?", "ko": "직업이 뭐예요?"},
            {"en": "Who is she?", "ko": "그녀는 누구예요?"},
            {"en": "What do you want?", "ko": "뭘 원해요?"},
        ],
        "practice": [
            {"q": "'이게 뭐예요?'", "a": "What is this?"},
            {"q": "'그는 누구예요?'", "a": "Who is he?"},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "📍",
        "title_en": "where / when",
        "title_ko": "의문사 (어디/언제)",
        "explain": "'어디'는 where, '언제'는 when.",
        "points": [
            {"en": "Where is ~?", "ko": "~은 어디예요?"},
            {"en": "Where do you ~?", "ko": "어디서 ~해요?"},
            {"en": "When is ~?", "ko": "~은 언제예요?"},
        ],
        "examples": [
            {"en": "Where is the station?", "ko": "역이 어디예요?"},
            {"en": "Where do you live?", "ko": "어디 살아요?"},
            {"en": "When is your birthday?", "ko": "생일이 언제예요?"},
            {"en": "When does it start?", "ko": "언제 시작해요?"},
        ],
        "practice": [
            {"q": "'화장실이 어디예요?'", "a": "Where is the bathroom?"},
            {"q": "'회의가 언제예요?'", "a": "When is the meeting?"},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "🤔",
        "title_en": "why / how",
        "title_ko": "의문사 (왜/어떻게)",
        "explain": "'왜'는 why, '어떻게'는 how. how 뒤에 단어를 붙여 양/정도도 물어요 (how much 얼마, how old 몇 살).",
        "points": [
            {"en": "Why ~?  /  Because ~", "ko": "왜 ~? / 왜냐하면 ~"},
            {"en": "How ~?", "ko": "어떻게 ~?"},
            {"en": "How much? / How many? / How old?", "ko": "얼마? / 몇 개? / 몇 살?"},
        ],
        "examples": [
            {"en": "Why are you sad?", "ko": "왜 슬퍼요?"},
            {"en": "How are you?", "ko": "어떻게 지내요?"},
            {"en": "How much is it?", "ko": "얼마예요?"},
            {"en": "How old are you?", "ko": "몇 살이에요?"},
        ],
        "practice": [
            {"q": "'얼마예요?'", "a": "How much is it?"},
            {"q": "'왜 늦었어요?'", "a": "Why are you late?"},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "🎨",
        "title_en": "Adjectives",
        "title_ko": "형용사",
        "explain": "사람·사물의 모습/상태를 꾸미는 말이에요. 명사 앞이나 be동사 뒤에 써요.",
        "points": [
            {"en": "big, small, good, new", "ko": "큰, 작은, 좋은, 새로운"},
            {"en": "a big house", "ko": "형용사 + 명사 (큰 집)"},
            {"en": "It is big.", "ko": "be동사 + 형용사 (그것은 크다)"},
        ],
        "examples": [
            {"en": "It's a beautiful day.", "ko": "아름다운 날이에요."},
            {"en": "She has long hair.", "ko": "그녀는 머리가 길어요."},
            {"en": "The food is delicious.", "ko": "음식이 맛있어요."},
            {"en": "I have a new car.", "ko": "나는 새 차가 있어요."},
        ],
        "practice": [
            {"q": "'큰 집' (어순 주의!)", "a": "a big house"},
            {"q": "'그 영화는 지루해요.'", "a": "The movie is boring."},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "💪",
        "title_en": "can (ability)",
        "title_ko": "can (할 수 있다)",
        "explain": "'~할 수 있다'는 can을 동사 앞에 써요. 부정은 can't. 질문은 Can you ~?",
        "points": [
            {"en": "I can ~", "ko": "나는 ~할 수 있어요"},
            {"en": "I can't ~", "ko": "나는 ~할 수 없어요"},
            {"en": "Can you ~?", "ko": "~할 수 있어요? / ~해 줄래요?"},
        ],
        "examples": [
            {"en": "I can swim.", "ko": "나는 수영할 수 있어요."},
            {"en": "She can't drive.", "ko": "그녀는 운전을 못해요."},
            {"en": "Can you help me?", "ko": "도와줄 수 있어요?"},
            {"en": "Can I sit here?", "ko": "여기 앉아도 돼요?"},
        ],
        "practice": [
            {"q": "'나는 영어를 조금 할 수 있어요.'", "a": "I can speak a little English."},
            {"q": "'도와줄 수 있어요?'", "a": "Can you help me?"},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "📦",
        "title_en": "There is / There are",
        "title_ko": "~이 있다",
        "explain": "'~이 있다'는 There is(하나) / There are(여럿)로 시작해요.",
        "points": [
            {"en": "There is + 단수", "ko": "~이 (하나) 있다"},
            {"en": "There are + 복수", "ko": "~이 (여럿) 있다"},
            {"en": "Is there ~?", "ko": "~이 있어요?"},
        ],
        "examples": [
            {"en": "There is a problem.", "ko": "문제가 하나 있어요."},
            {"en": "There are many people.", "ko": "사람이 많이 있어요."},
            {"en": "Is there a bank near here?", "ko": "이 근처에 은행이 있어요?"},
            {"en": "There is no time.", "ko": "시간이 없어요."},
        ],
        "practice": [
            {"q": "'탁자 위에 책이 한 권 있어요.'", "a": "There is a book on the table."},
            {"q": "'방이 두 개 있어요.'", "a": "There are two rooms."},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "📌",
        "title_en": "Prepositions (place)",
        "title_ko": "전치사 (장소)",
        "explain": "위치를 나타내는 말이에요. in(안), on(위), under(아래), next to(옆).",
        "points": [
            {"en": "in / on / under", "ko": "~안에 / ~위에 / ~아래에"},
            {"en": "next to / in front of", "ko": "~옆에 / ~앞에"},
        ],
        "examples": [
            {"en": "The keys are on the table.", "ko": "열쇠는 탁자 위에 있어요."},
            {"en": "The cat is under the chair.", "ko": "고양이는 의자 아래 있어요."},
            {"en": "The bank is next to the cafe.", "ko": "은행은 카페 옆에 있어요."},
            {"en": "It's in my bag.", "ko": "그건 내 가방 안에 있어요."},
        ],
        "practice": [
            {"q": "'고양이가 상자 안에 있어요.'", "a": "The cat is in the box."},
            {"q": "'가게는 호텔 옆에 있어요.'", "a": "The shop is next to the hotel."},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "⏰",
        "title_en": "Prepositions (time)",
        "title_ko": "전치사 (시간)",
        "explain": "시간에는 at(시각), on(요일·날짜), in(월·연도·아침/오후)을 써요.",
        "points": [
            {"en": "at + 시각", "ko": "at 7 o'clock"},
            {"en": "on + 요일/날짜", "ko": "on Monday"},
            {"en": "in + 월/연도/때", "ko": "in May, in the morning"},
        ],
        "examples": [
            {"en": "The movie starts at eight.", "ko": "영화는 8시에 시작해요."},
            {"en": "I'm busy on Friday.", "ko": "나는 금요일에 바빠요."},
            {"en": "It's cold in winter.", "ko": "겨울에는 추워요."},
            {"en": "See you in the morning.", "ko": "아침에 봐요."},
        ],
        "practice": [
            {"q": "___ 9 o'clock (at/on/in?)", "a": "at 9 o'clock"},
            {"q": "___ Sunday (at/on/in?)", "a": "on Sunday"},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "🔁",
        "title_en": "Frequency adverbs",
        "title_ko": "빈도부사",
        "explain": "얼마나 자주 하는지 나타내요. 보통 일반동사 앞, be동사 뒤에 와요.",
        "points": [
            {"en": "always > usually > sometimes > never", "ko": "항상 > 보통 > 가끔 > 절대 안"},
        ],
        "examples": [
            {"en": "I always drink coffee.", "ko": "나는 항상 커피를 마셔요."},
            {"en": "She is usually busy.", "ko": "그녀는 보통 바빠요."},
            {"en": "We sometimes eat out.", "ko": "우리는 가끔 외식해요."},
            {"en": "He never gives up.", "ko": "그는 절대 포기하지 않아요."},
        ],
        "practice": [
            {"q": "'나는 가끔 늦어요.'", "a": "I am sometimes late."},
            {"q": "'그녀는 항상 웃어요.'", "a": "She always smiles."},
        ],
    },
    {
        "unit": "Unit 3. 넓혀가기",
        "emoji": "🎯",
        "title_en": "Object pronouns",
        "title_ko": "목적격 대명사",
        "explain": "동사나 전치사 뒤에서 '~을/~에게'로 쓰는 형태예요. (I→me, he→him...)",
        "points": [
            {"en": "me / you / him / her", "ko": "나를 / 너를 / 그를 / 그녀를"},
            {"en": "it / us / them", "ko": "그것을 / 우리를 / 그들을"},
        ],
        "examples": [
            {"en": "Call me later.", "ko": "나중에 전화해요."},
            {"en": "I love you.", "ko": "사랑해요."},
            {"en": "Give it to her.", "ko": "그걸 그녀에게 줘요."},
            {"en": "I know them.", "ko": "나는 그들을 알아요."},
        ],
        "practice": [
            {"q": "'그를 도와주세요.'", "a": "Help him."},
            {"q": "'그것을 나에게 줘요.'", "a": "Give it to me."},
        ],
    },
    # ===== Unit 4. 시제 =====
    {
        "unit": "Unit 4. 시제",
        "emoji": "⏳",
        "title_en": "Present Continuous",
        "title_ko": "현재진행형 (~하는 중)",
        "explain": "'지금 ~하고 있다'는 be동사 + 동사ing로 표현해요.",
        "points": [
            {"en": "I am ~ing", "ko": "나는 ~하는 중이에요"},
            {"en": "He is ~ing / They are ~ing", "ko": "그/그들은 ~하는 중"},
        ],
        "examples": [
            {"en": "I am eating now.", "ko": "나는 지금 먹고 있어요."},
            {"en": "She is sleeping.", "ko": "그녀는 자고 있어요."},
            {"en": "They are working.", "ko": "그들은 일하고 있어요."},
            {"en": "It is raining.", "ko": "비가 오고 있어요."},
        ],
        "practice": [
            {"q": "'나는 TV를 보고 있어요.'", "a": "I am watching TV."},
            {"q": "'그는 공부하고 있어요.'", "a": "He is studying."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "❓",
        "title_en": "Present Continuous (neg/ques)",
        "title_ko": "현재진행형 부정/의문",
        "explain": "부정은 be동사 뒤에 not, 질문은 be동사를 문장 앞으로 보내요.",
        "points": [
            {"en": "I'm not ~ing", "ko": "~하고 있지 않아요"},
            {"en": "Are you ~ing?", "ko": "~하고 있어요?"},
        ],
        "examples": [
            {"en": "I'm not joking.", "ko": "농담하는 거 아니에요."},
            {"en": "She isn't listening.", "ko": "그녀는 안 듣고 있어요."},
            {"en": "Are you coming?", "ko": "올 거예요?"},
            {"en": "What are you doing?", "ko": "뭐 하고 있어요?"},
        ],
        "practice": [
            {"q": "'뭐 하고 있어요?'", "a": "What are you doing?"},
            {"q": "'나는 안 자고 있어요.'", "a": "I'm not sleeping."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "⏮️",
        "title_en": "Past BE (was / were)",
        "title_ko": "과거 be동사",
        "explain": "'~였다'는 be동사의 과거형. I/he/she/it = was, you/we/they = were.",
        "points": [
            {"en": "I / He / She / It was ~", "ko": "~였다"},
            {"en": "You / We / They were ~", "ko": "~였다"},
            {"en": "부정: wasn't / weren't", "ko": "~아니었다"},
        ],
        "examples": [
            {"en": "I was tired yesterday.", "ko": "나는 어제 피곤했어요."},
            {"en": "She was at home.", "ko": "그녀는 집에 있었어요."},
            {"en": "They were happy.", "ko": "그들은 행복했어요."},
            {"en": "It wasn't easy.", "ko": "쉽지 않았어요."},
        ],
        "practice": [
            {"q": "'나는 어제 바빴어요.'", "a": "I was busy yesterday."},
            {"q": "'그들은 거기 있었어요.'", "a": "They were there."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "⏪",
        "title_en": "Past (regular -ed)",
        "title_ko": "과거 일반동사 (규칙)",
        "explain": "대부분의 동사는 과거형에 -ed를 붙여요. (주어와 상관없이 모양이 똑같아요!)",
        "points": [
            {"en": "play→played, want→wanted", "ko": "-ed 붙이기"},
            {"en": "live→lived (e로 끝나면 -d만)", "ko": "-d만"},
        ],
        "examples": [
            {"en": "I watched a movie.", "ko": "나는 영화를 봤어요."},
            {"en": "We played soccer.", "ko": "우리는 축구를 했어요."},
            {"en": "She walked to school.", "ko": "그녀는 학교에 걸어갔어요."},
            {"en": "They liked the food.", "ko": "그들은 음식을 좋아했어요."},
        ],
        "practice": [
            {"q": "'나는 어제 일했어요.'", "a": "I worked yesterday."},
            {"q": "'visit'의 과거형은?", "a": "visited"},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "🔀",
        "title_en": "Past (irregular)",
        "title_ko": "과거 일반동사 (불규칙)",
        "explain": "어떤 동사는 -ed가 아니라 모양이 완전히 바뀌어요. 자주 쓰는 건 외워두면 좋아요.",
        "points": [
            {"en": "go→went, eat→ate, have→had", "ko": "가다/먹다/가지다"},
            {"en": "see→saw, get→got, make→made", "ko": "보다/얻다/만들다"},
        ],
        "examples": [
            {"en": "I went to Busan.", "ko": "나는 부산에 갔어요."},
            {"en": "We had dinner.", "ko": "우리는 저녁을 먹었어요."},
            {"en": "She saw a movie.", "ko": "그녀는 영화를 봤어요."},
            {"en": "He made a cake.", "ko": "그는 케이크를 만들었어요."},
        ],
        "practice": [
            {"q": "'go'의 과거형은?", "a": "went"},
            {"q": "'나는 그를 봤어요.'", "a": "I saw him."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "❓",
        "title_en": "Past (didn't / Did)",
        "title_ko": "과거 부정/의문",
        "explain": "과거를 부정하거나 질문할 때 did를 써요. 이때 동사는 원형으로 돌아가요!",
        "points": [
            {"en": "I didn't ~ (동사원형)", "ko": "~하지 않았어요"},
            {"en": "Did you ~?", "ko": "~했어요? → Yes, I did. / No, I didn't."},
        ],
        "examples": [
            {"en": "I didn't sleep well.", "ko": "나는 잘 못 잤어요."},
            {"en": "She didn't come.", "ko": "그녀는 안 왔어요."},
            {"en": "Did you eat?", "ko": "밥 먹었어요?"},
            {"en": "Did he call you?", "ko": "그가 전화했어요?"},
        ],
        "practice": [
            {"q": "'나는 그걸 안 봤어요.'", "a": "I didn't see it."},
            {"q": "'어제 잘 잤어요?'", "a": "Did you sleep well?"},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "🔮",
        "title_en": "Future (will)",
        "title_ko": "미래 (will)",
        "explain": "'~할 것이다'는 동사 앞에 will을 써요. 주어와 상관없이 똑같아요.",
        "points": [
            {"en": "I will ~ (I'll)", "ko": "나는 ~할 거예요"},
            {"en": "won't", "ko": "~하지 않을 거예요 (will not)"},
        ],
        "examples": [
            {"en": "I will call you later.", "ko": "나중에 전화할게요."},
            {"en": "It will rain tomorrow.", "ko": "내일 비가 올 거예요."},
            {"en": "She will be fine.", "ko": "그녀는 괜찮을 거예요."},
            {"en": "I won't forget.", "ko": "잊지 않을게요."},
        ],
        "practice": [
            {"q": "'내가 도와줄게요.'", "a": "I will help you."},
            {"q": "'그는 늦을 거예요.'", "a": "He will be late."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "🗺️",
        "title_en": "Future (be going to)",
        "title_ko": "미래 (be going to)",
        "explain": "이미 계획한 일은 be going to + 동사원형으로 자주 말해요.",
        "points": [
            {"en": "I am going to ~", "ko": "나는 ~할 거예요 (계획)"},
            {"en": "He is going to ~", "ko": "그는 ~할 거예요"},
        ],
        "examples": [
            {"en": "I'm going to study tonight.", "ko": "나는 오늘 밤 공부할 거예요."},
            {"en": "We are going to travel.", "ko": "우리는 여행 갈 거예요."},
            {"en": "She is going to buy a car.", "ko": "그녀는 차를 살 거예요."},
            {"en": "It's going to be okay.", "ko": "괜찮을 거예요."},
        ],
        "practice": [
            {"q": "'나는 친구를 만날 거예요.'", "a": "I'm going to meet a friend."},
            {"q": "'우리는 영화를 볼 거예요.'", "a": "We are going to watch a movie."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "⚖️",
        "title_en": "some / any, many / much",
        "title_ko": "수량 표현",
        "explain": "some은 긍정문, any는 부정·의문문에 주로 써요. 셀 수 있으면 many, 없으면 much.",
        "points": [
            {"en": "some (긍정) / any (부정·의문)", "ko": "약간, 조금"},
            {"en": "many + 셀 수 있는 / much + 셀 수 없는", "ko": "많은"},
            {"en": "a lot of (둘 다 OK)", "ko": "많은"},
        ],
        "examples": [
            {"en": "I have some money.", "ko": "나는 돈이 좀 있어요."},
            {"en": "I don't have any time.", "ko": "나는 시간이 전혀 없어요."},
            {"en": "How many people?", "ko": "몇 명이에요?"},
            {"en": "There isn't much water.", "ko": "물이 많지 않아요."},
        ],
        "practice": [
            {"q": "'나는 질문이 좀 있어요.'", "a": "I have some questions."},
            {"q": "'설탕이 많지 않아요.'", "a": "There isn't much sugar."},
        ],
    },
    {
        "unit": "Unit 4. 시제",
        "emoji": "📊",
        "title_en": "Comparatives (-er than)",
        "title_ko": "비교급",
        "explain": "둘을 비교할 때 형용사에 -er를 붙이고 than(~보다)을 써요. 긴 단어는 more를 앞에 써요.",
        "points": [
            {"en": "짧은 형용사 + er: taller, faster", "ko": "더 ~한"},
            {"en": "긴 형용사: more expensive", "ko": "더 ~한"},
            {"en": "불규칙: good→better, bad→worse", "ko": "더 좋은/나쁜"},
        ],
        "examples": [
            {"en": "I am taller than you.", "ko": "나는 너보다 키가 커요."},
            {"en": "This is cheaper.", "ko": "이게 더 싸요."},
            {"en": "She is more beautiful.", "ko": "그녀가 더 아름다워요."},
            {"en": "It's better than before.", "ko": "전보다 나아요."},
        ],
        "practice": [
            {"q": "'오늘이 어제보다 더워요.'", "a": "Today is hotter than yesterday."},
            {"q": "'good'의 비교급은?", "a": "better"},
        ],
    },
    # ===== Unit 5. 마무리 =====
    {
        "unit": "Unit 5. 마무리",
        "emoji": "🏆",
        "title_en": "Superlatives (the -est)",
        "title_ko": "최상급",
        "explain": "셋 이상 중 '가장 ~한'은 형용사에 -est를 붙이고 앞에 the를 써요. 긴 단어는 the most.",
        "points": [
            {"en": "the + 형용사est: the tallest", "ko": "가장 ~한"},
            {"en": "the most + 긴 형용사", "ko": "the most popular"},
            {"en": "불규칙: the best, the worst", "ko": "최고/최악"},
        ],
        "examples": [
            {"en": "He is the tallest in class.", "ko": "그는 반에서 가장 키가 커요."},
            {"en": "This is the best restaurant.", "ko": "여기가 최고의 식당이에요."},
            {"en": "It's the most famous place.", "ko": "그곳은 가장 유명한 곳이에요."},
            {"en": "Today is the hottest day.", "ko": "오늘이 가장 더운 날이에요."},
        ],
        "practice": [
            {"q": "'big'의 최상급은?", "a": "the biggest"},
            {"q": "'이게 제일 싼 거예요.'", "a": "This is the cheapest."},
        ],
    },
    {
        "unit": "Unit 5. 마무리",
        "emoji": "📢",
        "title_en": "Commands (Imperatives)",
        "title_ko": "명령문",
        "explain": "상대에게 '~해라/하지 마라'고 할 때 주어 없이 동사로 시작해요. 부정은 Don't.",
        "points": [
            {"en": "동사원형으로 시작: Sit down.", "ko": "~해라 (앉아요)"},
            {"en": "Don't + 동사: Don't worry.", "ko": "~하지 마 (걱정 마요)"},
        ],
        "examples": [
            {"en": "Open the window, please.", "ko": "창문 좀 열어주세요."},
            {"en": "Be careful.", "ko": "조심해요."},
            {"en": "Don't be late.", "ko": "늦지 마요."},
            {"en": "Turn right here.", "ko": "여기서 우회전해요."},
        ],
        "practice": [
            {"q": "'걱정 마요.'", "a": "Don't worry."},
            {"q": "'여기 앉으세요.'", "a": "Sit here, please."},
        ],
    },
    {
        "unit": "Unit 5. 마무리",
        "emoji": "🤝",
        "title_en": "Suggestions (Let's / How about)",
        "title_ko": "제안하기",
        "explain": "같이 하자고 제안할 때 Let's + 동사, 또는 How about + 동사ing를 써요.",
        "points": [
            {"en": "Let's ~", "ko": "~하자"},
            {"en": "How about ~ing?", "ko": "~하는 게 어때요?"},
            {"en": "Why don't we ~?", "ko": "우리 ~하는 게 어때요?"},
        ],
        "examples": [
            {"en": "Let's go.", "ko": "가자."},
            {"en": "Let's eat lunch.", "ko": "점심 먹자."},
            {"en": "How about coffee?", "ko": "커피 어때요?"},
            {"en": "Why don't we take a break?", "ko": "좀 쉬는 게 어때요?"},
        ],
        "practice": [
            {"q": "'쉬자.'", "a": "Let's take a break."},
            {"q": "'산책하는 게 어때요?'", "a": "How about taking a walk?"},
        ],
    },
    {
        "unit": "Unit 5. 마무리",
        "emoji": "🎯",
        "title_en": "Verb + to (want to, have to)",
        "title_ko": "동사 + to",
        "explain": "동사 두 개를 이을 때 'to + 동사원형'을 자주 써요. want to(~하고 싶다), have to(~해야 한다).",
        "points": [
            {"en": "want to ~", "ko": "~하고 싶다"},
            {"en": "have to ~", "ko": "~해야 한다"},
            {"en": "like to ~", "ko": "~하는 걸 좋아하다"},
        ],
        "examples": [
            {"en": "I want to go home.", "ko": "나는 집에 가고 싶어요."},
            {"en": "I have to work today.", "ko": "나는 오늘 일해야 해요."},
            {"en": "She likes to read.", "ko": "그녀는 읽는 걸 좋아해요."},
            {"en": "We need to hurry.", "ko": "우리는 서둘러야 해요."},
        ],
        "practice": [
            {"q": "'나는 자고 싶어요.'", "a": "I want to sleep."},
            {"q": "'나는 가야 해요.'", "a": "I have to go."},
        ],
    },
    {
        "unit": "Unit 5. 마무리",
        "emoji": "🔗",
        "title_en": "Connectors (and, but, so...)",
        "title_ko": "연결어",
        "explain": "문장을 이어주는 말이에요. 말을 더 길고 자연스럽게 만들어줘요.",
        "points": [
            {"en": "and / but / or", "ko": "그리고 / 그러나 / 또는"},
            {"en": "so / because", "ko": "그래서 / 왜냐하면"},
        ],
        "examples": [
            {"en": "I'm tired, so I'll rest.", "ko": "피곤해서 쉴 거예요."},
            {"en": "It's small but nice.", "ko": "작지만 좋아요."},
            {"en": "I like it because it's cheap.", "ko": "싸서 좋아요."},
            {"en": "Tea or coffee?", "ko": "차 아니면 커피요?"},
        ],
        "practice": [
            {"q": "'비가 와서 집에 있었어요.'", "a": "It rained, so I stayed home."},
            {"q": "'싸지만 좋아요.'", "a": "It's cheap but good."},
        ],
    },
]
