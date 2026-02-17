# Brand Guidelines

Common Sense Systems, Inc. — Kirkland, Washington — Founded 1996

This document defines the visual identity, editorial voice, and content standards for all Common Sense Systems materials, including the website, blog posts, concept papers, and client-facing documents. It is the reference for anyone (human or AI) producing content for this brand.

---

## Who We Are

Common Sense Systems helps organizations find and fix the constraints that keep them stuck. We apply Theory of Constraints methodology, systems architecture thinking, and AI-assisted analysis to problems that span departmental boundaries — in healthcare, manufacturing, technology, and anywhere complex systems produce chronic frustration.

We are not locked to a single industry. TOC, Lean, and systems thinking are domain-independent disciplines. Our healthcare work is deep and growing, but the methods apply wherever smart people are stuck on solvable problems. The website and all content should communicate this range directly and indirectly: the principles are universal, the applications are specific.

### Positioning

We are a systems architecture consulting practice, not a technology vendor. We sell clarity about what is actually going on and practical paths forward. Our differentiator is the combination of:

- Deep TOC methodology (Jonah-certified, trained directly by Goldratt)
- 30+ years of embedded systems engineering discipline
- AI-assisted analysis that extends what one person can hold in working memory
- A genuine outsider's perspective applied with respect for insiders' expertise

We are not a large firm. We do not pretend to be. The work is personal, direct, and accountable.

---

## Visual Identity

### Colors

| Token            | Hex       | Usage                                             |
| ---------------- | --------- | ------------------------------------------------- |
| Primary (Orange) | `#fe811b` | Brand accent, buttons, links, selection highlight |
| Secondary (Blue) | `#155dfc` | Supporting accent, charts, secondary actions      |
| Foreground       | `#292929` | Body text, headings (light mode)                  |
| Muted            | `#666`    | Secondary text, captions                          |
| Background       | `#fff`    | Page background (light mode)                      |
| Dark background  | `#292929` | Page background (dark mode), footer               |

Orange is the dominant brand color. It appears in CTAs, borders, the selection highlight, and any element that needs to feel like "us." Blue is a supporting color, not a competitor to orange. Use it for contrast and variety, not as a co-equal brand color.

### Typography

**Primary font:** Instrument Sans (Google Fonts), with system font fallbacks.

Headings use normal weight (400) at large sizes. This gives a clean, modern feel without heaviness. Body text is 16px base with 1.5 line height. The overall typographic tone is calm and readable, not aggressive or attention-seeking.

### Shape

- Card border radius: 20px
- Button border radius: 70px (pill shape)
- Input border radius: 70px

The rounded shapes soften the overall feel. Buttons should always be pills.

### Dark Mode

Full dark mode support is implemented. All colors have dark mode equivalents defined in `tokens.css`. Both modes should be tested when creating new components or pages.

---

## Editorial Voice

### Tone

**Calm, direct, and grounded.** We write like a senior engineer explaining something important to a peer — not like a salesperson, not like an academic, and not like a motivational speaker.

Specific qualities:

- **Plain language over jargon.** Say what you mean. If a technical term is needed, introduce it naturally with enough context that someone outside the field can follow.
- **Concrete over abstract.** Start with a specific situation, observation, or example. Earn the right to generalize by grounding the reader first. (Most people process concretely. Lead with experience and cause-effect before introducing frameworks.)
- **Honest about uncertainty.** "I think this is what's happening" is stronger than false confidence. "I could be wrong about this" is a feature, not a weakness.
- **Punchy and practical most of the time.** The default mode is "here's what's going on and what you might consider doing about it." Not every piece needs to be long. Say what needs saying and stop.
- **Room for depth when warranted.** Some topics (the PACP concept paper, the burnout series, the cath lab piece) deserve length and nuance. The reader should feel the length is earned, not padded.
- **Warm but not effusive.** We respect the reader's intelligence and time. No extravagant claims. No "This will revolutionize..." language. No exclamation points in prose.

### What We Sound Like

> "The cath lab is empty at 2 AM. It is empty at 10 PM. It is empty most of Saturday and all of Sunday. These are multimillion-dollar clinical spaces sitting dark for roughly three-quarters of every week. That is the fact."

> "I'm 66. I've been writing software for over thirty years. And I'm more capable today than I was five years ago. Not because I'm smarter, but because AI coding agents multiply the value of experience and judgment."

> "I welcome the pushback as much as the agreement. Both help."

### What We Don't Sound Like

- Marketing copy with bullet-pointed "benefits" and manufactured urgency
- Academic writing that hedges every claim into meaninglessness
- Consultant-speak that uses ten words where three would do
- Breathless AI hype ("revolutionary," "game-changing," "unprecedented")

### Avoiding AI-Generated Writing Tells

Content produced with AI assistance must still read as if a specific person wrote it. AI-generated text has recognizable patterns, and readers (especially sophisticated ones) will notice. Anyone producing content for this brand, including AI tools, should actively avoid the following.

**Overused AI vocabulary.** These words and phrases are so strongly associated with AI-generated text that they undermine credibility on contact: "delve," "dive into," "unpack," "navigate," "leverage," "harness," "foster," "empower," "elevate," "streamline," "cutting-edge," "game-changer," "paradigm shift." Also avoid the constructions "It's important to note that...," "It's worth noting that...," "In today's [X] landscape...," "At its core...," "This is where [X] comes in," and "Let's explore..." If any of these phrases appear in a draft, replace them with something a person would actually say.

**Structural tells.** AI text gravitates toward excessive formatting: too many headers, too many bullet points, too much bold text for content that would read better as prose. Watch for the "X. Here's why:" or "X. Here's how:" construction, which is nearly diagnostic. Lists of exactly three or five items with suspiciously parallel structure are another signal. Every paragraph wrapping up with a neat takeaway, or sections opening with a broad sweeping statement before narrowing ("In the ever-evolving world of..."), both read as machine-produced.

**Tone and rhythm problems.** AI writing tends toward relentless positivity without nuance, compulsive hedging that covers both sides of everything ("While X is important, Y is equally vital"), and formulaic transitions like "But here's the thing," "That said," and "The bottom line." It wraps up with inspirational calls to action that nobody asked for. Real writing has varied sentence rhythm, occasional roughness, and the willingness to land on one side of an argument.

**Content patterns.** AI text often restates the question before answering it, provides unsolicited caveats and disclaimers, and treats every topic as equally fascinating. It tends toward generic examples rather than specific ones drawn from actual experience. The antidote is specificity: real dates, real places, real observations, real opinions that a machine would not volunteer.

**The test.** Read the draft aloud. If it sounds like it could have been written about any company by any person for any audience, it fails. Our content should sound like John, or at minimum like someone who has done the specific work being described and has actual opinions about what they found.

### Engagement Posture

We actively invite scrutiny. The voice should convey: "I've thought carefully about this, I've shown my work, and I want to know where I'm wrong."

Standard patterns:

- "Help me check my thinking."
- "Your pushback is welcome here anytime."
- "I could be wrong about this."
- "Does this match what you see?"
- "I welcome the conversation."

This is not false modesty. It reflects a genuine epistemological stance: one person's analysis is always incomplete, and the best way to improve it is to expose it to people who see things differently. End pieces with an open hand, not a closed fist.

### Personal vs. Corporate Voice

Blog posts must be written in the first person. They come from a specific person with specific experiences, not from a faceless firm. If a post cannot be attributed to a specific human's experience, it should not be published as a blog post. Use "I" freely. Use "we" when referring to Common Sense Systems as an organization or when the reader is included ("we can see that...").

Occasionally a post may be primarily analytical rather than experiential, for example a deep read of a CMS report or an industry data set. If such a post is substantially generated by AI rather than written from personal experience, that must be clearly stated in the post itself (e.g., "This analysis was produced with significant AI assistance"). Transparency is non-negotiable.

The website's structural pages (Approach, About, Contact) can use "we" or third person as appropriate. Blog posts and concept papers should be unmistakably John's voice.

---

## Theory of Constraints Usage

TOC is central to our work and our credibility. Use it responsibly.

### Introducing TOC Terms

Never assume the reader knows TOC terminology. Introduce terms naturally with enough context that someone unfamiliar can follow. The first time a term appears in a piece, explain what it means in plain language.

Good: "In Theory of Constraints, an 'Evaporating Cloud' is a diagram that maps out a dilemma by showing two legitimate needs that appear to conflict. The power is in examining the assumptions that connect them."

Bad: "We applied the EC to identify the core conflict and challenged the injection."

### Key Terms and How to Use Them

- **Constraint:** The one thing that most limits the system's performance. Always clarify: "the constraint" means the bottleneck, the limiting factor, the thing that if improved would improve the whole system.
- **Evaporating Cloud (EC):** The conflict resolution tool. Explain the structure (common objective, two needs, two conflicting wants, hidden assumptions) when first used in a piece.
- **Current Reality Tree (CRT):** The cause-and-effect map that traces symptoms to root causes. Describe it as a logical map, not as a proprietary framework.
- **Undesirable Effects (UDEs):** The symptoms. Use "symptoms" or "chronic problems" as synonyms for readers unfamiliar with the term.
- **Throughput:** What the system produces that has value. In healthcare, this is patients completing their care journey successfully, not "billable codes submitted."

### TOC vs. Lean

When there are real contrasts between Lean and TOC, identify them fairly and directly. We are not anti-Lean. Lean has contributed enormously to operational thinking. But where the frameworks diverge, particularly on local optimization vs. global optimization and on the definition of value, we should be clear about the differences and why they matter.

A useful framing: Lean is strong at eliminating waste in known processes. TOC is strong at identifying which process to fix first. The distinction is problem-fit, not superiority. Most organizations undercommit to both. The honest observation is that most Lean and TOC implementations are more lip service than discipline, and we should say so when it is relevant rather than pretending everyone is doing either one well.

Example of fair treatment: the "Non-Value-Added Work" post, which credits Lean's definition of value as "a gift" while arguing that the three-category model (value-creating, enabling, waste) is more practical in regulated environments.

Do not set up Lean as a straw man. Do not dismiss it. Engage with it as a serious framework that has real limitations in specific contexts.

### Goldratt References

John studied under Goldratt directly. This is a meaningful credential. Reference it when relevant but don't overuse it. "Never say 'I know'" is Goldratt's principle and should be practiced, not just cited.

---

## Content Standards

### References and Evidence

Ground claims in verifiable evidence when the topic calls for it. Not every post needs footnotes, but analytical pieces and concept papers should cite sources. Use numbered footnotes for formal references. Link to original sources (not aggregators) when possible.

When citing data, prefer: peer-reviewed research, professional association reports (AHA, ACC), government data (CMS, BLS), established consulting benchmarks (Advisory Board, MedAxiom). Be skeptical of vendor-sponsored research.

When making claims from personal experience, be explicit: "In my experience..." or "I've seen this pattern in every organization I've worked with."

### Post Structure

There is no mandatory template. Different pieces call for different structures. But some patterns work well:

- **Open with a specific scene or observation.** The cath lab piece opens in a board meeting. The tax piece opens with "I'm doing my business taxes this year with AI coding agents. Not conceptually. Not as an experiment." Ground the reader immediately. The opening paragraph must contain a concrete noun: a person, a place, a specific report, a date, a number. If the first paragraph is all abstract concepts, rewrite it.
- **Earn your abstractions.** If you're going to introduce a framework or concept, establish the concrete problem first. The reader should be thinking "yes, I recognize this" before you name the pattern.
- **End with an open hand.** Invite engagement. Provide contact information. Don't end with a hard sell.

### Post Length

Match length to substance. A 400-word post that says one useful thing clearly is better than a 2,000-word post that pads a thin idea. A 6,000-word concept paper that develops a serious proposal is better than a series of short posts that fragment the argument.

As a rough guide:

- **Short posts (400-800 words):** One clear idea, one concrete example, done. Good for frameworks, observations, practical tips.
- **Standard posts (1,200-2,500 words):** Room to develop an argument with evidence and examples. Most analytical posts land here.
- **Long-form (3,000+ words):** Concept papers, series, deep analyses. Earn the length.

### CTAs and Contact

End posts with a low-pressure invitation. The standard patterns are:

- "You can reach me at john@common-sense.com."
- "If this resonates, I'd welcome the conversation."
- Link to `/contact` for more formal engagement.

The best closings connect the specific topic of the post to a concrete offer of help. Instead of a generic "let me know if you have questions," name the specific problem the reader might be stuck on and offer to think through it with them. This treats the reader as a peer, not a lead.

Good example (from the "Not All Waste Is Waste" post):

> "Distinguishing between true waste and protective capacity is rarely obvious. In fact, it is usually the hardest part of the analysis. If you are looking at a specific process in your system and aren't sure if it's waste or insurance, send me a note. I am happy to help you sanity-check your logic."

This works because it names the specific difficulty (waste vs. protective capacity), acknowledges that it is genuinely hard, and offers a concrete thing (sanity-checking the logic) rather than a vague invitation. It sounds like a colleague, not a sales funnel.

Do not end posts with formatted marketing CTAs, consultation-booking widgets, or multiple competing calls to action. Do not use styled boxes, colored backgrounds, or visual treatments that separate the closing from the rest of the prose. The tone and presentation of the ending should match the tone and presentation of the writing.

### Headlines

Headlines should be specific and concrete. They should tell the reader what the piece is about, not tease them.

Good: "The Cath Lab Is Empty at 2 AM"
Good: "Cancel Your SaaS, Keep Your Data"
Good: "Stop Hiring Your Way Out of a Process Problem"

Bad: "The Surprising Truth About Hospital Efficiency"
Bad: "What Nobody Tells You About AI"
Bad: "5 Ways to Transform Your Organization"

### Tags

Use title case for all tags: `Healthcare`, `Strategy`, `Theory of Constraints`, not `healthcare`, `strategy`. Tags should be consistent across all posts.

Current active tags (add new ones sparingly):

Healthcare, AI, Strategy, Leadership, Operations, Theory of Constraints, Decision-Making, Wellbeing, Analysis, Culture, Lean, Systems, MedTech, R&D, Systems Engineering, Quality, Regulatory, Workforce, Patient Flow, Labor Relations, Agency, Constraint Resolution, Frameworks, Practical Tips, Small Business, Cost Reduction, Delivery, Agile, Outcomes, Architecture, Networking, Sales

### Frontmatter

Every blog post requires: `title`, `description`, `metaTitle`, `metaDescription`, `date`, `author`, `tags`. No other fields should be added without discussion. Drafts get `draft: true`. Published posts should not include the `draft` field.

### Search, Social, and Structured Data

We want search engines, AI systems, and social platforms to understand our content accurately. The goal is not to game rankings. It is to describe what we have written clearly enough that the right people find it. This means doing the basics well and being thorough about metadata.

#### Meta Titles and Descriptions

Every page has two title-related fields in its frontmatter: `title` and `metaTitle`. They serve different purposes.

- **`title`** is the display headline the reader sees on the page. It can be conversational, punchy, or provocative. Example: "The Cath Lab Is Empty at 2 AM."
- **`metaTitle`** is what appears in browser tabs, search result listings, and social cards. It should be clear and descriptive even out of context, and should include the brand name. Example: "The Cath Lab Is Empty at 2 AM | Common Sense Systems." Keep it under 60 characters when possible. Front-load the important words; search engines and users both prioritize what comes first.

Similarly, `description` is the short summary shown on the blog listing page, while `metaDescription` is the snippet search engines may display in results.

- **`metaDescription`** should be 140-160 characters, written as a plain sentence (not a keyword list), and should tell a searcher what they will get if they click. It should address the reader's intent: what question does this piece answer, or what will they learn?
- Write each `metaDescription` individually. Never duplicate descriptions across posts. If you do not have time to write one, leave it blank; Google will pull a snippet from the page content, which is better than a generic placeholder.
- Include relevant terms naturally, but do not stuff keywords. Google bolds matching query terms in descriptions, which helps with click-through, but only if the description reads like a real sentence.

Good: `metaDescription: "Hospitals lose $25-40M annually on patients stuck in beds after being medically cleared. Here is how to find and fix the structural causes."`

Bad: `metaDescription: "Healthcare consulting hospital efficiency patient flow optimization Theory of Constraints AI analysis."`

#### Open Graph and Social Sharing

Every page should include Open Graph meta tags (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`) so that links shared on LinkedIn, Twitter/X, and other platforms render with a proper preview card. For blog posts, `og:type` should be `article`. For structural pages (About, Approach, Contact), use `website`.

The `og:image` should be at least 1200x630 pixels for good rendering across platforms. Our build pipeline auto-generates OG images for blog posts; verify they render correctly when sharing.

Also include Twitter card meta tags (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`). Use `summary_large_image` as the card type for posts with OG images.

#### JSON-LD Structured Data

We use JSON-LD (JavaScript Object Notation for Linked Data) to provide structured data to search engines and AI systems. Google recommends JSON-LD over Microdata or RDFa because it is easier to maintain and less error-prone. The markup lives in a `<script type="application/ld+json">` block in the page `<head>`, separate from the visible HTML.

The following schema types are relevant to our site:

- **`Organization`** (site-wide): Name, URL, logo, founding date, contact information, and `sameAs` links to official profiles (LinkedIn, GitHub, etc.). This establishes Common Sense Systems as a recognized entity.
- **`Person`** (author pages or site-wide): John Sambrook as the principal author, with name, URL, job title, and affiliation to the Organization.
- **`BlogPosting`** (every blog post): Headline, author (linked to the Person), datePublished, dateModified, description, image, publisher (linked to the Organization), and mainEntityOfPage. This is the schema type Google uses for blog content and can enable enhanced search result displays.
- **`BreadcrumbList`** (site-wide): Helps search engines understand site hierarchy and can display breadcrumb trails in search results.

Key rules for structured data:

- The structured data must reflect what is actually on the page. Do not mark up content that the user cannot see.
- Use the most specific schema type available. Blog posts should use `BlogPosting`, not the generic `Article`.
- Include all required properties for each type. For `BlogPosting`, that means at minimum: `headline`, `author`, `datePublished`, and `image`.
- Add recommended properties when the data is available: `dateModified`, `description`, `publisher`.
- Validate structured data using Google's Rich Results Test (https://search.google.com/test/rich-results) after adding or changing markup.
- Structured data is not "set and forget." When templates change or new page types are added, re-validate.

#### Canonical URLs

Every page should include a `<link rel="canonical">` tag pointing to its preferred URL. This prevents duplicate content issues if the same page is accessible at multiple URLs.

#### Sitemap and Robots

Maintain an up-to-date XML sitemap that includes all published pages and posts. The sitemap should be submitted to Google Search Console. The `robots.txt` file should allow crawling of all public content.

#### What We Do Not Do

- No keyword stuffing in any metadata field.
- No hidden text, cloaked content, or structured data that does not match page content.
- No doorway pages or thin content created for search ranking purposes.
- No purchasing of links or participating in link schemes.
- No obsessing over exact character counts. The length guidelines above are practical targets, not rigid rules. Clarity and accuracy matter more than hitting a number.

Our SEO philosophy matches our editorial philosophy: produce strong, useful content, then describe it honestly to the systems that index it.

### Images

Blog post OG images are auto-generated by the build pipeline. Custom images should match the existing style. No stock photography. No generic "business people shaking hands" imagery.

---

## Industry Positioning

### Cross-Domain, Not Single-Industry

The website should communicate that our methods work across industries. Healthcare is our deepest current vertical, but the intellectual framework is universal. Ways to reinforce this:

- The About page and Approach page should reference multiple domains (healthcare, government, manufacturing, technology, embedded systems).
- Blog posts from non-healthcare domains (MedTech, R&D, small business operations) demonstrate range.
- TOC concepts should be explained in domain-neutral terms first, then applied to specific contexts.
- Avoid language that implies we only work in healthcare ("our healthcare practice," "as a healthcare consulting firm"). Prefer: "we work with complex organizations" or "our current healthcare work."

### Healthcare Depth

Healthcare is where the deepest, most developed work lives. The PACP concept paper, the burnout series, the cath lab piece, the complex discharge analysis — these demonstrate genuine domain expertise. This depth is an asset, not a limitation, as long as the site also shows the methodology working in other contexts.

### The "Outsider" Advantage

John is not a healthcare insider and should not pretend to be. The value proposition is precisely that an outsider with systems discipline sees things that insiders, constrained by tribal assumptions, cannot. This should be communicated with respect: the insiders are smart, experienced, and dedicated. The outsider brings a different lens, not a superior one.

---

## Writing Checklist

Before publishing, check:

- [ ] Does the opening ground the reader in something concrete?
- [ ] Are TOC terms introduced with enough context for a newcomer?
- [ ] Is the length earned by the substance?
- [ ] Does the piece end with an open hand, not a hard sell?
- [ ] Are claims grounded in evidence or explicitly marked as personal experience?
- [ ] Would a hospital commissioner and a small business owner both find this credible?
- [ ] Are tags title-cased and consistent with existing tags?
- [ ] Does the frontmatter have all required fields?
- [ ] Has the piece been read aloud to check for natural flow?
- [ ] Is the draft free of AI writing tells (see "Avoiding AI-Generated Writing Tells" above)?
- [ ] Are `metaTitle` and `metaDescription` written individually for this post (not duplicated or left generic)?
- [ ] Does the opening paragraph contain at least one concrete noun (person, place, report, date, number)?

---

## AI Content Production Protocol

We use AI tools extensively in producing content. This is not a secret and not a problem. The problem is when AI produces content that does not sound like it came from a person who did the work. This section defines how to use AI well.

### The Core Rule

AI is an editor and a refiner. It is not a ghostwriter. Never prompt an AI with "Write a blog post about X." The AI cannot generate John's voice, John's observations, or John's specific experience from a topic sentence. It will produce generic content marketing, which is exactly what we are trying to avoid.

### What the AI Needs as Input

Every AI-assisted post must start with raw material that contains at least two of the following:

- **A specific anecdote or observation.** Something John saw, heard, or did. A board meeting exchange. A conversation with a commissioner. A pattern noticed across three client engagements. A number from a report that surprised him.
- **An argument with a direction.** Not "discuss the pros and cons of X" but "I think X is wrong because Y, and here's what I'd do instead." The AI can sharpen the argument, but it cannot invent the position.
- **A concrete example grounded in time and place.** "At the February 2026 EvergreenHealth board meeting, cardiology cited space as their growth constraint. But the cath lab sits empty 75% of the week. The real constraint is staffing."

Acceptable forms of raw input include: a conversation transcript with AI where John talks through the idea, a voice memo transcription, typed bullet points with specific details, a messy first draft, or an email John wrote to someone that contains the core argument.

What is not acceptable: a topic and a request to generate a post. A list of keywords. A competitor's article with "write something like this." An outline with no specifics.

### The Workflow

1. **John provides raw material.** This is the irreplaceable step. The raw material contains the experience, the opinions, and the specific observations that make the content worth reading. It does not need to be polished. It needs to be real.

2. **AI organizes and drafts.** The AI structures the raw material into a post, following the brand guidelines for tone, structure, and formatting. It should push back if the material is too abstract, if there is no concrete opening, or if the argument is unclear. It should ask questions rather than fill gaps with generic filler.

3. **Iterative refinement.** John and AI go back and forth. The AI should flag when writing is getting abstract, when it is hedging too much, when it sounds defensive, or when it has drifted into AI-tell patterns. John should feel free to say "that sounds like AI wrote it" and the AI should fix it without taking offense.

4. **Pre-flight check.** Before the post is considered done, run through the Writing Checklist above. Specifically: search for banned AI vocabulary (a simple Ctrl+F pass through the banned word list is sufficient), verify the opening contains a concrete noun, and read the piece aloud.

### What the AI Should Do During Drafting

- **Ask for specifics when the input is vague.** "You mentioned hospitals waste money on this. Can you give me a number or a specific example?"
- **Push back on abstraction.** "This paragraph is all framework. Can you ground it in something you actually saw?"
- **Flag defensive writing.** If the draft is explaining why we are credible instead of demonstrating it through the work, say so.
- **Resist the urge to pad.** If the raw material supports 800 words, write 800 words. Do not inflate to 1,500 because longer feels more substantial.
- **Maintain John's sentence rhythm.** Short sentences mixed with longer ones. Occasional fragments. Direct address. Not every paragraph needs a topic sentence. Not every section needs a transition.
- **Preserve rough edges.** Real writing has personality. If John's phrasing is slightly unusual but clear, keep it. Do not smooth everything into bland fluency.

### What the AI Should Not Do

- Generate opinions John has not expressed.
- Invent anecdotes or attribute experiences John did not describe.
- Add unsolicited frameworks, analogies, or metaphors.
- Produce a complete draft from a one-sentence prompt.
- Pad thin material with filler paragraphs, especially "why this matters" sections that add no information.
- Use any word or phrase from the banned list in the "Avoiding AI-Generated Writing Tells" section.

### Attribution

If a post is substantially written by John from his own experience and refined with AI assistance, no special attribution is needed. This is the normal workflow and the reader can assume it.

If a post is primarily analytical and the AI did most of the drafting (for example, summarizing a data set or synthesizing multiple sources), the post must include a clear statement of AI involvement. Place it naturally, not as a disclaimer buried in a footnote. Example: "This analysis was produced with significant AI assistance. The data sources and conclusions are mine; the prose was drafted collaboratively with Claude."
