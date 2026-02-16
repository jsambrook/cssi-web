# Notes for TheBlock.me (Sean & Andrea)

## What changed and why

This template was restructured to support spinning up multiple business websites from a single codebase. The main changes:

### Content extraction

All page text that was previously hardcoded in `.astro` component files has been moved to TypeScript data files in `src/data/pages/`. The `.astro` files are now pure layout templates. This means you can create a new site by editing data files rather than digging through component markup.

### Centralized brand config

`src/data/site.ts` is the single source of truth for the brand: name, tagline, logo, nav items, contact info, CTA text, font, and site URL. Changing values here propagates everywhere.

### Design token system

Colors, typography, spacing, and radii are all CSS custom properties in `src/assets/css/tokens.css`. Changing `--primary` re-themes the entire site. Feature card colors, CTA gradients, and other visual elements all reference tokens.

### Blog/Insights system

The hardcoded article stubs on the Insights page are now a real content collection. Blog posts are markdown files in `src/content/blog/` with frontmatter for metadata. The listing page and individual post pages are generated automatically.

### SEO infrastructure

Sitemap generation (`@astrojs/sitemap`), dynamic `robots.txt`, canonical URLs, and a custom 404 page are now built in.

## How to use this for client sites

1. Clone the template repo
2. Follow `docs/site-builder-guide.md` step by step
3. The data files in `src/data/pages/` are where 90% of the work happens for a new site
4. For structural changes (adding/removing pages, changing layouts), edit the `.astro` files in `src/pages/`

## What the template provides vs. what you own

**Template provides:**

- Component library (Header, Footer, Hero, Section, FeatureCard, TestimonialCard, CTASection)
- Design token system
- Layout templates
- Blog infrastructure
- SEO infrastructure
- Build toolchain (Astro + Tailwind)

**You own per-site:**

- Brand config (`src/data/site.ts`)
- Color tokens (`src/assets/css/tokens.css`)
- Page content (`src/data/pages/`)
- Blog posts (`src/content/blog/`)
- Images (`public/images/`)

## Ideas for future collaboration

- **Shared component library**: Extract components into an npm package so template updates propagate to all sites
- **Deployment pipeline**: Set up a standard deploy process (e.g., Vercel, Netlify, or Cloudflare Pages) with preview environments
- **CMS integration**: For clients who want to edit content without touching code, add a headless CMS (Keystatic, Decap, Sanity) that writes to the data files
- **Dark mode**: The token system already has a `.dark` class defined — just needs a toggle component
- **Contact form**: Add a form handler (Formspree, Netlify Forms, or a serverless function)
