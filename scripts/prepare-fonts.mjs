// Retrieve Dinamo's unmodified webfont at build time, keeping licensed binaries
// out of the public source repository. The site owner holds Areal's free license.
import { createHash } from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { mkdirSync, readFileSync, renameSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const fonts = [
  // Verified Dinamo UI subsets: name-table version 1.009, 2026-10-10.
  ['core', 'ABCAreal-v1.009.woff2', '2abd9f147f19a6f0d56058c168bc1ff052a9ad268514e99c9af0dae84497f70e'],
  ['ext', 'ABCAreal-ext-v1.009.woff2', 'd5708835300aeb293f191325b43e1dd2d9df718a9540fe46cc8ba5e793d7e38d'],
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
