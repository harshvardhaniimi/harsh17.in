---
title: Page to Markdown
subtitle: A browser extension for turning any webpage into clean Markdown
summary: A lightweight browser extension that converts webpages to Markdown, plain
  text, or downloadable .md files.
author: Harshvardhan
date: '2026-03-24'
slug: webpage-to-md
tags:
- browser-extension
- markdown
- tools
- typescript
github: https://github.com/harshvardhaniimi/page-to-markdown
cover:
  image: og.png
  hidden: true
---
I read a lot online. Articles, documentation, research threads, blog posts --- there's always something worth saving. For a while, I'd been copying and pasting text into my notes, losing all the formatting in the process. Or I'd save the whole page as HTML and end up with a bloated file full of ads and navigation bars. What I really wanted was a quick way to grab just the article content, nicely formatted as Markdown.

Additionally, there are times when I want to share an article as context to an LLM prompt. Providing the URL is often not enough, especially if the content is behind a paywall, requires a login, or is blocked for AI chatbots. Being able to copy the main content as Markdown allows me to include it directly in my prompts without worrying about access issues.

So I built a browser extension that does exactly that.

## What It Does

Click the toolbar icon and you get three options:

1. **Copy as Markdown** --- extracts the main content of the page and copies it to your clipboard as Markdown
2. **Copy as Plain Text** --- same extraction, but strips all formatting
3. **Download as .md** --- saves the page content as a Markdown file

The extension uses [Mozilla Readability](https://github.com/mozilla/readability) (the same engine behind Firefox's Reader View) to pull out the article content. This means it automatically strips away navigation, sidebars, ads, and other noise. For pages that don't have a clear "article" structure, it falls back to converting the entire page body.

Once it has the clean HTML, [Turndown](https://github.com/mixmark-io/turndown) converts it to Markdown with GitHub Flavored Markdown support --- so tables, strikethrough, and task lists all come through correctly.


## Building It

The extension is built with [WXT](https://wxt.dev/), a framework for building cross-browser extensions with TypeScript. WXT handles the annoying parts of extension development --- manifest generation, hot reloading in dev mode, and building for multiple browsers from a single codebase.

The core logic is surprisingly simple:

1. Inject a content script into the active tab
2. Clone the page's DOM and run it through Readability
3. Convert the extracted HTML to Markdown with Turndown
4. Copy to clipboard or trigger a download

The whole thing is about 400 lines of TypeScript across four modules.

## Chrome + Safari

The extension builds for both Chrome and Safari. Chrome is straightforward --- load the unpacked build or package it for the Chrome Web Store. Safari requires converting the extension with Apple's tooling and running through Xcode, which is a bit more ceremony but works well.

You can find the source code, build instructions, and Chrome Web Store assets on [GitHub](https://github.com/harshvardhaniimi/webpage-to-md).

This project was orchestrated into existence by [Claude Code](https://claude.ai/code).
