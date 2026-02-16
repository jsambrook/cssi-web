#!/usr/bin/env node

import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join, relative } from 'node:path';
import { parse } from 'parse5';

const DIST_DIR = join(process.cwd(), 'dist');
const TITLE_MIN = 15;
const TITLE_MAX = 70;
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

function walkNodes(node, visit) {
  visit(node);
  for (const child of node.childNodes ?? []) {
    walkNodes(child, visit);
  }
}

function getAttr(node, name) {
  const attr = node.attrs?.find((item) => item.name.toLowerCase() === name);
  return attr?.value ?? '';
}

function firstElement(root, predicate) {
  let found = null;
  walkNodes(root, (node) => {
    if (found || !node.tagName) {
      return;
    }
    if (predicate(node)) {
      found = node;
    }
  });
  return found;
}

function allElements(root, predicate) {
  const matches = [];
  walkNodes(root, (node) => {
    if (!node.tagName) {
      return;
    }
    if (predicate(node)) {
      matches.push(node);
    }
  });
  return matches;
}

function textContent(node) {
  let text = '';
  walkNodes(node, (current) => {
    if (current.nodeName === '#text') {
      text += current.value ?? '';
    }
  });
  return text.trim();
}

function getMetaContent(root, { name, property }) {
  const meta = firstElement(root, (node) => {
    if (node.tagName !== 'meta') {
      return false;
    }
    if (name) {
      return getAttr(node, 'name').toLowerCase() === name.toLowerCase();
    }
    if (property) {
      return getAttr(node, 'property').toLowerCase() === property.toLowerCase();
    }
    return false;
  });
  return meta ? getAttr(meta, 'content').trim() : '';
}

function getCanonicalHref(root) {
  const canonical = firstElement(root, (node) => {
    if (node.tagName !== 'link') {
      return false;
    }
    const rel = getAttr(node, 'rel').toLowerCase().split(/\s+/).filter(Boolean);
    return rel.includes('canonical');
  });
  return canonical ? getAttr(canonical, 'href').trim() : '';
}

function collectJsonLdTypes(value, types = []) {
  if (Array.isArray(value)) {
    for (const item of value) {
      collectJsonLdTypes(item, types);
    }
    return types;
  }

  if (!value || typeof value !== 'object') {
    return types;
  }

  const rawType = value['@type'];
  if (typeof rawType === 'string') {
    types.push(rawType);
  } else if (Array.isArray(rawType)) {
    for (const item of rawType) {
      if (typeof item === 'string') {
        types.push(item);
      }
    }
  }

  if (Array.isArray(value['@graph'])) {
    collectJsonLdTypes(value['@graph'], types);
  }

  return types;
}

function parseJsonLdTypes(documentRoot) {
  const scripts = allElements(
    documentRoot,
    (node) =>
      node.tagName === 'script' && getAttr(node, 'type').toLowerCase() === 'application/ld+json'
  );

  const types = [];
  for (const script of scripts) {
    try {
      const parsed = JSON.parse(textContent(script));
      collectJsonLdTypes(parsed, types);
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
  const documentRoot = parse(html);
  const ids = new Map();
  const duplicateIds = new Set();

  allElements(documentRoot, (node) => Boolean(getAttr(node, 'id'))).forEach((node) => {
    const id = getAttr(node, 'id');
    if (ids.has(id)) {
      duplicateIds.add(id);
    } else {
      ids.set(id, true);
    }
  });

  for (const duplicateId of duplicateIds) {
    errors.push(`${relPath}: duplicate id "${duplicateId}"`);
  }

  const requiredMeta = [
    ['description', () => getMetaContent(documentRoot, { name: 'description' })],
    ['robots', () => getMetaContent(documentRoot, { name: 'robots' })],
    ['canonical', () => getCanonicalHref(documentRoot)],
    ['og:type', () => getMetaContent(documentRoot, { property: 'og:type' })],
    ['og:url', () => getMetaContent(documentRoot, { property: 'og:url' })],
    ['og:title', () => getMetaContent(documentRoot, { property: 'og:title' })],
    ['og:description', () => getMetaContent(documentRoot, { property: 'og:description' })],
    ['og:image', () => getMetaContent(documentRoot, { property: 'og:image' })],
    ['og:image:alt', () => getMetaContent(documentRoot, { property: 'og:image:alt' })],
    ['twitter:card', () => getMetaContent(documentRoot, { name: 'twitter:card' })],
    ['twitter:site', () => getMetaContent(documentRoot, { name: 'twitter:site' })],
    ['twitter:creator', () => getMetaContent(documentRoot, { name: 'twitter:creator' })],
    ['twitter:title', () => getMetaContent(documentRoot, { name: 'twitter:title' })],
    ['twitter:description', () => getMetaContent(documentRoot, { name: 'twitter:description' })],
    ['twitter:image', () => getMetaContent(documentRoot, { name: 'twitter:image' })],
    ['twitter:image:alt', () => getMetaContent(documentRoot, { name: 'twitter:image:alt' })],
  ];

  const titleNode = firstElement(documentRoot, (node) => node.tagName === 'title');
  const titleText = titleNode ? textContent(titleNode) : '';

  if (!titleText) {
    errors.push(`${relPath}: missing title`);
  }

  for (const [label, getValue] of requiredMeta) {
    if (!getValue()) {
      errors.push(`${relPath}: missing ${label}`);
    }
  }

  const title = titleText;
  const description = getMetaContent(documentRoot, { name: 'description' });
  const canonical = getCanonicalHref(documentRoot);
  const ogUrl = getMetaContent(documentRoot, { property: 'og:url' });
  const robots = getMetaContent(documentRoot, { name: 'robots' });

  if (canonical && !canonical.startsWith('http://') && !canonical.startsWith('https://')) {
    errors.push(`${relPath}: canonical is not an absolute URL`);
  }

  if (canonical && ogUrl && canonical !== ogUrl) {
    errors.push(`${relPath}: canonical and og:url do not match`);
  }

  const isNoindex = robots.toLowerCase().includes('noindex');
  if (!isNoindex) {
    if (title.length < TITLE_MIN || title.length > TITLE_MAX) {
      errors.push(`${relPath}: title length ${title.length} outside ${TITLE_MIN}-${TITLE_MAX}`);
    }
    if (description.length < DESCRIPTION_MIN || description.length > DESCRIPTION_MAX) {
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
    [
      'article:published_time',
      () => getMetaContent(documentRoot, { property: 'article:published_time' }),
    ],
    [
      'article:modified_time',
      () => getMetaContent(documentRoot, { property: 'article:modified_time' }),
    ],
    ['article:author', () => getMetaContent(documentRoot, { property: 'article:author' })],
  ];

  for (const [label, getValue] of requiredArticleMeta) {
    if (!getValue()) {
      errors.push(`${relPath}: missing ${label}`);
    }
  }

  const jsonLdTypes = parseJsonLdTypes(documentRoot);
  if (!jsonLdTypes.includes('Organization')) {
    errors.push(`${relPath}: missing Organization JSON-LD`);
  }
  if (!jsonLdTypes.includes('BlogPosting') && !jsonLdTypes.includes('Article')) {
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
