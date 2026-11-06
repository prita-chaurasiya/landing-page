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

async function captureAllNew() {
  const port = 9260;
  const userDataDir = `C:\\Users\\Priya\\AppData\\Local\\Temp\\chrome_cdp_new_${Date.now()}`;
  
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

    const targets = await fetchJson(`http://127.0.0.1:${port}/json/list`);
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

    await client.send('Page.navigate', { url: URL });
    await sleep(2000);

    await client.send('Runtime.evaluate', {
      expression: 'document.querySelectorAll("[data-aos]").forEach(el => { el.classList.add("aos-animate"); el.style.opacity = "1"; el.style.transform = "none"; });'
    });

    // 1. Capture Hero
    await client.send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0);' });
    await sleep(400);
    const heroShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}/v_new_hero.png`, Buffer.from(heroShot.data, 'base64'));

    // 2. Capture Grid & Form
    await client.send('Runtime.evaluate', {
      expression: 'document.getElementById("membership").scrollIntoView({ behavior: "instant", block: "start" });'
    });
    await sleep(500);
    const gridShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}/v_new_grid.png`, Buffer.from(gridShot.data, 'base64'));

    // 3. Capture Plans
    await client.send('Runtime.evaluate', {
      expression: 'document.getElementById("plans").scrollIntoView({ behavior: "instant", block: "center" });'
    });
    await sleep(500);
    const plansShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}/v_new_plans.png`, Buffer.from(plansShot.data, 'base64'));

    // 4. Capture Minimal Footer
    await client.send('Runtime.evaluate', {
      expression: 'window.scrollTo(0, document.body.scrollHeight);'
    });
    await sleep(500);
    const footerShot = await client.send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(`${ARTIFACT_DIR}/v_new_footer.png`, Buffer.from(footerShot.data, 'base64'));

    console.log('All new screenshots captured successfully!');
    client.close();
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}

captureAllNew().catch(console.error);

