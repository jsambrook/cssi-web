# Repository Guidelines

## Project Structure & Module Organization
The repo serves built static pages from the root. Key directories:
- `src/blog/scripts` blog processors driving incremental rebuilds.
- `src/bin` automation for draft generation.
- `src/blog/content` Markdown sources by `YYYY/MM/slug/index.md`; `src/blog/drafts` holds JSON intermediates.
- `src/includes` reusable M4 fragments.
- `src/assets` reference art; `assets/` and `css/` hold published assets.
- `blog/` and root `*.html` are generated outputs tracked in Git.

## Build, Test, and Development Commands
- `python3 src/blog/scripts/process_blog.py` Incremental blog/site rebuild; prefer this for daily work.
- `python3 src/blog/scripts/process_blog.py --force-posts` or `--force-index` for template/index refreshes; reserve `--force` for full rebuilds (~18 min).
- `python3 check_links.py` Verifies site links before committing.
- `make blog-today DESCRIPTION="Prompt"` drafts JSON and HTML for the daily post.
- `make` full site build (pages, blog, sitemap, validation, content export).
- `make clean` clears generated artifacts before a fresh build; `make sitemap` updates `sitemap.xml` when needed.

## Coding Style & Naming Conventions
Use 4-space indentation for HTML, CSS, and Python. HTML filenames stay `kebab-case.html`; blog slugs remain lowercase. Prefer double-quoted attributes and wrap long tags onto multiple lines. Python follows PEP 8 with `snake_case` helpers and docstrings for complex routines. Organize CSS with section comments and centralize custom properties in `:root`. Group new macros at the top of `src/includes` fragments and end files with a newline to keep M4 happy.

## Testing Guidelines
Run `python3 src/blog/scripts/process_blog.py` followed by `python3 check_links.py` before staging. Use `make` when you need validation, sitemap, and content export together. After generators run, open the rendered page (`open blog/YYYY/MM/slug/index.html`) and confirm `blog/index.html` lists the entry. For sitemap updates, rerun `python src/scripts/generate_sitemap.py --site-url="https://common-sense.com" --debug`.

## Commit & Pull Request Guidelines
Always `git add .` after blog processing so updated HTML, JSON, cache, and index files land in the commit. Write imperative commit messages; scoped prefixes help (`Blog: Add 2025-04-22 ai-summaries`). Stage both generated HTML and source markdown/JSON for blog changes. Keep commits focused. PR descriptions should summarize intent, list validation commands, and attach before/after screenshots for layout updates. Link related issues or Trello cards. Keep secrets in env vars (`OPENAI_API_KEY`) and out of source control.

## Security & Configuration Tips
Store API keys in your shell profile; avoid hard-coded credentials. Ensure helper repos referenced in the `Makefile` (`~/git/cssi-ai/...`) exist before running generators. If you change those paths or add dependencies, update the `Makefile` and note it in your PR.
