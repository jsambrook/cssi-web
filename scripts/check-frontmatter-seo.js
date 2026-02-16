#!/usr/bin/env node

import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BLOG_DIR = join(process.cwd(), 'src/content/blog');

const META_TITLE_MIN = 15;
const META_TITLE_MAX = 60;
const META_DESCRIPTION_MIN = 50;
const META_DESCRIPTION_MAX = 160;

function parseFrontmatter(text) {
  const match = text.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    return null;
  }

  const data = new Map();
  for (const line of match[1].split('\n')) {
    const parsed = line.match(/^([A-Za-z0-9_]+):\s*(.*)$/);
    if (!parsed) {
      continue;
    }
    let value = parsed[2].trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    data.set(parsed[1], value);
  }
  return data;
}

const files = readdirSync(BLOG_DIR)
  .filter((file) => file.endsWith('.md'))
  .sort();

const issues = [];

for (const file of files) {
  const fullPath = join(BLOG_DIR, file);
  const text = readFileSync(fullPath, 'utf8');
  const frontmatter = parseFrontmatter(text);

  if (!frontmatter) {
    issues.push(`${file}: missing frontmatter block`);
    continue;
  }

  const isDraft = (frontmatter.get('draft') ?? '').toLowerCase() === 'true';
  if (isDraft) {
    continue;
  }

  const metaTitle = (frontmatter.get('metaTitle') ?? '').trim();
  const metaDescription = (frontmatter.get('metaDescription') ?? '').trim();

  if (!metaTitle) {
    issues.push(`${file}: missing metaTitle`);
  } else if (
    metaTitle.length < META_TITLE_MIN ||
    metaTitle.length > META_TITLE_MAX
  ) {
    issues.push(
      `${file}: metaTitle length ${metaTitle.length} outside ${META_TITLE_MIN}-${META_TITLE_MAX}`
    );
  }

  if (!metaDescription) {
    issues.push(`${file}: missing metaDescription`);
  } else if (
    metaDescription.length < META_DESCRIPTION_MIN ||
    metaDescription.length > META_DESCRIPTION_MAX
  ) {
    issues.push(
      `${file}: metaDescription length ${metaDescription.length} outside ${META_DESCRIPTION_MIN}-${META_DESCRIPTION_MAX}`
    );
  }
}

if (issues.length > 0) {
  console.error(`Frontmatter SEO check failed with ${issues.length} issue(s):`);
  for (const issue of issues) {
    console.error(`- ${issue}`);
  }
  process.exit(1);
}

console.log(
  `Frontmatter SEO check passed for ${files.length} blog markdown file(s).`
);
