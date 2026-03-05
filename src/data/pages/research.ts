import type { PageHeader } from '../types';

export interface ResearchPaperCard {
  title: string;
  summary: string;
  href?: string;
  status: 'Published' | 'In Progress';
  domain: string;
  method: string;
}

export const pageTitle = 'Research';
export const pageDescription =
  'Primary-source papers and technical concept notes by John Sambrook. Systems architecture, Theory of Constraints, healthcare operations, and AI-enabled delivery models.';

export const header: PageHeader = {
  label: 'Research',
  heading: 'Papers and Concept Notes',
  subheading: 'Long-form work with explicit logic, evidence links, and implementation assumptions.',
};

export const papers: ResearchPaperCard[] = [
  {
    title: 'The Post-Acute Care Plan (PACP): A Concept Paper',
    summary:
      'A proactive discharge-readiness model that moves critical post-acute planning inputs upstream into routine care.',
    href: '/research/pacp-concept-paper',
    status: 'Published',
    domain: 'Healthcare Operations',
    method: 'TOC + Systems Architecture',
  },
  {
    title: 'Why Burnout Persists: Systems Thinking and Structural Conflicts in Healthcare',
    summary:
      'Analysis of burnout as a structural safety problem rather than an individual resilience problem.',
    href: '/research/burnout-systems-thinking',
    status: 'Published',
    domain: 'Healthcare Workforce',
    method: 'TOC Thinking Processes',
  },
  {
    title: 'Surfing the AI Tidal Wave: A Discussion Paper for Health Systems',
    summary:
      'Framework for combining AI throughput with systems thinking quality controls in knowledge-work organizations.',
    href: '/research/surfing-ai-tidal-wave',
    status: 'Published',
    domain: 'AI Strategy',
    method: 'Constraint Analysis',
  },
];
