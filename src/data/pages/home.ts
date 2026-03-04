import type { HeroBullet, CTAContent, AmbitionCard, ServiceOffer } from '../types';

export const hero = {
  headline: "Find it. Fix it. Or don't pay.",
  subheadline:
    'Every business has one constraint holding it back. We identify yours in weeks, not months. You only pay if we deliver.',
  bullets: [
    { bold: 'Fixed fee, fixed timeline.', text: 'Two to four weeks for a clear diagnosis.' },
    {
      bold: 'You carry zero risk.',
      text: 'Pay only when you agree the work was delivered as promised.',
    },
    { bold: 'No dependency.', text: 'We build your capability, not a recurring consulting bill.' },
  ] satisfies HeroBullet[],
  primaryCta: {
    text: 'Book a Conversation',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  secondaryCta: { text: 'See How It Works', href: '/approach' },
};

export const ambitionCards: AmbitionCard[] = [
  {
    label: 'STUCK',
    text: 'We have tried everything and nothing moves the needle.',
    scrollTarget: 'service-constraint-analysis',
  },
  {
    label: 'INVISIBLE',
    text: 'Our website gets traffic but the phone never rings.',
    scrollTarget: 'service-offer-analysis',
  },
  {
    label: 'GROWING',
    text: 'We are busy but not profitable, and we cannot figure out why.',
    scrollTarget: 'service-constraint-analysis',
  },
];

export const featuresSection = {
  label: 'Two Services',
  heading: 'Find It. Fix It.',
  subheading:
    'Both services follow the same structure: a fixed-fee diagnostic phase, then implementation priced at a fraction of the value it creates. You only pay if we deliver.',
};

export const serviceOffers: ServiceOffer[] = [
  {
    id: 'constraint-analysis',
    title: 'Constraint Analysis',
    problem:
      'Your organization is stuck. You have invested in improvement projects, hired consultants, reorganized teams. Nothing sticks. The system is not performing and you cannot pinpoint why.',
    what: 'We identify the single constraint limiting your system, the one thing that, once addressed, moves everything else. Then we help you fix it.',
    deliverable:
      'A focused report identifying the constraint, the evidence, the estimated impact of addressing it, and a recommended direction. Delivered in a working session.',
    timeline: '2 to 4 weeks',
    fee: '$15,000 fixed for the diagnosis. Implementation priced at 10-15% of the estimated value of the fix.',
  },
  {
    id: 'offer-analysis',
    title: 'Offer Analysis',
    problem:
      'Your website gets traffic but the phone does not ring. Your marketing looks right. Your service is good. But prospects cannot tell you apart from three other firms, so they choose on price or convenience.',
    what: 'We diagnose why your offer is invisible and build one that makes the right client feel foolish saying no. Then we help you deploy it across your website, sales process, and referral language.',
    deliverable:
      'An analysis identifying the core customer frustration your industry has accepted as normal, the hidden conflict in the market, and a proposed offer that resolves it.',
    timeline: '2 to 4 weeks',
    fee: '$15,000 fixed for the diagnosis. Implementation priced at 10-15% of estimated revenue impact.',
  },
];

export const guaranteeSection = {
  heading: 'The Guarantee',
  statement: 'Unless you agree that what was promised was what was delivered, there is no charge.',
  explanation:
    'Most consultants hedge their bets and shift risk to the customer. We invert that. Before work begins, we agree in writing on what "delivered" means. If we do not meet that standard, you owe nothing.',
  reasons: [
    {
      bold: 'We qualify carefully.',
      text: 'We analyze your business before the first meeting. If it is not a fit, we say so.',
    },
    {
      bold: 'The methodology works.',
      text: 'Thirty years of constraint analysis with the Theory of Constraints. Defensible logic, not opinions.',
    },
    {
      bold: 'AI-assisted analysis.',
      text: 'We compress timelines with tools we have built, so the economics work even if a prospect occasionally declines to pay.',
    },
  ],
};

export const cta: CTAContent = {
  headline: 'Start with a Conversation',
  description:
    'No pitch, no obligation. A practical thirty-minute discussion about what is actually blocking progress in your organization. If it is not a fit, we will tell you.',
  primaryCta: {
    text: 'Book a Conversation',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  secondaryCta: { text: 'Email Instead', href: 'mailto:john@common-sense.com' },
  footnote:
    'Common Sense Systems, Inc. | Kirkland, WA | Serving organizations of all sizes across industries',
};
