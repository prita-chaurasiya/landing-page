const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 5175;
const DIST_DIR = path.resolve('dist');
const ARTIFACT_DIR = "C:\\Users\\Priya\\.gemini\\antigravity\\brain\\58269462-767f-4153-ab43-3be8002f365f";
const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";

const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.json': 'application/json'
};

const server = http.createServer((req, res) => {
  let reqPath = decodeURI(req.url.split('?')[0]);
  if (reqPath === '/') reqPath = '/index.html';
  let filePath = path.join(DIST_DIR, reqPath);
  if (!fs.existsSync(filePath)) filePath = path.join(__dirname, reqPath);
  if (!fs.existsSync(filePath)) {
    res.writeHead(404);
    res.end('Not found');
    return;
  }
  const ext = path.extname(filePath).toLowerCase();
  res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(PORT, async () => {
  const cdpPort = 9243;
  const userDataDir = `C:\\Users\\Priya\\AppData\\Local\\Temp\\chrome_cdp_plans_${Date.now()}`;
  
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${cdpPort}`,
    `--user-data-dir=${userDataDir}`,
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    '--hide-scrollbars',
    '--window-size=1440,900'
  ], { stdio: 'ignore' });

  function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

  function fetchJson(url) {
    return new Promise((resolve, reject) => {
      http.get(url, res => {
        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
          try { resolve(JSON.parse(data)); } catch (e) { reject(e); }
        });
      }).on('error', reject);
    });
  }

  class CDPClient {
    constructor(wsUrl) {
      this.wsUrl = wsUrl;
      this.ws = null;
      this.id = 1;
      this.callbacks = new Map();
    }
    connect() {
      return new Promise((resolve, reject) => {
        this.ws = new WebSocket(this.wsUrl);
        this.ws.onopen = () => resolve();
        this.ws.onerror = err => reject(err);
        this.ws.onmessage = evt => {
          const msg = JSON.parse(evt.data);
          if (msg.id && this.callbacks.has(msg.id)) {
            const { res, rej } = this.callbacks.get(msg.id);
            this.callbacks.delete(msg.id);
            if (msg.error) rej(msg.error);
            else res(msg.result);
          }
        };
      });
    }
    send(method, params = {}) {
      return new Promise((res, rej) => {
        const id = this.id++;
        this.callbacks.set(id, { res, rej });
        this.ws.send(JSON.stringify({ id, method, params }));
      });
    }
    close() { if (this.ws) this.ws.close(); }
  }

  try {
    let version = null;
    for (let i = 0; i < 20; i++) {
      await sleep(300);
      try {
        version = await fetchJson(`http://127.0.0.1:${cdpPort}/json/version`);
        if (version && version.webSocketDebuggerUrl) break;
      } catch (e) {}
    }

    const targets = await fetchJson(`http://127.0.0.1:${cdpPort}/json/list`);
    const target = targets.find(t => t.type === 'page') || targets[0];
    const client = new CDPClient(target.webSocketDebuggerUrl);
    await client.connect();

    await client.send('Page.enable');
    await client.send('Emulation.setDeviceMetricsOverride', {
      width: 1440,
      height: 900,
      deviceScaleFactor: 1,
      mobile: false
    });

    await client.send('Page.navigate', { url: `http://localhost:${PORT}` });
    await sleep(2000);

    // Scroll directly to plans
    await client.send('Runtime.evaluate', {
      expression: 'document.getElementById("plans").scrollIntoView({ behavior: "instant", block: "center" });'
    });
    await sleep(500);
    const plansShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}/v_react_plans_zoomed.png`, Buffer.from(plansShot.data, 'base64'));

    console.log("Plans screenshot captured successfully!");
    client.close();
  } catch (err) {
    console.error(err);
  } finally {
    try { chrome.kill(); } catch (e) {}
    server.close();
    process.exit(0);
  }
});

