---
title: 'Two Months Back on an 18-Month Project'
description: 'How standardizing a communication protocol on a smartphone-powered defibrillator project unblocked an entire engineering team and saved two months of development time.'
metaTitle: 'Case Study: Unblocking a Medical Device Project'
metaDescription: "How identifying the communication constraint on Defibrio's smartphone AED saved two months on an 18-month project."
date: 2026-02-22
author: 'John Sambrook'
tags: ['MedTech', 'R&D', 'Theory of Constraints', 'Systems Engineering', 'Case Study']
imageAlt: 'Defibrio smartphone-powered AED with communication protocol architecture diagram for medical device development'
---

In 2024, I joined an Andrews Cooper engineering team building Defibrio's smartphone-powered AED -- the first defibrillator that draws its energy from a phone's USB-C port. Andrews Cooper is a premier product development and engineering services firm with over 100 engineers across multiple offices in Oregon and Washington. They have been doing sophisticated hardware and software development for MedTech, consumer electronics, and industrial clients since 2000, and they are consistently recognized as a top workplace in the Pacific Northwest. When you need serious engineering talent for a complex product, they are the kind of firm you call.

The product itself is remarkable. Sudden cardiac arrest kills over 300,000 Americans a year. Survival rates jump from 10% to as high as 70% when a defibrillator is used in the first few minutes -- but traditional AEDs are expensive, require battery maintenance, and are rarely available where most cardiac arrests happen, which is at home. Defibrio's insight was to use the smartphone everyone already carries as the power source and the user interface, making personal defibrillation affordable and accessible for the first time. It is the kind of product that can genuinely change how many people survive.

The engineering team was strong, the mission was urgent, and the project was moving. But the pace of progress was not quite matching the effort being put in. It took me about a week to see why.

## A Constraint Hiding in Plain Sight

This is a pattern I have seen many times in device development. In the early stages of a project, when the team is small and everyone is heads-down building, informal communication channels work fine. Two or three people understand the hardware intimately. They can drive the device through a serial console, run tests by hand, and answer questions as they come up. This is normal and efficient when you are a small team moving fast.

But as a project grows -- as more engineers come on board, as testing demands increase, as integration work begins in earnest -- those informal channels become a bottleneck. Not because anyone did anything wrong, but because the project outgrew them.

That is exactly what happened here. The device's embedded firmware was controlled through a raw serial text interface. It worked, and the engineers who had built it knew it cold. But as the team expanded, more and more people needed to interact with the device: test engineers writing automated scripts, application developers integrating with the firmware, new team members learning the system. Each of them needed access to the device's behavior, and the path to that access ran through a small number of people who were already busy doing critical development work.

The symptoms were familiar. Lab sessions taking longer than they should, because setup time rivaled test time. Integration meetings spending half their agenda clarifying command behavior. Engineers waiting for bench time or for someone to walk them through an interface that was not documented.

In Theory of Constraints terms, the communication interface had become the constraint. Everything downstream of it -- testing, integration, verification, documentation -- was limited by the rate at which people could interact with the device. The team had plenty of talent and plenty of motivation. What it needed was a way to make the device accessible to everyone, without depending on the availability of the few people who knew the serial interface by heart.

## What I Did

I proposed a standardized binary communication protocol. Not an academic exercise -- a practical spec that any engineer on the project could read, implement against, and test independently.

I used AI-assisted code generation to accelerate the work. The protocol design itself required human judgment: understanding the device's state machine, the safety boundaries, the regulatory requirements, what the test engineers actually needed. But once the design was solid, AI helped me produce the implementation, the documentation, and the test suites far faster than I could have done alone.

Here is what I delivered:

**A formal protocol specification.** A document any engineer could pick up and understand: command structure, response formats, error handling, versioning. The knowledge that had been carried informally by a few experienced developers was now available to the whole team.

**IEC 62304-compatible documentation.** Medical device software has to be developed under a rigorous lifecycle standard. The protocol spec, its design rationale, and the test cases were structured from the start to satisfy the documentation requirements the regulatory affairs team would need downstream. This is one of those areas where doing it right the first time saves enormous pain later. Many projects treat compliance documentation as a cleanup task at the end, and then spend months backfilling traceability. We avoided that problem entirely.

**Automated test suites.** With a well-defined protocol, test automation became straightforward. Engineers could write scripts that exercised the device without needing another human in the loop. This alone transformed productivity in the lab.

**Feature flags for hardware variants.** The project had multiple hardware revisions in play at any given time. I standardized the use of feature flags so that the protocol could interrogate the hardware and adapt. This meant developers did not have to wait for the latest board spin to do useful work. If you had a Rev B board on your bench, you could develop and test against it while Rev C was being fabricated. The protocol told you what was available and what was not.

## What Changed

The effects were visible quickly.

Engineers who had been waiting on device access were working independently within days of getting the spec. They did not need the latest hardware. They did not need to schedule time with someone who knew the old interface. They had a documented contract between the host and the device, and they could write code against it.

Integration meetings got shorter and more productive, because the protocol was the shared language. Instead of spending time clarifying command behavior, people could point at the spec and move on to the real engineering questions.

Lab sessions during verification and validation became dramatically more efficient. Engineers could set up automated test runs instead of manually driving the device through a serial console. The quality of debugging improved because the tests were repeatable and the results were unambiguous.

Compliance came together quickly. When the external regulatory affairs group reviewed the documentation, the protocol spec and its traceability were already in place. There was no scramble to reconstruct design rationale after the fact.

The project manager, Jim LeBaron, told me that over the 18-month project, this change saved at least two months of development time. Engineers were happier and more productive. Product quality improved. The communication spec became the pillar around which the product software was organized.

## Why This Matters Beyond One Project

I tell this story not because protocol design is exotic. It is not. Any experienced embedded systems engineer knows that a clean communication interface changes everything downstream.

I tell it because the pattern is universal, and it shows up on the best teams, not just struggling ones. Defibrio brought deeply experienced business leadership and a clear product vision. Andrews Cooper brought cutting-edge product development expertise and a team of talented engineers. Nobody was underperforming. The constraint was structural -- a communication interface that had been perfectly adequate for an earlier stage of the project and had become a bottleneck as the team and the testing demands scaled up. Every growing project hits these inflection points. The question is how quickly you spot them and what you do about them.

This is what I bring to a project. I have the technical depth to work as a peer alongside the engineering team -- I am writing firmware, not just writing reports. And I have the systems perspective, informed by decades of Theory of Constraints practice, to step back and see where the real constraint is hiding. On a team of strong engineers who are heads-down solving hard problems, that outside perspective is often the missing piece. Not because the team lacks anything, but because the person with their hands in the code is rarely the person with the vantage point to see the structural issue.

If your engineering project has capable people and the progress does not match the effort, the issue is almost certainly structural rather than personal. I am happy to talk through what you are seeing. Sometimes naming the constraint is the hardest part, and a fresh set of eyes is the fastest way to find it.

You can reach me at john@common-sense.com.
