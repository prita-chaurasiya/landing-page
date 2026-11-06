const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 5174;
const DIST_DIR = path.resolve('dist');
const ARTIFACT_DIR = 'C:/Users/Priya/.gemini/antigravity/brain/58269462-767f-4153-ab43-3be8002f365f';
const CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp'
};

const server = http.createServer((req, res) => {
  let reqPath = decodeURI(req.url.split('?')[0]);
  if (reqPath === '/') reqPath = '/index.html';
  let filePath = path.join(DIST_DIR, reqPath);
  if (!fs.existsSync(filePath)) filePath = path.join(__dirname, reqPath);
  if (!fs.existsSync(filePath)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': mimeTypes[path.extname(filePath)] || 'text/plain' });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(PORT, async () => {
  const cdpPort = 9241;
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${cdpPort}`,
    '--headless=new',
    '--disable-gpu',
    `--user-data-dir=C:/Users/Priya/AppData/Local/Temp/chrome_cdp_p_${Date.now()}`,
    '--window-size=1440,900'
  ], { stdio: 'ignore' });

  await new Promise(r => setTimeout(r, 1200));

  function fetchJson(url) {
    return new Promise(res => {
      http.get(url, r => {
        let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
      });
    });
  }

  const list = await fetchJson(`http://127.0.0.1:${cdpPort}/json/list`);
  const ws = new WebSocket(list[0].webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);

  let id = 1;
  const callbacks = new Map();
  ws.onmessage = e => {
    const m = JSON.parse(e.data);
    if (m.id && callbacks.has(m.id)) { callbacks.get(m.id)(m.result); callbacks.delete(m.id); }
  };
  function send(method, params = {}) {
    return new Promise(res => {
      const i = id++;
      callbacks.set(i, res);
      ws.send(JSON.stringify({ id: i, method, params }));
    });
  }

  await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
  await send('Page.navigate', { url: `http://localhost:${PORT}` });
  await new Promise(r => setTimeout(r, 2000));

  // Scroll to plans
  await send('Runtime.evaluate', { expression: 'document.getElementById("plans").scrollIntoView({ behavior: "instant", block: "center" });' });
  await new Promise(r => setTimeout(r, 600));
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/v_react_plans_zoomed.png`, Buffer.from(shot.data, 'base64'));

  // Scroll to footer
  await send('Runtime.evaluate', { expression: 'document.getElementById("footer").scrollIntoView({ behavior: "instant", block: "center" });' });
  await new Promise(r => setTimeout(r, 600));
  const footShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(`${ARTIFACT_DIR}/v_react_footer_zoomed.png`, Buffer.from(footShot.data, 'base64'));

  ws.close();
  chrome.kill();
  server.close();
  console.log('Plans and footer captured successfully!');
});

