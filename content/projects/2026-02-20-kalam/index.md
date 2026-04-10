---
title: Kalam
subtitle: Local speech-to-text for macOS, powered by Whisper
summary: A native macOS menu-bar app for speech-to-text transcription — completely
  local, private, and free.
author: Harshvardhan
date: '2026-02-20'
slug: kalam
tags:
- macos
- speech-to-text
- swift
- tools
- whisper
---
## THIS IS A WORK-IN-PROGRESS APP. KINDLY EXCUSE THE ROUGH EDGES. FEEL FREE TO TRY IT OUT AND OPEN ISSUES OR CONTRIBUTIONS ON GITHUB.

Kalam (कलम) means "pen" in Hindi and Urdu, but it also carries the sense of speech and words — the things you write with a pen. It felt like the right name for an app that turns your voice into text.

Website: <https://harshvardhaniimi.github.io/kalam/>

## The Problem

macOS has built-in dictation, but it sends your audio to Apple's servers. There are third-party transcription services too, but they all want a subscription and your data. I wanted something that runs entirely on my Mac — no cloud, no subscriptions, no audio leaving my device.

OpenAI's [Whisper](https://github.com/openai/whisper) model is one of the best open-source speech recognition systems available, and thanks to [WhisperKit](https://github.com/argmaxinc/WhisperKit) by Argmax, it runs natively on Apple Silicon using CoreML and the Neural Engine. That's the foundation Kalam is built on.

## How It Works

Kalam sits in your menu bar as a small waveform icon. The fastest way to use it:

1. Press **Cmd+Shift+Space** from anywhere in macOS
2. Speak
3. Press **Cmd+Shift+Space** again
4. The transcribed text appears at your cursor and is copied to your clipboard

That's it. Writing an email? Click in the body, speak, and the text appears. Taking notes in Obsidian? Same thing. The global hotkey works across all applications.

You can also open the menu bar popover for a more visual interface with a waveform display, or use the full window mode for drag-and-drop file transcription.

## Models

Kalam supports five Whisper model sizes, from Tiny (75 MB) to Large (2.9 GB). The Base model is the default — it downloads automatically on first launch (142 MB) and can transcribe a minute of audio in about 6 seconds on Apple Silicon. If you need better accuracy, you can switch to a larger model in settings. All models support 50+ languages.

## Privacy

This was the whole point of building Kalam:

- All processing happens locally on your Mac
- No internet connection required (except for the initial model download)
- No telemetry, no analytics, no cloud APIs
- Audio never leaves your device
- Transcription history is stored locally

Models are downloaded once from Hugging Face and cached in `~/Library/Application Support/Kalam/models/`.

## Install

The quickest way:

```bash
curl -sL https://raw.githubusercontent.com/harshvardhaniimi/kalam/main/install.sh | bash
```

Or clone the [repo](https://github.com/harshvardhaniimi/kalam) and run `./build-app.sh` to build from source. Requires macOS 14+ (Sonoma).
