// 베팅 % 분모 검증 — 총자산이 100을 넘은 중반 턴에서
// 화면 표시 분모(budget = cash + sum(prevBets))가 실제 총자산(cash + sum(bets))과
// 같은지, 그래서 "본드 40 @ 총자산 200 → 20%"가 맞는지 실측한다.
const fs = require('fs');
const html = fs.readFileSync('/home/user/position-game/POSITION_v5_9_dashboard_tutorial.html', 'utf8');
const m = html.match(/<script>([\s\S]*)<\/script>\s*<\/body>/);
if (!m) { console.error('script not found'); process.exit(1); }

function el() {
  return new Proxy({
    style: {}, classList: { add(){}, remove(){}, toggle(){}, contains(){ return false; } },
    addEventListener(){}, appendChild(){}, removeChild(){}, remove(){},
    getBoundingClientRect(){ return {left:0,top:0,width:0,height:0,bottom:0,right:0}; },
    querySelector(){ return el(); }, querySelectorAll(){ return []; },
    set innerHTML(v){}, get innerHTML(){ return ''; },
    set textContent(v){}, get textContent(){ return ''; },
    scrollIntoView(){}, focus(){},
  }, { get(t, k){ if (k in t) return t[k]; return typeof k === 'string' && k !== 'then' ? (t[k] = el()) : undefined; }, set(){ return true; } });
}
global.document = { getElementById(){ return el(); }, createElement(){ return el(); }, querySelector(){ return el(); }, querySelectorAll(){ return []; }, body: el(), documentElement: el(), addEventListener(){} };
global.window = global;
global.localStorage = { getItem(){ return null; }, setItem(){}, removeItem(){} };
global.requestAnimationFrame = ()=>{};
global.confirm = ()=>true; global.alert = ()=>{};
global.location = { reload(){} }; global.addEventListener = ()=>{};

// 게임 코드 + 프로브를 한 스코프에서 eval (PERSONAS/state 등 const 접근 위해)
const probe = `
try { window.logRow = function(){}; } catch(e){}
(function(){
  const sum = o => Object.values(o||{}).reduce((a,b)=>a+b,0);
  PENDING_MODE = 'long';
  startGame(Object.keys(PERSONAS)[0]);
  for (const p of state.players) p.isHuman = false;
  let guard=0, printed=0, mismatches=0, checks=0;
  console.log('=== 베팅 % 분모 검증 (16턴 1게임) ===');
  console.log('형식: [턴] 페르소나 | 현금 + 베팅합 = 총자산 | budget(화면분모) | 최대베팅=금액 → 화면% vs 정답%');
  while (state.turn <= state.maxTurn && guard < 500) {
    guard++;
    switch (state.phase) {
      case 0:
        phase2_betting(); setPhase(1);
        for (const p of state.players) {
          const total  = p.cash + sum(p.bets);
          const budget = p.cash + sum(p.prevBets);
          let topSid=null, topv=-1;
          for (const k in p.bets) { if (p.bets[k] > topv) { topv=p.bets[k]; topSid=k; } }
          if (total > 150 && topv >= 1) {
            checks++;
            const shownPct = budget>0 ? Math.round(topv/budget*100) : 0;
            const truePct  = total >0 ? Math.round(topv/total *100) : 0;
            if (shownPct !== truePct) mismatches++;
            if (printed < 14) {
              console.log('T'+state.turn+' '+p.personaId.padEnd(10)+' | '+p.cash+' + '+sum(p.bets)+' = '+total+' | budget='+budget+' | '+topSid+'='+topv+' -> 화면 '+shownPct+'% vs 정답 '+truePct+'% '+(shownPct===truePct?'OK':'X불일치'));
              printed++;
            }
          }
        }
        break;
      case 1: phase3_macro(); setPhase(2); break;
      case 2:
        if (state.currentMacro && state.currentMacro.pending) {
          const assetOf = (p)=> p.cash + sum(p.bets);
          const leader = [...state.players].sort((a,b)=> assetOf(b)-assetOf(a))[0];
          fgExtremePick(fgPickIndexFor(leader, state.currentMacro.picks));
        }
        phase4_event(); setPhase(3); break;
      case 3: resolveEventVote(); phase5_settle(); setPhase(4); break;
      case 4: phase6_fg(); setPhase(5); break;
      case 5: phase7_next(); break;
      default: guard = 999;
    }
    if (state.turn > state.maxTurn) break;
  }
  console.log('\\n검사 '+checks+'건 중 분모 불일치 '+mismatches+'건');
  console.log(mismatches===0
    ? '-> 결론: 화면 % 분모 = 실제 총자산. 버그 없음 (총자산 200에서 40은 20%로 정확히 표시).'
    : '-> 결론: 분모 불일치 발견! 수정 필요.');
})();
`;

eval(m[1] + probe);
