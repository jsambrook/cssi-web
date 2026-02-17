import type { ColorVariant } from './types';

export const colorClasses: Record<ColorVariant, string> = {
  default: 'bg-accent/10 text-accent',
  red: 'bg-[var(--feature-red-bg)] text-[var(--feature-red)]',
  orange: 'bg-[var(--feature-orange-bg)] text-[var(--feature-orange)]',
  amber: 'bg-[var(--feature-amber-bg)] text-[var(--feature-amber)]',
  blue: 'bg-[var(--feature-blue-bg)] text-[var(--feature-blue)]',
  green: 'bg-[var(--feature-green-bg)] text-[var(--feature-green)]',
  purple: 'bg-[var(--feature-purple-bg)] text-[var(--feature-purple)]',
};
