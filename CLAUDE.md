# state-of-grass

reveal.js deck for the State of GRASS 2026 talk (FOSS4G North America, Sacramento).
Planner: Organization GRASS.

## Commands

- `npm start`: build `index.html` and serve on :8000.
- `npm run build`: `tools/build.py` assembles `index.html` from `slides/*.html` and
  `tools/template.html`. Never edit `index.html` by hand.
- `npm run dist`: `tools/dist.py` assembles the Pages site in `dist/`.
- `npm run lint` / `npm run check`: Biome (CSS, JSON, slide HTML; HTML formatter off).
- `pre-commit run --all-files`: what CI runs.

## Conventions

- One slide per file in `slides/`, ordered by numeric prefix; each is one
  `<section id="...">` with a 1920x1080 `div.slide` and optional `aside.notes`.
- Inline styles use single quotes and hex colors, for example
  `font-family:'Fira Mono',monospace;color:#00393f`. Do not paste browser-serialized
  styles (`&quot;`, `rgb()`); Biome's inline CSS parser rejects them.
- `theme/ds/` mirrors the GRASS design system tokens and is excluded from formatting.
- Releases: tag and GitHub Release named `0.1.YYYYMMDD`; publishing the release
  deploys to GitHub Pages. First release: `0.1.20261104`.
