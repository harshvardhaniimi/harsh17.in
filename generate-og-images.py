#!/usr/bin/env python3
"""Generate Open Graph images for all posts: title + author on cream background."""

import os
import re
import yaml
import textwrap
from PIL import Image, ImageDraw, ImageFont

CONTENT = os.path.expanduser("~/Dropbox/Personal/harsh17/content")
BG_COLOR = (250, 248, 245)  # matches --theme: #faf8f5
TEXT_COLOR = (45, 45, 45)    # matches --primary: #2d2d2d
ACCENT_COLOR = (122, 69, 34) # matches --link-color: #7a4522
WIDTH, HEIGHT = 1200, 630

# Site font first (matches the website's Tiro Devanagari Hindi), Georgia fallback.
# NOTE: PIL has no complex-script shaping — for Devanagari titles, render the
# OG image in a browser instead (see AGENTS.md).
FONT_PATHS = [
    os.path.expanduser("~/Dropbox/Personal/harsh17/.fonts/TiroDevanagariHindi-Regular.ttf"),
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/System/Library/Fonts/Georgia.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
]

def get_font(size):
    for path in FONT_PATHS:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            return {}
    return {}

def generate_og(title, output_path):
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Draw a subtle accent line at top
    draw.rectangle([0, 0, WIDTH, 6], fill=ACCENT_COLOR)

    # Title
    title_font = get_font(52)
    wrapped = textwrap.fill(title, width=32)
    lines = wrapped.split('\n')[:4]  # max 4 lines

    y = 160
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        tw = bbox[2] - bbox[0]
        x = (WIDTH - tw) // 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=title_font)
        y += 70

    # Author
    author_font = get_font(28)
    author = "Harshvardhan"
    bbox = draw.textbbox((0, 0), author, font=author_font)
    aw = bbox[2] - bbox[0]
    draw.text(((WIDTH - aw) // 2, HEIGHT - 120), author, fill=ACCENT_COLOR, font=author_font)

    # Subtle line above author
    line_y = HEIGHT - 150
    draw.line([(WIDTH // 2 - 60, line_y), (WIDTH // 2 + 60, line_y)], fill=ACCENT_COLOR, width=1)

    img.save(output_path, 'PNG', optimize=True)

def process_section(section):
    section_path = os.path.join(CONTENT, section)
    if not os.path.isdir(section_path):
        return 0
    count = 0
    for d in os.listdir(section_path):
        dirpath = os.path.join(section_path, d)
        if not os.path.isdir(dirpath) or d.startswith('_'):
            continue

        og_path = os.path.join(dirpath, "og.png")
        if os.path.exists(og_path):
            continue  # already generated

        # Find content file
        fm = {}
        for fname in ["index.md", "index.html"]:
            fpath = os.path.join(dirpath, fname)
            if os.path.exists(fpath):
                fm = parse_frontmatter(fpath)
                break

        title = fm.get("title", d)
        if not title:
            continue

        generate_og(title, og_path)
        count += 1

    return count

def main():
    total = 0
    for section in ["writing", "research", "talks", "projects"]:
        n = process_section(section)
        total += n
        print(f"{section}: {n} images generated")
    print(f"\nTotal: {total} OG images generated")

if __name__ == "__main__":
    main()
