---
title: "A New Home on the Internet"
subtitle: "Why I merged my two websites into one, and how to keep up"
author: Harshvardhan
date: '2026-04-10'
slug: new-website
tags:
  - personal
  - tools
---

For the last few years, I've maintained two separate websites. My [personal website](https://hv.netlify.app/) — built with Hugo Apero — housed my publications, projects, talks, and an about page. My [blog](https://blog.harsh17.in/) — a separate Hugo site with the Archie theme — held all my writing. The idea was to keep "professional" and "personal" apart. In practice, it meant I was never sure where something belonged. Is a technical tutorial about R a "project" or a "blog post"? Is a conference reflection a "talk" or a piece of writing? The boundaries were artificial, and maintaining two sites meant twice the headaches.

So I merged them.

## What Changed

Everything now lives at [harsh17.in](https://harsh17.in). One site, one theme, one place to find anything I've written or built.

The new site uses [PaperMod](https://github.com/adityatelange/hugo-PaperMod) — a minimal Hugo theme that I've customized with a warm cream palette, serif typography ([Libre Baskerville](https://fonts.google.com/specimen/Libre+Baskerville)), and a layout inspired by academic sites like [Kieran Healy's](https://kieranhealy.org/). The aesthetic is deliberately quiet. No boxes, no cards, no sidebars. Just text, links, and whitespace. I wanted it to feel like opening a well-organized notebook.

Oh, and the cursor is an autorickshaw. Because why not. 🛺

## Where Things Are

The navigation is simple:

- **[About](/about/)** — who I am, what I do, how to reach me
- **[Research](/research/)** — my publications, from the dissertation to conference papers
- **[Writing](/writing/)** — everything I write: essays, tutorials, travel notes, philosophy, technical notes, coffee musings. All of it, in one stream. You can filter by tags at the top of the page — click "philosophy" or "travel" or "data-science" to narrow things down
- **[Talks](/talks/)** — conference presentations, guest lectures, workshops
- **[CV](/docs/cv.pdf)** — PDF of my CV

If you're looking for something specific, there's a [search page](/search/) too.

All the old URLs still work. If you had bookmarked `blog.harsh17.in/meditation/`, it redirects to `harsh17.in/meditation/`. Nothing is lost.

## What I Dropped

I used to run everything through [blogdown](https://bookdown.org/yihui/blogdown/) in RStudio, which meant every post was an R Markdown file that needed R packages, knitting, and a specific Hugo version pinned in `.Rprofile`. It broke constantly — missing packages, stale caches, version conflicts. Every few months I'd sit down to write and spend an hour fixing the build instead.

No more. The new site is plain Markdown. I edit in VS Code (or any text editor), run `hugo server` in the terminal, and that's it. No R dependency, no blogdown, no `.Rmd` files. The old R Markdown sources are archived safely, and the rendered Markdown carries forward all the charts and tables they produced.

I also replaced the embedded [Are.na](https://www.are.na/) iframes with simple links. Those iframes were loading entire pages worth of content on every visit and eating through my Netlify bandwidth. A link works just as well.

## Staying Updated {#subscribe}

If you'd like to follow along, the best way is through **RSS** — an open, simple protocol that lets you subscribe to websites without giving away your email or depending on any platform's algorithm.

Here's the feed link — copy it into your reader of choice:

```
https://harsh17.in/writing/index.xml
```

**New to RSS?** It's like a personal newsfeed that you control. You pick the sources, and new posts show up in your reader automatically. No newsletters to manage, no inbox clutter, no tracking pixels. Here are some good readers to get started:

- **iOS:** [Feeeed](https://feeeed.nateparrott.com/) — beautiful, simple, free
- **Mac:** [NetNewsWire](https://netnewswire.com/) — open source, fast, no account needed
- **Web:** [Feedly](https://feedly.com/) — works everywhere, free tier is generous
- **Email delivery:** [Blogtrottr](https://blogtrottr.com/) — if you prefer getting posts in your inbox, paste the RSS link here and Blogtrottr will email you whenever I publish something new. No account on my end, no subscriber list — they handle it all.

I considered setting up a newsletter but every free service either charges for RSS-to-email automation or requires infrastructure I don't want to maintain. RSS is simpler, more private, and more honest. You subscribe when you want, unsubscribe by removing the feed, and I never see your email address. 

---

The old personal website is still accessible at [harsh17.in/old2](https://harsh17.in/old2) if you're feeling nostalgic, and the even older Google Sites version lives at [harsh17.in/old](https://harsh17.in/old). Three generations of the same impulse: put things on the internet and hope someone finds them interesting.

Here's to the new home. 🏡
