# AGENTS.md

## Cursor Cloud specific instructions

### What this is
This repository is a single self-contained static web app: `wealthcalc-advanced.html` (WealthCalc Advanced — a suite of financial-planning calculators). All HTML, CSS, and JavaScript are inline in that one file. There is no package manager, backend, build step, or automated test/lint tooling.

### Running (dev)
Serve the file with any static server from the repo root and open it in a browser:

```
python3 -m http.server 8000
# then open http://localhost:8000/wealthcalc-advanced.html
```

`python3` and `node` are preinstalled, so no dependency installation is required (the update script is a no-op).

### Non-obvious notes
- The page loads Chart.js from a CDN (`cdnjs.cloudflare.com`) at runtime. Charts require outbound internet access; without it the visualizations will not render (the rest of the calculators still work).
- Opening the `.html` file directly via `file://` also works, but serving over HTTP is preferred for a realistic dev setup.
- There is no lint/test/build; "testing" means opening the page and exercising a calculator (change inputs, click Calculate, confirm KPI numbers and charts update).
