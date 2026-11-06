const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const ARTIFACT_DIR = "C:\\Users\\Priya\\.gemini\\antigravity\\brain\\58269462-767f-4153-ab43-3be8002f365f";
const URL = "file:///d:/landing page/index.html";

async function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

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
    '--remote-debugging-port=9274',
    '--headless=new',
    '--window-size=1440,900'
  ]);
  await sleep(1500);
  const targets = await fetchJson('http://127.0.0.1:9274/json/list');
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
  await sleep(2500);

  // Trigger AOS
  await send('Runtime.evaluate', {
    expression: 'document.querySelectorAll("[data-aos]").forEach(el => { el.classList.add("aos-animate"); el.style.opacity = "1"; el.style.transform = "none"; });'
  });
  await sleep(400);

  // 1. Capture Contact Directory Cards
  await send('Runtime.evaluate', {
    expression: 'document.getElementById("contact").scrollIntoView({ behavior: "instant", block: "start" });'
  });
  await sleep(500);
  const contactShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_contact_vector_icons.png`, Buffer.from(contactShot.data, 'base64'));

  // 2. Capture Hero Floating Badges
  await send('Runtime.evaluate', {
    expression: 'window.scrollTo(0, 0);'
  });
  await sleep(500);
  const heroShot = await send('Page.captureScreenshot', {
    format: 'png',
    clip: { x: 500, y: 100, width: 900, height: 600, scale: 1 }
  });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_hero_vector_badges.png`, Buffer.from(heroShot.data, 'base64'));

  console.log('Vector icons screenshots captured successfully!');
  chrome.kill();
})();

