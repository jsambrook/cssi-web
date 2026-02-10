import type { PageHeader, CTAContent } from "../types";

export const pageTitle = "Contact Us in Kirkland, WA";
export const pageDescription =
  "Schedule a free consultation with John Sambrook at Common Sense Systems in Kirkland, Washington. Healthcare operations consulting for hospitals and health systems across the Puget Sound region and Washington State.";

export const header: PageHeader = {
  label: "Contact",
  heading: "Get in Touch",
  subheading:
    "Let's discuss your situation. No obligation, no sales pitch\u2014just a conversation about whether we can help.",
};

export const contactGrid = {
  discoveryCall: {
    heading: "Discovery Call",
    description: "Book a free call to discuss your situation and whether we can help.",
    linkText: "Schedule a Call",
    href: "https://calendar.app.google/wgWnth98gdaNvN5aA",
  },
  phone: {
    heading: "Phone",
    description: "Available Monday through Friday, 9 AM to 5 PM Pacific.",
  },
  email: {
    heading: "Email",
    description: "For general inquiries or to share background before a call.",
  },
  location: {
    heading: "Location",
    description: "Kirkland, WA \u2014 serving healthcare systems throughout Washington State.",
  },
  availability: {
    heading: "Availability",
    description:
      "We respond within one business day and can typically schedule an initial conversation within a week.",
  },
  linkedin: {
    heading: "Connect on LinkedIn",
    description: "Follow our healthcare systems insights and updates.",
    linkText: "View Profile",
    href: "https://www.linkedin.com/in/johnsambrook/",
  },
};

export const cta: CTAContent = {
  headline: "Not Sure Where to Start?",
  description:
    "Book a free call. We\u2019ll listen to what\u2019s going on and tell you honestly whether we can help.",
  primaryCta: { text: "Schedule a Call", href: "https://calendar.app.google/wgWnth98gdaNvN5aA" },
  secondaryCta: { text: "Our Approach", href: "/approach" },
};
