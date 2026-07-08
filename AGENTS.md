# harsh17.in — agent notes

Hugo + PaperMod, deployed by Netlify from GitHub (`harshvardhaniimi/harsh17.in`).
Local build: `hugo --gc`.
For post scaffolding conventions, use the `hugo-post` skill; this file documents the site machinery added in the July 2026 optimization pass.

## Things that are automatic (do not redo them by hand)

- **KaTeX** loads only on pages whose markdown contains `$$…$$` or `\(…\)`, detected at build time in `layouts/partials/extend_footer.html`.
No `math: true` front matter exists or is needed anywhere.
- **Content images** referenced in markdown are converted to capped-width (1500px) WebP with a 750w srcset variant, width/height attributes, and lazy loading by `layouts/_default/_markup/render-image.html`.
GIF, SVG, and external images pass through untouched.
Per-page opt-out: set `processImages: false` in front matter.
- **Project thumbnails** on /projects/ are generated at 240×180 (plus 2x) WebP by `layouts/projects/list.html` from each bundle's `featured.*`.
- **Confetti-on-click** is skipped for users with `prefers-reduced-motion: reduce`; the rickshaw cursor and confetti are intentional and stay.

## Rules that keep the Netlify build green

- `resources/_gen/` is **committed on purpose** (processed-image cache, ~40MB).
After adding or changing images, run `hugo --gc` locally and commit `resources/_gen` together with the content; otherwise Netlify re-encodes everything (or, worse, hits an undecodable image cold).
- **Image bytes must match the file extension.**
A WebP saved as `.jpg` crashes Hugo's processing with `image: unknown format` — this has happened twice (`2022-11-24-infallible-memory/featured.jpg`, `01-dharamkshetra-gandhari/sidebar.png`, both re-encoded 2026-07-07).
Check suspicious files with `file <img>`.

## Fonts

- Body font is Tiro Devanagari Hindi, self-hosted in `static/fonts/` as Google's own unicode-range subsets (latin ≈20KB, latin-ext, devanagari ≈64KB; regular + italic).
English pages download only the latin subset; Devanagari glyphs pull the devanagari file automatically.
- To update: fetch `https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&display=swap` with a Chrome UA, download the woff2 URLs, replace the files, and keep the `unicode-range` values in `assets/css/extended/custom.css` in sync.
- The latin regular subset is preloaded in `layouts/partials/extend_head.html`.
- `.fonts/TiroDevanagariHindi-Regular.ttf` (repo root, not deployed) exists for OG-image generation.

## OG images

- `generate-og-images.py` renders `og.png` (1200×630) for any bundle missing one, using the Tiro TTF from `.fonts/`.
- PIL cannot shape Devanagari conjuncts.
For Hindi titles, render the same design via headless Chrome instead:
build an HTML page with the OG layout (cream `#faf8f5`, maroon `#7a4522` bar, Tiro @font-face), then
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --force-device-scale-factor=1 --window-size=1200,630 --screenshot=og.png page.html`.

## Search

- `assets/js/fastsearch.js` (project-level, shadows PaperMod's) implements three-tier search: literal word/phrase matches with highlighted snippets, fuzzy Fuse.js results ("Related matches"), then embedding-based "Semantic matches".
- The `index.json` search index intentionally contains full post content — do not trim it; the owner wants exact recall of half-remembered phrases.
- **Semantic tier**: post vectors live in `static/embeddings.json` (Gemini `gemini-embedding-001`, 768-dim, int8+base64); queries are embedded at runtime by the Netlify function `netlify/functions/embed-query.mjs` (route `/api/embed-query`, key from `GEMINI_API_KEY` env var on Netlify).
- **After adding or editing posts, run `python generate-embeddings.py` and commit the updated `static/embeddings.json`** — it is incremental (only changed posts are re-embedded; needs `GOOGLE_API_KEY`/`GEMINI_API_KEY` in the environment).
- Corpus and query embeddings must come from the same model; the client checks this and silently hides the tier on mismatch. To switch providers, re-run the script and update Netlify env (`EMBED_PROVIDER`, key) together.
- Local testing of the semantic tier needs `netlify dev` (functions don't run under plain `hugo server`; the tier degrades silently there).

## Research section

- `/research/` entries read `authors`, `venue`, `pdf`, `doi`, `link` + `linkText` from front matter (`layouts/research/list.html`).
When a new paper is added, fill these from the CV (`static/docs/cv.pdf`) — never invent venue or DOI data.

## Caching

- `netlify.toml` serves `/assets/*` and `/fonts/*` with immutable 1-year caching (both are fingerprinted/versioned), `/img/*` with 1 week.
If a font file must change, rename it.
