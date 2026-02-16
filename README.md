# Common Sense Systems Web Template

A multi-site template for Common Sense Systems business websites.
Edit data files to spin up a new branded site — no component code changes needed.

## Quick Start

```bash
npm install
npm run dev
```

## Tooling Requirements

- `shellcheck` is required for `npm run lint:shell`
- macOS: `brew install shellcheck`
- Ubuntu/Debian: `sudo apt-get install shellcheck`

For a complete guide to creating a new site, see **[docs/site-builder-guide.md](docs/site-builder-guide.md)**.

## Technology Stack

- **Astro 5** — Static site generator
- **Tailwind CSS v3** — Utility-first CSS framework
- **Instrument Sans** — Primary typeface (Google Fonts)

## Architecture

All page content lives in TypeScript data files, not in component markup.
The `.astro` files are pure layout templates that import from data.

```
src/
├── data/
│   ├── site.ts            # Brand config (name, nav, contact, font, URLs)
│   ├── types.ts           # Shared interfaces
│   ├── pageDefaults.ts    # Header/Footer prop helpers
│   └── pages/             # Per-page content (home, about, approach, etc.)
├── assets/css/
│   └── tokens.css         # Design tokens (colors, typography, spacing)
├── components/            # Reusable Astro components
├── content/blog/          # Markdown blog posts
├── layouts/               # Page layouts (BaseLayout, BlogPostLayout)
├── pages/                 # Route templates
└── content.config.ts      # Blog collection schema
```

## Creating a New Site

1. Edit `src/data/site.ts` — identity, nav, contact, font
2. Edit `src/assets/css/tokens.css` — brand colors
3. Replace images in `public/images/`
4. Edit content in `src/data/pages/`
5. Add blog posts in `src/content/blog/`
6. Build and deploy

See [docs/site-builder-guide.md](docs/site-builder-guide.md) for detailed instructions and a verification checklist.

## Design System

The design uses CSS custom properties for full theme control:

- **Primary color** (`--primary`) — CTAs, links, and highlights
- **Foreground/Background** — text and page colors
- **Border radius** — 70px buttons, 20px cards
- **Typography** — configurable font with weight tokens

See `docs/design-system.md` for complete token documentation.

## Component Library

- **Header** — Sticky nav with logo, links, CTA, and active page highlighting
- **Hero** — Full-width hero with headline, bullets, and CTAs
- **Section** — Consistent section wrapper with optional background
- **FeatureCard** — Icon + title + description card with color variants
- **TestimonialCard** — Quote with attribution and avatar
- **CTASection** — Call-to-action banner with gradient background
- **Footer** — Multi-column footer with contact info

## SEO

Built-in SEO infrastructure:

- Sitemap generation via `@astrojs/sitemap`
- Dynamic `robots.txt` with sitemap URL
- Canonical URLs on every page
- Open Graph and Twitter meta tags
- Custom 404 page

## Blog

Markdown blog posts in `src/content/blog/` with frontmatter:

```md
---
title: 'Post Title'
description: 'Short description'
date: 2026-01-15
author: 'Author Name'
tags: ['tag1']
draft: false
---
```

Posts appear on `/insights` sorted by date. Individual posts render at `/insights/{slug}`.

## License

Internal use only — Common Sense Systems, Inc.
