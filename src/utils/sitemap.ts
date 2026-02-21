/**
 * Sitemap lastmod helper — reads blog post dates at build time and provides
 * a serialize function for @astrojs/sitemap that adds <lastmod> to all URLs.
 *
 * Blog posts: date from frontmatter (updatedDate ?? date).
 * Static pages: most recent git commit touching the page's source files.
 */
import { execSync } from 'node:child_process';
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, basename } from 'node:path';
import { manualInsights } from '../data/manualInsights';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = join(__dirname, '..', '..');
const BLOG_DIR = join(__dirname, '..', 'content', 'blog');

interface SitemapItem {
  url: string;
  lastmod?: string;
  changefreq?: string;
  priority?: number;
}

/** Extract date and updatedDate from markdown frontmatter. */
function parseFrontmatterDates(content: string): { date?: Date; updatedDate?: Date } {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  const fm = match[1];
  const dateMatch = fm.match(/^date:\s*['"]?(.+?)['"]?\s*$/m);
  const updatedMatch = fm.match(/^updatedDate:\s*['"]?(.+?)['"]?\s*$/m);
  return {
    date: dateMatch ? new Date(dateMatch[1]) : undefined,
    updatedDate: updatedMatch ? new Date(updatedMatch[1]) : undefined,
  };
}

/** Static pages and the source files whose edits should update <lastmod>. */
const STATIC_PAGES: [string, string[]][] = [
  ['/', ['src/pages/index.astro', 'src/data/pages/home.ts']],
  ['/about', ['src/pages/about.astro', 'src/data/pages/about.ts']],
  ['/approach', ['src/pages/approach.astro', 'src/data/pages/approach.ts']],
  ['/contact', ['src/pages/contact.astro', 'src/data/pages/contact.ts']],
  ['/insights', ['src/pages/insights.astro', 'src/data/pages/insights.ts']],
  [
    '/industries/healthcare',
    ['src/pages/industries/healthcare.astro', 'src/data/pages/industries.ts'],
  ],
  ['/industries/tech', ['src/pages/industries/tech.astro', 'src/data/pages/industries.ts']],
  ['/legal/privacy', ['src/pages/legal/privacy.astro', 'src/data/pages/privacy.ts']],
  ['/legal/terms', ['src/pages/legal/terms.astro', 'src/data/pages/terms.ts']],
  ['/legal/sms-consent', ['src/pages/legal/sms-consent.astro']],
];

/** Get the most recent git commit date (YYYY-MM-DD) touching any of the given files. */
function gitLastmod(files: string[]): string | undefined {
  try {
    const iso = execSync(`git log -1 --format=%aI -- ${files.join(' ')}`, {
      cwd: PROJECT_ROOT,
      encoding: 'utf-8',
      stdio: ['pipe', 'pipe', 'pipe'],
    }).trim();
    if (iso) return iso.split('T')[0];
  } catch {
    // Not a git repo or git unavailable — skip silently.
  }
  return undefined;
}

/** Build a map from URL path (no trailing slash) to YYYY-MM-DD lastmod string. */
function buildLastmodMap(): Map<string, string> {
  const map = new Map<string, string>();

  // Blog posts — date from frontmatter.
  for (const file of readdirSync(BLOG_DIR).filter((f) => f.endsWith('.md'))) {
    const slug = basename(file, '.md');
    const raw = readFileSync(join(BLOG_DIR, file), 'utf-8');
    const { date, updatedDate } = parseFrontmatterDates(raw);
    const best = updatedDate ?? date;
    if (best) {
      map.set(`/insights/${slug}`, best.toISOString().split('T')[0]);
    }
  }

  for (const insight of manualInsights) {
    map.set(`/insights/${insight.slug}`, insight.date.toISOString().split('T')[0]);
  }

  // Static pages — date from git history.
  for (const [urlPath, files] of STATIC_PAGES) {
    const lastmod = gitLastmod(files);
    if (lastmod) map.set(urlPath, lastmod);
  }

  return map;
}

const lastmodMap = buildLastmodMap();

/** Serialize callback for @astrojs/sitemap — adds lastmod to blog post URLs. */
export function sitemapSerialize(item: SitemapItem): SitemapItem {
  const path = new URL(item.url).pathname.replace(/\/$/, '') || '/';
  const lastmod = lastmodMap.get(path);
  if (lastmod) {
    return { ...item, lastmod };
  }
  return item;
}
