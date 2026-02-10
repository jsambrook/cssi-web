import type { HeroBullet, FeatureItem, CTAContent } from "../types";

export const hero = {
  headline: "Make Progress on the Issues That Matter",
  subheadline:
    "When division, stalled decisions, and cross-functional deadlocks consume your leadership bandwidth\u2014there's a different approach.",
  bullets: [
    { bold: "No comprehensive decks.", text: "Decision-ready artifacts instead of reports." },
    { bold: "No scope creep.", text: "Fixed fees, clear deliverables, explicit timelines." },
    { bold: "No dependency.", text: "Building your capability, not ours." },
  ] satisfies HeroBullet[],
  primaryCta: { text: "Book a Consultation", href: "/contact" },
  secondaryCta: { text: "Learn More", href: "/approach" },
};

export const featuresSection = {
  label: "Our Approach",
  heading: "A Different Way Forward",
  subheading:
    "We focus on decision-making processes and organizational capability\u2014not comprehensive reports that gather dust.",
};

export const features: FeatureItem[] = [
  {
    title: "Frame the Problem",
    description:
      "Co-author the real problem, decision boundaries, and stakeholders before jumping to solutions.",
  },
  {
    title: "Build Shared Facts",
    description:
      "Establish a minimum dataset everyone trusts. Joint fact-finding beats premature solutions.",
  },
  {
    title: "Design Decisions",
    description:
      "Map options, trade-offs, and owners. Make the implicit explicit with clear accountability.",
  },
  {
    title: "Ship & Learn",
    description:
      "Run short cycles, measure outcomes, adjust course. Fast feedback prevents drift.",
  },
];

export const cta: CTAContent = {
  headline: "Ready to Move Forward?",
  description:
    "Start with a 30-minute conversation. No pitch, no obligation. Just a practical discussion about what's actually blocking progress.",
  primaryCta: { text: "Schedule a Call", href: "/contact" },
  secondaryCta: { text: "Learn More", href: "/approach" },
  footnote: "Serving hospitals, health systems, and healthcare organizations across Washington, Oregon, Idaho, and Montana",
};
