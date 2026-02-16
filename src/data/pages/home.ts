import type {
  HeroBullet,
  FeatureItem,
  CTAContent,
  ServiceCardItem,
  Industry,
  AmbitionCard,
} from '../types';

export const hero = {
  headline: 'Break the Constraint. Scale the Flow.',
  subheadline:
    'We architect Unrefusable Offers and operational velocity for organizations that are tired of incremental growth. Serving Healthcare, MedTech, and Embedded Systems.',
  bullets: [
    { bold: 'No comprehensive decks.', text: 'Decision-ready artifacts instead of reports.' },
    { bold: 'No scope creep.', text: 'Fixed fees, clear deliverables, explicit timelines.' },
    { bold: 'No dependency.', text: 'Building your capability, not ours.' },
  ] satisfies HeroBullet[],
  primaryCta: {
    text: 'Book a Consultation',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  secondaryCta: { text: 'Learn More', href: '/approach' },
};

export const ambitionCards: AmbitionCard[] = [
  {
    label: 'ACCELERATE',
    text: 'We need to move 2x faster in R&D and Ops (The Drum-Buffer-Rope).',
    scrollTarget: 'service-flow-dynamics',
  },
  {
    label: 'DOMINATE',
    text: 'We need to change the rules of our market (The Mafia Offer).',
    scrollTarget: 'service-market-offer',
  },
  {
    label: 'UNIFY',
    text: 'We need Sales, Ops, and R&D to stop fighting (The Thinking Processes).',
    scrollTarget: 'service-synchronization',
  },
];

export const featuresSection = {
  label: 'Our Approach',
  heading: 'A Different Way Forward',
  subheading:
    'We focus on decision-making processes and organizational capability\u2014not comprehensive reports that gather dust.',
};

export const features: FeatureItem[] = [
  {
    title: 'Frame the Problem',
    description:
      'Co-author the real problem, decision boundaries, and stakeholders before jumping to solutions.',
  },
  {
    title: 'Build Shared Facts',
    description:
      'Establish a minimum dataset everyone trusts. Joint fact-finding beats premature solutions.',
  },
  {
    title: 'Design Decisions',
    description:
      'Map options, trade-offs, and owners. Make the implicit explicit with clear accountability.',
  },
  {
    title: 'Ship & Learn',
    description: 'Run short cycles, measure outcomes, adjust course. Fast feedback prevents drift.',
  },
];

export const defaultIndustry: Industry = 'healthcare';

export const serviceCards: ServiceCardItem[] = [
  {
    id: 'flow-dynamics',
    color: 'orange',
    variants: {
      healthcare: {
        title: 'Accelerate Patient Flow & Slash Length of Stay',
        description:
          'Identify the hidden constraints in your patient pathway. We help you unlock inpatient capacity and eliminate ED boarding without adding staff.',
      },
      tech: {
        title: 'Accelerate R&D & Slash Time-to-Market',
        description:
          "Stop managing the backlog; eliminate it. We identify the bottleneck in your dev cycle to shrink the time from 'commit' to 'cash'.",
      },
    },
  },
  {
    id: 'market-offer',
    color: 'blue',
    variants: {
      healthcare: {
        title: 'Direct-to-Employer Contracting & Network Integrity',
        description:
          "Stop competing on commoditized rates. We design 'Unrefusable Offers' for local employers that bypass insurance friction and secure volume.",
      },
      tech: {
        title: 'Risk-Shared Licensing & Recurring Revenue Models',
        description:
          'Move beyond feature wars. We structure licensing and pricing models that align perfectly with customer utility, making your product the obvious financial choice.',
      },
    },
  },
  {
    id: 'synchronization',
    color: 'green',
    variants: {
      healthcare: {
        title: 'Unify ED, Inpatient, and Discharge Teams',
        description:
          'Eliminate the friction between departments. We align clinical and operational incentives so the entire hospital moves as one synchronized system.',
      },
      tech: {
        title: 'Align Product Roadmaps with Sales Promises',
        description:
          'End the war between Sales and Engineering. We implement the operational handshake that ensures you can actually deliver what you sell, every time.',
      },
    },
  },
];

export const cta: CTAContent = {
  headline: 'Ready to Move Forward?',
  description:
    "Start with a conversation. No pitch, no obligation. Just a practical discussion about what's actually blocking progress.",
  primaryCta: { text: 'Schedule a Meeting', href: 'https://calendar.app.google/wgWnth98gdaNvN5aA' },
  secondaryCta: { text: 'Learn More', href: '/approach' },
  footnote:
    'Serving hospitals, health systems, and healthcare organizations across Washington State',
};
