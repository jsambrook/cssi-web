---
title: "I Woke Up Worried About a Denied Insurance Claim. Fifteen Minutes Later, I Wasn't."
description: "How I used Claude Code to turn a confusing insurance denial into a clear, organized answer -- and why I'm building an AI-managed insurance filing system for everything."
metaTitle: 'Insurance Denial Resolved Before Coffee | Common Sense Systems'
metaDescription: 'Woke up to a $1,316 insurance denial. Claude Code cross-referenced the EOB with my policy and explained the whole picture in three minutes. Here is the pattern.'
date: 2026-03-17
author: 'John Sambrook'
tags: ['AI', 'Practical Tips', 'Small Business']
imageAlt: 'A neat, well-organized filing cabinet contrasted with a messy pile of insurance paperwork'
---

## TL;DR

I woke up to a confusing insurance denial that looked like I owed over $1,000. Claude Code cross-referenced the EOB with my policy documents and explained the whole picture in three minutes. Turns out I owed nothing beyond what I was already paying. The same repo pattern I use for my business finances now manages my personal insurance.

---

<img src="/images/content/insurance-denial-filing-hero.webp" alt="A neat, well-organized filing cabinet contrasted with a messy pile of insurance paperwork" width="1408" height="768" loading="lazy" decoding="async" />

## 4:30 AM, phone buzzing

I woke up early this morning to a notification from Aetna. An Explanation of Benefits had come through for a dental visit where I had some cavities filled. Six of the eight line items said DENIED. The "Your Share" column added up to $1,316.

I was already annoyed that the dental work had cost $730 out of pocket. Now it looked like I owed another $600 on top of that. At 4:30 in the morning, staring at a phone screen, that is not a pleasant discovery.

Fifteen minutes later I got up, made coffee, and sat down at my workstation. But I didn't call the insurance company. I didn't start Googling dental codes. I opened a terminal.

## The pattern

Over the past few months, I have been [managing my small business finances](/insights/fired-quickbooks-built-something-better) with Claude Code and a Git repository. The approach is simple: I create a repo with a few key files -- a CLAUDE.md that tells Claude how the repo is organized, a schema that defines where documents go and how they're named, a journal for tracking what's happened, and a README that explains the whole system.

This pattern has worked so well for my business that I decided on the spot to do the same thing for my personal insurance. I created a new repo called john-insurance. Set up the CLAUDE.md, the schema, the journal. Created directories for health insurance, auto insurance, and homeowners insurance.

The whole setup took about 15 minutes and one cup of coffee.

## The analysis

With the repo in place, I dropped in the EOB document and my insurance policy documents. Then I asked Claude Code a simple question: look at this denied claim and tell me what's actually going on.

About three minutes later, Claude printed a summary that laid out the entire situation clearly. Here is what it found:

Two claims had been submitted for my dental visit. The first was for preventive and diagnostic services -- a cleaning and an evaluation. Those were covered. The second was for restorative work -- three composite fillings. Those were denied, along with a fluoride treatment, a pre-diagnostic, and a panoramic x-ray.

The reason was straightforward: my dental plan covers preventive services but explicitly excludes "comprehensive dental services." Fillings, panoramic x-rays, and fluoride varnish fall into the comprehensive category. The denial wasn't a mistake or an error in coding. It's simply what my plan covers and doesn't cover.

But here's the part that mattered most, and the part I would not have figured out easily on my own: the EOB's "Your Share" column showed $1,316, which is the full billed amount for all the denied services. But my dentist is in Aetna's network. That means they bill at the contracted rate, not the full rate. The actual amount I owe is $723.83 -- the number my dentist had already quoted me and that I was already paying off on a four-payment plan.

In other words, I didn't owe a penny more than I thought. The EOB was accurate but misleading if you didn't understand the difference between billed amounts and contracted rates. Claude understood that difference. At 5 AM, I did not.

<img src="/images/content/insurance-denial-claude-analysis.webp" alt="Claude Code terminal output showing a detailed insurance claim analysis with two claims broken down by service, Aetna's coverage decision for each line item, and an explanation of why the billed amounts differ from the contracted rates" width="1024" height="1310" loading="lazy" decoding="async" />

## What changed

There are a few things about this experience that I think are worth sharing.

_The anxiety dissolved almost immediately._ I went from "I might owe over a thousand dollars I wasn't expecting" to "everything is fine, this is just how EOBs work" in about three minutes. That shift happened because I had an assistant that could read the EOB, cross-reference it with my policy documents, and explain the whole picture in plain language.

_I'm now on equal footing with my insurance company._ Insurance policies are written in language that is technically precise but practically opaque. EOBs use terminology and formatting that create confusion. This is not always intentional, but the effect is the same: the insurance company understands your policy better than you do. That asymmetry has real consequences. People overpay. People don't appeal when they should. People accept denials that aren't legitimate. Having an AI that can read and cross-reference these documents puts the informational advantage back in your hands.

_My important documents are now organized and accessible._ Every EOB, every policy document, every piece of correspondence is filed in a structured, searchable system. The schema tells Claude where things go and how to name them. I can drop a new document into a "to be filed" folder, and Claude will read it, figure out what it is, and file it in the right place with the right name. No intervention needed.

_It connects to my email._ Claude Code can use Gmail tooling that I've set up, which means it can search my inbox, read messages, and send emails on my behalf. You can see this in the screenshot -- after completing its analysis, Claude offered to draft an email to my dentist's office. That's the whole loop: a document arrives, Claude reads and files it, analyzes the situation, and can act on it by sending correspondence. I'm not copying and pasting between five different apps. It's one conversation.

_This is a gift to whoever comes after me._ I'm 66. Sometime -- hopefully far in the future -- someone else is going to need to sort through my affairs. When that day comes, they won't find a drawer full of envelopes and a filing cabinet stuffed with papers in no particular order. They'll find an organized repository with a README that explains everything.

## What's next

I set up placeholder directories for my auto insurance and homeowners insurance. I plan to populate those the same way -- drop in the policy documents, let Claude build the picture. Once that's done, I'll have structured, comparable data across all my insurance coverage.

That means I can do something I've never been able to do efficiently: shop for better rates with real comparisons. Not "this company quoted me $X and that one quoted me $Y." Actual apples-to-apples comparisons of coverage limits, deductibles, exclusions, and total cost. I can have agents compete for my business, and I can verify their claims against the actual policy language.

I am genuinely looking forward to reviewing my auto insurance. That is not a sentence I ever expected to write.

## This is something I can help you do

I do not think there is anything particularly magical about what I'm doing here. The pattern is simple: structured repo, clear schema, good instructions for the AI, and then just asking it questions in plain English.

The part that takes some experience is the initial setup -- knowing how to structure the repo, what to put in the CLAUDE.md, how to write a schema that's specific enough to be useful. That's what I've been refining over months of doing this for my business.

If you're a small business owner, a sole proprietor, or just someone who wants to stop dreading insurance paperwork, I can sit down with you for an hour or two and help you set this up for yourself. You don't need to be technical. You don't need to know how to code. If you can have a conversation, you can use these tools.

The tools are available today. Claude Code is one option. Anthropic's Claude with the Co-Work feature is another that doesn't require any command-line experience at all. The important thing isn't which tool you use. It's the pattern -- the scaffolding that turns a general-purpose AI into a personal assistant that knows your documents, understands your situation, and can answer your questions in seconds.

I want other people to experience the sense of freedom and control and peace of mind that I got this morning. Being able to wake up to a confusing insurance denial and resolve it before my coffee got cold -- that changes your relationship with these institutions. It puts the power where it belongs: in your hands.

---

_John Sambrook is the principal of Common Sense Systems, Inc. in Kirkland, Washington. Reach him at john@common-sense.com._
