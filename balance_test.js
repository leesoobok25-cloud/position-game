// Headless balance test for POSITION v5.9
const fs = require('fs');
const html = fs.readFileSync('/home/user/position-game/POSITION_v5_9_dashboard_tutorial.html', 'utf8');
const m = html.match(/<script>([\s\S]*)<\/script>\s*<\/body>/);
if (!m) { console.error('script not found'); process.exit(1); }
let code = m[1];

// --- DOM stubs ---
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
global.document = {
  getElementById(){ return el(); }, createElement(){ return el(); },
  querySelector(){ return el(); }, querySelectorAll(){ return []; },
  body: el(), documentElement: el(),
  addEventListener(){},
};
global.window = global;
global.localStorage = { getItem(){ return null; }, setItem(){}, removeItem(){} };
global.requestAnimationFrame = (f)=>{};
global.confirm = ()=>true;
global.alert = ()=>{};
global.location = { reload(){} };
global.addEventListener = ()=>{};

eval(code);

const mode = process.argv[2] || 'normal';
const n = parseInt(process.argv[3] || '1000', 10);
runAutoTest(n, mode);
