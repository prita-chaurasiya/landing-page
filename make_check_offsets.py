from subprocess import run

code = """
const { spawn } = require('child_process');
const http = require('http');

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

(async () => {
  const chrome = spawn('C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe', [
    '--remote-debugging-port=9298',
    '--headless=new',
    '--window-size=1440,900'
  ]);
  await new Promise(r => setTimeout(r, 1500));
  const targets = await fetchJson('http://127.0.0.1:9298/json/list');
  const ws = new WebSocket(targets[0].webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  
  let id = 1;
  const send = (method, params={}) => new Promise(res => {
    const curId = id++;
    const handler = evt => {
      const msg = JSON.parse(evt.data);
      if (msg.id === curId) { ws.removeEventListener('message', handler); res(msg.result); }
    };
    ws.addEventListener('message', handler);
    ws.send(JSON.stringify({ id: curId, method, params }));
  });

  await send('Page.navigate', { url: 'file:///d:/landing page/index.html' });
  await new Promise(r => setTimeout(r, 2000));
  
  const expr = `(() => {
    const ids = ['hero', 'stats-bar', 'focus-areas', 'about', 'videos', 'plans', 'membership-form', 'faq', 'contact'];
    return ids.map(id => {
      const el = document.getElementById(id) || document.querySelector('.' + id);
      if (!el) return { id, notFound: true };
      const rect = el.getBoundingClientRect();
      return { id, top: Math.round(rect.top + window.scrollY), height: Math.round(rect.height) };
    });
  })()`;

  const res = await send('Runtime.evaluate', {
    expression: expr,
    returnByValue: true
  });
  console.log(JSON.stringify(res.result.value, null, 2));
  chrome.kill();
})();
"""

with open('check_section_offsets.cjs', 'w', encoding='utf-8') as f:
    f.write(code)
print("Saved check_section_offsets.cjs")

