# Code Review Findings

**Date:** 2026-02-16
**Scope:** Full codebase review of cssi-web (Astro 5 static site)
**Build:** Passes (66 pages). Lint: clean. Formatting: clean. SEO checks: pass.

---

## High

### 1. Standalone insight pages duplicate data from manualInsights.ts

**Files:** `src/pages/insights/pacp.astro:17-44`, `src/pages/insights/nursing-conflict.astro:17-44`, `src/data/manualInsights.ts`

The title, description, author, date, and tags are hardcoded in each standalone `.astro` page AND repeated in `manualInsights.ts`. If one is updated without the other, the insights listing page will show stale metadata while the article itself shows the new version (or vice versa).

**Fix:** Import metadata from `manualInsights.ts` (or a shared data file) in the standalone pages instead of redeclaring it.

### 2. `SITE_URL` in .env.example is misleading -- never used

**Files:** `.env.example:3`, `astro.config.mjs:8`, `src/data/site.ts:4`

`.env.example` defines `SITE_URL=https://example.com` and CLAUDE.md says "Set `SITE_URL` in `.env` before deploying." However, `astro.config.mjs` reads the site URL from `siteConfig.siteUrl` which is hardcoded as `'https://common-sense.com'`. The env variable is never referenced anywhere in the code.

**Fix:** Either wire `import.meta.env.SITE_URL` into `astro.config.mjs` (making it actually configurable) or remove the `.env.example` and update CLAUDE.md to reflect reality.

### 3. `@napi-rs/canvas` is in `dependencies` instead of `devDependencies`

**File:** `package.json:24`

This native binary package is only used by `scripts/generate-og-images.js` at build time. Putting it in `dependencies` means it would be installed in production contexts where it's not needed, adding significant install weight.

**Fix:** Move to `devDependencies`.

### 4. Unused `features` export in home.ts

**File:** `src/data/pages/home.ts:51-71`

The `features` array is exported but never imported by any file. The home page uses `serviceCards` via `IndustryToggle` instead. This is dead code that could confuse future maintainers.

**Fix:** Remove the `features` export, or document why it's kept (e.g., planned future use).

---

## Medium

### 5. `object-contain` vs `object-cover` inconsistency on blog thumbnails

**Files:** `src/pages/insights.astro:49` uses `object-contain`; `src/pages/insights/tag/[tag].astro:77` uses `object-cover`

The same thumbnail images render with different object-fit strategies on the main insights listing vs. the tag listing page.

**Fix:** Use `object-contain` in both places (or `object-cover` in both).

### 6. Duplicated post listing template across insights pages

**Files:** `src/pages/insights.astro:38-81`, `src/pages/insights/tag/[tag].astro:66-109`

These two templates render nearly identical post lists. Any future change to the card design must be made in both places.

**Fix:** Extract a shared `PostList.astro` or `PostCard.astro` component.

### 7. Duplicated `colorClasses` map

**Files:** `src/components/FeatureCard.astro:24-32`, `src/components/IndustryToggle.astro:23-31`

The same color variant mapping is defined in two components.

**Fix:** Export from a shared module (e.g., `src/data/colors.ts`) and import in both.

### 8. Legal pages skip PageLayout, missing breadcrumb and WebPage schema

**Files:** `src/pages/legal/privacy.astro`, `src/pages/legal/terms.astro`

These pages use `BaseLayout` directly rather than `PageLayout`, so they don't get the automatic breadcrumb JSON-LD or WebPage schema that all other inner pages get. The SEO check passes because it only requires structured data on article pages, but search engines benefit from breadcrumbs on all pages.

**Fix:** Use `PageLayout` for legal pages, or manually add breadcrumb schema.

### 9. No `<nav>` landmark for footer navigation

**File:** `src/components/Footer.astro:65-84`

The footer's link columns are rendered as plain `<div>` and `<ul>` elements without a `<nav>` wrapper. Screen reader users navigating by landmarks will miss this navigation.

**Fix:** Wrap the footer columns in `<nav aria-label="Footer navigation">`.

### 10. `IndustryToggle` uses singleton querySelector

**File:** `src/components/IndustryToggle.astro:131`

`document.querySelector('.industry-toggle')` will only find the first instance. If a second IndustryToggle is ever added to a page, it would be non-functional. The Header component correctly uses `data-header-root` + `forEach` pattern to support multiple instances.

**Fix:** Use `document.querySelectorAll('.industry-toggle').forEach(...)` like Header does.

### 11. Blog thumbnail images inside links have empty `alt` text

**Files:** `src/pages/insights.astro:44-50`, `src/pages/insights/tag/[tag].astro:72-77`

The `<img alt="">` is the sole content of its parent `<a>` link. When an image is the only content inside a link, `alt=""` makes the link invisible to screen readers (it has no accessible name). These are effectively duplicate navigation links alongside the title link, but screen readers will announce them as empty links.

**Fix:** Either set `alt={post.data.title}` or remove the image's wrapping `<a>` tag (making the image purely decorative inside the article, not a separate link).

### 12. Blog thumbnail images missing `width`/`height` attributes (CLS)

**Files:** `src/pages/insights.astro:46-50`, `src/pages/insights/tag/[tag].astro:74-77`

Images have `loading="lazy"` but no explicit `width` and `height` attributes. The browser can't reserve layout space before the image loads, causing Cumulative Layout Shift.

**Fix:** Add `width="80" height="80"` to match the displayed `w-20 h-20` CSS dimensions.

---

## Low

### 13. `key` prop has no effect in Astro templates

**Files:** `src/components/Header.astro:54`, `src/components/Footer.astro:67,71,96,133`

Astro renders server-side HTML; `key` is a React/Preact concept and has no effect here. Not harmful, but misleading to readers who might expect reconciliation behavior.

### 14. Duplicated `CTA` and `Bullet` interfaces

**Files:** `src/components/Hero.astro:21-30`, `src/components/CTASection.astro:16-19`

Local interfaces duplicate `CTA` and `HeroBullet` from `src/data/types.ts`. Should import the shared types instead.

### 15. `public/.DS_Store` tracked in git

**File:** `public/.DS_Store`

macOS-specific file. Already in `.gitignore` as a top-level pattern, but the one inside `public/` slipped through. Add `**/.DS_Store` to `.gitignore` and remove from tracking.

### 16. `bard/` directory at project root

Unclear purpose. May be stale content or a working directory. Worth cleaning up or adding to `.gitignore`.

### 17. `check-frontmatter-seo.js` and `check-seo.js` are not executable

**Files:** `scripts/check-frontmatter-seo.js` (644), `scripts/check-seo.js` (644)

These scripts have shebangs (`#!/usr/bin/env node`) but aren't executable, unlike `generate-og-images.js` and `check-shell.sh` which are. They're invoked via `node scripts/...` in `package.json` so this doesn't cause failures, but it's inconsistent.

**Fix:** `chmod +x scripts/check-frontmatter-seo.js scripts/check-seo.js`

### 18. Tailwind config uses `require()` in .mjs file

**File:** `tailwind.config.mjs:71`

`plugins: [require('@tailwindcss/typography')]` is CJS syntax in an ESM file. Works because Tailwind resolves plugins internally, but is an ESM/CJS style inconsistency.

---

## Positive Patterns

- **Data-driven architecture** is well-executed. Content lives in TypeScript data files with shared types, and `.astro` files are pure templates. This makes content changes safe and predictable.
- **SEO infrastructure** is thorough: automated postbuild SEO checker, frontmatter SEO linter in prebuild, proper canonical URLs, Open Graph, Twitter cards, structured data (Organization, WebPage, BreadcrumbList, BlogPosting), robots.txt, sitemap, RSS feed.
- **Accessibility basics** are solid: skip-to-content link, `aria-current="page"`, `aria-expanded` on mobile menu, `aria-hidden` on decorative SVGs, semantic heading hierarchy, dark mode toggle with dynamic `aria-label`.
- **Deploy script** is well-designed with file locking, atomic rollback on build failure, conditional `npm ci`, and syslog logging.
- **CSS custom properties** for theming with complete dark mode support, including feature card colors and CTA gradients.
- **TypeScript strict mode** with Zod schema validation on blog frontmatter.
- **OG image generation** pipeline with caching and design versioning is a nice touch.
