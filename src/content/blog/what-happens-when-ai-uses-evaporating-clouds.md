---
title: 'What Happens When an AI Agent Uses Evaporating Clouds?'
description: 'I built an AI agent that applies TOC Thinking Processes autonomously to improve business ideas. When I pointed it at itself, it resolved two real tensions via Evaporating Cloud across 10 iterations.'
metaTitle: 'AI Agent Uses Evaporating Clouds Autonomously | Common Sense Systems'
metaDescription: 'An AI agent applied TOC Evaporating Clouds to resolve real business tensions across 10 autonomous iterations. Full iteration log and open-source code included.'
date: 2026-03-19
author: 'John Sambrook'
tags: ['AI', 'Theory of Constraints', 'Constraint Resolution', 'Strategy']
imageAlt: 'Score progression chart showing 10 iterations of AI-driven idea improvement using TOC Thinking Processes'
---

<img src="/images/content/ai-evaporating-clouds-iteration-loop.webp" alt="Infographic showing an AI-driven iteration loop using Theory of Constraints: a circular 10-step process with Evaporating Cloud breakthroughs highlighted at iterations 5 and 10, alongside a score progression chart showing Testability, Value, Difficulty, and Failure Modes improving across iterations" width="1408" height="768" loading="lazy" decoding="async" />

## TL;DR

I built an AI agent that improves business ideas using TOC Thinking Processes, including Evaporating Clouds. Pointed at itself, it ran 10 iterations and resolved two genuine tensions — thoroughness vs. adoption friction, and speed vs. depth of output. The full tool and iteration log are open source.

---

On March 18, 2026, I attended Peter Cronin's TOCICO webinar, "Thinking Better with AI: Using TOC to Ask the Right Questions." Peter is the Head Instructor at [Black Belt in Thinking](https://blackbeltinthinking.com) and has taught TOC Thinking Processes to over 250 people across four continents. His talk hit close to home, because I have been building exactly what he was describing — an AI agent that applies the Thinking Processes to real problems, autonomously.

I want to show what that looks like in practice.

## What I built

The tool is straightforward. You give it a rough business idea. It asks clarifying questions — what problem does this solve, who is the customer, what is the mechanism, what makes it hard to copy — and writes a structured seed document. Then it runs N iterations autonomously.

Each iteration, the agent picks one improvement move from a catalog of seven:

| Move | Name                                | When to use                                  |
| ---- | ----------------------------------- | -------------------------------------------- |
| 1    | Make it more concrete               | Idea is vague; testability is low            |
| 2    | Reduce human dependency             | Too many manual steps                        |
| 3    | Adjust scope                        | Value is low (broaden) or unfocused (narrow) |
| 4    | Improve clarity                     | Coherent but hard to explain                 |
| 5    | Resolve tension (Evaporating Cloud) | A buried dilemma                             |
| 6    | Research and ground                 | Assumptions need evidence                    |
| 7    | Break oscillation (Magic Druids)    | A recurring swing between two approaches     |

It scores each variant on four dimensions — testability, value, implementation difficulty, failure modes — and keeps the best. Every move is recorded in an iteration log with before/after scores and a one-sentence rationale.

The [Evaporating Cloud](/insights/ai-facilitated-constraint-resolution) is the most interesting part. In Theory of Constraints, an Evaporating Cloud is a diagram that maps a dilemma: two legitimate needs that appear to conflict. You write out both sides, surface the assumptions connecting them, and look for the one assumption you can break. When you find it, the conflict dissolves. The agent does this autonomously — building real clouds, naming real assumptions, and producing injections that change the idea.

Move 7 uses the [Magic Druids](https://blackbeltinthinking.com/blog/introducing-the-magic-druid-thinking-tool/) tool, developed by James Powell and Peter Cronin and accepted into the TOCICO Body of Knowledge. Where the Evaporating Cloud resolves a one-time conflict, Magic Druids breaks a recurring oscillation — a pattern where you keep swinging between two behaviors because each one's side effects push you toward the other.

## The test: improving its own design

I pointed the tool at itself. The seed idea was vague: "an autonomous idea-improvement system that uses TOC." Starting scores: T:8 / V:7 / D:8 / F:6.

Here is the 10-iteration progression:

| Iteration | Move                    | T   | V     | D     | F     | New best? |
| --------- | ----------------------- | --- | ----- | ----- | ----- | --------- |
| Seed      | —                       | 8   | 7     | 8     | 6     | —         |
| 1         | Make concrete           | 9   | 7     | 8     | 6     | Yes       |
| 2         | Narrow scope            | 9   | 8     | 8     | 6     | Yes       |
| 3         | Reduce human dependency | 9   | 8     | 7     | 7     | Yes       |
| 4         | Clarity                 | 9   | 8     | 7     | 7     | Replaced  |
| 5         | **Evaporating Cloud**   | 9   | **9** | 7     | 7     | **Yes**   |
| 6         | Make concrete           | 9   | 9     | 7     | 7     | Replaced  |
| 7         | Broaden scope           | 9   | 9     | 6     | 7     | No        |
| 8         | Reduce human dependency | 9   | 9     | 7     | 7     | Yes       |
| 9         | Clarity                 | 9   | 9     | 7     | 7     | Replaced  |
| 10        | **Evaporating Cloud**   | 9   | 9     | **8** | **8** | **Yes**   |

The two biggest jumps came from Evaporating Clouds — iterations 5 and 10. Not from the mechanical moves (make concrete, adjust scope, improve clarity), which produced incremental gains. The structural breakthroughs came from surfacing and resolving buried conflicts.

## The two clouds

### Tension 1: Thoroughness vs. adoption friction (iteration 5)

The tool needed to be thorough — 10 iterations, adversarial scoring, full audit trail — AND easy to adopt. Consultants will not sit staring at a terminal for 15 minutes.

The agent built a cloud. The conflict was between a fast, minimal process (satisfying the need for low adoption friction) and a deep, multi-iteration process (satisfying the need for quality output). The assumed conflict: fast and thorough cannot coexist.

The challenged assumption: "Low friction means a fast process." That is wrong. Startup friction — how hard it is to begin — and wait friction — how annoying it is to wait — are different things. Wait friction disappears if the process runs in the background.

The injection: run the iteration loop as a background process. You brief the tool in 30 seconds and read the output when you are ready. The product reframing shifted from "a tool you use" to "an assistant you brief and check in on."

Value jumped from 8 to 9.

### Tension 2: Fast-to-read vs. deep-to-audit (iteration 10)

The output needed to be immediately actionable — consultants want answers, not reading assignments — AND trustworthy, with visible reasoning and nothing hidden.

The challenged assumption: "Low reading time means a single short document." Also wrong. Reading time and document depth are not coupled if the document is layered.

The injection: a layered report. Verdict (30 seconds of reading), Summary (5 minutes), Full reasoning (on demand, linked but not required). Readers who need speed stop after the Verdict. Readers who need to verify keep reading.

Both difficulty and failure modes jumped from 7 to 8 — because the layered format was actually _simpler_ to implement than the previous multi-file output structure. The structural simplification reduced both implementation work and cross-file inconsistency risk. A genuine win-win.

## What I notice

The clouds the agent produces are not perfect. A skilled human facilitator — someone like Peter Cronin who has run hundreds of these — would probably surface subtler assumptions and push harder on whether the injections truly dissolve the conflict or just defer it. I am genuinely curious about that gap.

But the fidelity is higher than I expected. The agent does not hand-wave. It names specific assumptions, challenges them with specific reasoning, and produces injections that measurably change the idea. You can trace every step in the iteration log.

The more interesting question is what happens when the Thinking Processes are available at iteration speed. A human facilitator might run one Evaporating Cloud in a two-hour workshop. This agent ran two in 15 minutes, alongside eight other improvement moves. That does not make it better than a facilitator — the quality of a single human-run cloud may be higher. But the speed changes what is practical. You can afford to resolve tensions early, when the idea is still forming, rather than saving the heavy tools for later.

## See for yourself

The full tool — every reference file, the scoring rubric, the move selection heuristics, the TOC Thinking Processes reference, and the complete self-improvement run with both resolved clouds — is open source:

**[github.com/jsambrook/cssi-plan-generator](https://github.com/jsambrook/cssi-plan-generator)**

Start with the [iteration log](https://github.com/jsambrook/cssi-plan-generator/blob/main/runs/self-improvement/iteration-log.md) to see the full progression, or the [report](https://github.com/jsambrook/cssi-plan-generator/blob/main/runs/self-improvement/report.md) for the summary. The [TOC Thinking Processes reference](https://github.com/jsambrook/cssi-plan-generator/blob/main/references/toc-thinking-processes.md) that the agent uses covers the full TP toolkit: Current Reality Tree, Evaporating Cloud, Magic Druids, Future Reality Tree, Negative Branch Reservation, Prerequisite Tree, and Transition Tree.

I am particularly interested in hearing from people who work with the Thinking Processes professionally. Does what the agent produces match your experience of how these tools work? Where does it fall short? What would you do differently?

I could be wrong about the quality of these AI-generated clouds. That is exactly why I want the conversation. You can reach me at john@common-sense.com.
