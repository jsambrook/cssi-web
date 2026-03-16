---
title: 'I Fired QuickBooks. Then I Built Something Better in Twenty Minutes.'
description: 'Replacing a $150/month accounting platform with open-source tools and AI revealed something bigger: the build-vs-buy calculus has shifted, and most of us have not caught up.'
metaTitle: 'I Fired QuickBooks and Built Something Better | Common Sense Systems'
metaDescription: 'Replaced QuickBooks with Beancount and Claude Code, saving $1,800/year. The real lesson: vertical integration for small business is now free.'
date: 2026-03-16
author: 'John Sambrook'
tags: ['AI', 'Small Business', 'Cost Reduction', 'Strategy', 'Practical Tips']
imageAlt: 'A small business owner at a desk with a simple terminal replacing a stack of SaaS subscription invoices, showing the shift from renting software to owning capability'
---

## TL;DR

I replaced QuickBooks with an open-source accounting system called Beancount, built a custom invoicing system in twenty minutes using Claude Code, and now pay $0/month for better accounting software than I had before. The specific tools matter less than the pattern: when building is this cheap, renting starts to look like a bad habit.

---

<img src="/images/content/fired-quickbooks-rent-build-own.webp" alt="Infographic showing four steps from renting software to owning capability: Rent (pay monthly for tools you don't control), Build (describe what you need, get working software), Integrate (own your data, own your workflow), Resilience (no vendor lock-in, no dependency)" width="1408" height="768" loading="lazy" decoding="async" />

Last week I sat down at my computer to continue a project I had been putting off for months: replacing QuickBooks. I had been paying Intuit about $150 a month for their online accounting platform. That comes out to $1,800 a year for software that has frustrated me for as long as I have used it.

I am not going to catalog every frustration. If you have used QuickBooks, you already have your own list. If you have not, count yourself lucky. The point is that I kept paying because I assumed the alternative -- setting up something different -- would be worse than the monthly irritation. That assumption turned out to be wrong, and in an interesting way.

## What Actually Happened

I moved my books to [Beancount](https://beancount.github.io/), an open-source, plain-text accounting system. Beancount stores everything in a simple text file. Double-entry bookkeeping, same as QuickBooks, but the data is mine in a format I can read, edit, search, and version-control. No database. No cloud subscription. No vendor lock-in.

The transition itself was straightforward, but the interesting part came when I needed to replace the things QuickBooks did beyond basic bookkeeping. Invoicing, for instance.

I opened Claude Code and said, roughly: "Generate an invoice for Jones Enterprises for $300 for AI consulting." Twenty minutes later I had a working invoicing system that produces clean PDF invoices and writes the corresponding entries directly into my Beancount ledger. Not a prototype. Not a hack. A working tool that I use daily.

A few months ago, my assumption would have been that building a custom invoicing system was a significant project -- days of work, at minimum. The kind of thing where you look at the effort, look at the $150/month, and decide the subscription is the lesser evil. That assumption was a relic. I just had not tested it recently.

## This Is Not About QuickBooks

The QuickBooks story is a good example because the numbers are tangible. $1,800 a year, recovered. Twenty minutes of setup. That math is hard to argue with.

But the more interesting thing is the pattern. Over the past several months, I have been [systematically canceling SaaS subscriptions](/blog/saas-subscriptions-ai-coding-agents) -- at least ten so far -- replacing each with tools I built, own, and control. I [prepared my own S-Corp tax filings](/blog/doing-taxes-with-ai-coding-agents) using AI coding agents. Each time, I find the same thing: the work that used to justify the subscription takes a fraction of the time it once did.

What I am actually doing, whether I planned it this way or not, is vertically integrating.

## Vertical Integration at Micro Scale

Vertical integration is usually a big-company concept. When a manufacturer buys its supplier, or a health system acquires a physician practice, that is vertical integration. The logic is straightforward: if you control more of your value chain, you reduce dependency, capture more margin, and gain flexibility.

The reason small businesses and solo operators have not historically done this is cost. Building your own tools, running your own infrastructure, maintaining your own systems -- all of that required more time and expertise than it was worth. So we rented. We subscribed. We outsourced. And we accepted the trade-offs: monthly fees, vendor lock-in, someone else's workflow imposed on our business.

What has changed is that the cost of building collapsed. Not gradually. Dramatically. When I can describe what I need in plain English and have working software in twenty minutes, the entire economic argument for renting commodity tools falls apart.

And it is not only the initial build. When something needs to change -- a new field on an invoice, a different tax calculation, a report I have not thought of yet -- I describe the change and it happens. No support tickets. No waiting for the vendor's product roadmap. No workarounds.

## Capital Efficiency and the Resilience Dividend

There is another dimension to this that goes beyond saving $150/month.

I recently set up a Mac Studio specifically to run open-source AI models locally. That is a capital expenditure -- a one-time purchase of hardware -- that replaces what would otherwise be an ongoing dependency on cloud-based AI services. I still use cloud services when they are the best tool, but I am no longer entirely dependent on them. If a provider changes pricing, changes terms, or goes down for a day, my core operations continue.

This is the same logic that drives large organizations to invest in owned infrastructure rather than renting everything. Capital expenditures that reduce recurring costs and increase operational independence are, dollar for dollar, among the highest-value investments a business can make. The difference is that this used to require significant scale to justify. It does not anymore.

For a small business, the math looks like this: a few thousand dollars in hardware plus time I was already spending, and I get lower monthly costs, no vendor lock-in, faster iteration, and resilience against disruption. For a large organization -- a health system, say, paying millions annually for platforms it could increasingly bring in-house -- the numbers are proportionally larger, but the logic is identical.

## What Made This Possible

I have been writing about AI coding agents for months now, so I will not belabor the point. But it would be dishonest to tell this story without naming the enabler.

The specific tools I used are Beancount for accounting and Claude Code for building everything around it. Six months from now, the best tools might be different. The names are less important than what they represent: the cost of turning domain knowledge into working software has dropped to near zero for a wide range of problems.

That last part matters. I have thirty-plus years of software experience, and that experience is what let me describe precisely what I needed and evaluate whether what I got was correct. The AI did not replace my judgment. It made my judgment dramatically more productive. I suspect this dynamic holds at every level of organizational complexity. The people who understand the work are suddenly able to build the tools for the work, without a procurement cycle or a six-month implementation timeline.

This is not a small shift. It is not an incremental improvement in developer productivity. It is a change in who can build and how fast, and it rewrites the economics of make-vs-buy for almost every organization I can think of.

## The Assumption I Had to Update

Here is the part I find most interesting, and most humbling. I do this for a living. I help organizations find and challenge their hidden assumptions. And I still caught myself operating under an assumption -- that building custom tools is expensive and time-consuming -- that stopped being true at least a year ago.

If I am subject to this, everyone is.

We evolved to treat yesterday's constraints as today's facts. That is a reasonable heuristic most of the time. Rules about how the physical world works do not change often. But we are in a period where the rules governing what is easy to build, what is expensive to maintain, and what requires outside help are changing fast. Faster than most people's assumptions are updating.

I do not have a tidy framework for this. I am updating my own priors one project at a time, and I expect I will keep finding places where I am paying a tax I no longer owe. If your experience is similar, I would be interested to hear about it.

You can reach me at john@common-sense.com. If you are looking at your own SaaS stack or vendor portfolio and wondering what the actual switching cost would be today -- not what it was two years ago, but today -- I am happy to think through it with you.
