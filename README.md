# Bifrost — Daniel Whicker

Personal site, hosted on GitHub Pages.

## Pages
- `index.html` — homepage (about, links, cruise history teaser)
- `history.html` — cruise history, rendered client-side from `cruise_history_public.json`
- `resume.md` — resume/CV, written in Markdown and rendered by Jekyll through `_layouts/resume.html`

## Deployment Notes (GitHub Pages)

The site is built by Jekyll (GitHub Pages' built-in Jekyll build), so no custom CI/build step is needed.

1. Push to the `main` branch (or whichever branch/folder you configure).
2. In the repo's **Settings → Pages**, set the source to that branch and the root (`/`) folder.
3. GitHub Pages runs Jekyll automatically (no `.nojekyll` file is present). `_config.yml` sets `markdown: kramdown` and excludes dev-only files (`process_data.py`, `README.md`, `cruise_history.json`) from the built site.
4. `index.html` and `history.html` have no front matter, so Jekyll copies them through unchanged; only `resume.md` is actually processed as Markdown.
5. If using a custom domain, add a `CNAME` file at the project root with the domain name and configure DNS accordingly.

Everything the site needs (`index.html`, `history.html`, `resume.md`, `_config.yml`, `_layouts/`, `styles.css`, `robots.txt`, `cruise_history_public.json`, `bifrost-berkano-logo.svg`, `assets/`) already lives at the project root, so nothing needs to be copied or reorganized before deploying. Just don't commit `cruise_history.json` (already git-ignored).

### Data
- `cruise_history.json` is the full private source record and is git-ignored — never deploy it.
- `cruise_history_public.json` is a sanitized subset used only by `history.html`'s client-side fetch. It is not linked from any page and is disallowed in `robots.txt` to limit exposure, but keep in mind anything fetched client-side on a static site is technically visible to anyone who inspects network requests.
- `process_data.py` is a local dev helper for regenerating summaries from `cruise_history.json`; it is not part of the deployed site.

### Customization
- Shared header, footer, buttons, and color variables live in `styles.css`. Update the CSS variables there to re-theme the whole site.
- Update `<title>`/meta tags per page for SEO.

## Local Development
- `index.html` / `history.html`: open directly, or run a local static server (e.g. `python3 -m http.server`) so the `fetch()` calls in `history.html` work correctly.
- `resume.md`: requires an actual Jekyll build to render (it's Markdown + Liquid front matter, not plain HTML). Install Jekyll (`gem install jekyll`) and run `jekyll serve` from the project root, then visit `/resume.html`.
