import type { PageHeader, ContentBlock, CTAContent } from "../types";

export const pageTitle = "About";
export const pageDescription =
  "Founded by John Sambrook, Common Sense Systems helps community hospital leaders in Washington, Oregon, Idaho, and Montana resolve complex operational problems using Theory of Constraints and systems thinking.";

export const header: PageHeader = {
  label: "About",
  heading: "Common Sense Systems",
  subheading:
    "A healthcare consulting practice helping community hospital leaders make progress on complex, divisive problems through rigorous reasoning and collaborative problem-solving.",
};

export const content: ContentBlock[] = [
  {
    text: "Common Sense Systems was founded by John Sambrook after years watching smart leaders struggle with stalled initiatives and cross-functional gridlock in community hospitals.",
    lead: true,
  },
  {
    text: "The practice is built around a simple premise: help hospitals make real progress on what matters most. Not through comprehensive reports or elaborate strategic plans, but through rigorous problem-framing, joint fact-finding, and decision-ready artifacts.",
  },
  {
    text: "John brings mediation and negotiation training, healthcare operations experience, and technology implementation expertise to every engagement. Based in the Pacific Northwest, Common Sense Systems primarily serves community hospitals across Washington, Oregon, Idaho, and Montana.",
  },
  {
    text: "Our principles guide every engagement: integrity over optics, practical over perfect, small bets and short loops, and privacy-first by default. Most projects run 2\u20136 weeks. We start small and prove value quickly.",
  },
];

export const cta: CTAContent = {
  headline: "Want to learn more?",
  description:
    "Let us know what you are trying to solve and we will propose a path forward.",
  primaryCta: { text: "Start a Conversation", href: "/contact" },
  secondaryCta: { text: "Our Approach", href: "/approach" },
};
