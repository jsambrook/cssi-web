# CODEX Findings (2026-02-16)

## Status
- Repository type: Astro 5 static site with Tailwind.
- Validation run: `npm run lint` passed, `npm run build` passed.
- Tracking issue created for intake form fix: https://github.com/jsambrook/cssi-web/issues/36

## Findings (ordered by severity)
1. High: Homepage intake form can reach a dead-end submit state.
- `src/pages/index.astro:24` always renders the form.
- `src/data/intakeForm.ts:126` sets `googleForms.actionUrl` to an empty string.
- `src/components/IntakeForm.astro:271` shows an error message instead of submitting when URL is unset.
- Impact: lead capture failure and confusing UX.

2. Medium: Build pipeline runs OG generation twice.
- `package.json:8` defines `prebuild`.
- `package.json:9` invokes `npm run prebuild` again inside `build`.
- Impact: unnecessary duplicate work on every build/deploy.

3. Medium: Insights thumbnails are cache-busted on every deploy.
- `src/pages/insights.astro:11` uses `Date.now()` for cache busting.
- `src/pages/insights.astro:27` appends that value to each image URL.
- Impact: avoidable image redownloads and reduced cache efficiency.

4. Low: Deployment script is environment-specific and brittle for template reuse.
- `deploy.sh:12` hardcodes `REPO_DIR=\"/git/cssi-web\"`.
- `deploy.sh:21` hardcodes an SSH key path.
- Impact: portability and maintenance risk outside one host setup.

5. Low: Site-builder documentation is out of sync with current code.
- `docs/site-builder-guide.md:26` references `logoSrc` in `siteConfig`, but `src/data/site.ts` does not define/use it.
- `docs/site-builder-guide.md:78` and `docs/site-builder-guide.md:79` reference non-existent page data files (`consulting.ts`, `advisory.ts`).
- Impact: onboarding confusion and incorrect setup steps.

## Additional quality note
- `npm run format:check` currently fails with style warnings across many tracked files (91 files reported), so formatting consistency is not currently enforced as pass/fail in workflow.
