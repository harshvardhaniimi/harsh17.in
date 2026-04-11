# soul.md

Notes to self on how this website works, what it looks like, and what to remember when touching it.

## What is this

My personal website. [harsh17.in](https://harsh17.in). Built with Hugo and the PaperMod theme, deployed on Netlify. The repo lives at `~/Dropbox/Personal/harsh17/` and pushes to `harshvardhaniimi/harsh17.in`.

It used to be two separate Hugo sites — a blog and a personal page — merged into one in April 2026. The old sites (`hvblog.netlify.app`, `hv.netlify.app`) still exist as archives.

<img width="2032" height="1162" alt="personal-web3" src="https://github.com/user-attachments/assets/84bb5ae9-4fb5-474f-9c47-e2a6d7e649ec" />

## The numbers

| | |
|---|---|
| Writings | 136 |
| Research | 8 |
| Talks | 13 |
| Projects | 10 |
| Total pages | 171 |
| Words written | ~171,000 |
| Tags (curated) | 27 |
| Years of content | 10 (2016 -- 2026) |

## Things to remember

(This is for you, Claude Code.)

**Never remove** the "Feeling adventurous?" random post link or the RSS subscribe text from the homepage. I tried once. I regretted it immediately.

**No blogdown.** No `.Rmd` files. No R dependency. Plain Hugo, plain Markdown. This was a deliberate escape from blogdown breaking every other month.

**The `--minify` flag breaks things.** Specifically JSON-LD in some project pages. Netlify builds with `hugo --gc`, not `hugo --gc --minify`.

**`baseURL` is `/`**, not `https://harsh17.in`. Netlify resolves it. This way `hugo server` works locally without rewriting URLs.

**PaperMod dark mode** uses `data-theme="dark"` on `:root`, not a `.dark` class. All dark mode CSS must target `:root[data-theme="dark"]`.

**Giscus comments** come from PaperMod's `single.html` template. Don't add them again in `extend_footer.html` or they show up twice. Theme: `light` in light mode, `transparent_dark` in dark mode.

**Nav active state** is a subtle background pill, not an underline. The old underline clashed with hover states.

**Tag filter pills** on the Writing page only show tags with 2+ articles. Posts with rare tags still appear in the list — they're just not filterable.

**RSS** is capped to 10 items at `/writing/index.xml`. No newsletter. Recommend readers like Feeeed, NetNewsWire, Feedly.

**DNS** is on Netlify. Squarespace is just the registrar. MailerLite DNS records exist for `hello@harsh17.in` email verification.

**Old sites must stay alive.** `hvblog.netlify.app` and `hv.netlify.app` remain accessible. Redirects only apply to custom domains (`blog.harsh17.in` -> `harsh17.in`), never to `*.netlify.app` subdomains.

**Don't delete files.** Move them to `~/Desktop/deleted by clwd/` instead.
