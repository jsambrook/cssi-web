/**
 * Slugify a tag name for use in URLs.
 * "AI & Automation" → "ai-automation"
 */
export function slugifyTag(tag: string): string {
  return tag
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

/** Build the href for a tag archive page. */
export function tagHref(tag: string): string {
  return `/insights/tag/${slugifyTag(tag)}`;
}
