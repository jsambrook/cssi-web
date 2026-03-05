# Site Builder Guide

How to create a new website from this template.

## Prerequisites

- Node.js 18+
- npm

## Step 1: Clone and install

```bash
git clone <this-repo> my-new-site
cd my-new-site
npm install
```

## Step 2: Brand identity (`src/data/site.ts`)

Edit the site config to set your brand:

```ts
export const siteConfig = {
  name: 'Your Company Name',
  tagline: 'Your company tagline',
  logoSrc: '/images/logo.png',
  siteUrl: 'https://your-domain.com',
  defaultDescription: 'Your Company - Your tagline',
  defaultOgImage: '/images/og-default.png',
  headerCta: { text: 'Get Started', href: '/contact' },
  footerContactHeading: 'Contact Us',
  font: {
    family: 'Instrument Sans',
    googleFontsUrl:
      'https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap',
  },
};
```

Also update `navItems`, `footerColumns`, `footerContact`, `legalLinks`, and `copyright` in the same file.

### Changing the font

If you change the font, update all three places:

1. `siteConfig.font.family` and `siteConfig.font.googleFontsUrl` in `src/data/site.ts`
2. `--font-sans` in `src/assets/css/tokens.css`
3. `fontFamily.sans` in `tailwind.config.mjs`

## Step 3: Brand colors (`src/assets/css/tokens.css`)

Edit the CSS custom properties under `:root` to change your brand colors:

- `--primary` / `--accent` — your brand accent color
- `--foreground` — main text color
- `--background` — page background
- `--cta-gradient-from` / `--cta-gradient-to` — CTA section gradient
- `--feature-*` — feature card icon colors

Also update the `.dark` section if you support dark mode.

## Step 4: Images (`public/images/`)

Replace these files with your own:

- `logo.png` — site logo (used in header and footer)
- `og-default.png` — default Open Graph image for social sharing
- `favicon.svg` — browser tab icon

## Step 5: Page content (`src/data/pages/`)

Each page has a corresponding data file:

| Page        | Data file                       |
| ----------- | ------------------------------- |
| Home        | `src/data/pages/home.ts`        |
| About       | `src/data/pages/about.ts`       |
| Approach    | `src/data/pages/approach.ts`    |
| Industries  | `src/data/pages/industries.ts`  |
| Insights    | `src/data/pages/insights.ts`    |
| Research    | `src/data/pages/research.ts`    |
| Contact     | `src/data/pages/contact.ts`     |
| Privacy     | `src/data/pages/privacy.ts`     |
| SMS Consent | `src/data/pages/sms-consent.ts` |
| Terms       | `src/data/pages/terms.ts`       |

Edit the data files to change page content. The `.astro` page files are layout templates and generally don't need editing.

## Step 6: Blog posts (`src/content/blog/`)

Add markdown files with this frontmatter format:

```md
---
title: 'Your Post Title'
description: 'A short description for the listing page.'
date: 2026-01-15
author: 'Your Name'
tags: ['tag1', 'tag2']
---

Post content in markdown...
```

Set `draft: true` in frontmatter to hide a post from the listing.

## Step 6b: Research papers (`src/pages/research/`)

Long-form canonical papers are published as page routes under `src/pages/research/` and their
PDF artifacts are stored in `public/assets/files/research/`.

For each paper:

1. Create a page in `src/pages/research/`
2. Add metadata and listing card in `src/data/pages/research.ts`
3. Add `ScholarlyArticle` JSON-LD using `buildScholarlyArticleSchema`
4. Place the source PDF in `public/assets/files/research/<topic>/`

## Step 7: Build and verify

```bash
npm run dev     # Start dev server
npm run build   # Production build
npm run preview # Preview production build
```

## Verification checklist

- [ ] Site name appears in header, footer, and page titles
- [ ] Logo renders in header and footer
- [ ] All navigation links work
- [ ] Active nav link highlights on each page
- [ ] Contact email is correct
- [ ] `/sitemap-index.xml` is generated
- [ ] `/robots.txt` contains correct sitemap URL
- [ ] `/insights` lists blog posts sorted by date
- [ ] Individual blog posts render with typography styles
- [ ] `/research` lists published papers
- [ ] Research paper pages include downloadable PDFs
- [ ] `/404` page renders properly
- [ ] OG meta tags have correct content (check with social sharing debugger)
- [ ] Changing `--primary` in tokens.css re-themes the entire site

## Project structure

```
src/
├── assets/css/tokens.css     # Design tokens (colors, typography, spacing)
├── components/               # Reusable Astro components
├── content/blog/             # Markdown blog posts
├── data/
│   ├── site.ts               # Brand config (name, nav, contact, font)
│   ├── types.ts              # Shared TypeScript interfaces
│   ├── pageDefaults.ts       # Header/Footer prop helpers
│   └── pages/                # Per-page content data
├── layouts/
│   ├── BaseLayout.astro      # Root HTML layout
│   └── BlogPostLayout.astro  # Blog post wrapper
├── pages/                    # Route templates
│   └── research/             # Canonical long-form paper pages
└── content.config.ts         # Blog collection schema
```
