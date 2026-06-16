# 신규 섹터 이벤트 카드 — 이미지 생성 프롬프트

ChatGPT(또는 이미지 생성 도구)에 아래 프롬프트를 넣어 생성하고,
`assets/cards/<카드ID>.jpg` 로 저장하면 게임에 자동 반영됩니다.
(이미지가 없으면 🗳️ 아이콘으로 표시되며, 게임은 정상 작동합니다.)

## 공통 스타일 (기존 카드 톤)
> Digital illustration, navy & electric-blue palette, glowing blue accents, modern financial/tech aesthetic,
> sci-fi card frame border, subtle city skyline background, clean and polished, cinematic lighting, NO text. 1:1.

각 카드는 위 공통 스타일 + 아래 장면(scene)을 붙여 생성하세요.

---

## Batch 1 — 성장군 (TECH·SEMI·BIO·AUTO), 신규 16장

### TECH
- **E_TECH_DEFENSIVE_SW** (방어적 SW·보안 수요): a glowing digital shield and padlock protecting server racks, steady defensive cybersecurity, calm blue tone
- **E_TECH_RERATING_NOISE** (회복 초기 옥석 가리기): diverging stock arrows — some rising, some falling — sorting gems from rubble, early-recovery volatility
- **E_TECH_IPO_BOOM** (초대형 성장주 IPO 붐): a giant rocket launching beside a ringing stock-exchange bell, confetti and crowds, euphoric mega-IPO listing
- **E_TECH_RATE_DERATING** (금리 급등·멀티플 압박): a steep red interest-rate arrow pressing down a tall glowing valuation skyscraper, growth multiples compressed

### SEMI
- **E_SEMI_SUBSIDY** (반도체 산업 보조금): government subsidy funds flowing into a semiconductor fab, policy support, blue industrial
- **E_SEMI_PRICE_LAG** (판가 회복 지연): rising chip-shipment volume bars but a flat, lagging price line, margin pressure
- **E_SEMI_OVERBUILD** (경쟁적 증설 과잉 우려): many semiconductor fabs under construction at once, cranes everywhere, oversupply warning
- **E_SEMI_SUPERCYCLE** (AI 슈퍼사이클 연장): an extended cresting wave of glowing AI chips, neural-network patterns, supercycle momentum, electric blue

### BIO
- **E_BIO_PANDEMIC** (팬데믹 확산·치료제 수요): a virus particle and a glowing vaccine vial over quiet empty city streets, pandemic, biotech demand surge
- **E_BIO_TRIAL_DELAY** (임상 지연·자금 경색): a stalled clinical-trial timeline with a drying funding pipeline, delayed research, muted tones
- **E_BIO_OBESITY_DRUG** (비만치료제 블록버스터): a glowing blockbuster injectable pen with a soaring pharma sales chart, obesity-treatment breakthrough
- **E_BIO_BUBBLE_WARN** (바이오 밸류 과열 경고): an over-inflated biotech valuation bubble with a warning crack, overheated speculation, red accents

### AUTO
- **E_AUTO_INCENTIVE** (노후차 교체·구매보조금): an old car traded for a shiny new EV with a government incentive coupon, bright showroom
- **E_AUTO_PRICE_WAR** (EV 가격 경쟁 심화): several EVs with slashing price tags in a fierce price war, downward price arrows
- **E_AUTO_RESHORING** (보호무역 속 현지생산 수혜): a thriving domestic auto factory protected behind a tariff wall, reshoring, blue industrial
- **E_AUTO_TRADE_WAR** (관세 전쟁 격화): escalating tariff walls between major economies blocking auto trade, stopped container ships, tension, red accents

---

## Batch 2 — 경기군 (INDU·FIN·CONS), 신규 12장

### INDU
- **E_INDU_INFRA_STIMULUS** (경기부양 인프라 발주): government infrastructure stimulus — roads and power-grid construction, cranes, blue
- **E_INDU_LABOR_COST** (인건비·파업 압박): factory workers striking with a rising wage-cost arrow, labor margin pressure
- **E_INDU_DEFENSE_BOOM** (지정학 긴장·방산 발주): defense-industry boom, military hardware factory, geopolitical tension, steel-blue
- **E_INDU_QUAKE** (대지진·공급망 충격): a major earthquake cracking a factory and severing a supply chain, disrupted logistics, dramatic

### FIN
- **E_FIN_RATE_CUT** (정책금리 인하·유동성 공급): a central bank cutting rates, liquidity flowing into markets, downward rate arrow, relief
- **E_FIN_REGULATION** (건전성 규제 강화): a bank under regulatory scrutiny, compliance documents, tighter capital rules
- **E_FIN_TRADING_BOOM** (거래대금 급증·IB 호황): a frenetic trading floor, soaring volume, IPO/M&A deals, euphoric
- **E_FIN_ELECTION_RISK** (주요 선거·정책 불확실성): a ballot box and an uncertain policy fork-in-the-road, election uncertainty, risk-off mood

### CONS
- **E_CONS_STAPLES** (필수소비 방어 수요): a grocery cart of essential goods, defensive consumer staples, steady demand
- **E_CONS_INPUT_COST** (원가 상승·마진 압박): rising raw-material costs squeezing a consumer-product margin
- **E_CONS_LUXURY** (고소득 소비·명품 호황): a luxury boutique boom, high-end shopping, wealth effect, gold accents
- **E_CONS_INFLATION_SQUEEZE** (인플레로 실질소비 위축): inflation eroding a shrinking shopping basket, weakened purchasing power

---

## Batch 3 — 가치·방어군 (ENG·MATE·UTIL·BOND), 신규 16장

### ENG
- **E_ENG_OPEC_CUT** (감산 합의로 유가 방어): oil-producing nations agreeing to production cuts, stabilizing an oil-price floor
- **E_ENG_INVENTORY_BUILD** (재고 증가·정제마진 약세): rising oil inventory tanks with a weak refining margin
- **E_ENG_GEO_SHOCK** (지정학 위기·공급 충격): a geopolitical conflict disrupting oil supply routes, blocked tankers, oil price jump
- **E_ENG_RENEWABLE_SHIFT** (재생에너지 전환 압박): renewable transition pressuring traditional oil — wind/solar rising beside an oil rig

### MATE
- **E_MATE_SUPPLY_CUT** (광산 감산·공급 조절): mine production cuts supporting commodity prices, disciplined supply
- **E_MATE_SUBSTITUTION** (대체재·효율화 압박): material substitution and efficiency reducing demand, alternative materials
- **E_MATE_COMMODITY_SUPERCYCLE** (원자재 슈퍼사이클): a commodity supercycle surge, raw materials soaring, mining boom, inflation glow
- **E_MATE_DEMAND_DESTRUCTION** (고가에 수요 파괴): commodity prices too high destroying demand, buyers retreating

### UTIL
- **E_UTIL_DEFENSIVE_BID** (방어주 선호·배당 매력): defensive utility stocks attracting safe-haven flows, stable dividend glow
- **E_UTIL_DEMAND_DROP** (산업 전력수요 둔화): softening industrial power demand, idle factory power lines
- **E_UTIL_CAPEX_BURDEN** (송배전 투자 부담): heavy grid-transmission investment burden, power-line construction cost
- **E_UTIL_POWER_PRICE** (전력 도매가 급등): wholesale electricity price spiking at peak demand, glowing power grid

### BOND
- **E_BOND_CREDIT_SPREAD** (신용 스프레드 급등): widening credit spreads, corporate-bond stress, a rising risk gauge
- **E_BOND_REFLATION** (리플레이션·금리 반등): reflation pushing yields up, bond prices dipping, rising yield curve
- **E_BOND_SOFT_LANDING** (연착륙 기대·금리 안정): a soft-landing scenario, stable rates, calm bond market, gentle descent
- **E_BOND_PEAK_RATE** (금리 정점 통과 기대): interest rates peaking and turning over, a bond rally on rate-cut hope

