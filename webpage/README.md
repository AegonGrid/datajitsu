# data-jujitsu — Pelican scaffold

The same design and content as the original HTML artifact, rebuilt as a
Pelican static site: one Jinja2 theme, Markdown blog posts, no backend.

## Quickstart

```bash
pip install -r requirements.txt

# one-off build -> output/
make html

# build + serve at http://localhost:8000
make serve

# build + rebuild on save + serve (for writing)
make devserver
```

No `make`? Run the Pelican commands directly:

```bash
pelican content -s pelicanconf.py -o output
cd output && python3 -m http.server 8000
```

## Writing a new post

Add a Markdown file to `content/articles/`, e.g. `2026-10-01-my-post.md`:

```
Title: My post title
Date: 2026-10-01
Slug: my-post
Summary: One line shown on the homepage list.
Status: published

Post body in Markdown starts here.
```

Rebuild (or leave `make devserver` running) and it appears under **Writing**
automatically — no template changes needed.

## Editing the static sections

Experience, "Currently", and freelance pricing are hand-written HTML in
`theme/templates/index.html` — edit that file directly. Shared chrome (nav,
fonts, footer) lives in `theme/templates/base.html`. All styling is in
`theme/static/css/style.css`, unchanged from the original design.

## Publishing

Set your real domain in `publishconf.py` (`SITEURL`), then:

```bash
make publish
```

Or
```bash
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push origin gh-pages
```
This builds `output/` with absolute URLs and Atom feeds enabled, ready to
upload anywhere that serves static files (GitHub Pages, Netlify, S3, etc.).

## Layout

```
pelicanconf.py       site settings for local builds
publishconf.py        overrides for the live deploy
content/articles/     one Markdown file per blog post
theme/templates/       base.html, index.html, article.html
theme/static/css/      style.css
```
