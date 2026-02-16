# Code Review Findings

**Date:** 2026-02-16
**Reviewer:** Claude Opus 4.6
**Scope:** Full codebase review of cssi-web (Astro 5 static site)
**Build:** Passes (66 pages). Lint: clean. Formatting: clean. SEO checks: pass.

> All 18 findings from the previous review have been fixed.

---

## High

### 1. `parseAddress` in schema.ts silently produces empty strings on malformed input

**File:** `src/data/schema.ts:3-12`

If `footerContact.address` in `site.ts` is ever changed to a format that doesn't match `"street\ncity, ST ZIP"`, the regex fails silently and all address fields in JSON-LD (`addressLocality`, `addressRegion`, `postalCode`) become empty strings. This produces invalid structured data with no build error.

```typescript
const cityMatch = cityLine?.match(/^(.+),\s*([A-Z]{2})\s+(\d{5})/);
return {
  addressLocality: cityMatch?.[1] ?? '',  // silently empty
```

**Fix:** Add assertions:

```typescript
function parseAddress(raw: string) {
  const parts = raw.split('\n');
  assert(parts.length === 2, `Address must be "street\\ncity, ST ZIP", got: ${raw}`);
  const [streetLine, cityLine] = parts;
  const match = cityLine.match(/^(.+),\s*([A-Z]{2})\s+(\d{5})/);
  assert(match, `City line must match "City, ST ZIP", got: ${cityLine}`);
  return {
    streetAddress: streetLine.trim(),
    addressLocality: match[1],
    addressRegion: match[2],
    postalCode: match[3],
  };
}
```

### 2. Footer emoji icons lack `aria-hidden="true"`

**File:** `src/components/Footer.astro:95, 107, 120`

The phone, email, and location emoji `<span>` elements are decorative but will be announced by screen readers as separate items (e.g., "telephone receiver", "envelope").

```astro
<span>📞</span>
<!-- line 95 -->
<span>✉️</span>
<!-- line 107 -->
<span>📍</span>
<!-- line 120 -->
```

**Fix:** Add `aria-hidden="true"` to each span.

### 3. ResultsSection emoji icons lack `aria-hidden="true"`

**File:** `src/components/ResultsSection.astro:107-109, 133-135`

The hospital (&#x1F3E5;) and scales (&#x2696;&#xFE0F;) emoji characters inside `<div>` elements are decorative but will be announced by screen readers.

**Fix:** Add `aria-hidden="true"` to the parent div, or wrap the emoji in a `<span aria-hidden="true">`.

### 4. IntakeForm email validation too lenient

**File:** `src/components/IntakeForm.astro:238`

```javascript
return input.value.trim() !== '' && input.value.includes('@');
```

This accepts strings like `"@"`, `"a@"`, `"@b"` as valid emails.

**Fix:** Use a minimal regex:

```javascript
return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
```

### 5. `colorClasses` typed as `Record<string, string>` -- no compile-time safety

**File:** `src/data/colors.ts:1`

```typescript
export const colorClasses: Record<string, string> = { ... };
```

The color union type `'default' | 'red' | 'orange' | 'amber' | 'blue' | 'green' | 'purple'` is defined in `types.ts` (on `FeatureItem.color` and `ServiceCardItem.color`) but `colorClasses` uses `Record<string, string>`. If a new color variant is added to the type, TypeScript won't flag the missing entry in `colorClasses`.

**Fix:**

```typescript
type ColorVariant = NonNullable<FeatureItem['color']>;
export const colorClasses: Record<ColorVariant, string> = { ... };
```

---

## Medium

### 6. ResultsSection hardcodes links to standalone insight pages

**File:** `src/components/ResultsSection.astro:122, 149`

```astro
<a href="/insights/pacp" ...>Read the Concept Paper &rarr;</a>
<a href="/insights/nursing-conflict" ...>View the Analysis &rarr;</a>
```

These URLs are baked into the component markup, not passed as props or imported from `manualInsights.ts`. If either page is renamed or removed, the links break silently with no build error.

**Fix:** Accept as props, or import slugs from `manualInsights.ts` and construct URLs.

### 7. Schema.ts duplicates `knowsAbout` and `hasCredential` arrays

**Files:** `src/data/schema.ts:140-198` (in `buildProfessionalServiceSchema`) and `src/data/schema.ts:276-334` (in `buildFounderSchema`)

The `knowsAbout` array (7 DefinedTerm items), `hasCredential`, and `alumniOf` arrays are copy-pasted between these two functions. Updating one without the other creates inconsistent structured data.

**Fix:** Extract to shared constants:

```typescript
const founderKnowsAbout = [ ... ];
const founderCredentials = [ ... ];
const founderAlumni = [ ... ];
```

### 8. Unused `input` Tailwind color token

**File:** `tailwind.config.mjs:37`

```javascript
input: 'var(--input)',
```

This token references `--input` from `tokens.css`, but no component uses `bg-input`, `text-input`, etc. The IntakeForm component uses `bg-[var(--input-background)]` directly instead. The token exists but serves no purpose.

**Fix:** Remove the `input` token from `tailwind.config.mjs`, or use it in components instead of the raw CSS variable.

### 9. `deploy.sh` hardcodes absolute path

**File:** `deploy.sh:12`

```bash
REPO_DIR="/git/cssi-web"
```

If the repo is cloned to a different location on a new server, this breaks.

**Fix:** Derive from script location:

```bash
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
```

### 10. Standalone insight pages use BaseLayout directly, missing WebPage schema

**Files:** `src/pages/insights/pacp.astro:46`, `src/pages/insights/nursing-conflict.astro`

Both standalone insight pages use `BaseLayout` instead of `PageLayout`. They get article schema and breadcrumbs, but miss the `WebPage` schema that all other inner pages receive via `PageLayout`. This is a minor SEO inconsistency.

**Fix:** Add `buildWebPageSchema(...)` to their `jsonLd` arrays, or switch to `PageLayout`.

---

## Low

### 11. Contact page duplicates address parsing from schema.ts

**File:** `src/pages/contact.astro:11`

```typescript
const [addressStreet, addressCity] = footerContact.address.split('\n');
```

This is the same split done in `src/data/schema.ts:5`. Minor DRY issue -- if the address format changes, both locations need updating.

**Fix:** Export the parsed address from `schema.ts` or add an `addressParts` helper.

### 12. Blog OG image fallback path not validated at build time

**File:** `src/pages/insights/[slug].astro:15`

```typescript
const ogImage = post.data.ogImage ?? `/images/blog/${post.id}.png`;
```

If a blog post lacks `ogImage` and the auto-generated PNG doesn't exist, the OG meta tag points to a 404. The `generate-og-images.js` script covers this case for markdown posts, but there's no build-time assertion that the fallback file actually exists.

### 13. IntakeForm Formspree error response handling is imprecise

**File:** `src/components/IntakeForm.astro:307-309`

```javascript
const data = await res.json();
if (data.ok) { ... }
```

If Formspree returns a non-JSON response (e.g., 500 with HTML body), `res.json()` throws, and the catch block shows "Network error" which is misleading. Consider checking `res.ok` first:

```javascript
if (!res.ok) {
  showError('Submission failed. Please try again.');
  return;
}
const data = await res.json();
```

---

## Positive Patterns

- **All 18 previous findings fixed.** Standalone insight pages now import from `manualInsights.ts`, legal pages use `PageLayout`, `colorClasses` deduplicated to `src/data/colors.ts`, post listings use shared `PostCard` component, scripts are executable, Tailwind uses ESM imports, etc.
- **Data-driven architecture** is well-executed. Content lives in TypeScript data files with shared types, and `.astro` files are pure templates.
- **SEO infrastructure** is thorough: automated postbuild SEO checker, frontmatter SEO linter in prebuild, canonical URLs, Open Graph, Twitter cards, structured data (Organization, WebPage, BreadcrumbList, BlogPosting), robots.txt, sitemap, RSS feed.
- **Accessibility** is solid: skip-to-content link, `aria-current="page"`, `aria-expanded` on mobile menu, `aria-hidden` on decorative SVGs, semantic heading hierarchy, dark mode toggle with dynamic `aria-label`, properly labeled footer nav landmark.
- **Deploy script** is well-designed with file locking, atomic rollback on build failure, conditional `npm ci`, and syslog logging.
- **CSS custom properties** for complete theming with dark mode support, including feature card colors and CTA gradients.
- **TypeScript strict mode** with Zod schema validation on blog frontmatter.
- **OG image generation** pipeline with caching and design versioning.
- **Shared utilities** (`src/utils/tags.ts`, `src/utils/dates.ts`, `src/utils/seo.ts`) keep logic DRY across pages.
