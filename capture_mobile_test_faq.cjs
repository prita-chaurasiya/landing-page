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
    '--remote-debugging-port=9276',
    '--headless=new',
    '--window-size=390,844'
  ]);
  await sleep(1500);
  const targets = await fetchJson('http://127.0.0.1:9276/json/list');
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
  await send('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  });
  await send('Page.navigate', { url: URL });
  await sleep(2500);

  // Trigger AOS
  await send('Runtime.evaluate', {
    expression: 'document.querySelectorAll("[data-aos]").forEach(el => { el.classList.add("aos-animate"); el.style.opacity = "1"; el.style.transform = "none"; });'
  });
  await sleep(400);

  // Mobile Testimonials
  await send('Runtime.evaluate', {
    expression: 'document.getElementById("testimonials").scrollIntoView({ behavior: "instant", block: "start" });'
  });
  await sleep(500);
  const testShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_mobile_testimonials.png`, Buffer.from(testShot.data, 'base64'));

  // Mobile FAQs
  await send('Runtime.evaluate', {
    expression: 'document.getElementById("faq").scrollIntoView({ behavior: "instant", block: "start" });'
  });
  await sleep(500);
  const faqShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_mobile_faqs.png`, Buffer.from(faqShot.data, 'base64'));

  console.log('Mobile Testimonials and FAQs captured successfully!');
  chrome.kill();
})();
