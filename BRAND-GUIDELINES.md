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

| Token | Hex | Usage |
|-------|-----|-------|
| Primary (Orange) | `#fe811b` | Brand accent, buttons, links, selection highlight |
| Secondary (Blue) | `#155dfc` | Supporting accent, charts, secondary actions |
| Foreground | `#292929` | Body text, headings (light mode) |
| Muted | `#666` | Secondary text, captions |
| Background | `#fff` | Page background (light mode) |
| Dark background | `#292929` | Page background (dark mode), footer |

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

John writes in first person. The blog posts are personal — they come from a specific person with specific experiences, not from a faceless firm. Use "I" freely. Use "we" when referring to Common Sense Systems as an organization or when the reader is included ("we can see that...").

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

When there are real contrasts between Lean and TOC, identify them fairly and directly. We are not anti-Lean. Lean has contributed enormously to operational thinking. But where the frameworks diverge — particularly on local optimization vs. global optimization, and on the definition of value — we should be clear about the differences and why they matter.

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

- **Open with a specific scene or observation.** The cath lab piece opens in a board meeting. The tax piece opens with "I'm doing my business taxes this year with AI coding agents. Not conceptually. Not as an experiment." Ground the reader immediately.
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

Do not end posts with formatted marketing CTAs, consultation-booking widgets, or multiple competing calls to action. The tone of the ending should match the tone of the writing.

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

### Images

Blog post OG images are auto-generated by the build pipeline. Custom images should match the existing style. No stock photography. No generic "business people shaking hands" imagery.

---

## Industry Positioning

### Cross-Domain, Not Single-Industry

The website should communicate that our methods work across industries. Healthcare is our deepest current vertical, but the intellectual framework is universal. Ways to reinforce this:

- The About page and Approach page should reference multiple domains (healthcare, manufacturing, technology, embedded systems).
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
