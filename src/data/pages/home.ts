import type { HeroBullet, FeatureItem, TestimonialItem, CTAContent } from "../types";

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

export const testimonialsSection = {
  label: "What Leaders Say",
  heading: "Trusted by Healthcare Executives",
};

export const testimonials: TestimonialItem[] = [
  {
    quote:
      "John cuts through the complexity. He helped us make a decision we'd been stalling on for months.",
    author: "SM",
    company: "COO, 180-bed community hospital, Eastern Washington",
    initials: "SM",
  },
  {
    quote:
      "Finally, a consultant who understands that we don't need another strategic plan. We needed someone to help us execute.",
    author: "RK",
    company: "CEO, rural healthcare system, Oregon",
    initials: "RK",
  },
  {
    quote:
      "He asked better questions than our last three consultants combined. We saved six months of committee meetings.",
    author: "JL",
    company: "Board Chair, critical access hospital, Idaho",
    initials: "JL",
  },
];

export const cta: CTAContent = {
  headline: "Ready to Move Forward?",
  description:
    "Start with a 30-minute conversation. No pitch, no obligation. Just a practical discussion about what's actually blocking progress.",
  primaryCta: { text: "Schedule a Call", href: "/contact" },
  secondaryCta: { text: "Learn More", href: "/approach" },
  footnote: "Serving community hospitals across Washington, Oregon, Idaho, and Montana",
};
