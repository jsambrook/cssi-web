---
title: "Why 'Agile' Fails in Hardware (And What Actually Works)"
description: "You cannot 'sprint' a circuit board design. How to apply Critical Chain Project Management to physical engineering challenges."
metaTitle: 'Why Agile Fails in Medical Device Hardware Development'
metaDescription: "Software methodologies break when applied to physics and FDA regulations. A systems architect's view on Critical Chain for MedTech."
date: 2026-02-16
author: 'John Sambrook'
tags: ['MedTech', 'R&D', 'Theory of Constraints', 'Delivery']
---

I have sat in countless engineering reviews where a well-meaning consultant tries to force a hardware team to work in two-week "Sprints."

The tension in the room is palpable. The firmware engineers are game—they can recompile in minutes. But the electrical engineers and mechanical designers are staring at their shoes.

They know something the consultant doesn't: **Physics doesn't sprint.**

You cannot iterate a printed circuit board (PCB) in two weeks. Fabrication takes time. Assembly takes time. Signal integrity testing takes time. FDA validation takes time.

When you force "Agile" on hardware, you don't get speed. You get **fragmentation**. Engineers break work into artificial "stories" just to feed the Jira beast, losing sight of the integrated system.

## The Alternative: Critical Chain

In the physical world, the constraint isn't usually "engineering hours." It is **integration latency**.

The solution isn't Scrum. It's **Critical Chain Project Management (CCPM)**.

1. **Identify the Longest Path:** In MedTech, this is almost always the "Design-Build-Test" cycle of the physical hardware.
2. **Buffer the Project, Not the Task:** Engineers pad their estimates because they are afraid of being late. CCPM strips that safety buffer from individual tasks and aggregates it at the end of the project.
3. **The Relay Runner Mindset:** When a task is on the Critical Chain, it is the only priority. The engineer works it like a relay race—full speed, hand off the baton, then rest. No multitasking.

## Stopping the "Student Syndrome"

Agile Sprints often encourage "Student Syndrome"—waiting until the end of the sprint to integrate. In hardware, this is fatal.

By shifting from "Sprints" (artificial timeboxes) to "Flow" (managing the Critical Chain buffers), we align the methodology with the physics of the product.

We don't need to pretend hardware is software. We need to respect the constraints of the physical world and architect our workflow to move through them, not pretend they don't exist.
