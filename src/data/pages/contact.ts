import type { PageHeader, CTAContent, ContactGrid } from '../types';

export const pageTitle = 'Contact Us in Kirkland, WA';
export const pageDescription =
  'Schedule a free consultation with Common Sense Systems in Kirkland, WA. We help organizations find and break the constraint that blocks throughput.';

export const header: PageHeader = {
  label: 'Contact',
  heading: 'Get in Touch',
  subheading:
    "Let's discuss your situation. No obligation, no sales pitch\u2014just a conversation about whether we can help.",
};

export const contactGrid: ContactGrid = {
  discoveryCall: {
    heading: 'Schedule a Meeting',
    description:
      'Schedule a meeting with John. It might be an initial conversation to explore your situation, or a regular ongoing meeting.',
    linkText: 'Schedule a Meeting',
    href: 'https://calendar.app.google/wgWnth98gdaNvN5aA',
  },
  phone: {
    heading: 'Telephone Call',
    description:
      'Call Mark, our AI voice agent. Mark can answer questions about our services, help you get oriented, or schedule a meeting with John.',
  },
  email: {
    heading: 'Email',
    description:
      'For general inquiries, to share background information, or to send materials ahead of a scheduled meeting. We typically respond within one business day.',
  },
  location: {
    heading: 'Location',
    description:
      'We serve organizations throughout Washington State. Located in the Totem Lake area, near I-405 and NE 128th Street.',
    linkText: 'Open in Google Maps',
    href: 'https://www.google.com/maps/search/?api=1&query=11227+NE+128+ST+Kirkland+WA+98034',
  },
};

export const cta: CTAContent = {
  headline: 'Not Sure Where to Start?',
  description:
    'Book a free meeting. We\u2019ll listen to what\u2019s going on and tell you honestly whether we can help.',
  primaryCta: { text: 'Schedule a Meeting', href: 'https://calendar.app.google/wgWnth98gdaNvN5aA' },
  secondaryCta: { text: 'Our Approach', href: '/approach' },
};
