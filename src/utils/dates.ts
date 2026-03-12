/**
 * Date utilities for frontmatter dates.
 *
 * Frontmatter dates are date-only values (e.g. "2026-02-16") that Zod coerces
 * via `new Date()`, producing UTC midnight.  The intended calendar date is
 * Pacific time (America/Los_Angeles), so we need helpers that:
 *   1. Display the correct calendar date (format in UTC to avoid day-shift).
 *   2. Produce ISO strings anchored to midnight Pacific, not midnight UTC.
 */

const PACIFIC = 'America/Los_Angeles';

function toIsoDateFromUtc(d: Date): string {
  const year = d.getUTCFullYear();
  const month = String(d.getUTCMonth() + 1).padStart(2, '0');
  const day = String(d.getUTCDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function pacificTodayIso(now: Date): string {
  const parts = new Intl.DateTimeFormat('en-US', {
    timeZone: PACIFIC,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).formatToParts(now);
  const year = parts.find((part) => part.type === 'year')?.value;
  const month = parts.find((part) => part.type === 'month')?.value;
  const day = parts.find((part) => part.type === 'day')?.value;
  if (!year || !month || !day) {
    throw new Error('Unable to compute Pacific date');
  }
  return `${year}-${month}-${day}`;
}

/**
 * Return an ISO-8601 string representing midnight Pacific for the given date.
 * Example: 2026-02-16 (PST) → "2026-02-16T08:00:00.000Z"
 *          2026-07-04 (PDT) → "2026-07-04T07:00:00.000Z"
 */
export function toPacificIso(d: Date): string {
  const noon = new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate(), 12));
  const isPDT = new Intl.DateTimeFormat('en-US', {
    timeZone: PACIFIC,
    timeZoneName: 'short',
  })
    .format(noon)
    .includes('PDT');
  const offsetHours = isPDT ? 7 : 8;
  return new Date(
    Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate(), offsetHours)
  ).toISOString();
}

/** True when the post's frontmatter date is today or earlier (Pacific calendar day). */
export function isPublished(d: Date): boolean {
  const postDate = toIsoDateFromUtc(d);
  const pacificToday = pacificTodayIso(new Date());
  return postDate <= pacificToday;
}

/** Format a frontmatter date for human display (e.g. "February 16, 2026"). */
export function formatDate(d: Date): string {
  return d.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    timeZone: 'UTC',
  });
}
