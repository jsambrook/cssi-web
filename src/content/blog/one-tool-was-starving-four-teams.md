---
title: 'One Tool Was Starving Four Teams'
description: 'A clinical ultrasound project was six months behind schedule. The constraint was not the engineering — it was the register map tool that every team depended on and nobody had questioned.'
metaTitle: 'Case Study: One Constraint Cost a MedTech Team Six Months'
metaDescription: 'How identifying a register map bottleneck on a clinical ultrasound project recovered six months of schedule slippage in eight weeks.'
date: 2026-03-05
author: 'John Sambrook'
tags: ['MedTech', 'R&D', 'Theory of Constraints', 'Systems Engineering', 'Case Study']
imageAlt: 'Register map constraint blocking four engineering teams on a clinical ultrasound development project'
---

## TL;DR

A clinical ultrasound project was six months behind schedule. The constraint was a web-based register map tool that forced every hardware change through four manual updates across four teams. Replacing it with a version-controlled Python framework recovered the schedule in eight weeks.

---

A clinical ultrasound manufacturer in the Pacific Northwest was building a high-end imaging system. The hardware architecture was serious: custom ASICs and a large FPGA at the center of the design. Thousands of register definitions — bit-fields, DMA semantics, interrupt controls — described the boundary between hardware and everything else. Hardware engineers, firmware developers, software engineers, and verification teams all needed accurate, current register maps to do their work.

The team was strong. The investment was real. The project was six months behind schedule.

I joined as systems architect and tooling lead. It took me about a week to see where the schedule had gone.

## The Constraint Was Not the Engineering

The team was managing all of its device register definitions through a static, web-based UI. Engineers would log in, define or update register fields, and the tool would store the data. It worked, in the narrow sense that the definitions were in there somewhere. But it had three properties that, in combination, were strangling the project.

**No version control.** Hardware register definitions changed constantly during active development. The web UI had no branching, no rollback, no way to see what changed between Tuesday and Thursday. When a bit-field shifted in the FPGA, there was no reliable way to know what downstream artifacts were now out of sync.

**Manual propagation.** A single register change in hardware required four separate manual updates: the RTL source, the C/C++ header files for firmware and software, the module specification document, and the debugger scripts. Four artifacts, maintained by hand, by different people, on different schedules. Each one was a chance for a transcription error. Each transcription error was a bug that would surface weeks later during integration, when it was expensive to find and expensive to fix.

**No automation path.** Because the tool was a closed UI rather than a data source, there was no way to generate downstream artifacts from it. Every team was doing translation work by hand — copying register layouts from the UI into their own formats, and re-doing that work every time something changed.

In Theory of Constraints terms, this tool was the system constraint. Everything downstream of it — firmware development, software integration, verification, documentation — was limited by the rate at which accurate register information could propagate through the project. Four teams were waiting on the same bottleneck, and the bottleneck was not a person or a lab or a piece of equipment. It was a tool that everyone depended on and nobody had questioned.

The symptoms were familiar. Integration bugs that turned out to be stale register definitions. Verification test failures that were really documentation drift. Engineers spending hours cross-checking header files against the UI instead of writing code. The project was not behind because people were slow. It was behind because a substantial fraction of engineering effort was being consumed by manual synchronization work that should not have existed.

## What I Built

The fix was conceptually simple: make the register map a single source of truth that could generate everything downstream automatically.

I designed a Python-based device modeling framework. Instead of filling out forms in a web UI, engineers wrote a Python constructor that built a hierarchical tree of first-class objects: System, Block, Register, Bitfield. The register map lived in version-controlled code, which meant it could be branched, diffed, merged, and reviewed like any other engineering artifact.

Once the data structure was instantiated, a suite of generators traversed the tree and produced the downstream artifacts automatically:

- **C/C++ API code and memory maps** for firmware and software teams. Header files that matched the hardware, generated from the same source, every time.
- **SystemVerilog test benches** for register-level verification. The verification team got test infrastructure that was guaranteed to match the current hardware definition.
- **Print-ready documentation.** A pipeline from reStructuredText through LaTeX to PDF produced a module specification — what the team called the ModSpec — that was complete and accurate by construction. No manual transcription, no drift.
- **Debugger macros** that let field engineers and developers inspect hardware state in plain English instead of decoding hex values by hand.

One change to a register definition propagated everywhere it needed to go. Automatically. Correctly.

## What Changed

The effects showed up fast.

The manual synchronization work disappeared. Engineers who had been spending hours cross-checking headers against the UI were writing code instead. Integration meetings got shorter because the artifacts matched — there was nothing to reconcile.

The class of bugs caused by stale or mismatched register definitions dropped to zero. Not reduced. Zero. When the register map is the single source of truth and everything else is generated from it, there is no room for transcription errors. We stopped debugging typos and started debugging physics.

The verification team saw the biggest immediate gain. Their test benches were generated from the same register definitions as the firmware headers and the RTL. When a test failed, it meant something real was wrong, not that someone had copied a bit-field offset incorrectly three weeks ago.

| Metric                   | Before           | After                     |
| :----------------------- | :--------------- | :------------------------ |
| **Development velocity** | Stalled (0.5x)   | Doubled (2.0x)            |
| **Schedule**             | 6 months behind  | Recovered in ~8 weeks     |
| **Register sync errors** | Frequent, costly | Zero                      |
| **Adoption**             | —                | Mandatory global standard |

The framework became the standard across the organization. Not because anyone mandated it from above, but because the teams that used it stopped having an entire category of problems that the teams still on the old process were fighting every week.

## The Pattern

I have seen versions of this constraint in every complex hardware-software development project I have worked on. The specifics change — sometimes it is a communication protocol, sometimes it is a build system, sometimes it is a requirements database — but the structure is the same. A shared dependency that every team touches becomes the limiting factor for the whole system, and nobody sees it as the constraint because it is infrastructure, not product.

The Five Focusing Steps from Theory of Constraints apply directly:

1. **Identify.** The register map tool was the constraint. Not the team, not the budget, not the hardware complexity.
2. **Exploit.** There was nothing to exploit — the tool had no unused capacity. It was architecturally incapable of supporting the project's needs.
3. **Subordinate.** The entire project had already involuntarily subordinated itself to this tool. Every team's schedule was paced by manual register propagation.
4. **Elevate.** Replace the tool with one that eliminates the constraint entirely. That is what the Python framework did.
5. **Repeat.** Once the register map was no longer the bottleneck, the next constraint became visible — and it was an engineering problem, not an infrastructure problem. That is how it should be.

The reason these bottlenecks persist is that they look like minor inconveniences from any single team's perspective. The firmware engineer who spends twenty minutes updating a header file does not think of it as a system constraint. It is just part of the job. But multiply that twenty minutes across four teams, dozens of registers, and hundreds of iterations over the life of a project, and you get six months of schedule slippage that nobody can point to a single cause for. That is what makes it a constraint rather than just a nuisance — it limits the throughput of the entire system, and the evidence is diffuse enough that it resists diagnosis.

Finding it requires stepping back far enough to see the whole system, not just the piece you are working on. That is hard to do when you are heads-down on a deadline. It is exactly the kind of thing an outsider with systems discipline can see in a week that insiders, buried in the work, have been living with for months.

If your engineering project has capable people and the progress does not match the effort, the problem is almost certainly structural. I am happy to think through what you are seeing. You can reach me at john@common-sense.com.
