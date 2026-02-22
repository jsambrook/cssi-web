# GEO Audit Report: Common Sense Systems

**Audit Date:** February 22, 2026
**URL:** https://common-sense.com
**Business Type:** Agency / Consulting Services (Operational Consulting)
**Pages Analyzed:** 37

---

## Executive Summary

**Overall GEO Score: 56/100 (Poor)**

Common Sense Systems has genuinely strong content with original intellectual frameworks (PACP, Assumption Space, TOC-based healthcare analysis) and technically sophisticated schema markup — but the site is nearly invisible outside its own domain. The fundamental problem is not content quality; it is entity invisibility. AI models cannot cite a source they have never encountered in training or retrieval. The site's excellent crawler access (fully open robots.txt) and above-average structured data go largely unused because there is no external corroboration on platforms AI models rely on: zero Reddit mentions, no Wikipedia presence, no YouTube content, no Google Business Profile, and no third-party reviews.

### Score Breakdown

| Category                 | Score  | Weight | Weighted Score |
| ------------------------ | ------ | ------ | -------------- |
| AI Citability            | 62/100 | 25%    | 15.5           |
| Brand Authority          | 18/100 | 20%    | 3.6            |
| Content E-E-A-T          | 62/100 | 20%    | 12.4           |
| Technical GEO            | 82/100 | 15%    | 12.3           |
| Schema & Structured Data | 72/100 | 10%    | 7.2            |
| Platform Optimization    | 52/100 | 10%    | 5.2            |
| **Overall GEO Score**    |        |        | **56/100**     |

---

## Critical Issues (Fix Immediately)

### 1. No llms.txt File (404)

**Impact:** AI systems have no structured summary of the site's purpose and content.
**URL:** https://common-sense.com/llms.txt (returns 404)
**Fix:** Create and deploy an llms.txt file summarizing the organization, services, founder credentials, and linking to key content pages. This is the single fastest win — takes 30 minutes, moves the llms.txt score from 0 to 70+.

### 2. Zero External Brand Presence

**Impact:** AI models cannot validate the entity "Common Sense Systems" or "John Sambrook" from any external source.
**Details:**

- No Wikipedia article or Wikidata entity
- Zero Reddit mentions
- No YouTube channel or videos
- No Google Business Profile
- No third-party reviews (Clutch, G2, Trustpilot)
- BBB profile exists but has no rating/reviews
- LinkedIn company page has ~90 followers
  **Fix:** Begin building external presence on Reddit, YouTube, and Google Business Profile (see 30-Day Action Plan).

### 3. All Security Headers Missing

**Impact:** Trust signals weakened; vulnerable to downgrade attacks despite HTTPS.
**Details:** No HSTS, no CSP, no X-Frame-Options, no X-Content-Type-Options, no Referrer-Policy, no Permissions-Policy. Server returns only default nginx headers.
**Fix:** Add security headers to nginx configuration:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: [appropriate policy]
```

### 4. No Testimonials or Client Endorsements Visible

**Impact:** 30 years of consulting with zero visible social proof severely limits authoritativeness signals.
**Fix:** Add 3-5 anonymized or named client quotes. Even "A CMO at a Pacific Northwest health system said..." would help. Consider a dedicated "Results" page with structured case outcomes.

---

## High Priority Issues

### 5. No `@id` Cross-Referencing in Schema Blocks

**Impact:** 37 pages of isolated schema islands — search engines and AI models see multiple disconnected "John Sambrook" and "Common Sense Systems" entities instead of a unified entity graph.
**Fix:** Add `@id` to all Organization, Person, WebSite, and ProfessionalService schema blocks. Reference via `@id` in BlogPosting author/publisher fields instead of duplicating inline objects.

### 6. No `speakable` Property on Any Page

**Impact:** 10 free points left on the table — this is a direct signal to AI assistants for which content blocks to read aloud or cite.
**Fix:** Add `speakable` with CSS selectors targeting `article h1` and `article > p:first-of-type` to all BlogPosting schema.

### 7. sameAs Coverage Critically Thin

**Impact:** Organization has 2 platforms (LinkedIn company, X/Twitter). Person has 1 platform (LinkedIn personal). AI entity resolution requires 5+ corroborated platforms.
**Fix:** Expand Organization sameAs to include YouTube, GitHub, Crunchbase, BBB. Expand Person sameAs to include X/Twitter, GitHub. Remove John Sambrook's personal LinkedIn from the Organization sameAs array (semantically incorrect).

### 8. Inconsistent Citation Practices Across Articles

**Impact:** Some articles cite sources (PACP cites Advisory Board), others make claims without any citations (Physics of Patient Flow has zero). Inconsistency undermines trustworthiness.
**Fix:** Establish minimum 2-3 external hyperlinked citations per article. Retrofit existing articles.

### 9. No Google Business Profile

**Impact:** Missing from Google's entity ecosystem entirely. Gemini and AI Overviews draw heavily from GBP data.
**Fix:** Claim and optimize GBP with exact NAP matching website schema. Resolve the BBB address discrepancy (Bothell vs. Kirkland).

### 10. Blog Headings Written as Statements, Not Queries

**Impact:** AI Overviews extract answers from question-format headings. Declarative headings ("The Physics of Patient Flow") don't match user queries.
**Fix:** Rewrite 5-8 key H2 headings as questions (e.g., "Why Does Hospital Discharge Planning Fail?") followed by 40-60 word direct-answer paragraphs.

---

## Medium Priority Issues

### 11. No Author Bylines on Insights Listing Page

The listing shows titles, dates, and tags but no author attribution. Crawlers indexing the listing page miss E-E-A-T signals.

### 12. Author Credentials Not Visible in Blog Bylines

Byline shows "John Sambrook, Founder & President" but not "TOC Jonah Certified." The Person schema contains the credential — make it visible in HTML too.

### 13. BlogPosting Author is Minimal Stub

Blog post author schema is `{name, jobTitle, url}` — disconnected from the rich Person schema on the About page. Without `@id` linking, AI models see two unrelated entities.

### 14. No Service Schema on Industry Pages

The /industries/healthcare/ and /industries/tech/ pages have only Organization + BreadcrumbList + WebPage. Adding Service schema with `provider` referencing Organization `@id` creates explicit service-entity connections.

### 15. Service Pages Are Thin (350-500 words)

Healthcare (~450 words) and Tech (~375 words) industry pages lack the depth needed for topical authority. Target 800-1,200 words each.

### 16. No IndexNow Protocol for Bing

Bing Copilot can only cite indexed content. Without IndexNow, new content waits for organic crawl discovery. Push-based indexing gets content into Bing within minutes.

### 17. Blog Post Images Missing Width/Height Attributes

The blog post image at `/images/content/ai-seo-audit-meta-fix.png` lacks width, height, loading, and decoding attributes. CLS risk on every blog post page.

### 18. No `<link rel="preload">` for Critical Resources

Google Fonts stylesheet is render-blocking without preload or media attribute. No preload hints for any resources.

### 19. No Person Image in Schema

The About page Person schema has no `image` or `description` property. A headshot and 1-2 sentence bio would complete the entity for knowledge panel eligibility.

### 20. Publishing Cadence Burst Pattern

14 articles in 3 weeks (Feb 2026) after months of 1-3 articles. Burst-publishing can trigger quality concerns. Space future articles more evenly.

---

## Low Priority Issues

### 21. Missing `Cache-Control` Headers

No explicit cache headers on static assets. Add `Cache-Control: public, max-age=31536000, immutable` for hashed Astro assets.

### 22. Blog Post Titles Missing Brand Suffix

Blog titles lack " | Common Sense Systems" — reducing brand visibility in SERPs and social shares.

### 23. X/Twitter Handle Appears Auto-Generated

`SenseSyste86813` doesn't strengthen brand recognition. Claim a more branded handle if available.

### 24. Homepage Title Slightly Over 60 Characters

"Operational Improvement & Constraint Analysis | Common Sense Systems" at 66 chars may be truncated in SERPs.

### 25. No Conflict of Interest Disclosures

Articles about AI tools (Claude Code) don't disclose any relationship with tool providers.

### 26. No `wordCount` in BlogPosting Schema

Minor addition but helps AI models assess content depth. Can be computed at build time.

### 27. `Content-Type` Header Missing Charset

`text/html` without `; charset=utf-8` — the HTML meta tag covers this, but the header provides defense-in-depth.

---

## Category Deep Dives

### AI Citability (62/100)

The site has strong content with genuine intellectual frameworks, but most passages are written as persuasive consulting narrative rather than reference-quality information blocks.

**Top Citation-Ready Passages:**

| Passage                                                                                                | Source                         | Score  | Why It Works                                                                                       |
| ------------------------------------------------------------------------------------------------------ | ------------------------------ | ------ | -------------------------------------------------------------------------------------------------- |
| FTE capacity calculation ("12-hour shift = 720 min, actual clinical value: 300 min = 0.4 FTE")         | workforce-planning-beyond-ftes | 82/100 | Self-contained calculation, directly answers "how much of a nursing shift is actual patient care?" |
| "25% of hospital days are avoidable" (Advisory Board)                                                  | pacp                           | 78/100 | Sourced statistic, clean and extractable                                                           |
| Administrative cost framework (20-30% of healthcare spending) + six-UDE chain                          | why-is-hc-so-stuck             | 74/100 | Original analytical contribution with causal chain                                                 |
| "Compliance means documentation matches the device. Quality means the device works safely."            | quality-illusion-medtech       | 71/100 | Crisp definitional framing, highly quotable                                                        |
| TOC vs. Lean distinction ("Does this activity affect the constraint?" vs. "Does this step add value?") | not-all-waste-is-waste         | 68/100 | Clean comparative framework                                                                        |

**Citation-Unlikely Content:**

- Homepage hero copy ("Break the Constraint. Scale the Flow.") — Score: 35/100. Marketing tagline, not citable.
- Case study outcomes ("0% Staff Turnover, 100% Client Satisfaction") — Score: 42/100. No sample size, timeframe, or methodology.
- Service pillar descriptions — Score: 38/100. Too compressed, lacks context.

**Key Gap:** Only ~5 of 30 articles produce high-quality citation blocks. The long tail scores 40-55. Most content is structured as persuasive essays rather than reference material. Adding TL;DR blocks, "Key Findings" summaries, and FAQ schema would unlock the citability potential that already exists in the content.

---

### Brand Authority (18/100)

This is the critical weakness and the primary drag on the overall GEO score.

| Platform         | Status                                                                                                                                                                                                                          | Score |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Wikipedia        | Absent — no article, no mentions                                                                                                                                                                                                | 0/30  |
| Reddit           | Zero mentions for firm, domain, or founder                                                                                                                                                                                      | 0/20  |
| YouTube          | No channel, no videos, no interviews                                                                                                                                                                                            | 0/15  |
| LinkedIn         | Company page (~90 followers) + personal profile                                                                                                                                                                                 | 6/10  |
| Industry Sources | BBB listing (no reviews), auto-generated directory entries (Datanyze, RocketReach). No TOCICO directory listing found. No G2, Clutch, Trustpilot. No industry publication mentions, conference credits, or podcast appearances. | 12/25 |

**The core problem:** Common Sense Systems exists almost entirely within its own domain. Without external corroboration, AI models have minimal basis to cite this source regardless of content quality. The brand name "Common Sense Systems" is also highly ambiguous — search results surface Common Sense Media, Common Sense Solutions, and 6+ other "Common Sense" companies competing for the same entity space.

---

### Content E-E-A-T (62/100)

| Dimension             | Score | Key Evidence                                                                                                                                                                                    |
| --------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Experience**        | 19/25 | 30-year track record, SonoSite/Verasonics roles, $4.8M IPO crisis (36-hour resolution), real AI audit case study with cost data. Unmistakably rooted in decades of doing the work.              |
| **Expertise**         | 18/25 | TOC Jonah certified (TOCICO), IEC 62304/60601 domain knowledge, original frameworks. No formal publications, speaking credits, or academic citations visible.                                   |
| **Authoritativeness** | 11/25 | Weakest dimension. No testimonials, no client logos, no media mentions, no external backlink evidence, no case study page with quantified outcomes, no third-party reviews.                     |
| **Trustworthiness**   | 16/25 | Full NAP, HTTPS, fixed-fee transparency, schema markup. But: privacy policy exists at /legal/privacy (not initially detected), inconsistent citation practices, no editorial/correction policy. |

**Content Metrics:**

- 30 articles + 7 core pages
- Word counts: 375 (Tech page) to 2,800 (Physics of Patient Flow)
- Readability: Flesch ~55-60 (appropriate for B2B healthcare audience)
- External citations: 0-2 per article (under-sourced)
- Visual content: Minimal — no diagrams, charts, or screenshots in most articles
- Internal linking: Present via navigation/tags/CTAs but sparse contextual links within body text

**AI Content Assessment:** Likely human-edited with AI assistance. The intellectual content (original frameworks, specific case anecdotes, cross-domain synthesis) is clearly human-originated. Production workflow likely involves AI drafting with heavy human editorial input on substance — the pattern Google has explicitly stated it does not penalize.

---

### Technical GEO (82/100)

| Category                 | Score   | Status                                                                                                                                                                   |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Server-Side Rendering    | 100/100 | Astro SSG — all content fully rendered in HTML. AI crawlers see 100% of content.                                                                                         |
| Meta Tags & Indexability | 90/100  | Title, description, canonical, viewport, robots all present and correct. OG tags and Twitter Cards fully implemented (correcting initial report). Geo meta tags present. |
| Crawlability             | 90/100  | Robots.txt fully permissive. Sitemap with 37 URLs and lastmod dates. RSS feed present.                                                                                   |
| Security Headers         | 18/100  | Every recommended header missing. Only default nginx headers.                                                                                                            |
| Core Web Vitals Risk     | 65/100  | Google Fonts render-blocking, blog images missing dimensions, no preload hints.                                                                                          |
| Mobile Optimization      | 90/100  | Tailwind responsive framework, proper viewport, hamburger nav, skip-to-content link.                                                                                     |
| URL Structure            | 95/100  | Clean, hierarchical, keyword-rich slugs, consistent trailing slashes.                                                                                                    |

**Strengths:** The Astro SSG architecture is ideal for GEO — static HTML means all AI crawlers see complete content without JavaScript execution. The URL structure is exemplary. Meta tags are comprehensive including geo-location tags.

**Weaknesses:** Security headers are the single largest technical gap. No llms.txt. No IndexNow for Bing. Blog images need width/height attributes.

**Correction:** The initial assessment flagged "No Open Graph or Twitter Card tags." This is **incorrect** — both are fully implemented across homepage and blog posts, including `og:image` (1200x630), `article:published_time`, `twitter:card` (summary_large_image), and proper per-page variation.

---

### Schema & Structured Data (72/100)

**9 unique schema types detected, all JSON-LD, zero validation errors.**

| Schema Type         | Pages             | Rich Result Eligible | Assessment                                                                  |
| ------------------- | ----------------- | -------------------- | --------------------------------------------------------------------------- |
| Organization        | All pages         | N/A                  | Complete but missing `@id` and `description`                                |
| ProfessionalService | Homepage, Contact | Yes (Local Business) | Exceptionally detailed — geo, services, credentials, area served            |
| WebSite             | Homepage          | Partial              | Missing SearchAction                                                        |
| WebPage             | All pages         | N/A                  | Correct                                                                     |
| ContactPage         | Contact           | N/A                  | Correct                                                                     |
| BreadcrumbList      | All inner pages   | Yes                  | Correctly implemented                                                       |
| BlogPosting         | All insights      | Yes (Article)        | Well-implemented, missing `speakable` and `wordCount`                       |
| OfferCatalog        | Homepage          | N/A                  | 3 service offerings properly structured                                     |
| Person              | About page        | N/A                  | Strong — DefinedTerm with Wikipedia/Wikidata sameAs is advanced GEO pattern |

**Notable Strength:** The use of `DefinedTerm` with Wikipedia and Wikidata `sameAs` links for John Sambrook's `knowsAbout` areas is an advanced GEO pattern that most sites completely lack. The `hasCredential` with `recognizedBy` (TOCICO) is also excellent for E-E-A-T signaling.

**Critical Gap:** No `@id` properties anywhere. Each schema block is an isolated island. The rich Person data on the About page does not flow to BlogPosting author objects. AI models and search engines cannot confirm these are the same entity across pages.

**Missing Opportunities:**

- `speakable` on BlogPosting (direct AI citation signal)
- `Service` schema on industry pages
- `FAQPage` schema on content with implicit Q&A
- Person `image` and `description`
- Organization `description` and `foundingDate` (present on ProfessionalService but not Organization)

---

### Platform Optimization (52/100)

| Platform            | Score  | Status | Key Gap                                                                     |
| ------------------- | ------ | ------ | --------------------------------------------------------------------------- |
| Google AI Overviews | 58/100 | Fair   | Declarative headings don't match queries; no question-answer content blocks |
| Google Gemini       | 56/100 | Fair   | No Google Business Profile, no YouTube, no Knowledge Panel                  |
| Bing Copilot        | 51/100 | Fair   | No IndexNow, no Bing Webmaster Tools verification                           |
| ChatGPT Web Search  | 49/100 | Poor   | Ambiguous brand name, no Wikipedia/Wikidata entity, no llms.txt             |
| Perplexity AI       | 44/100 | Poor   | Zero community validation (Reddit, forums, reviews)                         |

**Cross-Platform Pattern:** The site's technical foundation is solid across all platforms (SSG, clean HTML, rich schema). The universal weakness is external ecosystem presence. Every platform scores poorly on entity recognition and community validation dimensions.

---

## Quick Wins (Implement This Week)

1. **Deploy llms.txt** — 30-minute effort, moves score from 0 to 70+. Summarize organization, services, credentials, and link to top 10 content pages. (+7 composite points estimated)

2. **Add security headers to nginx** — Single config file change. Add HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy. (+5 technical points)

3. **Add `@id` to all schema blocks** — Template-level change in Astro, touches all 37 pages at once. Transforms isolated schema islands into unified entity graph. (+8 schema points)

4. **Add `speakable` to BlogPosting template** — One-line addition targeting h1 and first paragraph. Direct AI citation signal. (+5 schema points)

5. **Claim Google Business Profile** — Free, 15-minute setup. Ensure NAP matches website schema exactly. Fix BBB address discrepancy. (+6 platform points)

---

## 30-Day Action Plan

### Week 1: Foundation (Technical + Schema)

- [ ] Deploy llms.txt file at site root
- [ ] Add all security headers to nginx configuration
- [ ] Add `@id` to Organization, Person, WebSite, ProfessionalService schema blocks
- [ ] Update BlogPosting template: author/publisher use `@id` references, add `speakable`, add `wordCount`
- [ ] Add `description` to Organization schema, `image`+`description` to Person schema
- [ ] Claim and optimize Google Business Profile
- [ ] Verify site in Bing Webmaster Tools, implement IndexNow
- [ ] Add width/height/loading/decoding attributes to all blog post images

### Week 2: Content Structure

- [ ] Rewrite 5-8 key blog H2 headings as question-format queries
- [ ] Add 40-60 word direct-answer paragraphs after each question heading
- [ ] Add TL;DR / "Key Findings" summary blocks to top 10 articles
- [ ] Add 2-3 hyperlinked external citations to each article missing sources
- [ ] Add FAQPage schema to PACP, nursing conflict, and patient flow articles
- [ ] Add Service schema to both industry pages
- [ ] Add author bylines with credentials to Insights listing page
- [ ] Expand sameAs on Organization (5+ platforms) and Person (3+ platforms)

### Week 3: External Presence

- [ ] Create 3-5 substantive Reddit posts in r/healthcare, r/nursing, r/theoryofconstraints
- [ ] Register on TOCICO practitioner directory
- [ ] Create Clutch.co or G2 profile, request 2-3 client reviews
- [ ] Publish PACP concept paper as downloadable PDF with persistent URL
- [ ] Begin YouTube channel setup — record first 2 explainer videos (5-10 min each)

### Week 4: Authority Building

- [ ] Publish 2-3 more YouTube videos (TOC vs. Lean, FTE capacity, discharge planning)
- [ ] Draft article pitch to healthcare industry publication (HFMA, Becker's, or ACHE)
- [ ] Add testimonials or anonymized case outcomes to a Results page
- [ ] Create dedicated Case Studies page ($4.8M Cabletron, PACP development, labor analysis)
- [ ] Add contextual internal links within article body text (2-4 per article)

---

## Appendix: Pages Analyzed

| URL                                                           | Title                                                 | GEO Issues                                                               |
| ------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------ |
| /                                                             | Operational Improvement & Constraint Analysis         | No llms.txt, hero copy not citable, case outcomes unsubstantiated        |
| /approach                                                     | Our Approach to Healthcare Consulting                 | No Service/HowTo schema, ~800 words adequate                             |
| /about                                                        | About John Sambrook                                   | Strong bio, missing Person image in schema, no external profile links    |
| /contact                                                      | Contact Us in Kirkland, WA                            | Good NAP, no business hours, no map embed                                |
| /industries/healthcare                                        | Healthcare Consulting Services                        | Thin (~450 words), no Service schema                                     |
| /industries/tech                                              | Technology Consulting Services                        | Thin (~375 words), no Service schema                                     |
| /insights                                                     | Insights                                              | No author bylines on listing, 30 articles indexed                        |
| /insights/pacp                                                | The Post-Acute Care Plan (PACP)                       | Good citability (78), needs linked Advisory Board citation               |
| /insights/ai-seo-audit                                        | I Fired My SEO Expert (And Hired Claude Code Instead) | Strong case study (2,200 words), no disclosure re: AI tool relationships |
| /insights/physics-of-patient-flow                             | The Physics of Patient Flow                           | Deep content (1,850 words), zero external citations                      |
| /insights/nursing-conflict                                    | Structural Labor Conflict Analysis                    | Primary research (10 CBAs), high citation potential                      |
| /insights/workforce-planning-beyond-ftes                      | Workforce Planning Beyond FTEs                        | Highest citability score (82), FTE calculation is a quotable asset       |
| /insights/quality-illusion-medtech                            | The Quality Illusion                                  | Strong compliance-vs-quality framing, unique perspective                 |
| /insights/not-all-waste-is-waste                              | Not All Waste Is Waste                                | Good TOC vs. Lean distinction, missing statistical backing               |
| /insights/ai-facilitated-constraint-resolution                | AI-Facilitated Constraint Resolution                  | Framework article, no metrics or case outcomes                           |
| /insights/ai-self-limiting-assumptions                        | AI Self-Limiting Assumptions                          | AI topic, freshness good                                                 |
| /insights/align-teams-on-minimum-dataset                      | Align Teams on Minimum Dataset                        | Healthcare ops topic                                                     |
| /insights/architecting-hc                                     | Architecting HC                                       | Abbreviated slug, oldest article (Aug 2025)                              |
| /insights/burnout-antidote-voice-agents                       | Burnout Antidote: Voice Agents                        | AI + healthcare intersection                                             |
| /insights/decision-ready-beats-presentation-ready             | Decision-Ready Beats Presentation-Ready               | Strategy topic                                                           |
| /insights/doing-taxes-with-ai-coding-agents                   | Doing Taxes with AI Coding Agents                     | AI practical topic                                                       |
| /insights/hidden-conflicts                                    | Hidden Conflicts                                      | TOC Evaporating Cloud application                                        |
| /insights/non-value-added-work-lean                           | Non-Value-Added Work (Lean)                           | Lean methodology topic                                                   |
| /insights/perfect-product-killed-company                      | Perfect Product Killed Company                        | MedTech case study                                                       |
| /insights/post-acute-care-plan-concept                        | Post-Acute Care Plan Concept                          | Earlier version of PACP concept                                          |
| /insights/saas-subscriptions-ai-coding-agents                 | SaaS Subscriptions & AI Coding Agents                 | AI/business topic                                                        |
| /insights/short-cycles-real-outcomes                          | Short Cycles, Real Outcomes                           | Agile/TOC methodology                                                    |
| /insights/speed-as-a-strategy                                 | Speed as a Strategy                                   | Strategy topic                                                           |
| /insights/stop-blaming-people                                 | Stop Blaming People                                   | Leadership/systems thinking                                              |
| /insights/the-cath-lab-is-empty-at-2am                        | The Cath Lab Is Empty at 2AM                          | Original "Assumption Space" framework                                    |
| /insights/three-way-email-paradox                             | Three-Way Email Paradox                               | Communication/operations                                                 |
| /insights/why-agile-fails-in-hardware-and-what-actually-works | Why Agile Fails in Hardware                           | MedTech/embedded development                                             |
| /insights/why-burnout-persists-series                         | Why Burnout Persists (Series)                         | Healthcare workforce                                                     |
| /insights/why-is-hc-so-stuck                                  | Why Is Healthcare So Stuck?                           | Six-UDE framework, high citability                                       |
| /legal/privacy                                                | Privacy Policy                                        | Legal page                                                               |
| /legal/terms                                                  | Terms of Service                                      | Legal page                                                               |
| /legal/sms-consent                                            | SMS Consent                                           | Legal page                                                               |

---

_Report generated by GEO Audit System on February 22, 2026._
_Methodology: 5-agent parallel analysis covering AI Citability, Brand Authority, Technical Infrastructure, Content E-E-A-T, Schema Markup, and Platform Optimization._
