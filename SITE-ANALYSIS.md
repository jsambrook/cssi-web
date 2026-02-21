# Googlebot Audit: common-sense.com

_Conducted 2026-02-21 against the `dist/` build output (the actual HTML Googlebot sees)._

## What's Working Well

**Meta Tags — Excellent across the board**

- Every page has `<title>`, `<meta description>`, `<canonical>`, `<robots>`, full OG suite, full Twitter Card suite
- Blog posts correctly use `og:type="article"` with `article:published_time`, `article:author`, and `article:tag`
- OG images specify dimensions (1200x630) and type
- Blog posts have per-article OG images (`/images/blog/{slug}.png`)
- Geo meta tags on every page (geo.region, geo.placename, geo.position, ICBM)

**JSON-LD Structured Data — Among the best I've seen on a small business site**

- Homepage: 5 JSON-LD blocks — Organization, WebSite, WebPage, ProfessionalService (with geo, areaServed, hasOfferCatalog, serviceType), and a separate OfferCatalog with healthcare + tech service variants
- About page: Person schema with detailed `knowsAbout` (DefinedTerm entries linking to Wikipedia/Wikidata/ISO), `hasCredential` (TOC Jonah), `alumniOf`
- Contact page: ContactPage + ProfessionalService with the same depth
- Blog posts: BlogPosting with author, publisher, datePublished, dateModified, keywords, articleSection, image — plus BreadcrumbList
- BreadcrumbList on every subpage
- The `sameAs` links to Wikipedia, Wikidata, TOCICO, and ISO standards are exactly what knowledge graphs consume

**Technical Foundation — Solid**

- Fully static HTML (Astro SSG) — every page is server-rendered, fully crawlable, zero JS-dependent content
- Custom 404 page with `noindex, nofollow`
- Skip-to-content link, `lang="en"`, `aria-label`s on all interactive elements, `aria-hidden` on decorative SVGs
- `preconnect` to Google Fonts
- Render-blocking dark mode script prevents FOUC
- sitemap-index.xml properly references sitemap-0.xml
- RSS feed with all 25 articles, proper guids and pubDates
- robots.txt allows everything, references sitemap

**Content Quality — Strong**

- Articles are substantive, original, and well-argued (not SEO filler)
- Coherent topical clusters: healthcare operations, TOC methodology, AI/automation, MedTech
- Each article has clear authorship, dates, and tag taxonomy
- The blog listing page has thumbnails, descriptions, dates, and tag links

---

## Failings

**1. Meta descriptions are literally truncated with "..."**
Multiple pages have descriptions that end with `...` in the actual HTML:

- Homepage: `"...operational interventions for..."`
- Approach: `"...Theory of Constraints methodology to frame..."`
- Contact: `"...Healthcare operations consulting for hospitals and..."`
- Industries pages: `"...design direct-to-employer contracts, and..."`

Google will render these as-is. You're wasting 3 characters on an ellipsis instead of completing the sentence. Every description should be 150-160 characters of complete, compelling copy.

**2. Blog `<title>` tags are missing the brand suffix**
Every non-blog page appends `| Common Sense Systems` to the title. Blog posts do not:

- `<title>The Biggest Satisficing Trap AI Breaks Isn&#39;t What You Think</title>`

vs. non-blog:

- `<title>About John Sambrook | Common Sense Systems</title>`

This is an inconsistency that weakens brand recognition in SERPs for your most-shared content.

**3. No `<lastmod>` on non-blog sitemap entries**
The 10 static pages (`/`, `/about/`, `/approach/`, `/contact/`, `/industries/*`, `/insights/`, `/legal/*`) have no `<lastmod>` in the sitemap. Google uses lastmod to allocate crawl budget. Without it, Google may crawl these pages less frequently.

**4. Industry pages have weak JSON-LD**
`/industries/healthcare` and `/industries/tech` only have Organization + BreadcrumbList + WebPage. They're missing the ProfessionalService or Service schema that the homepage and contact page have. These are your keyword-targeted landing pages — they should have the richest schema.

**5. All non-blog pages share the same OG image**
Every page that isn't a blog post uses `/images/og-default.png`. When someone shares your `/industries/healthcare` page on LinkedIn, it looks identical to your contact page. Industry pages and the approach page should have distinct OG images.

**6. Tag pages are crawlable but not in the sitemap**
The footer links to 7 tag pages (`/insights/tag/healthcare`, `/insights/tag/ai`, etc.) and articles link to many more. These are crawlable by Googlebot but absent from the sitemap. If any tag has only 1-2 articles, it's a thin content page that dilutes crawl budget. You should either add them to the sitemap (if they have meaningful content) or add `noindex` to thin tag pages.

**7. RSS feed missing standard fields**
The `<channel>` lacks `<language>`, `<lastBuildDate>`, and `<managingEditor>`. Individual `<item>` entries lack `<author>` and `<category>`. These are used by feed readers and some crawlers.

**8. Blog articles are text-only — no images in body content**
Your articles are well-written prose but contain no in-article images, diagrams, or charts. Google Discover, image search, and featured snippets all favor articles with visual content. A single relevant diagram per article would significantly help.

---

## Three Content Suggestions

**1. Dedicated Case Studies page**
Your homepage has the $4.8M IPO Standoff story — it's compelling, but it's the only concrete result anywhere on the site. Create `/results` or `/case-studies` with 3-5 detailed stories, each with: the situation, the constraint identified, the intervention, and quantified outcomes. Searches like "theory of constraints consulting case study" and "healthcare operations improvement results" have strong buying intent and almost no one in your niche has this content done well.

**2. TOC Pillar Page**
You reference Evaporating Cloud, Drum-Buffer-Rope, Mafia Offer, Throughput Accounting, and Thinking Processes across your articles, but there's no single page that explains these concepts and links to the articles that apply them. A `/approach/theory-of-constraints` pillar page would capture educational search traffic ("what is an evaporating cloud," "drum-buffer-rope explained") and establish topical authority. Each concept links to relevant insights articles, creating a hub-and-spoke structure that Google rewards.

**3. Tech-vertical blog content**
Your blog skews heavily toward healthcare (patient flow, discharge planning, burnout, nursing CBAs). The tech industry page exists but has minimal supporting content. Articles like "Why Sprint Velocity Lies About Throughput," "The Real Constraint in Your CI/CD Pipeline," or "How MedTech R&D Teams Ship 2x Faster with Critical Chain" would build search authority for the tech vertical and give the `/industries/tech` page internal link equity from topically relevant content.

---

## Making the Site Useful to AI Agents

**1. Add `llms.txt` at the root**
This is the emerging convention (analogous to robots.txt for AI). Create `/llms.txt` with a structured plain-text description of:

- Who you are, what you do, what industries you serve
- Your core methodology (TOC)
- A list of your key content with URLs
- How to contact/engage

Add a companion `/llms-full.txt` that provides a plain-text rendering of your about page, approach, and service descriptions — so an AI agent can ingest your value proposition in a single fetch without parsing HTML.

**2. Add `FAQPage` schema to key pages**
On approach, contact, and industry pages, add `FAQPage` JSON-LD with common questions: "What is Theory of Constraints consulting?", "How long do engagements last?", "What does a constraint analysis cost?". AI agents (including Google SGE) pull FAQ content directly into generated answers.

**3. Your structured data is already unusually good for AI**
The `DefinedTerm` entries with `sameAs` links to Wikipedia/Wikidata, the `knowsAbout` arrays, `hasCredential`, and `hasOfferCatalog` — these are exactly what AI knowledge graphs consume. Most small business sites have none of this. The `speakable` schema on blog articles would be the next addition — it tells AI agents which paragraphs are best to excerpt or read aloud.

**4. Add a structured content index**
Consider a `/content-index.json` endpoint that provides a machine-readable map of your content: each article's URL, title, description, tags, date, and canonical topic. AI agents that want to recommend your content or cite specific articles can consume this without scraping.
