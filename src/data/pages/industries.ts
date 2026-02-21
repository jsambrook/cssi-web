import type { PageHeader, CTAContent, ColorVariant } from '../types';

export interface IndustryServiceCard {
  category: string;
  title: string;
  description: string;
  color: ColorVariant;
}

export interface IndustryPageData {
  pageTitle: string;
  pageDescription: string;
  header: PageHeader;
  sectionHeading: string;
  serviceCards: IndustryServiceCard[];
  cta: CTAContent;
}

export const industries: Record<string, IndustryPageData> = {
  healthcare: {
    pageTitle: 'Healthcare Consulting Services',
    pageDescription:
      'Constraint analysis for hospitals and health systems. Accelerate patient flow, slash length of stay, and unify clinical teams. Kirkland, WA.',
    header: {
      label: 'Healthcare',
      heading: 'Operational Architecture for Health Systems',
      subheading:
        'We help hospitals and health systems break operational bottlenecks, accelerate patient flow, and design market offers that bypass insurance friction.',
    },
    sectionHeading: 'How We Help Health Systems',
    serviceCards: [
      {
        category: 'Flow Dynamics & Throughput',
        title: 'Accelerate Patient Flow & Slash Length of Stay',
        description:
          'Identify the hidden constraints in your patient pathway. We help you unlock inpatient capacity and eliminate ED boarding without adding staff.',
        color: 'orange',
      },
      {
        category: 'Market Offer Architecture',
        title: 'Direct-to-Employer Contracting & Network Integrity',
        description:
          "Stop competing on commoditized rates. We design 'Unrefusable Offers' for local employers that bypass insurance friction and secure volume.",
        color: 'blue',
      },
      {
        category: 'Synchronization & Alignment',
        title: 'Unify ED, Inpatient, and Discharge Teams',
        description:
          'Eliminate the friction between departments. We align clinical and operational incentives so the entire hospital moves as one synchronized system.',
        color: 'green',
      },
    ],
    cta: {
      headline: 'Ready to Move Forward?',
      description:
        "Start with a conversation. No pitch, no obligation. Just a practical discussion about what's actually blocking progress in your health system.",
      primaryCta: {
        text: 'Schedule a Meeting',
        href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
      },
      secondaryCta: { text: 'Learn More', href: '/approach' },
      footnote:
        'Serving hospitals, health systems, and healthcare organizations across Washington State',
    },
  },

  tech: {
    pageTitle: 'Technology Consulting Services',
    pageDescription:
      'Constraint analysis for tech and product teams. Accelerate R&D, structure risk-shared licensing, and align product roadmaps with sales commitments.',
    header: {
      label: 'Technology',
      heading: 'Operational Architecture for Tech & Product Teams',
      subheading:
        'We help technology companies break R&D bottlenecks, design risk-shared licensing models, and align product roadmaps with sales promises.',
    },
    sectionHeading: 'How We Help Tech & Product Teams',
    serviceCards: [
      {
        category: 'Flow Dynamics & Throughput',
        title: 'Accelerate R&D & Slash Time-to-Market',
        description:
          "Stop managing the backlog; eliminate it. We identify the bottleneck in your dev cycle to shrink the time from 'commit' to 'cash'.",
        color: 'orange',
      },
      {
        category: 'Market Offer Architecture',
        title: 'Risk-Shared Licensing & Recurring Revenue Models',
        description:
          'Move beyond feature wars. We structure licensing and pricing models that align perfectly with customer utility, making your product the obvious financial choice.',
        color: 'blue',
      },
      {
        category: 'Synchronization & Alignment',
        title: 'Align Product Roadmaps with Sales Promises',
        description:
          'End the war between Sales and Engineering. We implement the operational handshake that ensures you can actually deliver what you sell, every time.',
        color: 'green',
      },
    ],
    cta: {
      headline: 'Ready to Move Forward?',
      description:
        "Start with a conversation. No pitch, no obligation. Just a practical discussion about what's actually blocking progress on your product team.",
      primaryCta: {
        text: 'Schedule a Meeting',
        href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
      },
      secondaryCta: { text: 'Learn More', href: '/approach' },
      footnote: 'Serving technology and product organizations across the Pacific Northwest',
    },
  },
};
