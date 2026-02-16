# CODEX Findings (2026-02-16)

## Scope and Validation

- Repo reviewed as an Astro 5 static site with content-driven SEO checks.
- Commands run:
- `npm run lint` passed.
- `npm run build` passed (including `prebuild` and `postbuild` SEO checks).
- `npm run format:check` failed (94 files not Prettier-formatted).

## Findings (ordered by severity)

1. High: Homepage intake form ships unconfigured and produces a dead-end submit state.

- Evidence:
- `src/data/intakeForm.ts:126` sets `googleForms.actionUrl` to an empty string.
- `src/pages/index.astro:38` always mounts the intake form on the homepage.
- `src/components/IntakeForm.astro:271`-`src/components/IntakeForm.astro:280` shows a warning state instead of submitting when `actionUrl` is missing.
- Impact:
- Primary conversion path can fail for all users until environment-specific form wiring is applied.
- Recommendation:
- Gate rendering until `actionUrl` is configured, or provide a fully working fallback submission target.

2. Medium: Machine-trimmed metadata (ellipsis endings) is still present in published articles and compiled HTML.

- Evidence:
- Source frontmatter examples:
- `src/content/blog/ai-voice-agents-small-business.md:4`
- `src/content/blog/post-acute-care-plan-concept.md:4`
- `src/content/blog/three-way-email-paradox.md:7`
- `src/content/blog/why-is-hc-so-stuck.md:5`
- Built output examples:
- `dist/insights/post-acute-care-plan-concept/index.html:1`
- `dist/insights/why-is-hc-so-stuck/index.html:1`
- Impact:
- Lower SERP and social snippet quality; metadata appears unfinished or truncated.
- Recommendation:
- Manually rewrite affected `metaTitle`/`metaDescription` values and add a guardrail check (e.g., fail on trailing `...` patterns in non-draft posts).

3. Medium: Frontmatter SEO validation uses regex line parsing and can mis-handle valid YAML.

- Evidence:
- `scripts/check-frontmatter-seo.js:13`-`scripts/check-frontmatter-seo.js:35` parses frontmatter via regex line matching only.
- Impact:
- False positives/negatives become likely if multiline strings or richer YAML constructs are introduced.
- Recommendation:
- Replace parser logic with a YAML-aware parser (`gray-matter` or `js-yaml`) and validate typed fields from parsed frontmatter.

4. Medium: Compiled HTML SEO validation is regex-fragile and tightly coupled to current HTML serialization.

- Evidence:
- `scripts/check-seo.js:73`-`scripts/check-seo.js:94` requires exact regex matches for many tags.
- `scripts/check-seo.js:102`-`scripts/check-seo.js:133` extracts title/description via regex for policy checks.
- Impact:
- Non-semantic output changes from Astro/minification can produce noisy failures or hide edge cases.
- Recommendation:
- Parse HTML with an HTML parser (e.g., `cheerio`) and assert by DOM semantics rather than string shape.

5. Low: Formatting policy exists but is currently non-compliant across most of the repo.

- Evidence:
- `npm run format:check` fails with 94 warnings, including source, docs, and scripts.
- Impact:
- Higher diff noise and lower consistency for review/maintenance.
- Recommendation:
- Run `npm run format` once and enforce `format:check` in CI to keep drift from returning.

6. Low: Deploy script is hardcoded to a single host layout and SSH key path.

- Evidence:
- `deploy.sh:12` hardcodes `REPO_DIR="/git/cssi-web"`.
- `deploy.sh:21` hardcodes an absolute SSH key path.
- Impact:
- Reduced portability and higher setup friction across environments.
- Recommendation:
- Accept env var overrides with defaults, and document required deploy environment variables.

7. Low: No automated test harness beyond lint/build checks.

- Evidence:
- `package.json:6`-`package.json:18` has no `test` script.
- Impact:
- Regressions in scripts/content contracts are caught only indirectly during builds.
- Recommendation:
- Add a minimal test suite for SEO/frontmatter validators and critical data transforms.
