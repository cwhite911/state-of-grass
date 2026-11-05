#!/usr/bin/env python3
"""Assemble index.html from tools/template.html and slides/*.html.

Slides are included in filename order; use the numeric prefix (010, 020, ...) to
order them and pick an unused number to insert a slide. Each file holds one
<section id="..."> element with a .slide wrapper and an optional aside.notes.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
files = sorted((ROOT / "slides").glob("*.html"))
parts, ids = [], set()
for f in files:
    text = f.read_text().strip()
    m = re.match(r'<section id="([^"]+)"', text)
    if not m:
        sys.exit(f"{f.name}: must start with <section id=\"...\">")
    if m.group(1) in ids:
        sys.exit(f"{f.name}: duplicate section id {m.group(1)}")
    ids.add(m.group(1))
    parts.append(text)
tpl = (ROOT / "tools" / "template.html").read_text()
(ROOT / "index.html").write_text(tpl.replace("<!--SLIDES-->", "\n\n".join(parts)))
print(f"wrote index.html with {len(parts)} slides")
