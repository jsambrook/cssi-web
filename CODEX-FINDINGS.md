# CODEX Findings (2026-02-16)

## Scope and Validation

- Reviewed `src/` pages/layouts/components, content, and build/lint scripts.
- Commands run:
  - `npm run lint` (passed)
  - `npm run build` (passed: `prebuild`, `build`, `postbuild`)
  - `npm run lint:shell` (failed: missing `shellcheck`)
  - Internal local link/asset check across `dist/**/*.html` (`href/src` starting with `/`) (no broken local targets found)

## Findings (ordered by severity)

1. Medium: Content pipeline is inconsistent for nested blog posts; SEO checks and OG generation miss files that Astro includes.

- Evidence:
  - Collection loader is recursive: `src/content.config.ts:6` (`pattern: '**/*.md'`).
  - Frontmatter SEO check is non-recursive: `scripts/check-frontmatter-seo.js:73`.
  - OG image generation is non-recursive: `scripts/generate-og-images.js:91`.
- Impact:
  - A post in a subfolder would publish via Astro but skip frontmatter QA and likely miss generated OG assets, causing silent quality regressions.
- Recommendation:
  - Make both scripts recursive (match `**/*.md` behavior) so validation and asset generation cover the same content set as the site build.

2. Medium: Two published insights bypass the blog collection pipeline and are excluded from `Insights` listing + RSS.

- Evidence:
  - Standalone pages: `src/pages/insights/pacp.astro:1`, `src/pages/insights/nursing-conflict.astro:1`.
  - Insights index only pulls collection posts: `src/pages/insights.astro:9`.
  - RSS feed only pulls collection posts: `src/pages/rss.xml.ts:6`.
- Impact:
  - `/insights/pacp` and `/insights/nursing-conflict` are not discoverable in the main archive or RSS feed, which can reduce content visibility and distribution.
- Recommendation:
  - Either migrate these pages into `src/content/blog` (preferred for consistency) or explicitly inject them into both `insights.astro` and `rss.xml.ts`.

3. Low: Shell linting is not runnable in a default local setup and is undocumented in onboarding.

- Evidence:
  - Script hard-fails if `shellcheck` is missing: `scripts/check-shell.sh:4`.
  - README quick-start does not mention this dependency: `README.md:6`.
  - Observed failure: `npm run lint:shell` exited `127` with “shellcheck is not installed.”
- Impact:
  - Contributors/CI may assume lint passes while shell checks are effectively skipped unless the environment is preconfigured.
- Recommendation:
  - Document `shellcheck` in setup docs and/or run shell lint in a pinned CI image where the tool is guaranteed.

## Residual Risks / Gaps

- No automated test suite is configured (`package.json` has no `test` script), so behavior regressions rely on lint/build plus manual review.
