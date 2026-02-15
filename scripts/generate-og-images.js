#!/usr/bin/env node

/**
 * generate-og-images.js
 *
 * Generates per-post OG images (1200x630 PNG) for all non-draft blog posts.
 * Skips generation when the PNG is newer than the source markdown file.
 *
 * Usage: node scripts/generate-og-images.js
 */

import { createCanvas, loadImage, GlobalFonts } from '@napi-rs/canvas';
import { readFileSync, statSync, mkdirSync, readdirSync, writeFileSync } from 'node:fs';
import { join, resolve } from 'node:path';

const ROOT = resolve(import.meta.dirname, '..');
const BLOG_DIR = join(ROOT, 'src/content/blog');
const OUTPUT_DIR = join(ROOT, 'public/images/blog');
const LOGO_PATH = join(ROOT, 'public/favicon.svg');

// Bump to force regeneration of all images (e.g. after design token changes)
const DESIGN_VERSION = '2';

// Design tokens (matching og-default.png)
const WIDTH = 1200;
const HEIGHT = 630;
const BG_COLOR = '#f5f5f5';
const ACCENT_COLOR = '#fe811b';
const ACCENT_BAR_HEIGHT = 8;
const PADDING_X = 60;
const TITLE_MAX_WIDTH = WIDTH - PADDING_X * 2;
const TITLE_FONT_SIZE = 48;
const URL_FONT_SIZE = 24;
const URL_TEXT = 'common-sense.com';

// ---------------------------------------------------------------------------
// Frontmatter helpers
// ---------------------------------------------------------------------------

function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  assert(match, 'No frontmatter found');
  const block = match[1];

  const get = (key) => {
    const m = block.match(new RegExp(`^${key}:\\s*(.+)$`, 'm'));
    return m ? m[1].replace(/^["']|["']$/g, '') : undefined;
  };

  return {
    title: get('title'),
    draft: get('draft') === 'true',
  };
}

// ---------------------------------------------------------------------------
// Word-wrap helper
// ---------------------------------------------------------------------------

function wrapText(ctx, text, maxWidth) {
  const words = text.split(' ');
  const lines = [];
  let currentLine = words[0];

  for (let i = 1; i < words.length; i++) {
    const test = `${currentLine} ${words[i]}`;
    if (ctx.measureText(test).width <= maxWidth) {
      currentLine = test;
    } else {
      lines.push(currentLine);
      currentLine = words[i];
    }
  }
  lines.push(currentLine);
  return lines;
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function assert(condition, message) {
  if (!condition) {
    throw new Error(`generate-og-images: ${message}`);
  }
}

async function main() {
  mkdirSync(OUTPUT_DIR, { recursive: true });

  const mdFiles = readdirSync(BLOG_DIR).filter((f) => f.endsWith('.md'));
  assert(mdFiles.length > 0, `No markdown files found in ${BLOG_DIR}`);

  const logo = await loadImage(LOGO_PATH);

  // Check if design version changed — if so, regenerate everything
  const versionFile = join(OUTPUT_DIR, '.design-version');
  let forceAll = false;
  try {
    forceAll = readFileSync(versionFile, 'utf-8').trim() !== DESIGN_VERSION;
  } catch {
    forceAll = true;
  }

  let generated = 0;
  let skipped = 0;

  for (const file of mdFiles) {
    const mdPath = join(BLOG_DIR, file);
    const slug = file.replace(/\.md$/, '');
    const outPath = join(OUTPUT_DIR, `${slug}.png`);

    // Parse frontmatter
    const content = readFileSync(mdPath, 'utf-8');
    const { title, draft } = parseFrontmatter(content);

    if (draft) {
      skipped++;
      continue;
    }

    assert(title, `Missing title in ${file}`);

    // Skip if output exists and is newer than source (unless design version changed)
    if (!forceAll) {
      try {
        const mdStat = statSync(mdPath);
        const pngStat = statSync(outPath);
        if (pngStat.mtimeMs > mdStat.mtimeMs) {
          skipped++;
          continue;
        }
      } catch {
        // Output doesn't exist yet — generate it
      }
    }

    // -----------------------------------------------------------------------
    // Render the OG image
    // -----------------------------------------------------------------------

    const canvas = createCanvas(WIDTH, HEIGHT);
    const ctx = canvas.getContext('2d');

    // Background
    ctx.fillStyle = BG_COLOR;
    ctx.fillRect(0, 0, WIDTH, HEIGHT);

    // Top accent bar
    ctx.fillStyle = ACCENT_COLOR;
    ctx.fillRect(0, 0, WIDTH, ACCENT_BAR_HEIGHT);

    // Title text (white, bold, centered)
    ctx.fillStyle = '#1a1a1a';
    ctx.font = `bold ${TITLE_FONT_SIZE}px sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';

    const lines = wrapText(ctx, title, TITLE_MAX_WIDTH);
    const lineHeight = TITLE_FONT_SIZE * 1.3;
    const totalTextHeight = lines.length * lineHeight;

    // Vertical centering: account for accent bar at top and logo area at bottom (~100px)
    const availableHeight = HEIGHT - ACCENT_BAR_HEIGHT - 100;
    const textStartY = ACCENT_BAR_HEIGHT + (availableHeight - totalTextHeight) / 2;

    for (let i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i], WIDTH / 2, textStartY + i * lineHeight);
    }

    // Logo + URL at bottom
    const logoHeight = 40;
    const logoWidth = (logo.width / logo.height) * logoHeight;
    const bottomY = HEIGHT - 50 - logoHeight / 2;

    // Draw logo and URL centered together
    const urlMetrics = (() => {
      ctx.font = `bold ${URL_FONT_SIZE}px sans-serif`;
      return ctx.measureText(URL_TEXT);
    })();
    const gap = 12;
    const totalWidth = logoWidth + gap + urlMetrics.width;
    const startX = (WIDTH - totalWidth) / 2;

    ctx.drawImage(logo, startX, bottomY - logoHeight / 2, logoWidth, logoHeight);

    ctx.fillStyle = ACCENT_COLOR;
    ctx.font = `bold ${URL_FONT_SIZE}px sans-serif`;
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText(URL_TEXT, startX + logoWidth + gap, bottomY);

    // Write PNG
    const buffer = canvas.toBuffer('image/png');
    writeFileSync(outPath, buffer);
    generated++;
    console.log(`  ✓ ${slug}.png`);
  }

  writeFileSync(versionFile, DESIGN_VERSION);
  console.log(`\nDone. Generated: ${generated}, Skipped: ${skipped}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
