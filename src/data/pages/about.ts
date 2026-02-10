import type { PageHeader, ContentBlock, CTAContent } from "../types";

export const pageTitle = "About John Sambrook";
export const pageDescription =
  "John Sambrook is a healthcare systems architect based in Kirkland, Washington, with 30+ years of systems engineering experience including medical device development. He applies Theory of Constraints methodology to help healthcare organizations across Washington State resolve operational bottlenecks.";

export const header: PageHeader = {
  label: "About",
  heading: "John Sambrook",
  subheading:
    "Healthcare systems architect helping hospital and health system leaders identify and resolve the operational constraints that stall progress, drain staff, and erode margins.",
};

export const content: ContentBlock[] = [
  {
    text: "Common Sense Systems was founded in 1996 by John Sambrook, a systems engineer who spent decades building safety-critical embedded software for medical devices before turning that same discipline toward the organizations that use them. Based in Kirkland, Washington, the practice serves healthcare organizations across the Puget Sound region, throughout Washington State, and across the Pacific Northwest.",
    lead: true,
  },
  {
    text: "John\u2019s engineering career includes significant work at SonoSite, where he developed software for portable ultrasound systems, and at Verasonics, working on research ultrasound platforms. Earlier roles involved defibrillators and other Class C medical devices, with deep expertise in real-time operating systems, device drivers, and QA/regulatory affairs. This background gives him an unusual ability to see healthcare operations as systems \u2014 with inputs, outputs, constraints, and feedback loops \u2014 rather than as collections of departments and personalities.",
  },
  {
    text: "In the 1990s, John trained directly under Eli Goldratt, the creator of Theory of Constraints, earning his Jonah certification at Washington State University. That training shaped his core method: find the constraint, understand the conflict that sustains it, and design a solution that resolves the conflict without compromise. It is a rigorous, logical approach that cuts through the political fog that often surrounds operational problems in hospitals and health systems.",
  },
  {
    text: "Today, John works with hospital executives, medical staff leadership, and boards on problems that span departmental boundaries \u2014 complex discharge bottlenecks, surgical capacity constraints, workforce allocation conflicts, and the structural policy contradictions that keep these problems stuck. His approach combines AI-assisted analysis of operational data and policy documents with the kind of structured reasoning that surfaces root causes rather than symptoms.",
  },
  {
    text: "John is known for showing up well in meetings, asking the questions that reframe stalled conversations, and recognizing good work when he sees it \u2014 praising people for what they actually accomplished rather than offering empty flattery. He believes consultants should build their clients\u2019 capability, not their own dependency.",
  },
  {
    text: "Common Sense Systems primarily serves healthcare organizations in Washington State \u2014 including community hospitals, regional health systems, critical access hospitals, and specialty groups \u2014 with additional work across Oregon, Idaho, and Montana. Most engagements run two to six weeks with fixed fees and explicit deliverables.",
  },
];

export const cta: CTAContent = {
  headline: "Want to learn more?",
  description:
    "Let us know what you are trying to solve and we will propose a path forward.",
  primaryCta: { text: "Start a Conversation", href: "https://calendar.app.google/wgWnth98gdaNvN5aA" },
  secondaryCta: { text: "Our Approach", href: "/approach" },
};
