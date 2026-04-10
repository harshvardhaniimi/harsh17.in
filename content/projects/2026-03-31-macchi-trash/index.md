---
title: Macchi Trash
subtitle: Animated flies for your macOS Trash icon
summary: A tiny macOS menu-bar app that shows animated flies buzzing around your Trash
  when it has items.
author: Harshvardhan
date: '2026-03-31'
slug: macchi-trash
tags:
- fun
- macos
- swift
- tools
github: https://github.com/harshvardhaniimi/macchi-trash
website: https://harshvardhaniimi.github.io/macchi-trash/
---
Macchi (मक्खी) is Hindi for fly --- the pesky kind that won't leave your food alone. If you've ever left trash out for too long in an Indian summer, you know the flies will find it before you do.

That's the entire premise of this app: if your Mac's Trash has items in it, shouldn't it attract flies?

## What It Does

Macchi Trash watches your `~/.Trash` directory. When there are items in it and you hover your cursor over the Trash icon in your Dock, small animated flies appear and buzz around the icon. Move your cursor away and they disappear. Empty the trash and they're gone for good --- until you throw something away again.

It's a completely useless app and I love it.

## How It Works

The technical challenge was more interesting than you might expect. macOS doesn't have a straightforward API for "tell me where the Trash icon is on screen." Instead, Macchi Trash uses the Accessibility APIs to find the Dock process, locate the Trash icon within it, and get its screen coordinates. Then it monitors cursor position and overlays transparent windows with animated fly views when the conditions are right.

The app:

1. Watches `~/.Trash` for changes using file system events
2. Uses Accessibility APIs to find the Trash icon's position in the Dock
3. Tracks cursor proximity to the icon
4. When both conditions are met (trash has items + cursor is near), spawns SwiftUI fly animations at the icon's coordinates

Since Dock icon positions can shift (different screen sizes, Dock positions, icon arrangements), there's a calibration tool built in. Run it once and the fly positioning stays accurate.

## Install

Download [MacchiTrash.zip](https://github.com/harshvardhaniimi/macchi-trash/releases/latest/download/MacchiTrash.zip), extract, move to Applications, and right-click → Open the first time. Grant Accessibility permission when prompted.

Or build from source:

```bash
git clone https://github.com/harshvardhaniimi/macchi-trash.git
cd macchi-trash
./build_app.sh
open MacchiTrash.app
```

Requires macOS 13+ and Accessibility permission.

Not every project needs a reason. Sometimes you just want flies on your trash.
