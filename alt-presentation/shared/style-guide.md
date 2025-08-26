# EvergreenHealth Presentation - Style Guide

## Overview
This style guide ensures consistency across all pages in the AI Voice Agents presentation for EvergreenHealth. All LLM-generated code must follow these standards.

## Design System Architecture

### File Structure
```
shared/
├── css/
│   ├── variables.css      # CSS custom properties (colors, spacing, typography)
│   ├── base.css          # Base styles, typography, utilities
│   └── components.css    # Reusable UI components
├── js/
│   └── navigation.js     # Presentation navigation system
├── templates/
│   └── page-template.html # Standard HTML structure
└── assets/               # Images, fonts, icons
```

## Color System

### Primary Palette
```css
--eh-green: #006633        /* Main EvergreenHealth brand color */
--eh-green-accent: #4CAF50 /* Lighter accent green */
--eh-blue: #007BFF         /* CSSI blue for highlights */
--eh-blue-light: #E3F2FD   /* Light blue for backgrounds */
--eh-grey: #666666         /* Body text */
--eh-red: #DC3545          /* Alerts and warnings */
--eh-white: #FFFFFF        /* Background */
```

### Usage Guidelines
- **Headings**: Use `--eh-green` for main headings (h1, h2)
- **Body Text**: Use `--eh-grey-dark` (#333333) for primary text
- **Accents**: Use `--eh-blue` for links and call-to-action elements
- **Backgrounds**: Primarily `--eh-white` with subtle `--eh-grey-light` variations

## Typography Scale

### Font Family
- **Primary**: `font-family: var(--font-family-primary)` (Lato from Google Fonts)
- **Monospace**: `font-family: var(--font-family-mono)` (for code/technical content)

### Responsive Typography
```css
h1 { 
  font-size: var(--font-size-4xl);  /* 36px base, 48px tablet, 60px desktop */
  color: var(--eh-green);
}
h2 { 
  font-size: var(--font-size-3xl);  /* 30px base, 36px tablet, 48px desktop */
  color: var(--eh-green);
}
h3 { 
  font-size: var(--font-size-2xl);  /* 24px base, 30px tablet, 36px desktop */
}
```

### Font Weights
- **Light**: `var(--font-weight-light)` (300)
- **Normal**: `var(--font-weight-normal)` (400)
- **Medium**: `var(--font-weight-medium)` (500)
- **Semibold**: `var(--font-weight-semibold)` (600)
- **Bold**: `var(--font-weight-bold)` (700)

## Layout System

### Page Structure
```html
<main class="presentation-page">
  <div class="page-content">
    <!-- Page content here -->
  </div>
</main>
```

### Spacing Scale
Use CSS custom properties for consistent spacing:
```css
--space-2: 0.5rem    /* 8px */
--space-4: 1rem      /* 16px */
--space-6: 1.5rem    /* 24px */
--space-8: 2rem      /* 32px */
--space-12: 3rem     /* 48px */
```

### Responsive Breakpoints
```css
/* Mobile-first approach */
/* Base styles: 320px+ */

@media (min-width: 768px) {
  /* Tablet styles */
}

@media (min-width: 1024px) {
  /* Desktop styles */
}
```

## Component Library

### Buttons
```html
<!-- Primary button -->
<button class="btn btn--primary">Next Page</button>

<!-- Secondary button -->
<button class="btn btn--secondary">Learn More</button>

<!-- Accent button -->
<button class="btn btn--accent">Get Started</button>
```

### Navigation
```html
<nav class="navigation">
  <div class="nav-container">
    <!-- Previous Page (use <a> with href or disabled <button>) -->
    <a href="../page_previous/page_previous.html" class="nav-button nav-prev" aria-label="Previous page: Page Title">Previous</a>
    <!-- OR for first page -->
    <button class="nav-button nav-prev" disabled>Previous</button>
    
    <div class="progress-indicator">...</div>
    
    <!-- Next Page (use <a> with href or disabled <button>) -->
    <a href="../page_next/page_next.html" class="nav-button nav-next" aria-label="Next page: Page Title">Next</a>
    <!-- OR for last page -->
    <button class="nav-button nav-next" disabled>Next</button>
  </div>
</nav>
```

#### Navigation Requirements
- **First Page**: Previous button disabled, Next button links to second page
- **Middle Pages**: Both buttons link to appropriate adjacent pages
- **Last Page**: Previous button links to previous page, Next button disabled
- **Link Format**: Use `<a>` tags with `href` for active navigation, `<button disabled>` for inactive
- **ARIA Labels**: Include descriptive labels with destination page names
- **Relative Paths**: Use `../page_name/page_name.html` format

### Cards
```html
<div class="card">
  <div class="card__header">
    <h3 class="card__title">Card Title</h3>
    <p class="card__subtitle">Optional subtitle</p>
  </div>
  <!-- Card content -->
</div>
```

### Alerts
```html
<div class="alert alert--success">Success message</div>
<div class="alert alert--info">Information message</div>
<div class="alert alert--warning">Warning message</div>
<div class="alert alert--error">Error message</div>
```

## Code Generation Standards

### HTML Requirements
1. **Semantic Structure**: Use proper HTML5 semantic elements (`<main>`, `<section>`, `<article>`, `<nav>`)
2. **Accessibility**: Include ARIA labels, alt text, proper heading hierarchy
3. **Template Usage**: Start with `shared/templates/page-template.html`
4. **Class Naming**: Use BEM methodology (`.block__element--modifier`)

### CSS Requirements
1. **Import Order**:
   ```css
   @import url('../shared/css/variables.css');
   @import url('../shared/css/base.css');
   @import url('../shared/css/components.css');
   ```
2. **Custom Properties**: Use CSS variables, not hardcoded values
3. **Mobile-First**: Write responsive styles starting with mobile
4. **Utility Classes**: Use existing utility classes before creating custom styles

### JavaScript Requirements
1. **Navigation**: Include `../shared/js/navigation.js`
2. **Progressive Enhancement**: Ensure functionality without JavaScript
3. **Event Handling**: Use modern event listeners and async/await
4. **Performance**: Minimize DOM queries, use event delegation

## Content Guidelines

### Writing Style
- **Executive Tone**: Professional, confident, healthcare-appropriate
- **Concise**: 3-5 main points per page maximum
- **Value-Focused**: Emphasize ROI and measurable benefits
- **Action-Oriented**: Clear calls-to-action where appropriate

### Content Structure
```html
<div class="page-content">
  <h1>Page Title</h1>
  <p class="text-large">Brief introduction or key message</p>
  
  <section>
    <h2>Key Points</h2>
    <ul>
      <li>Bullet point 1</li>
      <li>Bullet point 2</li>
      <li>Bullet point 3</li>
    </ul>
  </section>
  
  <!-- Additional sections as needed -->
</div>
```

## Accessibility Standards

### WCAG 2.1 AA Compliance
- **Color Contrast**: Minimum 4.5:1 for normal text, 3:1 for large text
- **Keyboard Navigation**: All interactive elements accessible via keyboard
- **Screen Reader Support**: Proper ARIA labels and semantic markup
- **Focus Management**: Visible focus indicators

### Required Attributes
```html
<!-- Images -->
<img src="image.jpg" alt="Descriptive alt text">

<!-- Buttons -->
<button aria-label="Descriptive label">Icon Button</button>

<!-- Navigation -->
<nav role="navigation" aria-label="Presentation navigation">
```

## Performance Requirements

### Loading Performance
- **Initial Load**: Under 3 seconds on 3G connection
- **Images**: WebP format with fallbacks, lazy loading
- **Fonts**: Efficient web font loading with fallbacks
- **CSS/JS**: Minified and optimized for production

### Animation Guidelines
```css
/* Smooth transitions */
.element {
  transition: all var(--transition-base); /* 250ms ease */
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Brand Consistency

### Logo Usage
- **File**: `cssi_logo_symbol_1.png` (located in `shared/assets/`)
- **Placement**: Top-left corner using `.logo` class
- **Size**: 48×48px (square symbol format)
- **Link**: Clickable link to `https://common-sense.com`
- **Link Attributes**: `target="_blank" rel="noopener noreferrer"`
- **Accessibility**: `aria-label="Visit Common Sense Systems website"`
- **Alt Text**: "Common Sense Systems, Inc."
- **Path**: `../shared/assets/cssi_logo_symbol_1.png` (from page directories)

### Company Name Links
- **Text**: "Common Sense Systems, Inc." should be a clickable link
- **URL**: `https://common-sense.com`
- **Styling**: Use `.company-name` class with `--eh-blue` color
- **Link Attributes**: `target="_blank" rel="noopener noreferrer"`
- **Hover Effect**: Underline on hover (default link behavior)

### Footer Requirements
```html
<footer class="presentation-footer">
  <div class="confidential-mark">Company Confidential</div>
  <div class="page-counter">1 of 8</div>
</footer>
```

## Quality Checklist

Before considering a page complete, verify:
- [ ] Follows HTML template structure
- [ ] Uses shared CSS system consistently
- [ ] Responsive on mobile, tablet, desktop
- [ ] Accessible keyboard navigation
- [ ] Proper ARIA labels and semantic markup
- [ ] Fast loading performance
- [ ] EvergreenHealth brand colors used correctly
- [ ] CSSI logo and confidential marking present
- [ ] Navigation integration working
- [ ] Cross-browser compatibility verified