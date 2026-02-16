#!/usr/bin/env node

import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join, relative } from 'node:path';

const DIST_DIR = join(process.cwd(), 'dist');
const TITLE_MIN = 15;
const TITLE_MAX = 60;
const DESCRIPTION_MIN = 50;
const DESCRIPTION_MAX = 160;

if (!existsSync(DIST_DIR)) {
  console.error('SEO check failed: dist/ directory not found. Run build first.');
  process.exit(1);
}

function walkHtmlFiles(dir, files = []) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const fullPath = join(dir, entry.name);
    if (entry.isDirectory()) {
      walkHtmlFiles(fullPath, files);
      continue;
    }
    if (entry.isFile() && entry.name.endsWith('.html')) {
      files.push(fullPath);
    }
  }
  return files;
}

function decodeHtmlEntities(value) {
  const named = value
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
  return named.replace(/&#(\d+);/g, (_, code) =>
    String.fromCodePoint(Number(code))
  );
}

function extract(html, regex) {
  const match = html.match(regex);
  return match ? match[1] : '';
}

function parseJsonLdTypes(html) {
  const scripts = [
    ...html.matchAll(
      /<script\s+type="application\/ld\+json">([\s\S]*?)<\/script>/gi
    ),
  ];
  const types = [];
  for (const script of scripts) {
    try {
      const parsed = JSON.parse(script[1]);
      types.push(parsed?.['@type'] ?? 'UNKNOWN');
    } catch {
      types.push('INVALID_JSON');
    }
  }
  return types;
}

const htmlFiles = walkHtmlFiles(DIST_DIR);
const errors = [];

for (const file of htmlFiles) {
  const relPath = relative(DIST_DIR, file).replaceAll('\\', '/');
  const html = readFileSync(file, 'utf8');

  const requiredMeta = [
    ['title', /<title>[^<]+<\/title>/i],
    ['description', /<meta\s+name="description"\s+content="[^"]+"/i],
    ['robots', /<meta\s+name="robots"\s+content="[^"]+"/i],
    ['canonical', /<link\s+rel="canonical"\s+href="[^"]+"/i],
    ['og:type', /<meta\s+property="og:type"\s+content="[^"]+"/i],
    ['og:url', /<meta\s+property="og:url"\s+content="[^"]+"/i],
    ['og:title', /<meta\s+property="og:title"\s+content="[^"]+"/i],
    ['og:description', /<meta\s+property="og:description"\s+content="[^"]+"/i],
    ['og:image', /<meta\s+property="og:image"\s+content="[^"]+"/i],
    ['og:image:alt', /<meta\s+property="og:image:alt"\s+content="[^"]+"/i],
    ['twitter:card', /<meta\s+name="twitter:card"\s+content="[^"]+"/i],
    ['twitter:site', /<meta\s+name="twitter:site"\s+content="[^"]+"/i],
    ['twitter:creator', /<meta\s+name="twitter:creator"\s+content="[^"]+"/i],
    ['twitter:title', /<meta\s+name="twitter:title"\s+content="[^"]+"/i],
    [
      'twitter:description',
      /<meta\s+name="twitter:description"\s+content="[^"]+"/i,
    ],
    ['twitter:image', /<meta\s+name="twitter:image"\s+content="[^"]+"/i],
    ['twitter:image:alt', /<meta\s+name="twitter:image:alt"\s+content="[^"]+"/i],
  ];

  for (const [label, regex] of requiredMeta) {
    if (!regex.test(html)) {
      errors.push(`${relPath}: missing ${label}`);
    }
  }

  const title = decodeHtmlEntities(
    extract(html, /<title>([^<]*)<\/title>/i)
  ).trim();
  const description = decodeHtmlEntities(
    extract(html, /<meta\s+name="description"\s+content="([^"]*)"/i)
  ).trim();
  const canonical = extract(html, /<link\s+rel="canonical"\s+href="([^"]*)"/i);
  const ogUrl = extract(html, /<meta\s+property="og:url"\s+content="([^"]*)"/i);
  const robots = extract(html, /<meta\s+name="robots"\s+content="([^"]*)"/i);

  if (canonical && !canonical.startsWith('http://') && !canonical.startsWith('https://')) {
    errors.push(`${relPath}: canonical is not an absolute URL`);
  }

  if (canonical && ogUrl && canonical !== ogUrl) {
    errors.push(`${relPath}: canonical and og:url do not match`);
  }

  const isNoindex = robots.toLowerCase().includes('noindex');
  if (!isNoindex) {
    if (title.length < TITLE_MIN || title.length > TITLE_MAX) {
      errors.push(
        `${relPath}: title length ${title.length} outside ${TITLE_MIN}-${TITLE_MAX}`
      );
    }
    if (
      description.length < DESCRIPTION_MIN ||
      description.length > DESCRIPTION_MAX
    ) {
      errors.push(
        `${relPath}: description length ${description.length} outside ${DESCRIPTION_MIN}-${DESCRIPTION_MAX}`
      );
    }
  }

  const isArticle =
    relPath.startsWith('insights/') &&
    relPath.endsWith('/index.html') &&
    !relPath.includes('/tag/') &&
    relPath !== 'insights/index.html';

  if (!isArticle) {
    continue;
  }

  const requiredArticleMeta = [
    ['article:published_time', /<meta\s+property="article:published_time"\s+content="[^"]+"/i],
    ['article:modified_time', /<meta\s+property="article:modified_time"\s+content="[^"]+"/i],
    ['article:author', /<meta\s+property="article:author"\s+content="[^"]+"/i],
  ];

  for (const [label, regex] of requiredArticleMeta) {
    if (!regex.test(html)) {
      errors.push(`${relPath}: missing ${label}`);
    }
  }

  const jsonLdTypes = parseJsonLdTypes(html);
  if (!jsonLdTypes.includes('Organization')) {
    errors.push(`${relPath}: missing Organization JSON-LD`);
  }
  if (
    !jsonLdTypes.includes('BlogPosting') &&
    !jsonLdTypes.includes('Article')
  ) {
    errors.push(`${relPath}: missing BlogPosting/Article JSON-LD`);
  }
  if (!jsonLdTypes.includes('BreadcrumbList')) {
    errors.push(`${relPath}: missing BreadcrumbList JSON-LD`);
  }
}

if (errors.length > 0) {
  console.error(`SEO check failed with ${errors.length} issue(s):`);
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log(`SEO check passed for ${htmlFiles.length} HTML page(s).`);
