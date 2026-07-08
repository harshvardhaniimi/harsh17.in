#!/usr/bin/env python3
"""Generate semantic-search embeddings for all posts -> static/embeddings.json.

Incremental: re-embeds only pages whose text (or the model config) changed.
Provider: Gemini by default; set EMBED_PROVIDER=openai to switch. The Netlify
function that embeds queries (netlify/functions/embed-query.mjs) must use the
SAME provider — set EMBED_PROVIDER there too. Vectors are L2-normalized then
int8-quantized (per-vector scale) and base64-encoded to keep the JSON small.

Keys: GOOGLE_API_KEY (or GEMINI_API_KEY) / OPENAI_API_KEY, from the environment.
"""

import base64
import datetime
import hashlib
import json
import math
import os
import re
import struct
import sys
import time
import urllib.request

SITE = os.path.expanduser("~/Dropbox/Personal/harsh17")
CONTENT = os.path.join(SITE, "content")
OUT = os.path.join(SITE, "static", "embeddings.json")
SECTIONS = ["writing", "research", "talks", "projects"]

PROVIDER = os.environ.get("EMBED_PROVIDER", "gemini").lower()
DIMS = 768
MODELS = {"gemini": "gemini-embedding-001", "openai": "text-embedding-3-small"}
MODEL = MODELS[PROVIDER]
MAX_CHARS = 18000  # ~4.5k tokens; enough for every post that matters


def api_key():
    if PROVIDER == "gemini":
        key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    else:
        key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit(f"No API key in environment for provider '{PROVIDER}'.")
    return key


def post_json(url, payload, headers):
    req = urllib.request.Request(
        url, json.dumps(payload).encode(), {"Content-Type": "application/json", **headers}
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 4:
                time.sleep(2**attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def embed(text, key, task="RETRIEVAL_DOCUMENT"):
    if PROVIDER == "gemini":
        data = post_json(
            f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:embedContent",
            {
                "content": {"parts": [{"text": text}]},
                "taskType": task,
                "outputDimensionality": DIMS,
            },
            {"x-goog-api-key": key},
        )
        vec = data["embedding"]["values"]
    else:
        data = post_json(
            "https://api.openai.com/v1/embeddings",
            {"model": MODEL, "input": text, "dimensions": DIMS},
            {"Authorization": f"Bearer {key}"},
        )
        vec = data["data"][0]["embedding"]
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def quantize(vec):
    maxabs = max(abs(v) for v in vec) or 1.0
    scale = maxabs / 127.0
    i8 = bytes((round(v / scale)) & 0xFF for v in vec)
    return round(scale, 8), base64.b64encode(i8).decode()


def parse_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        import yaml

        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, text[m.end():]


def clean(body, is_html):
    body = re.sub(r"```.*?```", " ", body, flags=re.DOTALL)
    if is_html:
        body = re.sub(r"<script.*?</script>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<style.*?</style>", " ", body, flags=re.DOTALL | re.IGNORECASE)
        body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", body)  # images
    body = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", body)  # links -> text
    body = re.sub(r"[`*_#>|]", " ", body)
    return re.sub(r"\s+", " ", body).strip()


def collect_pages():
    today = datetime.date.today().isoformat()
    pages = []
    for section in SECTIONS:
        spath = os.path.join(CONTENT, section)
        if not os.path.isdir(spath):
            continue
        for d in sorted(os.listdir(spath)):
            dirpath = os.path.join(spath, d)
            if not os.path.isdir(dirpath) or d.startswith("_"):
                continue
            fpath, is_html = None, False
            for fname in ("index.md", "index.html"):
                p = os.path.join(dirpath, fname)
                if os.path.exists(p):
                    fpath, is_html = p, fname.endswith("html")
                    break
            if not fpath:
                continue
            raw = open(fpath, encoding="utf-8", errors="replace").read()
            fm, body = parse_frontmatter(raw)
            if fm.get("draft") is True:
                continue
            date = str(fm.get("date", ""))[:10]
            if date and date > today:
                continue  # future-dated: not on the live site
            title = str(fm.get("title", d))
            slug = fm.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", d)
            text = f"{title}\n{fm.get('summary', '')}\n{clean(body, is_html)}"[:MAX_CHARS]
            pages.append({"p": f"/{slug}/", "t": title, "text": text})
    return pages


def main():
    key = api_key()
    old = {}
    meta_changed = True
    if os.path.exists(OUT):
        prev = json.load(open(OUT))
        meta_changed = prev.get("model") != MODEL or prev.get("dims") != DIMS
        if not meta_changed:
            old = {it["p"]: it for it in prev.get("items", [])}

    items, added, kept = [], 0, 0
    pages = collect_pages()
    for page in pages:
        h = hashlib.sha256(f"{MODEL}|{DIMS}|{page['text']}".encode()).hexdigest()[:12]
        prev_it = old.get(page["p"])
        if prev_it and prev_it.get("h") == h:
            items.append(prev_it)
            kept += 1
            continue
        vec = embed(page["text"], key)
        s, v = quantize(vec)
        items.append({"p": page["p"], "t": page["t"], "h": h, "s": s, "v": v})
        added += 1
        print(f"embedded {page['p']}")
        time.sleep(0.35)

    out = {"provider": PROVIDER, "model": MODEL, "dims": DIMS, "items": items}
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    size = os.path.getsize(OUT) // 1024
    print(f"\n{added} embedded, {kept} reused, {len(items)} total -> {OUT} ({size}KB)")


if __name__ == "__main__":
    main()
