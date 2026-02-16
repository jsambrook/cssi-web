#!/usr/bin/env node

import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { parseDocument } from 'yaml';

const BLOG_DIR = join(process.cwd(), 'src/content/blog');

const META_TITLE_MIN = 15;
const META_TITLE_MAX = 60;
const META_DESCRIPTION_MIN = 50;
const META_DESCRIPTION_MAX = 160;
const TRUNCATION_PATTERN = /(?:\.{3}|…)$/u;

function extractFrontmatter(raw) {
  const text = raw.replace(/\r\n/g, '\n');
  const lines = text.split('\n');
  if (lines[0]?.trim() !== '---') {
    return null;
  }

  for (let index = 1; index < lines.length; index += 1) {
    const line = lines[index].trim();
    if (line === '---' || line === '...') {
      return lines.slice(1, index).join('\n');
    }
  }
  return null;
}

function parseFrontmatter(raw) {
  const frontmatter = extractFrontmatter(raw);
  if (!frontmatter) {
    return { data: null, error: 'missing frontmatter block' };
  }

  const doc = parseDocument(frontmatter, { prettyErrors: true });
  if (doc.errors.length > 0) {
    const messages = doc.errors.map((error) => error.message).join('; ');
    return { data: null, error: `invalid frontmatter YAML (${messages})` };
  }

  const data = doc.toJS();
  if (!data || typeof data !== 'object' || Array.isArray(data)) {
    return { data: null, error: 'frontmatter is not a key/value mapping' };
  }

  return { data, error: null };
}

function normalizeString(value) {
  if (typeof value === 'string') {
    return value.trim();
  }
  return '';
}

function isDraft(frontmatter) {
  const draft = frontmatter.draft;
  if (typeof draft === 'boolean') {
    return draft;
  }
  if (typeof draft === 'string') {
    return draft.trim().toLowerCase() === 'true';
  }
  return false;
}

function looksMachineTrimmed(value) {
  return TRUNCATION_PATTERN.test(value);
}

const files = readdirSync(BLOG_DIR)
  .filter((file) => file.endsWith('.md'))
  .sort();

const issues = [];

for (const file of files) {
  const fullPath = join(BLOG_DIR, file);
  const text = readFileSync(fullPath, 'utf8');
  const { data: frontmatter, error } = parseFrontmatter(text);

  if (error || !frontmatter) {
    issues.push(`${file}: ${error ?? 'missing frontmatter block'}`);
    continue;
  }

  if (isDraft(frontmatter)) {
    continue;
  }

  const metaTitle = normalizeString(frontmatter.metaTitle);
  const metaDescription = normalizeString(frontmatter.metaDescription);

  if (!metaTitle) {
    issues.push(`${file}: missing metaTitle`);
  } else if (
    metaTitle.length < META_TITLE_MIN ||
    metaTitle.length > META_TITLE_MAX
  ) {
    issues.push(
      `${file}: metaTitle length ${metaTitle.length} outside ${META_TITLE_MIN}-${META_TITLE_MAX}`
    );
  } else if (looksMachineTrimmed(metaTitle)) {
    issues.push(
      `${file}: metaTitle appears machine-trimmed (trailing ellipsis)`
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
  } else if (looksMachineTrimmed(metaDescription)) {
    issues.push(
      `${file}: metaDescription appears machine-trimmed (trailing ellipsis)`
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
