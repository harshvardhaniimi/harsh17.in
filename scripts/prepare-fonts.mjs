// Use verified local copies, or recover them from the site's own versioned assets.
// Keep licensed binaries out of the public source repository. Dinamo is a fallback.
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
  const sources = [
    `https://harsh17.in/fonts/${filename}`,
    `https://cdn.abcdinamo.com/webfonts/${subset}/ABCArealSuperfamilyVariable.woff2`,
  ];
  let recovered = false;
  for (const source of sources) {
    try {
      execFileSync('curl', [
        '--fail', '--silent', '--show-error', '--location',
        '--retry', '1', '--connect-timeout', '10', '--max-time', '45',
        '--referer', 'https://abcdinamo.com/',
        '--user-agent', 'Mozilla/5.0', source,
        '--output', temporary,
      ], { stdio: 'inherit' });
      if (digest(temporary) !== expected) {
        throw new Error('Downloaded font does not match the pinned SHA-256.');
      }
      renameSync(temporary, target);
      recovered = true;
      break;
    } catch (error) {
      console.warn(`Could not recover ${filename} from ${source}: ${error.message}`);
    }
  }
  if (!recovered) {
    throw new Error(`Unable to recover ${filename}. Restore the verified file from the owner's private font backup into static/fonts/.`);
  }
}
console.log('Areal webfont verified.');
