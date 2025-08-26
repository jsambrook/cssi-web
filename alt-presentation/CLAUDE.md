# CLAUDE.md - EvergreenHealth AI Voice Agents Presentation

## Project Overview
Web-based presentation: "Unlocking Value with Voice Agents: Opportunities for EvergreenHealth"
- **Target Audience**: EvergreenHealth executives (COO, CTO, Director of Innovation)  
- **Duration**: 12-18 minutes (10 pages total)
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

## Fact-Check Documentation

### EvergreenHealth 2025 Levy - VERIFIED FACTS
- **Proposed levy rate**: 50 cents per $1,000 assessed value (for collection in 2026)
- **Current levy rate**: ~14 cents per $1,000 assessed value  
- **Increase amount**: 36 cents per $1,000 (verified from King County Elections)
- **Source**: King County Elections ballot measures (Reference #11)
- **Last verified**: January 2025
- **Note**: Do NOT confuse current rate (14¢) with proposed rate (50¢)

### EvergreenHealth Financial Losses - VERIFIED FACTS
- **2022 Financial Loss**: $87.9 million (calculated from cumulative $158M - 2023 loss of $70.1M)
- **2023 Financial Loss**: $70.1 million (verified from EH 2023 Annual Report, page 6)
- **Cumulative 2022-2023**: $158 million total (verified from Chief Healthcare Executive)
- **Source**: EH 2023 Annual Report + Chief Healthcare Executive article
- **Last verified**: January 2025
- **Note**: Individual yearly figures provide more specific context than cumulative totals

### Healthcare Industry Claims - CORRECTED FACTS (January 2025)
- **Rural Healthcare Shortages**: 91% of rural counties NATIONALLY lack primary care (NOT Washington-specific)
- **Washington State Physician Shortage**: Projected short 6,037 doctors; 32.7% within retirement range
- **King County Population Growth**: 0.3% annual growth (NOT 3% as originally claimed)
- **Ransomware Increase**: 149% increase in 2025 verified through multiple cybersecurity sources
- **Hospital Consolidation**: 20-30% price increases since 1980s verified through academic research
- **Source Attribution**: All statistics now properly attributed to verifiable sources
- **Last verified**: January 2025

### Healthcare Challenge Page - VERIFIED STATISTICS (January 2025)
- **Call Abandonment**: 7% abandonment rate for healthcare call centers (140 patients/day for 2,000 call centers)
- **Staff Burnout**: 56% of nurses report burnout, 41% plan to leave within 2 years
- **Physician Burnout**: 47.3% of physicians report burnout, down from 63% peak in 2021
- **Wait Time Impact**: 60% of patients abandon calls after 1 minute wait, costing $45,000 daily per practice
- **Patient Experience Gap**: 7.7-point satisfaction gap between age groups (18-34 vs 65-79)
- **Financial Impact**: Healthcare burnout costs $4.6B annually; $500K-$1M per physician turnover
- **Source Attribution**: AMA 2024, Press Ganey 2024, Dialog Health 2025, KLAS Research 2024
- **Last verified**: January 2025

### Content Accuracy Guidelines
- Always verify financial figures against primary sources
- Double-check ballot measure details before publication
- Cross-reference board minutes with official election materials
- **CRITICAL**: Verify national vs. state-specific statistics before attribution
- **MANDATORY**: Test all reference links quarterly for 404 errors
- **REQUIRED**: Add "Last verified" dates to all statistical claims
- Document all fact-checks in this section to prevent regression
- Prefer specific yearly breakdowns over cumulative figures when available
- Maintain source hierarchy: Government > Academic > Industry reports