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
    '--remote-debugging-port=9270',
    '--headless=new',
    '--window-size=1440,900'
  ]);
  await sleep(1500);
  const targets = await fetchJson('http://127.0.0.1:9270/json/list');
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

  // Extract computed styles from ngowebsite.in
  const styles = await send('Runtime.evaluate', {
    expression: '(() => {\n' +
      'const h1 = document.querySelector("h1");\n' +
      'const btn = document.querySelector(".hero a, .hero button, .btn, button");\n' +
      'const card = document.querySelector(".card, [class*=\'card\'], .item");\n' +
      'const body = document.body;\n' +
      'return {\n' +
      '  fontFamily: window.getComputedStyle(body).fontFamily,\n' +
      '  h1Font: h1 ? window.getComputedStyle(h1).fontFamily : "",\n' +
      '  h1Size: h1 ? window.getComputedStyle(h1).fontSize : "",\n' +
      '  h1Weight: h1 ? window.getComputedStyle(h1).fontWeight : "",\n' +
      '  h1LetterSpacing: h1 ? window.getComputedStyle(h1).letterSpacing : "",\n' +
      '  btnBg: btn ? window.getComputedStyle(btn).backgroundImage || window.getComputedStyle(btn).backgroundColor : "",\n' +
      '  btnRadius: btn ? window.getComputedStyle(btn).borderRadius : "",\n' +
      '  btnShadow: btn ? window.getComputedStyle(btn).boxShadow : "",\n' +
      '  cardRadius: card ? window.getComputedStyle(card).borderRadius : "",\n' +
      '  cardShadow: card ? window.getComputedStyle(card).boxShadow : "",\n' +
      '  cardBorder: card ? window.getComputedStyle(card).border : ""\n' +
      '};\n' +
    '})()',
    returnByValue: true
  });
  console.log('NGOWebsite Styles:', JSON.stringify(styles.result.value, null, 2));

  chrome.kill();
})();

