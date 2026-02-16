const TITLE_MAX_LENGTH = 70;
const DESCRIPTION_MAX_LENGTH = 155;
const ELLIPSIS = '...';
const TITLE_SEPARATOR = ' | ';

function collapseWhitespace(value: string): string {
  return value.replace(/\s+/g, ' ').trim();
}

function truncateAtWord(value: string, maxLength: number): string {
  if (value.length <= maxLength) {
    return value;
  }

  const contentBudget = Math.max(maxLength - ELLIPSIS.length, 1);
  const provisional = value.slice(0, contentBudget + 1).trimEnd();
  const lastSpace = provisional.lastIndexOf(' ');

  if (lastSpace >= Math.floor(contentBudget * 0.6)) {
    return `${provisional.slice(0, lastSpace).trimEnd()}${ELLIPSIS}`;
  }

  return `${provisional.slice(0, contentBudget).trimEnd()}${ELLIPSIS}`;
}

/**
 * Build an SEO-safe <title>.
 *
 * Strategy:
 *  1. If the full title fits within the limit, return it as-is.
 *  2. If the title contains " | Brand", truncate only the page-title
 *     portion while keeping the brand suffix intact.
 *  3. If keeping the brand leaves too little room (< 20 chars) for
 *     the page title, drop the brand and truncate the page title alone.
 */
export function toSeoTitle(title: string): string {
  const cleaned = collapseWhitespace(title);
  if (cleaned.length <= TITLE_MAX_LENGTH) return cleaned;

  const separatorIndex = cleaned.lastIndexOf(TITLE_SEPARATOR);
  if (separatorIndex === -1) {
    return truncateAtWord(cleaned, TITLE_MAX_LENGTH);
  }

  const pagePart = cleaned.slice(0, separatorIndex);
  const brandSuffix = cleaned.slice(separatorIndex); // " | Brand Name"

  const pageBudget = TITLE_MAX_LENGTH - brandSuffix.length;
  if (pageBudget >= 20) {
    return truncateAtWord(pagePart, pageBudget) + brandSuffix;
  }

  // Brand suffix is too long to keep; use only the page title.
  return truncateAtWord(pagePart, TITLE_MAX_LENGTH);
}

export function toSeoDescription(description: string): string {
  return truncateAtWord(collapseWhitespace(description), DESCRIPTION_MAX_LENGTH);
}
