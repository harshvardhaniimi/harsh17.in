// Retrieve Dinamo's unmodified webfont at build time, keeping licensed binaries
// out of the public source repository. The site owner holds Areal's free license.
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync, readFileSync, renameSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const fonts = [
  ['core', 'ABCAreal-v1.524.woff2', '9d0cb0fb0ceb17b84275eedbb0ec5e81e4af485609ec8512ed24efeb051683db'],
  ['ext', 'ABCAreal-ext-v1.524.woff2', '345d97af478c494c2b4b68243b5802af49b923a9a7f87ca50887412acf763e7d'],
];
const digest = (path) => createHash('sha256').update(readFileSync(path)).digest('hex');

for (const [subset, filename, expected] of fonts) {
  const target = fileURLToPath(new URL(`../static/fonts/${filename}`, import.meta.url));
  if (existsSync(target) && digest(target) === expected) continue;
  mkdirSync(fileURLToPath(new URL('../static/fonts/', import.meta.url)), { recursive: true });
  const temporary = `${target}.download`;
  execFileSync('curl', [
    '--fail', '--silent', '--show-error', '--location',
    '--retry', '2', '--max-time', '45',
    '--referer', 'https://abcdinamo.com/',
    '--user-agent', 'Mozilla/5.0',
    `https://cdn.abcdinamo.com/webfonts/${subset}/ABCArealSuperfamilyVariable.woff2`,
    '--output', temporary,
  ], { stdio: 'inherit' });
  if (digest(temporary) !== expected) {
    throw new Error('Areal webfont changed. Verify the vendor file and version before updating the pinned hash.');
  }
  renameSync(temporary, target);
}
console.log('Areal webfont verified.');
