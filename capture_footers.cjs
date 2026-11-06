
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
    '--remote-debugging-port=9299',
    '--headless=new',
    '--window-size=1440,900'
  ]);
  await sleep(1500);
  const targets = await fetchJson('http://127.0.0.1:9299/json/list');
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
  await sleep(2000);

  // Desktop Footer
  await send('Runtime.evaluate', {
    expression: 'document.querySelector(".simple-landing-footer").scrollIntoView({ behavior: "instant", block: "start" });'
  });
  await sleep(500);
  const footerShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_section_footer.png`, Buffer.from(footerShot.data, 'base64'));

  // Switch to Mobile
  await send('Emulation.setDeviceMetricsOverride', {
    width: 390,
    height: 844,
    deviceScaleFactor: 2,
    mobile: true
  });
  await sleep(500);

  // Mobile Footer
  await send('Runtime.evaluate', {
    expression: 'document.querySelector(".simple-landing-footer").scrollIntoView({ behavior: "instant", block: "start" });'
  });
  await sleep(500);
  const mobFooterShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/audit_mobile_footer.png`, Buffer.from(mobFooterShot.data, 'base64'));

  console.log('Desktop & Mobile Footer captured successfully!');
  chrome.kill();
})();
