import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlFile = path.join(__dirname, 'play-and-work.html');
const outFile = path.join(__dirname, 'play-and-work.pdf');

const browser = await puppeteer.launch({
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  headless: true,
});

const page = await browser.newPage();
await page.goto(`file://${htmlFile}`, { waitUntil: 'networkidle0', timeout: 30000 });

// Wait for Google Fonts to load
await new Promise(r => setTimeout(r, 2000));

await page.pdf({
  path: outFile,
  width: '794px',
  height: '1123px',
  printBackground: true,
  pageRanges: '',
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});

await browser.close();
console.log('PDF generado:', outFile);
