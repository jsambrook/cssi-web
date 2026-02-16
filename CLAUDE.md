# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development Commands

```bash
npm install          # Install dependencies
npm run dev          # Start dev server with hot reload
npm run build        # Production build to dist/
npm run preview      # Preview production build locally
npm run lint         # Check code quality (ESLint)
npm run lint:fix     # Auto-fix linting issues
npm run format       # Format all files (Prettier)
npm run format:check # Check formatting compliance
```

No test framework is configured.

## Architecture

This is an **Astro 5 static site template** for business websites. The key architectural principle is **data-driven content**: all page content lives in TypeScript data files, not in component markup. The `.astro` files are pure layout templates.

### Content/Data Flow

```
src/data/site.ts          → Brand identity, nav, contact, font config
src/data/pages/*.ts       → Per-page content (hero, features, testimonials, CTAs)
src/data/types.ts         → Shared TypeScript interfaces for all content types
src/data/pageDefaults.ts  → Header/Footer prop helpers
    ↓
src/pages/*.astro         → Route templates that import page data
    ↓
src/components/*.astro    → Reusable UI components receiving typed props
    ↓
src/layouts/*.astro       → BaseLayout (HTML shell + SEO meta) / PageLayout / BlogPostLayout
```

To change page content, edit `src/data/pages/*.ts`. To change site-wide branding, edit `src/data/site.ts`. To change colors/typography, edit `src/assets/css/tokens.css`.

### Blog System

Markdown posts in `src/content/blog/` with Zod-validated frontmatter (title, description, date, author, tags, draft). Schema defined in `src/content.config.ts`. Posts render at `/insights/{slug}` via dynamic route `src/pages/insights/[slug].astro`.

### Design Tokens

All theming uses CSS custom properties in `src/assets/css/tokens.css`. Primary brand color is `--primary` (#fe811b orange). Buttons use 70px border-radius (pill shape), cards use 20px. Full token docs in `docs/design-system.md`.

## Path Aliases

Configured in `tsconfig.json`:

- `@/*` → `src/*`
- `@components/*` → `src/components/*`
- `@layouts/*` → `src/layouts/*`
- `@data/*` → `src/data/*`
- `@assets/*` → `src/assets/*`

## Code Style

- Prettier: 2-space indent, single quotes, 100 char width, ES5 trailing commas
- ESLint with Astro and TypeScript plugins
- TypeScript strict mode (extends `astro/tsconfigs/strict`)

## Environment

The site URL is hardcoded in `src/data/site.ts` as the single source of truth.
