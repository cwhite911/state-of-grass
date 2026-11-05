#!/usr/bin/env python3
"""Assemble the static site in dist/ for GitHub Pages.

Copies index.html, favicon.svg, assets/, theme/, and the reveal.js files that
tools/template.html references under node_modules/, keeping the same relative
paths so the generated index.html works unchanged.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"

FILES = ["index.html", "favicon.svg"]
DIRS = [
    "assets",
    "theme",
    "node_modules/reveal.js/dist",
    "node_modules/reveal.js/plugin/notes",
]

if not (ROOT / "index.html").exists():
    raise SystemExit("index.html missing; run tools/build.py first")

shutil.rmtree(DIST, ignore_errors=True)
DIST.mkdir()
for name in FILES:
    shutil.copy2(ROOT / name, DIST / name)
for name in DIRS:
    shutil.copytree(ROOT / name, DIST / name)
(DIST / ".nojekyll").touch()
print(f"wrote {DIST.relative_to(ROOT)}/")
