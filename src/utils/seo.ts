const TITLE_MAX_LENGTH = 60;
const DESCRIPTION_MAX_LENGTH = 155;
const ELLIPSIS = '...';

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

export function toSeoTitle(title: string): string {
  return truncateAtWord(collapseWhitespace(title), TITLE_MAX_LENGTH);
}

export function toSeoDescription(description: string): string {
  return truncateAtWord(collapseWhitespace(description), DESCRIPTION_MAX_LENGTH);
}
