/**
 * Sitemap lastmod helper — reads blog post dates at build time and provides
 * a serialize function for @astrojs/sitemap that adds <lastmod> to post URLs.
 */
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, basename } from 'node:path';
import { manualInsights } from '../data/manualInsights';

const __dirname = dirname(fileURLToPath(import.meta.url));
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

/** Build a map from URL path (no trailing slash) to YYYY-MM-DD lastmod string. */
function buildLastmodMap(): Map<string, string> {
  const map = new Map<string, string>();

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

  return map;
}

const lastmodMap = buildLastmodMap();

/** Serialize callback for @astrojs/sitemap — adds lastmod to blog post URLs. */
export function sitemapSerialize(item: SitemapItem): SitemapItem {
  const path = new URL(item.url).pathname.replace(/\/$/, '');
  const lastmod = lastmodMap.get(path);
  if (lastmod) {
    return { ...item, lastmod };
  }
  return item;
}
