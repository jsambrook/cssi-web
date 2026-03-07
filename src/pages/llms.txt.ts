import type { APIRoute } from 'astro';
import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { footerContact, navItems, siteConfig } from '../data/site';
import { industries } from '../data/pages/industries';
import { papers } from '../data/pages/research';

function toAbsoluteUrl(href: string): string {
  if (href.startsWith('http://') || href.startsWith('https://')) {
    return href;
  }
  const normalizedPath = new URL(href, `${siteConfig.siteUrl}/`).pathname.replace(/\/$/, '') || '/';
  return `${siteConfig.siteUrl}${normalizedPath}`;
}

function titleCaseFromSlug(slug: string): string {
  const uppercaseTokens = new Set(['ai', 'api', 'geo', 'llm', 'llms', 'seo', 'toc']);
  const lowercaseConnectors = new Set(['a', 'an', 'and', 'for', 'in', 'of', 'on', 'the', 'to']);

  return slug
    .split('-')
    .filter(Boolean)
    .map((part, i) => {
      if (uppercaseTokens.has(part)) {
        return part.toUpperCase();
      }
      if (i > 0 && lowercaseConnectors.has(part)) {
        return part;
      }
      return part[0].toUpperCase() + part.slice(1);
    })
    .join(' ');
}

function discoverApproachSubpages(): { label: string; href: string }[] {
  const pagesDir = join(process.cwd(), 'src', 'pages', 'approach');
  if (!existsSync(pagesDir)) {
    return [];
  }

  return readdirSync(pagesDir, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .filter((entry) => existsSync(join(pagesDir, entry.name, 'index.astro')))
    .map((entry) => ({
      label: `Approach: ${titleCaseFromSlug(entry.name)}`,
      href: `/approach/${entry.name}`,
    }));
}

function uniqueByHref<T extends { href: string }>(items: T[]): T[] {
  const seen = new Set<string>();
  const result: T[] = [];

  for (const item of items) {
    const key = toAbsoluteUrl(item.href);
    if (seen.has(key)) {
      continue;
    }
    seen.add(key);
    result.push(item);
  }

  return result;
}

export const GET: APIRoute = () => {
  const navKeyPages = navItems
    .filter((item) => item.href.startsWith('/'))
    .filter((item) => !item.href.includes('#'))
    .map((item) => ({ label: item.label, href: item.href }));
  const industryKeyPages = Object.entries(industries).map(([slug, page]) => ({
    label: `${page.header.label} Services`,
    href: `/industries/${slug}`,
  }));
  const keyPages = uniqueByHref([
    ...navKeyPages,
    ...industryKeyPages,
    ...discoverApproachSubpages(),
    { label: 'Insights (Blog)', href: '/insights' },
    { label: 'Research (Papers)', href: '/research' },
  ]);

  const researchLines = papers
    .filter((paper) => paper.href)
    .map((paper) => `- ${paper.title}: ${toAbsoluteUrl(paper.href!)}`)
    .join('\n');

  const body = `# ${siteConfig.name}, Inc.

> Constraint analysis and offer strategy for organizations that are ready to stop guessing and start moving. Based in Kirkland, WA since 1996.

## Organization

${siteConfig.name}, Inc. is a consulting firm based in Kirkland, WA, founded in 1996. We apply Theory of Constraints (TOC) methodology to help organizations identify and exploit their primary constraint, accelerating throughput and eliminating operational bottlenecks. All engagements carry a satisfaction guarantee: unless you agree that what was promised was what was delivered, there is no charge.

## Founder

John Sambrook is a TOC Jonah Certified systems architect and constraint analyst. He holds credentials from TOCICO and a degree from Washington State University. He has deep expertise in healthcare patient flow, medical device software (IEC 62304, IEC 60601), embedded systems engineering, and throughput accounting.

## Services

- Constraint Analysis ($15,000 fixed): We identify the single constraint limiting your system and help you fix it. Diagnosis delivered in 2 to 4 weeks. Implementation priced at 10-15% of estimated value.
- Offer Analysis ($15,000 fixed): We diagnose why your offer is invisible and build one that makes the right client feel foolish saying no. Diagnosis delivered in 2 to 4 weeks. Implementation priced at 10-15% of estimated revenue impact.

Both services carry a satisfaction guarantee: unless you agree that what was promised was what was delivered, there is no charge.

## Industries

- Healthcare: Hospital operations, patient flow optimization, complex discharge analysis, direct-to-employer contracting
- Technology: R&D acceleration, risk-shared licensing, product roadmap alignment

## Key Pages

${keyPages.map((page) => `- ${page.label}: ${toAbsoluteUrl(page.href)}`).join('\n')}

## Research Papers

${researchLines}

## Contact

- Phone: ${footerContact.phones[0]}
- Email: ${footerContact.email}
- Founder Direct Email: john@common-sense.com
- Address: ${footerContact.address.replace('\n', ', ')}
- LinkedIn: https://www.linkedin.com/company/common-sense-systems
- X/Twitter: ${siteConfig.xProfileUrl}
- YouTube: ${siteConfig.youtubeUrl}
- Google Business Profile: https://maps.google.com/?cid=14125900726605051430
`;

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
