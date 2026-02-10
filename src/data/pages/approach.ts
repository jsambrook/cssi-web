import type { PageHeader, GridItem, CTAContent } from "../types";

export const pageTitle = "Our Approach to Healthcare Consulting";
export const pageDescription =
  "A practical, fixed-fee consulting approach for healthcare organizations in Washington State. We use Theory of Constraints methodology to frame problems, build shared facts, and design decisions that resolve operational bottlenecks -- not reports that gather dust.";

export const header: PageHeader = {
  label: "Approach",
  heading: "A Different Way to Work Together",
  subheading:
    "A practical, low-risk approach designed around what actually creates progress in healthcare organizations -- not what maximizes billable hours.",
};

export const steps: GridItem[] = [
  {
    title: "Discovery & Alignment",
    description:
      "Co-author the real problem, decision boundaries, and stakeholders before jumping to solutions. Surface actual risk appetites and frame choices as explicit trade-offs.",
  },
  {
    title: "Joint Fact-Finding",
    description:
      "Establish a minimum dataset everyone trusts. Run facilitated sessions that create shared problem definitions before solving. Joint fact-finding beats premature solutions.",
  },
  {
    title: "Decision Design",
    description:
      "Map options, trade-offs, and owners explicitly. Make the implicit explicit with clear accountability. Design governance that aligns\u2014not fragments.",
  },
  {
    title: "Action & Feedback",
    description:
      "Run short cycles, measure outcomes, adjust course. Fast feedback prevents drift. Identify high-leverage changes you can execute credibly.",
  },
];

export const cta: CTAContent = {
  headline: "Ready to move forward?",
  description:
    "Start with a focused discovery call. No pitch, just clarity about what's actually blocking progress.",
  primaryCta: { text: "Schedule a Call", href: "https://calendar.app.google/wgWnth98gdaNvN5aA" },
  secondaryCta: { text: "About Us", href: "/about" },
  footnote: "Serving hospitals, health systems, and healthcare organizations across Washington, Oregon, Idaho, and Montana",
};
