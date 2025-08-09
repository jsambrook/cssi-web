# Home Page Specification

## Page Overview
The home page serves as the title slide for the presentation, creating a professional first impression for EvergreenHealth executives. This page should establish credibility, set expectations, and reflect both CSSI's expertise and understanding of healthcare challenges.

## Content Requirements

### Primary Title
**"AI Voice Agents - A Discussion with EvergreenHealth"**
- Large, prominent display using EvergreenHealth green (#006633)
- Should be the visual focal point of the page
- Professional, healthcare-executive appropriate typography

### Presentation Metadata
- **Date**: August 27, 2025
- **Author**: John Sambrook, President
- **Company**: Common Sense Systems, Inc.
- Display in smaller, professional typography below main title

### Visual Design Requirements

#### Color Scheme
- **Background**: Clean white (#FFFFFF) with subtle texture or gradient if appropriate
- **Primary Title**: EvergreenHealth green (#006633)
- **Metadata**: Text grey (#666666)
- **Accent Elements**: CSSI blue (#007BFF) for company name or other highlights

#### Layout
- **Centered Design**: All content centered on page with generous whitespace
- **Visual Hierarchy**: Clear distinction between title, subtitle, and metadata
- **Responsive**: Must work perfectly on mobile, tablet, and desktop
- **Professional**: Clean, uncluttered, executive-boardroom appropriate

#### Branding Elements
- **CSSI Logo**: Common Sense logo symbol (`cssi_logo_symbol_1.png`) in upper-left corner, 48×48px
  - Must be clickable link to `https://common-sense.com`
  - Use `target="_blank" rel="noopener noreferrer"`
  - Include `aria-label="Visit Common Sense Systems website"`
- **Company Name Link**: "Common Sense Systems, Inc." text must be clickable
  - Links to `https://common-sense.com`
  - Use CSSI blue color (#007BFF) for styling
  - Include hover underline effect
- **Company Confidential**: Small footer marking as per requirements
- **EvergreenHealth Colors**: Use brand colors to show attention to their identity

### Interactive Elements
- **Navigation Hint**: Subtle indication that this is a navigable presentation
- **Next Page**: Clear way to proceed to next page (arrow, button, or swipe hint)
- **Progress Indicator**: Show this is page 1 of 8 total pages

## Navigation Requirements

### Page Position
- **Current Page**: 1 of 8
- **Progress**: 12.5% (1/8 * 100)

### Navigation Links
- **Previous Page**: None (this is the first page - Previous button should be disabled)
- **Next Page**: `../page_va_architecture/page_va_architecture.html` (Voice Agent Architecture)
- **Page Order**: Home → Voice Agent Architecture → [Future Pages]

## Technical Specifications

### Generated Files
- **page_home.html**: Complete standalone HTML page
- **styles.css**: Page-specific styling (if needed beyond shared styles)
- **script.js**: Any page-specific JavaScript functionality

### Responsive Breakpoints
- **Mobile (320-768px)**: Title readable, clean layout, touch-friendly navigation
- **Tablet (768-1024px)**: Optimized spacing, larger typography
- **Desktop (1024px+)**: Full design with optimal proportions for presentation

### Performance Requirements
- Fast loading with optimized assets
- Smooth transitions and animations
- Works without JavaScript (progressive enhancement)

### Accessibility
- Proper heading hierarchy (h1 for main title)
- Alt text for logo and any images
- Keyboard navigation support
- High contrast ratios

## Content Tone
- **Professional**: Appropriate for healthcare C-level executives
- **Confident**: Establishes CSSI as expert in healthcare AI solutions
- **Focused**: Clear value proposition for EvergreenHealth specifically
- **Trustworthy**: Healthcare industry requires high trust and credibility

## Success Criteria
This page should immediately communicate:
1. This is a professional, executive-level presentation
2. The focus is specifically on EvergreenHealth's opportunities
3. Common Sense Systems understands healthcare challenges
4. The presentation will provide actionable insights about voice AI
5. Easy navigation to continue through the presentation
