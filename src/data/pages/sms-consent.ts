import type { LegalBlock } from '../types';

export const pageTitle = 'SMS Consent & Privacy';
export const pageDescription =
  'How we obtain consent for SMS communications, what we send, and how to opt out.';

export const lastUpdated = 'February 20, 2026';

export const consentScript =
  'Hi [Name], this is [Agent] from Common Sense Systems, Inc. We\u2019d like to offer you the option of receiving text messages about your services, such as scheduling, reminders, and important updates, from our toll-free number +1 (833) 570-5023. Message and data rates may apply, and frequency varies. Text messages are entirely optional \u2014 you can still receive all updates and information by phone or email if you prefer. Would you like to also receive certain updates and reminders by text message from +1 (833) 570-5023? You can reply STOP anytime to opt out and HELP for support.';

export const content: LegalBlock[] = [
  { type: 'heading', text: 'How We Obtain SMS Consent', level: 2 },
  {
    type: 'text',
    html: 'We only send text messages to clients and prospects who have clearly agreed to receive them. Our primary consent methods are:',
  },

  { type: 'heading', text: 'Verbal Consent', level: 3 },
  {
    type: 'text',
    html: 'During a phone call with one of our voice agents, we use the following script:',
  },
  // The consent script blockquote is rendered separately in the page template.

  {
    type: 'text',
    html: 'If you agree, our agent records your consent in our database, including phone number, name (if provided), date/time, agent name/initials, call recording ID (when available), and consent source (Verbal or Keyword). A confirmation SMS is sent immediately.',
  },

  { type: 'heading', text: 'SMS Messages Are Entirely Optional', level: 3 },
  {
    type: 'text',
    html: '<strong>Important:</strong> SMS messages are entirely optional. You will continue to receive services and support even if you do not consent to text messaging.',
  },

  { type: 'heading', text: 'Keyword Opt-In', level: 3 },
  {
    type: 'text',
    html: 'You may also opt in by texting an explicit keyword (e.g., <strong>YES</strong>) to our toll-free number <strong>+1 (833) 570-5023</strong>.',
  },

  {
    type: 'text',
    html: '<em>We do not send marketing or promotional texts without explicit prior agreement.</em>',
  },

  { type: 'heading', text: 'Types of Messages You May Receive', level: 2 },
  {
    type: 'list',
    items: [
      'Appointment confirmations and reminders',
      'Service updates and notifications',
      'Contact information or follow-up details from a call',
      'Responses to your inquiries',
    ],
  },

  { type: 'heading', text: 'How to Revoke Your Consent', level: 2 },

  { type: 'heading', text: 'Text STOP (Fastest)', level: 3 },
  {
    type: 'text',
    html: 'Reply <strong>STOP</strong> to any message from <strong>+1 (833) 570-5023</strong>. You will <strong>immediately</strong> receive a confirmation that you\u2019ve been unsubscribed. For assistance, reply <strong>HELP</strong> to receive our support contact details. To resume messages after opting out, reply <strong>UNSTOP</strong>.',
  },

  { type: 'heading', text: 'Contact Us', level: 3 },
  {
    type: 'list',
    items: [
      'Call us (voice only): (425) 979-2282',
      'Email: <a href="mailto:info@common-sense.com">info@common-sense.com</a>',
      '<a href="/contact">Contact form</a>',
    ],
  },

  { type: 'heading', text: 'Important Information', level: 2 },
  {
    type: 'text',
    html: '<strong>Message Frequency.</strong> Typically 1\u20134 messages per month, unless you request additional updates.',
  },
  {
    type: 'text',
    html: '<strong>Message and Data Rates.</strong> Standard carrier message and data rates may apply. We do not charge for SMS messages.',
  },
  {
    type: 'text',
    html: '<strong>Supported Carriers.</strong> We work with all major U.S. carriers. Delivery and timing may vary by provider.',
  },
  {
    type: 'text',
    html: '<strong>Privacy.</strong> Your phone number and SMS preferences are protected under our <a href="/legal/privacy">privacy practices</a>. We do not share your information with third parties without your consent.',
  },

  { type: 'heading', text: 'Consent Workflow', level: 2 },
  {
    type: 'text',
    html: 'The diagram below shows how we obtain, record, and manage SMS consent:',
  },
  // The flow diagram image is rendered separately in the page template.

  { type: 'heading', text: 'Questions or Concerns?', level: 2 },
  {
    type: 'text',
    html: 'If you have any questions about our SMS consent practices or need help with your preferences, please contact us:',
  },
  {
    type: 'list',
    items: [
      'Phone (voice only): (425) 979-2282',
      'Email: <a href="mailto:info@common-sense.com">info@common-sense.com</a>',
      '<a href="/contact">Contact Us Online</a>',
    ],
  },
];
