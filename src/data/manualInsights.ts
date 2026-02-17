import type { ManualInsight } from './types';

export function getManualInsight(slug: string): ManualInsight {
  const insight = manualInsights.find((i) => i.slug === slug);
  if (!insight) throw new Error(`No manual insight with slug "${slug}"`);
  return insight;
}

export const manualInsights: ManualInsight[] = [
  {
    slug: 'pacp',
    title: 'The Post-Acute Care Plan (PACP)',
    description:
      'A proactive approach to discharge readiness that treats discharge delays as an input quality problem, not a process problem.',
    date: new Date('2026-02-16'),
    author: 'John Sambrook',
    tags: ['Healthcare', 'Patient Flow', 'Theory of Constraints'],
    ogImage: '/images/og-default.png',
  },
  {
    slug: 'nursing-conflict',
    title: 'Structural Conflicts in WA State Nursing Agreements',
    description:
      "Analysis of 134 structural conflicts across 10 Washington State nursing CBAs reveals why higher wages aren't fixing nurse burnout.",
    date: new Date('2026-02-16'),
    author: 'John Sambrook',
    tags: ['Labor Relations', 'Healthcare', 'Theory of Constraints'],
    ogImage: '/images/og-default.png',
  },
];
