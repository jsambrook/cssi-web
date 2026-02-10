import type { LegalBlock } from "../types";

export const pageTitle = "Privacy Policy";
export const pageDescription =
  "Privacy Policy for Common Sense Systems, Inc. — how we collect, use, and protect your information.";

export const lastUpdated = "September 29, 2025";

export const content: LegalBlock[] = [
  { type: "heading", text: "Introduction", level: 2 },
  {
    type: "text",
    html: 'Common Sense Systems, Inc. ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or use our services.',
  },

  { type: "heading", text: "Information We Collect", level: 2 },

  { type: "heading", text: "Information You Provide", level: 3 },
  {
    type: "list",
    items: [
      "Contact information (name, email, phone number, organization)",
      "Professional information (role, organization details)",
      "Communications with us (contact forms, emails, voice agent interactions)",
      "Newsletter subscription preferences",
    ],
  },

  { type: "heading", text: "Automatically Collected Information", level: 3 },
  {
    type: "list",
    items: [
      "Website usage data via Google Analytics (pages visited, time spent, device type)",
      "IP addresses and browser information",
      "Cookies and similar tracking technologies",
    ],
  },

  { type: "heading", text: "How We Use Your Information", level: 2 },
  { type: "text", html: "We use the information we collect to:" },
  {
    type: "list",
    items: [
      "Respond to your inquiries and provide requested services",
      "Send newsletters and updates (with your consent)",
      "Improve our website and services",
      "Analyze website usage and trends",
      "Comply with legal obligations",
    ],
  },

  { type: "heading", text: "Voice Agent Data", level: 2 },
  {
    type: "text",
    html: "When you interact with our practice voice agent, we may capture and store audio recordings and transcripts with your explicit consent. This data is used solely to improve the agent's functionality and is retained for a limited period. We do not collect or store any personally identifiable information (PII) or protected health information (PHI) through the voice agent.",
  },

  { type: "heading", text: "Data Sharing and Disclosure", level: 2 },
  {
    type: "text",
    html: "We do not sell, rent, or trade your personal information. We may share information with:",
  },
  {
    type: "list",
    items: [
      "Service providers who assist with website hosting, analytics, and email services",
      "Legal authorities when required by law",
      "Professional advisors under confidentiality obligations",
    ],
  },

  { type: "heading", text: "Cookies", level: 2 },
  {
    type: "text",
    html: "We use cookies and similar technologies to improve your browsing experience and analyze site traffic. You can control cookie preferences through your browser settings.",
  },

  { type: "heading", text: "Data Retention", level: 2 },
  {
    type: "text",
    html: "We retain your personal information only as long as necessary to fulfill the purposes outlined in this policy, comply with legal obligations, or resolve disputes. Newsletter contacts are retained until you unsubscribe. Form submissions and voice agent data are retained according to our data retention schedule.",
  },

  { type: "heading", text: "Your Rights", level: 2 },
  { type: "text", html: "You have the right to:" },
  {
    type: "list",
    items: [
      "Access the personal information we hold about you",
      "Request correction of inaccurate information",
      "Request deletion of your information",
      "Opt out of marketing communications",
      "Object to certain data processing activities",
    ],
  },
  {
    type: "text",
    html: "To exercise these rights, contact us at contact@common-sense.com.",
  },

  { type: "heading", text: "Security", level: 2 },
  {
    type: "text",
    html: "We implement reasonable security measures to protect your information, including HTTPS encryption, secure hosting, and access controls. However, no internet transmission is completely secure, and we cannot guarantee absolute security.",
  },

  { type: "heading", text: "HIPAA Notice", level: 2 },
  {
    type: "text",
    html: "<strong>Important:</strong> This website is not a HIPAA-compliant platform. Do not submit any protected health information (PHI) through our contact forms, voice agent, or email. If your inquiry involves PHI, we will arrange alternative, secure communication channels.",
  },

  { type: "heading", text: "Third-Party Links", level: 2 },
  {
    type: "text",
    html: "Our website may contain links to third-party sites. We are not responsible for the privacy practices of these external sites. We encourage you to review their privacy policies.",
  },

  { type: "heading", text: "Children's Privacy", level: 2 },
  {
    type: "text",
    html: "Our services are not directed to individuals under 18. We do not knowingly collect personal information from children.",
  },

  { type: "heading", text: "Changes to This Policy", level: 2 },
  {
    type: "text",
    html: 'We may update this Privacy Policy periodically. Changes will be posted on this page with an updated "Last updated" date. Continued use of our website constitutes acceptance of the updated policy.',
  },

  { type: "heading", text: "Contact Us", level: 2 },
  { type: "text", html: "If you have questions about this Privacy Policy, contact us at:" },
  {
    type: "list",
    items: ["Email: contact@common-sense.com", "Phone: (425) 979-2282"],
  },
];
