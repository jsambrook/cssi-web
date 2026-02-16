import type { PageHeader, ContentBlock, CTAContent } from '../types';

export const pageTitle = 'About John Sambrook';
export const pageDescription =
  'Systems architect applying Theory of Constraints to help organizations across healthcare, manufacturing, and technology resolve operational bottlenecks.';

export const header: PageHeader = {
  label: 'About',
  heading: 'John Sambrook',
  subheading:
    'Practical, focused, effective expertise. Helping organizations rapidly identify and resolve the constraints that stall progress, drain staff, and erode margins.',
};

export const content: ContentBlock[] = [
  {
    text: 'Common Sense Systems was founded in 1996 by John Sambrook, a systems engineer who spent decades building safety-critical embedded software for medical devices before turning that same discipline toward the organizations and businesses that need it most. Based in Kirkland, Washington, the practice helps organizations across healthcare, manufacturing, and technology identify their real constraints and make measurable progress, whether the problem is operational, structural, or strategic.',
    lead: true,
  },
  {
    text: 'John\u2019s engineering career includes significant work at SonoSite, where he developed software for portable ultrasound systems, and at Verasonics, working on research ultrasound platforms. Earlier roles involved defibrillators and other Class C medical devices, with deep expertise in real-time operating systems, device drivers, and QA/regulatory affairs. This background gives him an unusual ability to see operations as systems, with inputs, outputs, constraints, and feedback loops, rather than as collections of departments and personalities.',
  },
  {
    text: 'In the 1990s, John studied Theory of Constraints extensively under Eli Goldratt, attending his conferences, participating in TOC for Education, and earning his Jonah certification at Washington State University. That training shaped his core method: find the constraint, understand the conflict that sustains it, and design a solution that resolves the conflict without compromise. It is a rigorous, logical approach that cuts through the political fog that often surrounds operational problems in any organization. John is drawn to the problems that everyone else has written off as unsolvable or accepted as just the way things are. He doesn\u2019t accept that the status quo is the best we can do.',
  },
  {
    text: 'Today, John works with executives, leadership teams, and boards on problems that span departmental boundaries: complex discharge bottlenecks in hospitals, sales process breakdowns, workforce allocation conflicts, regulatory compliance challenges, and the structural policy contradictions that keep these problems stuck. His approach combines AI-assisted analysis of operational data and policy documents with the kind of structured reasoning that surfaces root causes rather than symptoms.',
  },
  {
    text: 'John is known for showing up well in meetings, asking the questions that reframe stalled conversations, and recognizing good work when he sees it, praising people for what they actually accomplished rather than offering empty flattery. He believes consultants should build their clients\u2019 capability, not their own dependency.',
  },
  {
    text: 'Common Sense Systems primarily serves organizations in Washington State, with additional work across the Pacific Northwest. Engagements range from focused constraint analyses and process automation projects to ongoing advisory relationships. Most run two to six weeks with fixed fees and explicit deliverables.',
  },
];

export const cta: CTAContent = {
  headline: 'Want to learn more?',
  description: 'Let us know what you are trying to solve and we will propose a path forward.',
  primaryCta: {
    text: 'Start a Conversation',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  secondaryCta: { text: 'Our Approach', href: '/approach' },
};
