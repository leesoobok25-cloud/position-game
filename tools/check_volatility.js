// 진짜 '변동성' 측정 — 페르소나별 최종 점수의 게임 간 분산(표준편차/분위)을
// 리스크 토큰(p.risk)과 분리해 보여준다. "HUNTER는 변동성이 압도적으로 높다"를 수치로 검증.
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
    set innerHTML(v){}, get innerHTML(){ return ''; }, set textContent(v){}, get textContent(){ return ''; },
    scrollIntoView(){}, focus(){},
  }, { get(t, k){ if (k in t) return t[k]; return typeof k === 'string' && k !== 'then' ? (t[k] = el()) : undefined; }, set(){ return true; } });
}
global.document = { getElementById(){ return el(); }, createElement(){ return el(); }, querySelector(){ return el(); }, querySelectorAll(){ return []; }, body: el(), documentElement: el(), addEventListener(){} };
global.window = global;
global.localStorage = { getItem(){ return null; }, setItem(){}, removeItem(){} };
global.requestAnimationFrame = ()=>{}; global.confirm = ()=>true; global.alert = ()=>{};
global.location = { reload(){} }; global.addEventListener = ()=>{};

const mode = process.argv[2] || 'long';
const N = parseInt(process.argv[3] || '2000', 10);

const probe = `
try { window.logRow = function(){}; } catch(e){}
(function(){
  const sum = o => Object.values(o||{}).reduce((a,b)=>a+b,0);
  PENDING_MODE = '${mode}';
  const scores = {}; const tokens = {};
  Object.keys(PERSONAS).forEach(p=>{scores[p]=[];tokens[p]=[];});
  for (let g=0; g<${N}; g++){
    startGame(Object.keys(PERSONAS)[0]);
    for (const p of state.players) p.isHuman = false;
    let guard=0;
    while (state.turn <= state.maxTurn && guard < 500){
      guard++;
      switch(state.phase){
        case 0: phase2_betting(); setPhase(1); break;
        case 1: phase3_macro(); setPhase(2); break;
        case 2:
          if (state.currentMacro && state.currentMacro.pending){
            const assetOf=(p)=>p.cash+sum(p.bets);
            const leader=[...state.players].sort((a,b)=>assetOf(b)-assetOf(a))[0];
            fgExtremePick(fgPickIndexFor(leader, state.currentMacro.picks));
          }
          phase4_event(); setPhase(3); break;
        case 3: resolveEventVote(); phase5_settle(); setPhase(4); break;
        case 4: phase6_fg(); setPhase(5); break;
        case 5: phase7_next(); break;
        default: guard=999;
      }
      if (state.turn > state.maxTurn) break;
    }
    for (const p of state.players){
      const sc = (typeof p.totalScore==='number') ? p.totalScore : (p.cash+sum(p.bets));
      scores[p.personaId].push(sc);
      tokens[p.personaId].push(p.risk||0);
    }
  }
  const stat = arr => {
    const n=arr.length, mean=arr.reduce((a,b)=>a+b,0)/n;
    const sd=Math.sqrt(arr.reduce((a,b)=>a+(b-mean)*(b-mean),0)/n);
    const s=[...arr].sort((a,b)=>a-b); const q=p=>s[Math.min(n-1,Math.floor(n*p))];
    return {mean, median:q(0.5), sd, p5:q(0.05), p95:q(0.95), max:s[n-1]};
  };
  console.log('=== 분포 기준 평가 (${mode} ${N}판) — 승률 외 분포 전체 ===');
  console.log('페르소나   | 평균 | 중앙값 | 변동성SD | 5%하위 | 95%상위 |  최대 | 원칙훼손');
  for (const pid of Object.keys(PERSONAS)){
    const s=stat(scores[pid]); const tk=tokens[pid].reduce((a,b)=>a+b,0)/tokens[pid].length;
    console.log(pid.padEnd(10)+' | '+s.mean.toFixed(0).padStart(4)+' | '+String(s.median).padStart(5)+' | '+s.sd.toFixed(1).padStart(7)+' | '+String(s.p5).padStart(5)+' | '+String(s.p95).padStart(6)+' | '+String(s.max).padStart(5)+' | '+tk.toFixed(2));
  }
  console.log('\\n* 중앙값=일반적 체감, SD=변동성, 5%하위=망했을 때, 95%상위·최대=한 방. HUNTER는 중앙값↓·95%/최대↑가 정상.');
})();
`;
eval(m[1] + probe);
