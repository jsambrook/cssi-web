---
title: 'The Other Calculation'
description: 'A hospital CFO runs the same numbers two ways and gets answers that disagree by a factor of five. Episode 04 of the Cascade Valley audio drama series.'
metaTitle: 'The Other Calculation -- Cost vs Throughput | Common Sense Systems'
metaDescription: 'What does an empty OR block really cost? A hospital CFO discovers that cost accounting and throughput accounting give answers that disagree by a factor of five.'
date: 2026-03-07
author: 'John Sambrook'
tags: ['Healthcare', 'Theory of Constraints', 'Operations', 'Strategy', 'AI', 'Systems']
imageAlt: 'A hospital CFO at his desk early in the morning, spreadsheet open, two tabs visible -- one labeled Cost Analysis, the other Alternative Analysis -- the numbers on each tab telling a different story about the same empty rooms'
updatedDate: 2026-03-18
draft: false
---

## TL;DR

An empty operating room costs a hospital roughly 36 to 50 dollars per minute in wasted overhead. But the throughput it fails to generate can be five to ten times that. These are not competing answers to the same question. They are precise answers to two different questions, one from financial accounting and one from managerial accounting. Episode 04 of the Cascade Valley series follows CFO Steven Park as he discovers the gap.

---

There is a number that hospital CFOs know well: the cost of one minute of operating room time. The published literature puts it at 36 to 50 dollars per minute depending on who is counting and what they include. A [2018 JAMA Surgery study](https://jamanetwork.com/journals/jamasurgery/fullarticle/2673385) benchmarked it at 37 dollars per minute across California hospitals. A [2022 literature review in the Journal of Orthopaedic Business](https://jorthobusiness.org/index.php/jorthobusiness/article/view/23) landed at 46. The range is wide, but the floor is high.

This number gets used to calculate the cost of waste. When an OR block sits empty, you multiply the minutes by the per-minute cost and arrive at a figure that feels meaningful. For a hospital with six ORs and 15% unutilized time during staffed hours, the math works out to roughly four million dollars per year. Not nothing. But against a 25-million-dollar capital request for new operating suites, it does not sound catastrophic.

There is another calculation. It asks a different question. Not "what did the empty room cost us?" but "what did the empty room fail to produce?"

## Two questions, not one

The distinction matters, and it is easy to miss. These two calculations are not rival answers to the same question. They come from different branches of accounting, and they measure different things.

Financial accounting, the framework hospitals use for reporting, tax filings, and regulatory compliance, asks: what does it cost to operate this room? When the room sits idle, it assigns a share of the overhead, the staff, the depreciation, to that idle time. This produces a real and auditable number. It is useful for understanding where money goes.

[Throughput Accounting](/approach/theory-of-constraints#throughput-accounting), a framework developed by the physicist Eli Goldratt as an alternative to traditional cost accounting, asks a different question: what does this room produce when it runs? Revenue minus the costs that are only incurred because a specific patient is on the table. Everything else, the salaries, the overhead, the building, is already spent whether the room runs or not. When the room sits idle, that production simply does not happen.

Financial accounting tells you what idle time costs. Throughput Accounting tells you what idle time fails to produce. Both are correct. But when it comes to evaluating operational investments, only one of them measures the actual economic stakes.

## The gap

In [Goldratt's](https://en.wikipedia.org/wiki/Eliyahu_M._Goldratt) framework, throughput is revenue minus truly variable costs. The money that only gets spent because a specific patient is on the table: implants, disposable supplies, drugs consumed during the procedure. Everything else is already committed. The surgeon is salaried. The nurses are hourly, but if they are already scheduled and on the clock for that block, their cost is the same whether a patient is on the table or not. The anesthesiologist is on contract. The room is built. The lights are on.

For a typical surgical case, revenue might average 22,000 dollars. Truly variable costs might be 4,000 dollars. The throughput per case is 18,000 dollars. That is the contribution to paying for everything else in the hospital. When a block sits empty, that 18,000 does not happen.

And if the OR is the constraint, the bottleneck on what the hospital can produce, it cannot be recovered. There is no slack in next week's schedule to absorb a delayed case. Next week's blocks are full too. An hour lost at the bottleneck is an hour lost for the entire system, permanently. Goldratt considered this one of his most important insights.

Run the numbers with this framing, and the same empty rooms that looked like a four-million-dollar problem now look like a 22-million-dollar problem. Same hours. Same idle time. Different question about what they are worth.

## Why it matters for purchasing decisions

This gap does not just change how you evaluate capital spending. It changes how you evaluate every operational tool, every scheduling system, every staffing model.

Consider a real pattern. A health system evaluates an AI-powered OR scheduling platform. The platform costs a meaningful annual subscription. The CFO compares the subscription cost against the cost of wasted OR time. The ROI is marginal. The system is deemed "too expensive." They pass.

Meanwhile, a competing health system down the road deploys the same platform. They unlock 3,200 additional surgical cases in a single year. They increase staffed room utilization by 25%. They do it without adding rooms or staff.

What happened? Both CFOs did the math. But they were measuring against different numbers. The first measured against the cost of waste (four million dollars). The second, whether they used Goldratt's language or not, was measuring against the throughput they could generate (22 million or more). The same subscription fee looks trivial against one number and expensive against the other.

## The audio drama

Episode 04 of the Cascade Valley series, "The Other Calculation," follows CFO Steven Park through a single day as he works through this exact discovery. It is the morning after the board meeting depicted in Episode 01. Park runs the standard cost-of-waste calculation. He gets the expected answer. Then he stumbles into an article about Throughput Accounting and runs the numbers a second way.

The episode opens with a narrator's foreword that frames the two accounting frameworks before Park's story begins. This is intentional. The distinction between financial accounting and managerial accounting is precise and important, and having it stated clearly up front gives the listener the scaffolding to follow Park's reasoning as he works through it in real time.

The episode is a companion piece to Episode 02, "After the Meeting," which followed Chief Nursing Officer Barbara Fleming as she processed the board meeting from a completely different angle. Fleming discovered structural conflicts embedded in nursing contracts. Park discovers a structural gap in how the hospital measures value. Both are preparing, without knowing it, to bring something new to the working group that the board authorized at the end of Episode 01.

<div class="aspect-video my-8">
  <iframe
    src="https://www.youtube.com/embed/2kPbYCnyFvk"
    title="The Other Calculation -- Cascade Valley Health System, Episode 04"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
    class="w-full h-full"
  ></iframe>
</div>

## What is real here

The hospital is fictional. Steven Park is fictional. But the numbers are real.

OR cost per minute comes from published research. The throughput calculation uses averages consistent with actual hospital case data. The pattern where a health system passes on an optimization tool because it was evaluated against the wrong number is something I have seen firsthand. And the competing health system that deployed the platform and unlocked thousands of additional cases? That is [a matter of public record](https://www.healthcareitnews.com/news/multicare-uses-predictive-analytics-add-3200-surgeries-one-year).

The cost-world vs. throughput-world distinction is not new. Goldratt wrote about it decades ago. But it remains surprisingly rare in how hospital finance teams evaluate operational investments. Most capital decisions and vendor evaluations in healthcare still use cost-based framing. The question "what does this fail to produce?" is asked far less often than "what does this cost?"

## The series so far

If you are new to the Cascade Valley series:

[Episode 01: The Meeting That Went Differently](/insights/the-meeting-that-went-differently) is the 56-minute board meeting where Sam, an AI, participates for the first time and asks the questions nobody else was positioned to ask.

[Episode 02: After the Meeting](/insights/after-the-meeting) follows CNO Barbara Fleming through the week after the board meeting as she discovers structural conflicts in nursing contracts that explain the staffing problems she has been managing for years.

[Episode 03: Resolving a Sweet Dilemma](/insights/resolving-a-sweet-dilemma) is a standalone teaching episode that walks through the Evaporating Cloud tool using a bakery pricing dilemma.

Episode 04, this one, follows the CFO.

[Episode 05: The First Session](/insights/the-first-session) is the ensemble working group episode where the private discoveries from earlier episodes enter a room and converge.

[Episode 06: After the First Session](/insights/after-the-first-session) is the quiet conversation afterward — Commissioner Tanaka stays behind and asks Sam why the session went differently than any meeting he has seen in six years.

## The question underneath the question

Park's discovery in this episode is not really about OR scheduling or vendor pricing. It is about the sufficiency of the framework you use to evaluate decisions. Cost accounting is not wrong. It correctly measures what it measures. The problem is what it does not measure. And when the thing it does not measure is five times larger than the thing it does, the framework is not just incomplete. It is actively misleading.

Every organization has some version of this. A metric that answers the question you are asking while hiding the question you should be asking. The distance between those two questions is where the real money lives.

If you run a hospital, a clinic, or any operation where expensive capacity sits idle while demand goes unmet, and you have been evaluating solutions against the cost of the waste rather than the throughput you are not generating, it might be worth running the numbers both ways. The gap may surprise you.

I am happy to think through the specifics with you. john@common-sense.com.

---

## Sources

- Childers CP, Maggard-Gibbons M. [Understanding Costs of Care in the Operating Room](https://jamanetwork.com/journals/jamasurgery/fullarticle/2673385). _JAMA Surgery_. 2018;153(4):e176233. Mean OR cost of $37/min across California hospitals.
- Zygourakis CC, et al. [The Cost of OR Time is $46.04 per Minute](https://jorthobusiness.org/index.php/jorthobusiness/article/view/23). _Journal of Orthopaedic Business_. 2022. Literature review of 51 articles on OR cost per minute.
- [MultiCare Uses Predictive Analytics to Add 3,200 Surgeries in One Year](https://www.healthcareitnews.com/news/multicare-uses-predictive-analytics-add-3200-surgeries-one-year). _Healthcare IT News_. 25% increase in staffed room utilization without adding rooms or staff.
- Goldratt EM. _[The Goal](<https://en.wikipedia.org/wiki/The_Goal_(novel)>)\_. 1984. The foundational work on Theory of Constraints and Throughput Accounting.
