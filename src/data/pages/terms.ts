import type { LegalBlock } from '../types';

export const pageTitle = 'Terms of Use';
export const pageDescription = 'Terms of Use for the Common Sense Systems, Inc. website.';

export const lastUpdated = 'September 29, 2025';

export const content: LegalBlock[] = [
  { type: 'heading', text: 'Acceptance of Terms', level: 2 },
  {
    type: 'text',
    html: 'By accessing and using the Common Sense Systems, Inc. website ("Site"), you accept and agree to be bound by these Terms of Use. If you do not agree to these terms, please do not use the Site.',
  },

  { type: 'heading', text: 'Use of Site Content', level: 2 },
  {
    type: 'text',
    html: 'All content on this Site, including text, graphics, logos, and software, is the property of Common Sense Systems, Inc. or its licensors and is protected by copyright and other intellectual property laws.',
  },
  { type: 'text', html: 'You may:' },
  {
    type: 'list',
    items: [
      'View and download content for personal, non-commercial use',
      'Share links to our essays and blog posts',
      'Quote brief excerpts with proper attribution',
    ],
  },
  { type: 'text', html: 'You may not:' },
  {
    type: 'list',
    items: [
      'Reproduce, distribute, or create derivative works without permission',
      'Use content for commercial purposes without authorization',
      'Remove copyright or attribution notices',
    ],
  },

  { type: 'heading', text: 'Advisory Nature of Services', level: 2 },
  {
    type: 'text',
    html: 'The information and services provided through this Site are advisory in nature. Common Sense Systems provides strategic guidance and decision-making support to healthcare organizations. We do not:',
  },
  {
    type: 'list',
    items: [
      'Provide medical advice or clinical recommendations',
      'Make operational decisions on behalf of client organizations',
      'Guarantee specific outcomes or results',
      'Serve as a covered entity or business associate under HIPAA',
    ],
  },

  { type: 'heading', text: 'No Medical Advice', level: 2 },
  {
    type: 'text',
    html: '<strong>Important:</strong> Nothing on this Site constitutes medical advice, diagnosis, or treatment. Our services address organizational governance, decision-making processes, and strategic planning\u2014not clinical care. Always consult qualified healthcare professionals for medical decisions.',
  },

  { type: 'heading', text: 'User Conduct', level: 2 },
  { type: 'text', html: 'You agree not to:' },
  {
    type: 'list',
    items: [
      'Use the Site for any unlawful purpose',
      'Submit false, misleading, or fraudulent information',
      'Transmit viruses, malware, or harmful code',
      'Attempt to gain unauthorized access to Site systems',
      "Interfere with other users' access to the Site",
      'Submit protected health information (PHI) through non-secure channels',
    ],
  },

  { type: 'heading', text: 'Third-Party Links and Services', level: 2 },
  {
    type: 'text',
    html: 'This Site may contain links to third-party websites and services (e.g., Calendly for scheduling). We are not responsible for the content, privacy practices, or terms of these external sites. Use of third-party services is subject to their respective terms and policies.',
  },

  { type: 'heading', text: 'Disclaimer of Warranties', level: 2 },
  {
    type: 'text',
    html: 'The Site and its content are provided "as is" without warranties of any kind, either express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, or non-infringement.',
  },
  {
    type: 'text',
    html: 'We do not warrant that the Site will be uninterrupted, error-free, or free of viruses or other harmful components.',
  },

  { type: 'heading', text: 'Limitation of Liability', level: 2 },
  {
    type: 'text',
    html: 'To the fullest extent permitted by law, Common Sense Systems, Inc., its officers, directors, employees, and agents shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising from your use of the Site or services.',
  },

  { type: 'heading', text: 'Indemnification', level: 2 },
  {
    type: 'text',
    html: 'You agree to indemnify and hold harmless Common Sense Systems, Inc. from any claims, losses, damages, or expenses (including legal fees) arising from your use of the Site or violation of these Terms.',
  },

  { type: 'heading', text: 'Privacy', level: 2 },
  {
    type: 'text',
    html: 'Your use of the Site is also governed by our <a href="/legal/privacy" class="text-primary hover:text-primary/80">Privacy Policy</a>. Please review it to understand our data practices.',
  },

  { type: 'heading', text: 'Modifications to Terms', level: 2 },
  {
    type: 'text',
    html: 'We reserve the right to modify these Terms at any time. Changes will be posted on this page with an updated "Last updated" date. Continued use of the Site constitutes acceptance of modified Terms.',
  },

  { type: 'heading', text: 'Governing Law', level: 2 },
  {
    type: 'text',
    html: 'These Terms are governed by the laws of the State of Washington, United States, without regard to conflict of law principles. Any disputes shall be resolved in the courts of Washington.',
  },

  { type: 'heading', text: 'Severability', level: 2 },
  {
    type: 'text',
    html: 'If any provision of these Terms is found to be unenforceable, the remaining provisions shall remain in full force and effect.',
  },

  { type: 'heading', text: 'Contact Information', level: 2 },
  { type: 'text', html: 'For questions about these Terms, contact us at:' },
  {
    type: 'list',
    items: ['Email: contact@common-sense.com', 'Phone: (425) 979-2282'],
  },
];
