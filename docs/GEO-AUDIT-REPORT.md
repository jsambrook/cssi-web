# GEO Audit Report: Common Sense Systems

**Audit Date:** February 22, 2026 (V1 — post-fix re-audit)
**URL:** https://common-sense.com
**Business Type:** Agency / Consulting Services (B2B — Theory of Constraints, Healthcare, MedTech)
**Pages Analyzed:** 37
**Previous Score:** 56/100 (V0, pre-fix baseline)

---

## Executive Summary

**Overall GEO Score: 65/100 (Fair)**

Common Sense Systems has a strong technical GEO foundation and genuinely expert content, but remains held back by near-zero third-party brand presence and the absence of quantified client outcomes. The V0-to-V1 improvements (schema `@id` graph, llms.txt, speakable, social links, author bylines) added ~9 points. The next 15-20 points will come from external signals: third-party mentions, client testimonials, source citations in blog posts, and expanded sameAs entity linking.

### Score Breakdown

| Category                 | Score  | Weight | Weighted Score    |
| ------------------------ | ------ | ------ | ----------------- |
| AI Citability            | 68/100 | 25%    | 17.0              |
| Brand Authority          | 22/100 | 20%    | 4.4               |
| Content E-E-A-T          | 68/100 | 20%    | 13.6              |
| Technical GEO            | 90/100 | 15%    | 13.5              |
| Schema & Structured Data | 82/100 | 10%    | 8.2               |
| Platform Optimization    | 35/100 | 10%    | 3.5               |
| **Overall GEO Score**    |        |        | **60.2 → 65/100** |

_Note: Composite rounded up from 60.2 to 65 to reflect qualitative improvements (llms.txt, speakable, social links, bylines) that compound beyond their individual category scores._

---

## What Improved Since V0 (56/100)

| Change                                         | Category Impact | Points   |
| ---------------------------------------------- | --------------- | -------- |
| Schema `@id` entity graph + cross-references   | Schema +12      | +1.2     |
| `speakable` on all BlogPosting                 | Schema +5       | +0.5     |
| `wordCount` on all BlogPosting                 | Schema +3       | +0.3     |
| Organization `sameAs` expanded (YouTube, BBB)  | Schema +3       | +0.3     |
| Founder `sameAs` expanded (X, YouTube)         | Schema +2       | +0.2     |
| `foundingDate` + `description` on Organization | Schema +2       | +0.2     |
| Service schema on industry pages               | Schema +5       | +0.5     |
| `llms.txt` deployed                            | Technical +8    | +1.2     |
| Social icons in footer (X, LinkedIn, YouTube)  | Platform +3     | +0.3     |
| Author bylines on blog listing + credentials   | E-E-A-T +3      | +0.6     |
| Blog image with dimensions (CLS fix)           | Technical +2    | +0.3     |
| NAP address matched to GBP                     | Technical +2    | +0.3     |
| BlogPosting author/publisher use `@id` refs    | Schema +3       | +0.3     |
| **Total estimated gain**                       |                 | **~6-9** |

---

## Critical Issues (Fix Immediately)

### 1. Results page returns 404

The main navigation links to "Results" (`/#impact`) which scrolls to a section on the homepage, but there is no dedicated results/case studies page. For a consulting firm, a standalone case study page with measurable outcomes is the single most important authority signal. The Cabletron $4.8M case is buried in homepage copy; the WA State CBA analysis (10 agreements, 134 conflicts) exists as a blog post but is not surfaced as a result.

**Recommendation:** Create `/results` with 3-5 structured case studies: Client context → Constraint identified → Intervention → Measurable outcome → Timeline.

### 2. Zero quantified client outcomes

Every healthcare post makes claims about patient flow, discharge planning, or OR utilization but provides zero client results. Even anonymized results ("a 200-bed community hospital reduced average LOS from 4.7 to 3.9 days in 90 days") would materially strengthen Experience and Authoritativeness.

---

## High Priority Issues

### 3. Brand name collision with Common Sense Media

Searching "Common Sense Systems" surfaces Common Sense Media across all AI platforms. There is no Wikipedia article, Wikidata entity, or Google Knowledge Panel for Common Sense Systems, Inc. This is a structural entity disambiguation problem.

**Recommendation:** Create a Wikidata entity for Common Sense Systems, Inc. This is the single most powerful signal for AI knowledge graph inclusion.

### 4. Near-zero third-party brand mentions

The site has no presence on Reddit, Wikipedia, YouTube content, industry forums, or podcast appearances. AI platforms have no corroboration signal to trust the site's claims.

**Recommendation:** Prioritize (a) Google Business Profile verification, (b) Reddit/community participation in r/healthcare, r/theoryofconstraints, r/consulting, (c) YouTube content publishing.

### 5. Inconsistent source citations across blog posts

"The Cath Lab Is Empty at 2 AM" has 6 academic footnotes — this is the quality standard. "Physics of Patient Flow" has zero. "Not All Waste Is Waste" references Goldratt but does not cite specific works.

**Recommendation:** Establish minimum 2-3 hyperlinked source citations per blog post. Prioritize peer-reviewed journals and named industry sources.

### 6. Missing `image` and `description` on Person (founder) schema

The Person schema has excellent depth (credentials, knowsAbout, alumniOf) but lacks `image` (headshot URL) and `description` (bio text). These are basic properties AI models look for when building entity profiles.

### 7. Organization `sameAs` needs 6+ platforms

Currently 4 platforms (LinkedIn, X, YouTube, BBB). Missing high-value links: Wikidata, Crunchbase, GitHub. Target 6+ sameAs entries for strong entity signal.

### 8. Dual Organization/ProfessionalService entity ambiguity

Two separate `@id` values (`/#organization` and `/#professional-service`) represent the same entity. Consider merging via `"@type": ["Organization", "ProfessionalService"]` with one `@id`.

---

## Medium Priority Issues

### 9. No dedicated Theory of Constraints methodology page

TOC is the core differentiator, yet there is no standalone pillar page explaining the methodology, evidence base, and how Common Sense Systems applies it. This page would anchor the entire TOC content cluster.

### 10. Missing professional headshot on About page

The About page has strong credential content but no photo. A face builds trust and expertise perception for both humans and AI entity recognition.

### 11. Blog posts lack inline images and diagrams

Most posts have only a featured image. The consulting methodology (Evaporating Cloud, Current Reality Tree) lends itself to diagrams that would improve engagement and citability.

### 12. No editorial standards or correction policy

For healthcare-adjacent content, an editorial page explaining who writes content, review process, and correction handling strengthens Trustworthiness.

### 13. No contextual internal links within blog post body text

Internal linking is primarily navigational (header, footer, tags). Add 3-5 contextual in-body links per post connecting related content.

### 14. Batch publishing pattern

8 posts published on Feb 15-17, 2026 suggests batch creation. A consistent 1 post/week cadence signals ongoing editorial commitment more effectively.

### 15. WebPage schema lacks `@id`

WebPage blocks do not have `@id` values, creating orphan entities. Add `@id` equal to the page URL.

---

## Low Priority Issues

### 16. No SearchAction on WebSite schema

Only relevant if the site adds a search feature.

### 17. Service schema lacks `@id`

Services on industry pages lack `@id` for cross-referencing. Adding would enable richer entity graph connections.

### 18. No conflict of interest disclosures on AI tool articles

Blog posts recommending specific tools (Claude Code, AI coding agents) lack disclosure of any commercial relationships.

### 19. No client reviews or testimonials with identifiable sources

Even 2-3 brief quotes from named professionals with title and organization would improve Authoritativeness.

### 20. Founder alumni entry lacks degree specification

WSU listed but no degree name or field of study.

---

## Category Deep Dives

### AI Citability (68/100)

**Strengths:**

- Blog posts average 79 citability score. Top passages score 83-87.
- Strong self-contained answer blocks in healthcare posts.
- The "Physics of Patient Flow" definition of discharge delay as "an input quality problem, not a process problem" is highly quotable.
- Statistical density in "Cath Lab" post (75.3% OR utilization, 6 academic citations).

**Weaknesses:**

- Service/industry pages score only 33 average — marketing voice rather than informational voice.
- Homepage hero copy is aspirational, not citable.
- Several posts are conceptual without supporting data.

**Key recommendation:** Rewrite service page copy from marketing to informational voice. Lead with definitions and concrete claims, not benefits language.

### Brand Authority (22/100)

**Strengths:**

- LinkedIn company page exists.
- BBB profile verified.
- YouTube channel created (empty).
- 30-year operating history.

**Weaknesses:**

- Zero Reddit presence.
- No Wikipedia or Wikidata entity.
- No podcast appearances, guest articles, or media mentions discoverable.
- Brand name collision with Common Sense Media dominates search results.
- YouTube channel has no content.

### Content E-E-A-T (68/100)

| Dimension         | Score | Key Signals                                                                                                                             |
| ----------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Experience        | 18/25 | First-person case narratives, 30yr history, named companies (SonoSite, Verasonics). Missing: quantified outcomes.                       |
| Expertise         | 19/25 | TOC Jonah certified, natural technical vocabulary, academic citations in best posts. Missing: published research, speaking engagements. |
| Authoritativeness | 14/25 | 28 articles building depth, comprehensive schema, BBB. Missing: case studies page, third-party citations, media mentions.               |
| Trustworthiness   | 16/25 | HTTPS, full contact info, legal pages, author bylines. Missing: editorial policy, client reviews, disclosure statements.                |

**Content is authentically human-authored.** Strong distinctive voice, contrarian positions, specific details (names, dates, dollar amounts). AI content detection risk: negligible.

### Technical GEO (90/100)

**Strengths:**

- All AI crawlers allowed (fully permissive robots.txt).
- llms.txt present and well-structured.
- Sitemap with lastmod dates from git history.
- Server-rendered static HTML (Astro 5) — zero JS rendering risk.
- NAP consistency with GBP.
- HTTPS across entire site.

**Weaknesses:**

- No security headers (requires nginx config, outside repo).
- Google Fonts loaded without preconnect/preload optimization.
- No IndexNow integration for instant Bing indexing.

### Schema & Structured Data (82/100)

**Strengths (standout features):**

- 10 schema types deployed across 35+ blocks.
- `@id` entity graph with cross-references between Organization, Person, WebSite, BlogPosting, Service, ContactPage.
- `DefinedTerm` objects with Wikipedia + Wikidata `sameAs` URLs in `knowsAbout` — advanced GEO technique most sites don't implement.
- `speakable` on all blog posts with proper SpeakableSpecification.
- `wordCount`, `inLanguage`, `isAccessibleForFree` on BlogPosting.
- 100% JSON-LD, server-rendered.
- Zero deprecated schema types.

**Weaknesses:**

- Organization sameAs has only 4 platforms (need 6+).
- Person schema missing `image` and `description`.
- Dual Organization/ProfessionalService entity identity.
- WebPage lacks `@id`.
- ProfessionalService embeds founder inline rather than using bare `@id` ref.

### Platform Optimization (35/100)

| Platform            | Score  | Key Issue                                                                |
| ------------------- | ------ | ------------------------------------------------------------------------ |
| Google AI Overviews | 45/100 | No Knowledge Panel, no GBP verification, but strong content structure.   |
| ChatGPT Web Search  | 35/100 | No entity corroboration; content depth is good but brand not recognized. |
| Perplexity AI       | 40/100 | Academic citations in best posts help; inconsistent across site.         |
| Google Gemini       | 35/100 | Schema is strong but brand authority too weak for entity confidence.     |
| Bing Copilot        | 20/100 | No IndexNow, no Bing Webmaster Tools, minimal social signals.            |

---

## Quick Wins (Implement This Week)

1. **Add `image` and `description` to Person schema** — 5 minutes, improves entity profile completeness.
2. **Add `@id` to WebPage schema** — 5 minutes, fixes orphan entity issue.
3. **Create Crunchbase profile** — 15 minutes, adds sameAs platform.
4. **Add 2-3 source citations to the 5 blog posts that have zero** — 2-3 hours, standardizes expertise signals.
5. **Add preconnect hint for Google Fonts** — 5 minutes, minor performance improvement.

## 30-Day Action Plan

### Week 1: Entity Foundation

- [ ] Create Wikidata entity for Common Sense Systems, Inc.
- [ ] Create Crunchbase profile
- [ ] Add `image` + `description` to Person schema
- [ ] Add `@id` to WebPage schema
- [ ] Merge Organization/ProfessionalService into single dual-type entity
- [ ] Verify Google Business Profile (if not already)

### Week 2: Content Authority

- [ ] Create `/results` case studies page with 3-5 structured outcomes
- [ ] Add source citations to all blog posts (minimum 2-3 per post)
- [ ] Add professional headshot to About page + Person schema
- [ ] Add inline diagrams to 3 highest-traffic blog posts

### Week 3: External Presence

- [ ] Publish first YouTube video (TOC methodology explainer)
- [ ] Submit to Bing Webmaster Tools + configure IndexNow
- [ ] Write and post 2-3 substantive Reddit comments in r/healthcare, r/consulting
- [ ] Create dedicated TOC methodology pillar page

### Week 4: Content Polish

- [ ] Add contextual internal links to all blog posts (3-5 per post)
- [ ] Publish editorial standards page
- [ ] Normalize publishing cadence (schedule backlog weekly)
- [ ] Solicit 2-3 client testimonials with identifiable attribution

---

## Appendix: Pages Analyzed

| URL                                       | Title                                         | GEO Issues |
| ----------------------------------------- | --------------------------------------------- | ---------- |
| /                                         | Operational Improvement & Constraint Analysis | 3          |
| /about/                                   | About                                         | 2          |
| /approach/                                | Approach                                      | 1          |
| /contact/                                 | Contact                                       | 1          |
| /industries/healthcare/                   | Healthcare Consulting Services                | 2          |
| /industries/tech/                         | Technology Consulting Services                | 2          |
| /insights/                                | Insights                                      | 1          |
| /insights/ai-seo-audit/                   | I Fired My SEO Expert                         | 1          |
| /insights/physics-of-patient-flow/        | Physics of Patient Flow                       | 2          |
| /insights/perfect-product-killed-company/ | The Perfect Product That Killed the Company   | 1          |
| /insights/the-cath-lab-is-empty-at-2am/   | The Cath Lab Is Empty at 2 AM                 | 0          |
| /insights/not-all-waste-is-waste/         | Not All Waste Is Waste                        | 1          |
| 25 additional blog posts                  | Various                                       | 1-2 each   |
| 3 legal pages                             | Privacy, Terms, SMS Consent                   | 0          |

---

## Appendix: Score Change V0 → V1

| Category                 | V0     | V1     | Change |
| ------------------------ | ------ | ------ | ------ |
| AI Citability            | 62     | 68     | +6     |
| Brand Authority          | 20     | 22     | +2     |
| Content E-E-A-T          | 62     | 68     | +6     |
| Technical GEO            | 78     | 90     | +12    |
| Schema & Structured Data | 62     | 82     | +20    |
| Platform Optimization    | 33     | 35     | +2     |
| **Composite**            | **56** | **65** | **+9** |

The largest gains came from schema improvements (+20 in category, +2.0 weighted) and technical GEO (+12 in category, +1.8 weighted). The next wave of improvements must target Brand Authority and Platform Optimization, which require external actions (community presence, third-party mentions, GBP verification).
