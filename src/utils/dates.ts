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

/** True when the post's frontmatter date is today or earlier (UTC calendar day). */
export function isPublished(d: Date): boolean {
  const now = new Date();
  const today = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
  const postDay = Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate());
  return postDay <= today;
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
