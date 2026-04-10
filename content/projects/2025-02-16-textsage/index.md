---
title: TextSage
subtitle: AI-powered fact-checking and text explanation in your browser
summary: A Chrome extension that lets you explain or fact-check any selected text
  with a right-click.
author: Harshvardhan
date: '2025-02-16'
slug: textsage
tags:
- ai
- browser-extension
- chrome
- fact-checking
- tools
---
We read a lot of things online that make us go "wait, is that actually true?" or "what does that even mean?" Usually the next step is to open a new tab, paste the text into ChatGPT or Perplexity, and ask. TextSage cuts out those steps.

## What It Does

Select any text on a webpage, right-click, and choose one of four options:

- **Explain with ChatGPT** --- opens ChatGPT with a prompt asking it to explain the selected text
- **Explain with Claude** --- same thing, but with Claude
- **Fact Check with Perplexity** --- sends the text to Perplexity with a fact-checking prompt
- **Fact Check with Grok** --- sends it to Grok instead

That's it. No setup, no API keys, no accounts to create (beyond whatever AI service you already use). The extension just builds a smart URL with your selected text and opens it in a new tab.

## Privacy First

TextSage collects zero data. No analytics, no tracking, no telemetry. The selected text goes directly from your browser to the AI platform you chose --- it never passes through any intermediary server. The extension is open source, so you can verify this yourself.

## How It's Built

The extension is remarkably simple --- it's built on Chrome's Manifest V3 and uses the Context Menu API. The core logic is about 50 lines of JavaScript:

1. Register context menu items when the extension loads
2. When clicked, grab the selected text
3. Encode it into a URL with a pre-crafted prompt
4. Open a new tab to the chosen AI platform

There's no background processing, no content scripts injected into pages, no storage. It's essentially a smart URL generator that saves you the copy-paste-prompt cycle.

## Install

TextSage is available on the [Chrome Web Store](https://chromewebstore.google.com/detail/textsage-ai-factchecking/abdikojdjeedacfmhofkpikjdomaceao) --- install it and it's ready to use immediately. You can also check out the [website](https://textsage.netlify.app/) for more details.

The [source code](https://github.com/harshvardhaniimi/textsage-website) is on GitHub.
