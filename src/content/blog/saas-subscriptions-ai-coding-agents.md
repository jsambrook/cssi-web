---
title: 'Cancel your SaaS, keep your data: how AI coding agents change the economics'
description: 'When you can build a custom import tool in fifteen minutes, the calculus on which subscriptions to keep changes dramatically.'
metaTitle: 'Cancel SaaS and keep your data with AI agents'
metaDescription: 'When you can build a custom import tool in fifteen minutes, the calculus on which subscriptions to keep changes dramatically.'
date: 2026-02-12
author: 'John Sambrook'
tags: ['AI', 'Practical Tips', 'Cost Reduction']
---

My business costs are going down. My workload is going down. And my capabilities are going up. All at the same time.

That's not supposed to happen. Usually when you cut costs, you lose capacity or take on more work yourself. But AI coding agents have broken that tradeoff, and I want to show you how with a concrete example from this morning.

I canceled ProtonMail today. Not because it's a bad service -- it's excellent, and I have zero complaints. But the subscription was about to renew, and I'm in the middle of a deliberate campaign to cut expenses. ProtonMail was the latest in a line of at least ten SaaS tools I've canceled in recent months. I'll walk through exactly how below. If you want the punchline first, jump to [A Broader Observation](#a-broader-observation) -- but the how is what makes it practical.

## The "Export My Data" Problem

Most SaaS tools today offer some kind of data export. That's good. What's less good is what you get: a zip file full of structured data in formats that are technically open but practically opaque. MBOX files. JSON dumps. CSV files with dozens of columns. EML archives.

For years, the implicit bargain was: _you can leave anytime, and here's your data to prove it._ But "here's your data" often meant "here's a pile of bits you'll never actually use." The export existed to check a box, not to give you real agency.

I used to be able to get by with `grep` and `strings` and a few shell scripts. Those days are over. The volume and structure of exported data from modern tools is beyond what command-line text utilities can reasonably handle.

## What Changed

AI coding agents changed the equation.

This morning, ProtonMail was exporting my email archive to local disk. While the export was running, I sat down with Claude Code and described what I needed: a tool to read ProtonMail's export format and import the messages into my own email archive system. ProtonMail's documentation on their export format is thorough and well-organized, which helped considerably.

Fifteen minutes later, the import tool was done and working. Not a prototype. Not a rough script I'd need to spend a weekend polishing. A working tool that reads the export, parses the messages, and loads them into the archive I already use for my primary email.

That archive system, incidentally, was itself built with Claude Code. I use it as my preferred AI coding agent, though I sometimes switch to Codex or use both to cross-check each other's work.

The point is not that I'm clever. The point is that the barrier to building small, purpose-built tools has dropped to nearly zero for anyone comfortable describing what they need.

## The Recurring Pattern

Once I started paying attention, I noticed this pattern repeating across every SaaS cancellation:

1. Export the data using the provider's export feature.
2. Examine the export format. Read the provider's documentation if it exists.
3. Ask an AI coding agent to build an import tool for whatever system I want the data to live in going forward.
4. Run the import. Verify the results. Done.

Step 3 used to be the hard part. It used to mean days or weeks of work, reading format specs, handling edge cases, writing tests. Now it takes minutes to hours depending on complexity. That changes the entire cost-benefit analysis of keeping a subscription.

## Doing the Math

I'm not going to pretend every SaaS tool can be replaced this way. Some provide ongoing value that's hard to replicate: collaboration features, real-time sync across teams, integrations with other services you depend on. Those are worth paying for.

But a surprising number of subscriptions persist simply because leaving feels too costly. Not emotionally costly. _Practically_ costly. The switching cost is high because your data is trapped in a format you can't easily use elsewhere.

AI coding agents compress that switching cost dramatically. When you can build a custom data migration tool in fifteen minutes, you start asking a different question. Not "can I afford to leave?" but "can I justify staying?"

I've canceled at least ten tools in the past few months. The savings add up quickly.

## It Goes Beyond Canceling Subscriptions

Once you get comfortable working with an AI coding agent, you start seeing opportunities everywhere, not just in cutting costs.

I used to dread the end of every quarter. Filing business reports with the IRS and Washington State agencies was tedious, error-prone, and stressful. Now I have playbooks for each filing that Claude Code follows to get the reports prepared and filed. The dread is gone. The quarterly filings just happen.

Same story with monitoring my website. I get a daily brief that pulls data from Google Analytics and Google Search Console, summarizes what's happening with traffic and search performance, and includes a few actionable tips that Claude Code can implement directly. Why would I pay an SEO consultant for something I can get every morning before coffee?

These aren't hypothetical examples. They're running right now in my business. Each one started as a small experiment, took a few hours at most to set up, and now runs reliably with minimal attention.

## A Broader Observation

What ties all of this together is vertical integration. Data migration, tax filing, website analytics -- these used to be things you either paid someone else to do or suffered through manually. Now they're capabilities I've brought in-house, built to my exact specifications, maintained on my own terms. And because they're automated, they don't add to my workload. They subtract from it. The email archive ingests new mail on its own. The website brief shows up every morning without me asking. The quarterly filings run from playbooks.

I'm not trading one form of manual labor for another. I'm building systems that run themselves.

This is what it actually looks like to become an AI-first operation. Not a slide deck about AI strategy. Not a pilot program. Just a steady accumulation of small, automated capabilities that compound over time. Costs go down, workload goes down, and the business gets more capable, not less, as it gets leaner.

A lot of companies and organizations want to be AI-first. This is one concrete path to getting there. You don't need to become a programmer. You need to be able to describe what you want clearly and evaluate whether the result works. If you can do that, the economics of build-versus-buy have shifted dramatically in your favor.

---

If any of this resonates and you'd like to think through how these ideas apply to your situation, I'd welcome the conversation. You can reach me at [common-sense.com/contact](https://common-sense.com/contact).
