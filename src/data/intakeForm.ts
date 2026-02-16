import type { IntakeFormConfig } from './types';

export const intakeFormConfig: IntakeFormConfig = {
  steps: [
    {
      id: 'challenge',
      question: "What's your primary challenge?",
      subtitle: "Select the issue that's consuming the most leadership bandwidth",
      inputType: 'select',
      options: [
        {
          id: 'ai-tech',
          icon: '🤖',
          title: 'AI/Tech Deployment',
          description: 'Deciding how to evaluate, pilot, or scale AI solutions safely',
        },
        {
          id: 'gridlock',
          icon: '🔒',
          title: 'Decision Gridlock',
          description: 'Critical decisions stall due to disagreement or unclear authority',
        },
        {
          id: 'alignment',
          icon: '🎯',
          title: 'Strategic Alignment',
          description: 'Leadership team not aligned on priorities or direction',
        },
        {
          id: 'cross-functional',
          icon: '🔀',
          title: 'Cross-Functional Issues',
          description: 'Persistent problems spanning multiple departments',
        },
        {
          id: 'governance',
          icon: '🏛️',
          title: 'Board Governance',
          description: 'Board-level decision processes or oversight frameworks',
        },
        {
          id: 'multiple',
          icon: '❓',
          title: 'Not Sure / Multiple',
          description: 'Multiple challenges or unclear which is most critical',
        },
      ],
    },
    {
      id: 'situation',
      question: 'Tell us about your situation',
      subtitle: 'This helps us tailor our approach',
      inputType: 'select',
      options: [
        {
          id: 'starting',
          icon: '🌱',
          title: 'Just Getting Started',
          description: "We know we need help but haven't begun",
        },
        {
          id: 'stalled',
          icon: '🚧',
          title: 'Stalled Initiative',
          description: 'We started but hit a wall',
        },
        {
          id: 'scaling',
          icon: '🚀',
          title: 'Ready to Scale',
          description: 'Things are working — we need to grow',
        },
        {
          id: 'crisis',
          icon: '⚡',
          title: 'Urgent Situation',
          description: 'We need to act fast on a pressing issue',
        },
      ],
    },
    {
      id: 'timeline',
      question: 'How urgent is this?',
      subtitle: "We'll prioritize accordingly",
      inputType: 'select',
      options: [
        {
          id: 'asap',
          icon: '🔥',
          title: 'ASAP',
          description: 'We need to move this week',
        },
        {
          id: 'month',
          icon: '📅',
          title: 'This Month',
          description: 'Important but not an emergency',
        },
        {
          id: 'quarter',
          icon: '🗓️',
          title: 'This Quarter',
          description: 'Planning ahead for the next few months',
        },
        {
          id: 'exploring',
          icon: '🔍',
          title: 'Just Exploring',
          description: 'Researching options for the future',
        },
      ],
    },
    {
      id: 'contact',
      question: 'Where should we send your insights?',
      subtitle: "We'll follow up with a personalized action plan",
      inputType: 'email',
      placeholder: 'you@hospital.org',
      required: true,
    },
  ],
  footerText: 'Get immediate insights tailored to your challenge',
  submitButtonText: 'Get My Insights',
  successMessage: 'Thanks! Check your inbox for personalized insights.',
  formspree: {
    endpoint: 'https://formspree.io/f/xwpkdjkl',
    fieldNames: {
      challenge: 'Primary Challenge',
      situation: 'Situation',
      timeline: 'Timeline',
      contact_name: 'Name',
      contact_email: 'Email',
    },
  },
};
