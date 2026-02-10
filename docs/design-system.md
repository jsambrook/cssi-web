# Design System Documentation

Design tokens and patterns extracted from common-sense.com (January 2026).

## Color Palette

### Primary Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--primary` | `#fe811b` | Primary buttons, links, accents |
| `--primary-foreground` | `#fff` | Text on primary backgrounds |
| `--accent` | `#fe811b` | Same as primary (unified accent) |
| `--accent-foreground` | `#fff` | Text on accent backgrounds |

### Neutral Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--background` | `#fff` | Page background |
| `--foreground` | `#292929` | Primary text color |
| `--muted` | `rgba(41,41,41,0.05)` | Subtle backgrounds |
| `--muted-foreground` | `#666` | Secondary text, captions |
| `--border` | `#fe811b` | Card borders, dividers |

### Secondary Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--secondary` | `#155dfc` | Secondary actions (blue) |
| `--secondary-foreground` | `#fff` | Text on secondary |
| `--destructive` | `#dc2626` | Error states, warnings |
| `--destructive-foreground` | `#fff` | Text on destructive |

### Chart Colors

| Token | Value |
|-------|-------|
| `--chart-1` | `#fe811b` |
| `--chart-2` | `#d75e00` |
| `--chart-3` | `#ffc08d` |
| `--chart-4` | `#155dfc` |
| `--chart-5` | `#666` |

## Typography

### Font Family

**Primary:** Instrument Sans (Google Fonts)

```css
font-family: 'Instrument Sans', -apple-system, BlinkMacSystemFont, 
             'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 
             'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
```

### Type Scale

| Token | Size | Usage |
|-------|------|-------|
| `--text-h1` | 60px | Page titles |
| `--text-h2` | 34px | Section headings |
| `--text-h3` | 30px | Subsection headings |
| `--text-h4` | 18px | Card titles |
| `--text-base` | 16px | Body text |
| `--text-sm` | 14px | Secondary text |
| `--text-xs` | 12px | Captions, labels |

### Font Weights

| Token | Value |
|-------|-------|
| `--font-weight-normal` | 400 |
| `--font-weight-medium` | 500 |
| `--font-weight-semibold` | 600 |
| `--font-weight-bold` | 700 |

## Spacing

Base spacing unit: `0.25rem` (4px)

Common spacing values use Tailwind conventions:
- `1` = 0.25rem (4px)
- `2` = 0.5rem (8px)
- `4` = 1rem (16px)
- `6` = 1.5rem (24px)
- `8` = 2rem (32px)

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius` | 20px | Cards, containers |
| `--radius-button` | 70px | Buttons (pill shape) |
| `--radius-input` | 70px | Input fields |
| `--radius-badge` | 18px | Tags, badges |
| `--radius-sm` | calc(var(--radius) - 8px) | Small elements |

## Shadows

```css
--elevation-sm: 0px 1px 3px 0px rgba(0,0,0,0.1), 
                0px 1px 2px -1px rgba(0,0,0,0.1);
```

## Component Patterns

### Buttons

**Primary Button:**
- Background: `--primary`
- Text: `--primary-foreground`
- Border radius: `--radius-button` (70px)
- Padding: `px-10 py-5` (40px horizontal, 20px vertical)
- Height: 54px
- Hover: 90% opacity

**Secondary/Outline Button:**
- Background: white
- Border: 1px solid `--border`
- Text: `--foreground`
- Same radius and padding as primary

### Cards

- Background: transparent or `--card`
- Border: 2px solid `--border` (orange)
- Border radius: `--radius` (20px)
- Padding: 24px (p-6)
- Shadow: `--elevation-sm` on hover

### Section Layout

- Container max-width: 80rem (1280px)
- Horizontal padding: px-4 sm:px-6 lg:px-8
- Vertical section padding: py-16 to py-20

### Header

- Height: 102px
- Sticky positioning
- Background: white with shadow
- Logo height: 40px (h-10)

### Footer

- Background: `--foreground` (#292929)
- Text: white with 75% opacity for secondary text
- Multi-column grid layout

## Dark Mode

The template includes dark mode tokens (prefixed with `.dark`):

```css
.dark {
  --background: #292929;
  --foreground: #fff;
  --card: #333;
  --muted: rgba(255,255,255,0.05);
  --muted-foreground: #b4b4b4;
  /* ... etc */
}
```

## Responsive Breakpoints

Following Tailwind defaults:
- `sm`: 40rem (640px)
- `md`: 48rem (768px)
- `lg`: 64rem (1024px)
- `xl`: 80rem (1280px)
- `2xl`: 96rem (1536px)

## Animation

Transitions use:
- Duration: 150ms default, 200-300ms for emphasis
- Timing: `cubic-bezier(0.4, 0, 0.2, 1)` (ease-out)

Common transitions:
- `transition-colors` for hover states
- `transition-shadow` for card interactions
- `transition-transform` for button hover effects
