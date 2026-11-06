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

  close() {
    if (this.ws) this.ws.close();
  }
}

async function captureAudits() {
  const port = 9232;
  const userDataDir = `C:\\Users\\Priya\\AppData\\Local\\Temp\\chrome_cdp_${Date.now()}`;
  
  const chrome = spawn(CHROME_PATH, [
    `--remote-debugging-port=${port}`,
    `--user-data-dir=${userDataDir}`,
    '--headless=new',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    '--hide-scrollbars',
    '--window-size=1440,900'
  ], { stdio: 'ignore' });

  try {
    let version = null;
    for (let i = 0; i < 20; i++) {
      await sleep(300);
      try {
        version = await fetchJson(`http://127.0.0.1:${port}/json/version`);
        if (version && version.webSocketDebuggerUrl) break;
      } catch (e) {}
    }

    if (!version) throw new Error("Chrome debug endpoint unreachable");

    const targets = await fetchJson(`http://127.0.0.1:${port}/json/list`);
    const target = targets.find(t => t.type === 'page') || targets[0];
    const client = new CDPClient(target.webSocketDebuggerUrl);
    await client.connect();

    await client.send('Page.enable');
    await client.send('DOM.enable');
    await client.send('CSS.enable');

    // 1. DESKTOP VIEWPORT
    await client.send('Emulation.setDeviceMetricsOverride', {
      width: 1440,
      height: 900,
      deviceScaleFactor: 1,
      mobile: false
    });

    await client.send('Page.navigate', { url: URL });
    await sleep(2500);

    // Force AOS elements visible
    await client.send('Runtime.evaluate', {
      expression: `
        document.querySelectorAll('[data-aos]').forEach(el => {
          el.classList.add('aos-animate');
          el.style.opacity = '1';
          el.style.transform = 'none';
        });
      `
    });
    await sleep(400);

    // 1A. Desktop Hero
    const heroShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}\\v_authentic_desktop_hero.png`, Buffer.from(heroShot.data, 'base64'));

    // 1B. Desktop Grid Top
    await client.send('Runtime.evaluate', {
      expression: `
        const m = document.getElementById('membership');
        if (m) m.scrollIntoView({ behavior: 'instant', block: 'start' });
        window.scrollBy(0, -60);
      `
    });
    await sleep(400);
    const gridShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}\\v_authentic_desktop_grid.png`, Buffer.from(gridShot.data, 'base64'));

    // 2. MOBILE VIEWPORT (390 x 844 iPhone)
    await client.send('Emulation.setDeviceMetricsOverride', {
      width: 390,
      height: 844,
      deviceScaleFactor: 2,
      mobile: true
    });
    await client.send('Page.navigate', { url: URL });
    await sleep(2500);

    await client.send('Runtime.evaluate', {
      expression: `
        document.querySelectorAll('[data-aos]').forEach(el => {
          el.classList.add('aos-animate');
          el.style.opacity = '1';
          el.style.transform = 'none';
        });
        window.scrollTo(0, 0);
      `
    });
    await sleep(400);

    const mobileHero = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}\\v_authentic_mobile.png`, Buffer.from(mobileHero.data, 'base64'));

    const overflowCheck = await client.send('Runtime.evaluate', {
      expression: `
        ({
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: document.documentElement.clientWidth,
          hasOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
        })
      `,
      returnByValue: true
    });
    console.log("Mobile Overflow:", JSON.stringify(overflowCheck.result.value));
    console.log("Captured all authentic audit screenshots successfully!");
    client.close();
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}

captureAudits().catch(console.error);
