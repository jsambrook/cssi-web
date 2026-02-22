---
title: 'I Fired My SEO Expert (And Hired Claude Code Instead)'
description: "A small business owner's account of running a complete SEO audit with an AI coding agent in one session, fixing every issue the same afternoon, and what it means for the $80 billion SEO industry."
metaTitle: 'I Fired My SEO Expert (And Hired Claude Code Instead)'
metaDescription: 'How a small business owner ran a full SEO audit with Claude Code, fixed every issue the same day, and cut a $1,000/month expense to zero.'
date: 2026-02-21
author: 'John Sambrook'
tags: ['AI', 'Practical Tips', 'Small Business', 'Cost Reduction']
---

This afternoon I ran a full Googlebot-perspective SEO audit of my business website. Not a summary. Not a surface-level checklist. A line-by-line review of every meta tag, every JSON-LD block, every sitemap entry, and every RSS field across all 36 pages and 25 blog articles.

It took one session with Claude Code. The audit found eight specific failings. I fixed all of them the same afternoon. Total cost: my Claude Code subscription, which I was already paying for.

For context, a comparable audit from an SEO agency runs $2,000 to $5,000. A monthly retainer for ongoing SEO work runs $1,000 to $3,000. And in my experience, the deliverable is usually a PDF full of screenshots from Screaming Frog and Ahrefs, with recommendations you then have to implement yourself or pay someone else to implement.

I got the audit _and_ the implementation in a single sitting.

## What the Audit Actually Found

Claude Code read the raw HTML of every page in my build output -- the actual markup that Googlebot sees. Not a crawl report. Not a third-party tool's interpretation. The actual `<meta>` tags, `<title>` elements, JSON-LD scripts, and sitemap XML.

Here's what it found working well: strong meta tags on every page, unusually detailed JSON-LD structured data (Organization, ProfessionalService, BlogPosting, Person schemas with links to Wikipedia and Wikidata), proper canonical URLs, full Open Graph and Twitter Card coverage, RSS feed, XML sitemap, accessibility fundamentals.

Here's what it found broken. I'm going to show you the actual HTML so you can check your own site for the same problems.

### Truncated Meta Descriptions

Five pages had descriptions that ended with "..." in the actual HTML. Right-click View Source on your own homepage and search for `<meta name="description"`. Here's what mine looked like:

```html
<meta
  name="description"
  content="Break bottlenecks and accelerate throughput
in Healthcare, MedTech, and Embedded Systems. We design 'Mafia Offers' and
operational interventions for..."
/>
```

See that trailing "..."? That's what Google renders in your search result. Your meta description is the ad copy for your page in the SERP, and mine ended mid-sentence. Google doesn't fix this for you. It prints exactly what you give it.

The cause was simple: my descriptions were over 155 characters, and a utility function was truncating them with an ellipsis. Nobody had ever checked the built HTML to see what Google actually received.

Claude Code rewrote all five. Here's the homepage after:

```html
<meta
  name="description"
  content="Theory of Constraints consulting that breaks
organizational bottlenecks. We find the constraint, design the fix, and scale
the flow. Kirkland, WA."
/>
```

146 characters. Complete sentence. Keywords up front. No ellipsis. Go check yours right now -- you might be surprised.

### Missing Sitemap Timestamps

Open your sitemap (usually at `yoursite.com/sitemap.xml` or `sitemap-index.xml`). Here's what my static pages looked like:

```xml
<url><loc>https://common-sense.com/</loc></url>
<url><loc>https://common-sense.com/about/</loc></url>
<url><loc>https://common-sense.com/approach/</loc></url>
```

No `<lastmod>`. Now compare that to my blog posts, which had dates:

```xml
<url>
  <loc>https://common-sense.com/insights/physics-of-patient-flow/</loc>
  <lastmod>2025-09-04T00:00:00.000Z</lastmod>
</url>
```

Google uses `<lastmod>` to decide how often to recrawl a page. Without it, your homepage -- the most important page on your site -- gets no priority signal. Google might recrawl your three-year-old blog post more often than your homepage simply because the blog post has a date and the homepage doesn't.

Most small business websites I've looked at have this problem. Check yours.

### Inconsistent Title Tags

View Source on any of your blog posts and look at the `<title>` tag. Then do the same on your About or Contact page. Here's what mine looked like:

Blog post: `<title>The Physics of Patient Flow</title>`

About page: `<title>About John Sambrook | Common Sense Systems</title>`

Every non-blog page had the brand suffix. Blog posts didn't. That means when someone shares your best article on LinkedIn, your company name doesn't appear in the link preview title. You're giving away brand impressions on exactly the content people are most likely to share.

### Bare-Bones Structured Data Where It Matters Most

This one requires looking at the JSON-LD in your page source (search for `application/ld+json`). My homepage had five rich JSON-LD blocks: Organization, WebSite, WebPage, ProfessionalService with geographic coverage and service catalogs, and a detailed OfferCatalog. That's excellent.

But my industry landing pages -- the pages I built specifically to rank for "healthcare consulting" and "tech consulting" searches -- had only a basic WebPage schema. No ProfessionalService. No service descriptions. No geographic coverage. The pages I cared about most for search had the weakest structured data.

Most business websites I've looked at have little or no JSON-LD at all. If you search your page source for `ld+json` and find nothing, that's a significant missed opportunity. Structured data is how you tell Google exactly what your business does, where you operate, and what services you offer -- in a format it can directly consume.

There were four more findings beyond these. Each was specific, evidence-based, and actionable.

## From Audit to Fix in Minutes

This is the part that would be impossible with a traditional SEO engagement.

A conventional SEO audit is a _deliverable_. You receive it, read it, put it in a queue, and eventually implement the recommendations -- or more likely, you forward it to your developer and wait for their sprint cycle. The gap between "identified" and "fixed" is typically weeks to months.

With Claude Code, the gap is minutes. We went from "your meta descriptions are truncated" to "here are five rewritten descriptions, all under 155 characters, all ending with complete sentences" in a single conversation turn. I reviewed them, gave feedback (I wanted industry-neutral language on the homepage instead of listing specific verticals), and Claude Code revised them. Then it edited the source files, ran the build, and verified that no description in the built HTML contained an ellipsis.

The sitemap fix was more interesting. The static pages needed `<lastmod>` dates, but I didn't want to hardcode them -- that's one more thing to remember to update. Claude Code wrote a solution that reads the git commit history at build time. Every page's `<lastmod>` now reflects the most recent commit that touched its source files. When I edit a page and push, the sitemap date updates automatically. Zero maintenance.

That's not an SEO recommendation. That's a working implementation, tested, committed, and deployed in the time it would take most agencies to schedule a kickoff call.

## The Economics

Let me be concrete about what this costs.

A typical SEO retainer for a small business: $1,000 to $3,000 per month. For that, you get a monthly report, some keyword research, maybe a few content suggestions, and recommendations that still need to be implemented. You're locked into a contract. The agency is incentivized to keep you dependent, not to make you self-sufficient.

A Claude Code subscription: $200 per month. For that, I get an SEO expert, a developer, a copywriter, and a QA tester -- all available instantly, at 2 PM on a Friday, with no scheduling friction and no billable-hour clock running.

I'm not exaggerating when I say the entire audit-and-fix cycle I described above happened between lunch and dinner. Try getting that turnaround from an agency.

## What Makes This Different from SEO Tools

You might be thinking: there are already SEO tools that do audits. Screaming Frog, Ahrefs, SEMrush, Sitebulb. I've used them. They're good at what they do. But what they do is generate reports.

Here's the difference. When Ahrefs tells you "5 pages have meta descriptions over 155 characters," you still need to:

1. Open each page's source file
2. Figure out where the description is defined (is it in the template? A data file? A CMS field?)
3. Write a better description that's under the limit
4. Verify it reads well as SERP ad copy
5. Rebuild and check the output
6. Repeat for each page

Claude Code does steps 1 through 6. It understands the codebase. It knows that my descriptions live in TypeScript data files, not in the Astro templates. It knows the `toSeoDescription()` utility truncates at 155 characters. It writes descriptions that are actually good -- not just short enough, but compelling, keyword-targeted, and consistent with the brand voice. Then it edits the files, builds the site, and verifies the fix.

An audit tool tells you what's wrong. An AI agent fixes it.

## The Vertical Integration Pattern

This is now the third article I've written about using AI coding agents to bring capabilities in-house. The [first was about canceling SaaS subscriptions](/insights/saas-subscriptions-ai-coding-agents/). The [second was about doing my own taxes](/insights/doing-taxes-with-ai-coding-agents/). This one is about replacing an SEO consultant.

The pattern is the same every time: a recurring expense for a service that used to require specialized expertise, replaced by a conversation with an AI agent that has that expertise built in. Not because the expertise isn't real -- it absolutely is. But because the delivery mechanism has changed.

SEO knowledge hasn't gotten less valuable. What's changed is that you no longer need a human intermediary to access it. The knowledge is embedded in the model. You just need to know enough about your own business to direct the conversation and evaluate the results.

This is vertical integration in the truest sense. I'm not outsourcing SEO to a cheaper provider. I'm bringing the capability inside my business, where it executes faster, costs less, and compounds with every other capability I've already built this way.

## What I'd Tell Other Small Business Owners

If you're paying for SEO services and you're comfortable working with AI tools, try this experiment. Ask Claude Code (or whatever AI coding agent you prefer) to audit your website the way Googlebot sees it. Tell it to read the actual HTML, not summarize from a web fetch. Tell it to check your meta tags, structured data, sitemap, and RSS feed. Ask for specific findings with evidence.

You'll get an audit as thorough as anything a $3,000 agency delivers. And then, unlike the agency report, you can fix everything in the same session.

You don't need to be a developer. You need to be able to read the findings and decide which ones matter for your business. The AI handles the implementation. That's the skill shift that's happening right now: from _knowing how to operate specialized tools_ to _knowing what good looks like and being able to direct the work_.

Every month you keep paying for expertise that's available on demand through AI is a month of unnecessary expense. Not because the experts are wrong. Because the delivery model is obsolete.

---

If this interests you and you'd like to talk about it, I'd welcome the conversation. Or send me your website address -- I'll run a free review and show you what Googlebot actually sees when it crawls your site. No pitch, no obligation. You can reach me at [common-sense.com/contact](https://common-sense.com/contact).
