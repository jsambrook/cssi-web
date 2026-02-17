# Code Review Findings

**Date:** 2026-02-16
**Reviewer:** Claude Opus 4.6
**Scope:** Full codebase review of cssi-web (Astro 5 static site)
**Previous reviews:** 2 prior rounds (18 findings fixed, 13 findings in last round)

---

## High

### 1. Dead components: FeatureCard and TestimonialCard

**Files:**
- `src/components/FeatureCard.astro` (entire file, never rendered)
- `src/components/TestimonialCard.astro` (entire file, never rendered)
- `src/data/types.ts:27-39` (`FeatureItem`, `TestimonialItem` interfaces)

Neither `<FeatureCard>` nor `<TestimonialCard>` is rendered anywhere in the codebase. `TestimonialItem` is never imported. `FeatureItem` is imported only in `src/data/colors.ts:1` solely to extract the `ColorVariant` type.

**Fix:** Export `ColorVariant` as a standalone type in `types.ts`. Remove both unused components and their interfaces.

### 2. ColorVariant type duplicated in three places

**Files:**
- `src/data/types.ts:30` (inside `FeatureItem.color`)
- `src/data/types.ts:97` (inside `ServiceCardItem.color`)
- `src/components/FeatureCard.astro:19` (inline in Props)

The union `'default' | 'red' | 'orange' | 'amber' | 'blue' | 'green' | 'purple'` appears three times. Adding or removing a color requires updating all three independently.

**Fix:** Export `ColorVariant` from `types.ts` and reference it in `ServiceCardItem` and `colors.ts`. (Subsumes the FeatureCard fix from finding #1 since that component should be removed.)

### 3. Inconsistent date handling in manual insight pages

**Files:**
- `src/pages/insights/pacp.astro:20`
- `src/pages/insights/nursing-conflict.astro:20`

Both use `insight.date.toISOString().slice(0, 10)` for schema.org `datePublished`, producing a bare date string (`"2026-02-16"`). The rest of the codebase uses `toPacificIso()` from `src/utils/dates.ts`, which produces a full Pacific-anchored ISO timestamp (`"2026-02-16T08:00:00.000Z"`). This means structured data has inconsistent date formats between markdown blog posts and manual insight pages.

**Fix:** Import and use `toPacificIso` in both manual insight pages.

### 4. Misleading CTA and duplicate destinations on PACP page

**File:** `src/pages/insights/pacp.astro:245-257`

Two issues:
1. The secondary CTA reads "Download the Concept Paper" but links to `/contact`. There is no downloadable document. Users expect a PDF download.
2. Both CTAs ("Discuss a Pilot Implementation" and "Download the Concept Paper") link to the same URL (`/contact`), making the two-button layout misleading.

**Fix:** Either create an actual downloadable concept paper, change the button text to "Request the Concept Paper", or consolidate into a single CTA.

---

## Medium

### 5. Missing type annotation on contactGrid

**File:** `src/data/pages/contact.ts:14`

`contactGrid` is an untyped export with a complex nested shape (four sections with varying optional properties). Every other page data export in the project has an explicit type annotation (`PageHeader`, `CTAContent`, `LegalBlock[]`, etc.). This is inconsistent and loses compile-time safety.

**Fix:** Define a `ContactGridItem` interface and `ContactGrid` type in `types.ts`, then annotate the export.

### 6. `parseAddress` in schema.ts silently produces empty strings on malformed input

**File:** `src/data/schema.ts:3-12`

If `footerContact.address` in `site.ts` doesn't match the expected `"street\ncity, ST ZIP"` format, the regex fails silently and all address fields in JSON-LD become empty strings. This produces invalid structured data with no build error.

**Fix:** Add assertions to fail loudly on malformed input.

### 7. Schema.ts duplicates founder data arrays

**Files:** `src/data/schema.ts` (`buildProfessionalServiceSchema` and `buildFounderSchema`)

The `knowsAbout`, `hasCredential`, and `alumniOf` arrays are copy-pasted between these two functions. Updating one without the other creates inconsistent structured data.

**Fix:** Extract to shared constants.

### 8. ResultsSection hardcodes links to standalone insight pages

**File:** `src/components/ResultsSection.astro:122, 149`

URLs `/insights/pacp` and `/insights/nursing-conflict` are baked into the component markup, not imported from `manualInsights.ts`. If either page is renamed or removed, the links break silently.

**Fix:** Import slugs from `manualInsights.ts` and construct URLs.

### 9. IntakeForm email validation too lenient

**File:** `src/components/IntakeForm.astro:238`

```javascript
return input.value.trim() !== '' && input.value.includes('@');
```

Accepts `"@"`, `"a@"`, `"@b"` as valid emails. The browser's native `type="email"` validation catches some of these, but the custom JS validation runs first.

**Fix:** Use `/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim())`.

---

## Low

### 10. Footer emoji icons lack `aria-hidden="true"`

**File:** `src/components/Footer.astro:95, 107, 120`

The phone, email, and location emoji spans are decorative but will be announced by screen readers.

**Fix:** Add `aria-hidden="true"` to each span.

### 11. Contact page duplicates address parsing from schema.ts

**File:** `src/pages/contact.astro:11`

`footerContact.address.split('\n')` duplicates the same split done in `src/data/schema.ts:5`.

**Fix:** Export parsed address from a shared location.

### 12. `deploy.sh` hardcodes absolute path

**File:** `deploy.sh:12`

```bash
REPO_DIR="/git/cssi-web"
```

**Fix:** Derive from script location: `REPO_DIR="$(cd "$(dirname "$0")" && pwd)"`.

### 13. Blog OG image fallback path not validated at build time

**File:** `src/pages/insights/[slug].astro:15`

If a blog post lacks `ogImage` and the auto-generated PNG doesn't exist, the OG meta tag points to a 404.

---

## Summary

| # | Finding | Severity | Effort |
|---|---------|----------|--------|
| 1 | Dead FeatureCard/TestimonialCard components | High | Small |
| 2 | ColorVariant type duplication | High | Small |
| 3 | Inconsistent date handling in manual insights | High | Small |
| 4 | Misleading/duplicate PACP CTA | High | Small |
| 5 | Missing contactGrid type annotation | Medium | Small |
| 6 | parseAddress silent failure | Medium | Small |
| 7 | Schema.ts duplicate founder data | Medium | Small |
| 8 | ResultsSection hardcoded links | Medium | Small |
| 9 | IntakeForm email validation | Medium | Small |
| 10 | Footer emoji accessibility | Low | Small |
| 11 | Contact page address parsing DRY | Low | Small |
| 12 | deploy.sh hardcoded path | Low | Small |
| 13 | Blog OG image fallback not validated | Low | Small |

---

## Positive Patterns

- **Data-driven architecture** is well-executed. Content lives in TypeScript data files with shared types, `.astro` files are pure templates.
- **SEO infrastructure** is thorough: automated postbuild SEO checker, frontmatter SEO linter in prebuild, canonical URLs, Open Graph, Twitter cards, structured data, robots.txt, sitemap, RSS feed.
- **Accessibility** is solid: skip-to-content link, `aria-current="page"`, `aria-expanded` on mobile menu, `aria-hidden` on decorative SVGs, semantic heading hierarchy, dark mode toggle.
- **CSS custom properties** provide complete theming with dark mode support.
- **TypeScript strict mode** with Zod schema validation on blog frontmatter.
- **Shared utilities** (`dates.ts`, `tags.ts`, `seo.ts`) keep logic DRY across pages.
- **Deploy script** has file locking, atomic rollback, conditional `npm ci`, and syslog logging.
- **metaTitle/metaDescription** frontmatter fields are properly wired through `[slug].astro` to `BlogPostLayout.astro` for per-post SEO overrides.
