# CLAUDE.md - EvergreenHealth AI Voice Agents Presentation

## Project Overview
Web-based presentation: "Unlocking Value with Voice Agents: Opportunities for EvergreenHealth"
- **Target Audience**: EvergreenHealth executives (COO, CTO, Director of Innovation)  
- **Duration**: 10-15 minutes (8 pages total)
- **Deployment**: Digital Ocean droplet at test.common-sense.com
- **Technology**: Modern HTML5/CSS3/JavaScript web presentation

## Build Commands
- `make build` - Generate all pages and assemble presentation
- `make page PAGE=<subject>` - Build individual page from spec.md
- `make deploy` - Deploy to Digital Ocean droplet
- `make dev` - Start local development server
- `make clean` - Remove generated files
- `make validate` - Check all pages for compliance

## Directory Structure
```
page_<subject>/
├── spec.md              # Rich specification for LLM code generation
├── index.html          # Generated HTML structure  
├── styles.css          # Generated CSS styles
├── script.js           # Generated JavaScript functionality
└── assets/             # Page-specific assets

shared/
├── css/                # Common styles and EvergreenHealth theme
├── js/                 # Navigation and presentation logic
├── assets/             # Global images, fonts, CSSI logo
└── components/         # Reusable HTML components

dist/                   # Production build output
```

## LLM Code Generation Workflow
1. Create `page_<subject>/spec.md` with detailed requirements
2. LLM generates HTML/CSS/JS based on specification following strict guidelines
3. **MUST READ** `shared/style-guide.md` before generating any code
4. **MUST USE** `shared/templates/page-template.html` as starting point
5. Follow EvergreenHealth color palette and CSSI branding
6. Ensure responsive design for mobile/tablet/desktop
7. Build script assembles pages with shared navigation

### Code Generation Rules (NON-NEGOTIABLE)
- **Template**: Always start with `shared/templates/page-template.html`
- **CSS Imports**: Must include all three shared stylesheets in order:
  ```html
  <link rel="stylesheet" href="../shared/css/variables.css">
  <link rel="stylesheet" href="../shared/css/base.css">
  <link rel="stylesheet" href="../shared/css/components.css">
  ```
- **CSS Variables**: Use CSS custom properties, never hardcoded values
- **HTML Structure**: Follow semantic HTML5 with proper accessibility
- **File Naming**: Generate `page_<subject>.html` (not `index.html`)
- **Dependencies Check**: Only regenerate if `page_<subject>.html` older than `spec.md`
- **Logo Links**: Logo must link to `https://common-sense.com` (already in template)
- **Company Name Links**: "Common Sense Systems, Inc." text must be clickable link to `https://common-sense.com`
- **Navigation**: Read Navigation Requirements section in spec.md and implement exact links/disabled states

## Design Standards
- **Colors**: EvergreenHealth green (#006633), accent green (#4CAF50), CSSI blue (#007BFF)
- **Typography**: Web fonts with fallbacks, healthcare-appropriate styling  
- **Logo**: Common Sense symbol (`cssi_logo_symbol_1.png`) in upper-left, 48×48px
- **Layout**: Mobile-first responsive design, WCAG 2.1 AA compliance
- **Navigation**: Keyboard shortcuts, touch gestures, semantic URLs
- **Performance**: Under 3 seconds load time, smooth transitions

## Content Requirements
- Professional healthcare executive tone
- Value-focused messaging with ROI emphasis
- 3-5 key points maximum per page
- Supporting evidence with specific metrics
- Clear call-to-action where appropriate

## Technical Specifications
- **Framework**: Vanilla JavaScript or lightweight library
- **Routing**: Semantic URLs (`/page_introduction`, `/page_challenges`)
- **Assets**: WebP images with fallbacks, optimized fonts
- **Hosting**: Static site optimized for Digital Ocean environment
- **Security**: HTTPS, proper headers, no sensitive data exposure

## Deployment Target
- **Server**: test.common-sense.com Digital Ocean droplet
- **Path**: `/eh-presentation/` or dedicated subdomain
- **SSL**: Required for professional presentation
- **Performance**: CDN considerations for fast loading

## LLM Code Generation Instructions

### Before Generating Code
1. **Read the style guide**: Always read `shared/style-guide.md` first
2. **Check dependencies**: Only generate if HTML file missing or older than spec.md
3. **Review spec.md**: Understand page requirements and content needs

### Code Generation Process
1. **Copy template**: Start with `shared/templates/page-template.html`
2. **Read Navigation Requirements**: Check spec.md for page position, previous/next links
3. **Replace variables**: Update all `{{TEMPLATE_VARIABLES}}` with actual values
4. **Implement Navigation**: Set correct Previous/Next button links or disabled states
5. **Add content**: Insert semantic HTML in `{{PAGE_CONTENT}}` section
6. **Use shared classes**: Leverage existing CSS components and utilities
7. **Test responsiveness**: Ensure mobile-first responsive design
8. **Validate accessibility**: Include proper ARIA labels and semantic structure

### File Naming and Structure
- **HTML File**: `page_<subject>.html` (e.g., `page_home.html`)
- **CSS File**: Optional `page_<subject>.css` only if custom styles needed
- **JS File**: Optional `page_<subject>.js` only if custom functionality needed
- **Assets**: Place page-specific assets in `page_<subject>/assets/`

### Quality Standards for Generated Code
- Semantic HTML5 with proper heading hierarchy
- Mobile-first responsive CSS using shared variables
- Accessibility compliance (WCAG 2.1 AA)
- Performance optimization (fast loading, minimal assets)
- Cross-browser compatibility
- Proper error handling and graceful degradation

## Quality Checklist (Before Marking Page Complete)
- [ ] Uses shared template as starting point
- [ ] All CSS variables used (no hardcoded values)  
- [ ] Mobile responsive on all devices
- [ ] Keyboard navigation functional  
- [ ] WCAG accessibility compliance
- [ ] EvergreenHealth branding colors correct
- [ ] CSSI logo symbol (`cssi_logo_symbol_1.png`) in upper-left corner
- [ ] Logo links to `https://common-sense.com` with proper attributes
- [ ] Company name text links to `https://common-sense.com`
- [ ] "Company Confidential" footer present
- [ ] Page loads under 3 seconds
- [ ] Cross-browser compatibility verified
- [ ] Navigation integration working
- [ ] Semantic HTML structure maintained