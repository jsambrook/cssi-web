---
title: 'Doing My Taxes with Claude Code and Codex'
description: "A small business owner's account of automating tax preparation with AI coding agents, and what it suggests about the near future of knowledge work."
metaTitle: 'Doing My Taxes with Claude Code and Codex'
metaDescription: "A small business owner's account of automating tax preparation with AI coding agents, and what it suggests about the near future of knowledge work."
date: 2026-02-15
author: 'John Sambrook'
tags: ['AI', 'Practical Tips', 'Small Business']
imageAlt: 'AI coding agents processing tax forms and financial schedules for small business S-Corp tax preparation'
---

I'm doing my business taxes this year with AI coding agents. Not conceptually. Not as an experiment. I mean the actual tax forms, schedules, and filings for my S-Corp.

Here's what the setup looks like: financial data from QuickBooks and bank statements goes into a private Git repo. Claude Code writes Python scripts that parse that data and compute the tax forms. Codex reviews the scripts with a high-reasoning model. I direct the process, check the results, and make the decisions. Between the three of us, the taxes are getting done.

## Two Agents, One Checking the Other

The workflow has a structure that turned out to be more important than I expected. Claude Code with Opus 4.6 writes most of the code. Codex then reviews it. This isn't a formality. Codex finds real errors.

Here's a concrete example. Codex ran a review of my 1120S scripts and flagged three findings, severity-ordered. The most serious: an incorrect Schedule L field mapping where Line 18 (ending) was being computed from total liabilities instead of other current liabilities. That's the kind of error that's easy to make and hard to catch by staring at a spreadsheet. Codex caught it by tracing the data from source JSON through to the generated CSV.

The review process is often multi-turn. Codex flags an issue, Claude Code fixes it, Codex reviews again. They go back and forth until both agree the code is correct. It's not unlike a code review between two experienced developers, except it happens in minutes instead of days.

## The Photoshop Problem

One of the unexpected benefits is having a QuickBooks expert available whenever I need one.

I don't spend enough time in QuickBooks to know it well. It's the Photoshop problem: you know the software can do what you need, but you only use it a few times a year, so you never build fluency. Every session starts with fumbling through menus, trying to remember how reconciliations work, wondering what changed in the latest update.

With Claude Code, that friction disappears. I don't need to know what's under every dropdown in the QuickBooks UI. I describe what I need in plain English. When I needed to reconcile my business credit card, I just said "Let's reconcile -7301." Claude Code knew that -7301 referred to my business credit card, told me what data I'd need, and gave me the full pathname to the proper credit card statement in the repo. No fumbling. No searching.

This pattern generalizes far beyond QuickBooks. Any complex software you use infrequently imposes a recurring tax on your attention. You lose time re-learning the interface every time you sit down with it. AI agents eliminate that tax. You describe what you want to accomplish, and they handle the how.

## What I'm Actually Learning

Since 1996, I've had my CPA prepare both my business and personal taxes. That's thirty years of someone else understanding my tax situation better than I do.

This year is different. By working through the process with AI agents, I'm learning how my own taxes actually work. Not because I set out to learn -- the learning is a side effect of directing the process. When you have to describe to an AI agent what needs to happen with your Schedule K-1, you end up understanding your Schedule K-1.

I found errors I made in 2025 in how I managed certain aspects of the business. They weren't catastrophic, but they were real, and I wouldn't have caught them if I'd just handed everything to a CPA as usual. I'll be much less likely to make them again in 2026.

## What's Next: Plain Text Accounting

Once taxes are done, I'm planning to replace QuickBooks with Beancount, an open-source double-entry accounting system that uses plain text files for its records.

That sounds crazy. I know. But consider what actually matters now. QuickBooks is designed for human eyeballs: menus, forms, reconciliation wizards. Beancount is designed for both humans and machines to read: structured plain text that lives in a Git repo, diffs cleanly, and is trivial for an AI agent to parse and modify.

This is the direction tools are heading. Software designed purely for human interaction through graphical interfaces is being supplemented -- and in some cases replaced -- by tools that are readable by both humans and AI. Plain text accounting isn't a step backward. It's a better fit for how work actually gets done now.

## The Broader Pattern

This tax project is part of a larger shift in my business. Over the past several months, I've been systematically replacing SaaS subscriptions with capabilities built on demand using AI coding agents. Not because those services were bad. Because the economics changed.

When building a custom tool takes minutes instead of weeks, the buy-versus-build calculation shifts dramatically. For a small business, accumulated SaaS subscriptions represent a significant ongoing cost. Many of them persist not because the service is irreplaceable, but because the switching cost felt too high. AI agents compress that switching cost to near zero.

Quarterly tax filings that used to cause dread now run from playbooks. Website analytics that used to require a consultant now show up as a daily brief. Data exports that used to sit unused in zip files now get imported with tools built in fifteen minutes. Each of these is a capability I own, running on my terms, at a fraction of the cost.

## What This Means for Knowledge Work

If you're a knowledge worker reading this, I want to be clear about what I think is happening. This isn't a story about jobs disappearing. It's a story about the skills that matter changing.

For thirty years, knowing _how to operate specific software_ was a valuable skill. Knowing QuickBooks, knowing Excel, knowing Photoshop -- these were resume items. They still have value, but the balance is shifting. What matters more now is knowing _what needs to happen_: understanding the domain, being able to describe a problem clearly, and evaluating whether a solution is correct.

I'm 66. I've been writing software for over thirty years. And I'm more capable today than I was five years ago. Not because I'm smarter, but because AI coding agents multiply the value of experience and judgment. If you can describe what you need and tell whether the result is right, you can build things that would have required a team a few years ago.

That's not a threat. It's an on-ramp.

---

If this resonates and you want to think through how it might apply to your situation, I'd welcome the conversation. You can reach me at [common-sense.com/contact](https://common-sense.com/contact).
