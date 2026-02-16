# CODEX Findings (2026-02-16)

## Scope and Validation

- Reviewed runtime and build/SEO code in `src/` and `scripts/`.
- Commands run:
- `npm run lint` (passed)
- `npm run build` (passed, including `prebuild` and `postbuild`)
- Additional reproducibility check:
- Built twice with no source changes and compared `dist/insights/index.html` checksums; they changed between builds.

## Findings (ordered by severity)

1. Medium: Insights listing is non-deterministic and busts all thumbnail caches on every build.

- Evidence:
- `src/pages/insights.astro:12` defines `const cacheBust = Date.now();`
- `src/pages/insights.astro:28` appends `?v=${cacheBust}` to every thumbnail URL
- Two consecutive builds produced different checksums for `dist/insights/index.html` with no source edits
- Impact:
- Every deploy invalidates browser/CDN caches for all insight thumbnails, increasing bandwidth and reducing cache hit rate.
- Recommendation:
- Remove `Date.now()` query params and use stable asset URLs (or deterministic per-file hashes/mtimes).

2. Medium: Build-critical scripts rely on transitive dependencies that are not declared directly.

- Evidence:
- `scripts/check-frontmatter-seo.js:5` imports `yaml`
- `scripts/check-seo.js:5` imports `parse5`
- `package.json:19`-`package.json:35` does not list `yaml` or `parse5` as direct dependencies
- `npm ls parse5 yaml --depth=0` returns no direct install
- Impact:
- Dependency-tree changes in upstream packages can break `prebuild`/`postbuild` unexpectedly.
- Recommendation:
- Add `yaml` and `parse5` as direct dependencies (or devDependencies) with explicit version ranges.

3. Low: `noindex` legal pages are still included in the generated sitemap.

- Evidence:
- `src/pages/legal/privacy.astro:11` and `src/pages/legal/terms.astro:11` set `noindex={true}`
- `astro.config.mjs:7` enables sitemap generation with no exclusions
- Generated sitemap includes both legal URLs (`dist/sitemap-0.xml:1`)
- Impact:
- Mixed indexing signals (`noindex` plus sitemap inclusion) can waste crawl budget and make indexing behavior less predictable.
- Recommendation:
- Exclude legal/noindex routes from sitemap output.

## Residual Risks / Gaps

- No automated test suite is configured (`package.json:6`-`package.json:18` has no `test` script); regressions are mainly caught during full builds.
