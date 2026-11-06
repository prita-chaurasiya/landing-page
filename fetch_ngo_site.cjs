const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const URL = 'https://ngowebsite.in/ngo-software';

async function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
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
  const chrome = spawn(CHROME_PATH, [
    '--remote-debugging-port=9280',
    '--headless=new',
    '--window-size=1440,900'
  ]);
  await sleep(1500);
  const targets = await fetchJson('http://127.0.0.1:9280/json/list');
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

  await send('Page.enable');
  await send('Page.navigate', { url: URL });
  await sleep(4000);

  const res = await send('Runtime.evaluate', {
    expression: '(() => {\n' +
      'const headings = Array.from(document.querySelectorAll("h1, h2, h3, h4, h5, h6, section")).map(el => ({\n' +
      '  tag: el.tagName,\n' +
      '  text: el.innerText ? el.innerText.trim().slice(0, 80) : "",\n' +
      '  className: el.className\n' +
      '})).filter(h => h.text.length > 0);\n' +
      'return headings;\n' +
    '})()',
    returnByValue: true
  });
  console.log('Headings on ngowebsite.in:');
  console.log(JSON.stringify(res.result.value, null, 2));

  // Find testimonials or reviews section and scroll to it
  const scrollRes = await send('Runtime.evaluate', {
    expression: '(() => {\n' +
      'const all = Array.from(document.querySelectorAll("section, div"));\n' +
      'for (const el of all) {\n' +
      '  const txt = (el.innerText || "").toLowerCase();\n' +
      '  if (txt.includes("what our") || txt.includes("testimonial") || txt.includes("reviews") || txt.includes("trusted by") || txt.includes("stories")) {\n' +
      '    el.scrollIntoView({ behavior: "instant", block: "center" });\n' +
      '    return { found: true, text: txt.slice(0, 100), className: el.className };\n' +
      '  }\n' +
      '}\n' +
      'return { found: false };\n' +
    '})()',
    returnByValue: true
  });
  console.log('Scroll Result:', JSON.stringify(scrollRes.result.value, null, 2));
  await sleep(1000);

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('C:\\Users\\Priya\\.gemini\\antigravity\\brain\\58269462-767f-4153-ab43-3be8002f365f\\ngo_testimonials_capture.png', Buffer.from(shot.data, 'base64'));
  console.log('Saved ngo_testimonials_capture.png');
  chrome.kill();
})();
