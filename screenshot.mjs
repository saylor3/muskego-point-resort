// screenshot.mjs — full-page screenshot via Puppeteer (bundled Chromium).
// Usage:
//   node screenshot.mjs                              -> shoots http://localhost:3000
//   node screenshot.mjs http://localhost:3000        -> same, explicit URL
//   node screenshot.mjs http://localhost:3000 hero   -> saves screenshot-N-hero.png
// Output: ./temporary screenshots/screenshot-N[-label].png  (auto-incremented)

import puppeteer from 'puppeteer';
import { mkdir, readdir } from 'node:fs/promises';
import { join } from 'node:path';

const url = process.argv[2] || 'http://localhost:3000';
const label = (process.argv[3] || '').replace(/[^a-z0-9-_]/gi, '');
const OUT_DIR = 'temporary screenshots';

function nextIndex(files) {
  let max = 0;
  for (const f of files) {
    const m = f.match(/^screenshot-(\d+)/);
    if (m) max = Math.max(max, parseInt(m[1], 10));
  }
  return max + 1;
}

(async () => {
  await mkdir(OUT_DIR, { recursive: true });
  let files = [];
  try {
    files = await readdir(OUT_DIR);
  } catch {}
  const n = nextIndex(files);
  const name = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;
  const outPath = join(OUT_DIR, name);

  const browser = await puppeteer.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
  });
  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 2 });
    await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
    // Scroll to bottom to trigger lazy images, then back to top.
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await new Promise((r) => setTimeout(r, 800));
    await page.evaluate(() => window.scrollTo(0, 0));
    // Let fonts / entrance animations settle.
    await new Promise((r) => setTimeout(r, 1000));
    await page.screenshot({ path: outPath, fullPage: true });
    console.log(`Saved ${outPath}`);
  } finally {
    await browser.close();
  }
})().catch((err) => {
  console.error('Screenshot failed:', err.message);
  process.exit(1);
});
