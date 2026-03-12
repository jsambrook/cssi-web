import type { PageHeader, GridItem, CTAContent } from '../types';

export const pageTitle = 'Our Approach';
export const pageDescription =
  'Fixed-fee consulting using Theory of Constraints. We find what limits your system and fix it. You only pay if we deliver.';

export const header: PageHeader = {
  label: 'Approach',
  heading: 'A Different Way to Work Together',
  subheading:
    'A practical, low-risk approach designed around what actually creates progress -- not what maximizes billable hours.',
};

export const steps: GridItem[] = [
  {
    title: 'Discovery & Alignment',
    description:
      'Co-author the real problem, decision boundaries, and stakeholders before jumping to solutions. Surface actual risk appetites and frame choices as explicit trade-offs.',
  },
  {
    title: 'Joint Fact-Finding',
    description:
      'Establish a minimum dataset everyone trusts. Run facilitated sessions that create shared problem definitions before solving. Joint fact-finding beats premature solutions.',
  },
  {
    title: 'Decision Design',
    description:
      'Map options, trade-offs, and owners explicitly. Make the implicit explicit with clear accountability. Design governance that aligns\u2014not fragments.',
  },
  {
    title: 'Action & Feedback',
    description:
      'Run short cycles, measure outcomes, adjust course. Fast feedback prevents drift. Identify high-leverage changes you can execute credibly.',
  },
];

export const cta: CTAContent = {
  headline: 'Ready to move forward?',
  description:
    "Start with a focused discovery call. No pitch, just clarity about what's actually blocking progress.",
  primaryCta: {
    text: 'Book a Conversation',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  secondaryCta: { text: 'About Us', href: '/about' },
  footnote:
    'Common Sense Systems, Inc. | Kirkland, WA | Constraint analysis and offer strategy since 1996',
};
