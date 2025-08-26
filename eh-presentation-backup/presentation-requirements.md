# Presentation Requirements

## Overview
This document defines global standards and requirements for the "Unlocking Value with Voice Agents: Opportunities for EvergreenHealth" presentation. Individual slide specifications are maintained in separate `slide_X/spec.md` files.

## Metadata
- **Title**: Unlocking Value with Voice Agents: Opportunities for EvergreenHealth
- **Author**: John Sambrook, President, Common Sense Systems, Inc.
- **Date**: August 27, 2025
- **Target Audience**: EvergreenHealth executives (COO, CTO, Director of Innovation)
- **Duration**: 10-15 minutes (1-2 minutes per page)
- **Total Pages**: 8
- **Format**: Modern Web Presentation (responsive design)

## Technical Specifications

### Build System
- **Primary Format**: Modern Web Presentation for responsive, interactive experience
- **Page Generation**: LLM-generated HTML/CSS/JS per page in `page_<subject>/` directories
- **Master Assembly**: Build script assembles all pages into cohesive presentation
- **Output**: Static HTML site deployed to Digital Ocean droplet

### Directory Structure
```
page_<subject>/
├── spec.md              # Rich specification for LLM code generation
├── index.html          # Generated HTML structure
├── styles.css          # Generated CSS styles
├── script.js           # Generated JavaScript functionality
└── assets/             # Page-specific assets (optional)

shared/
├── css/                # Common styles and theme
├── js/                 # Shared navigation and presentation logic
├── assets/             # Global images, fonts, icons
└── components/         # Reusable HTML components

dist/
├── index.html          # Main presentation entry point
├── page_*/             # Compiled individual pages
└── assets/             # All bundled assets
```

## Visual Design Standards

### Color Palette
Based on EvergreenHealth branding with professional healthcare aesthetics:
- **Primary Green**: `#006633` (ehgreen) - Titles, key accents
- **Accent Green**: `#4CAF50` (ehgreenaccent) - Background elements, positive indicators
- **Primary Blue**: `#007BFF` (ehblue) - Links, highlights, call-to-action elements
- **Light Blue**: `#E3F2FD` (ehbluelight) - Background fills, subtle highlights
- **Text Grey**: `#666666` (ehgrey) - Body text, descriptions
- **Alert Red**: `#DC3545` (ehred) - Challenge indicators, urgent items
- **Background**: `#FFFFFF` (white) - Primary background

### Typography
- **Primary Font**: Lato (clean, professional, healthcare-appropriate)
- **Title Font**: Large, bold Lato for slide titles
- **Body Font**: Normal weight Lato for content
- **Code/Technical**: Monospace for any technical specifications

### Layout Principles
- **Responsive Design**: Mobile-first approach with tablet and desktop breakpoints
- **Viewport**: Full-screen presentation with responsive scaling
- **Whitespace**: Generous margins and spacing optimized for various screen sizes
- **Alignment**: Left-aligned content with centered titles, flexible grid system
- **Consistency**: Uniform spacing, font sizes, and positioning across pages
- **Visual Hierarchy**: Clear distinction between titles, subtitles, and body content
- **Accessibility**: WCAG 2.1 AA compliance, keyboard navigation, screen reader support

### Visual Elements
- **Icons**: Professional, minimalist icons where appropriate (FontAwesome5)
- **Charts**: Clean, data-focused visualizations using TikZ
- **Diagrams**: Process flows, timelines, and organizational charts using TikZ
- **Images**: High-quality, relevant photography with appropriate overlays
- **Branding**: Consistent CSSI logo placement and sizing

## Content Standards

### Messaging Approach
- **Value-Focused**: Emphasize ROI and measurable business benefits
- **Problem-Solution**: Clear articulation of challenges and AI solutions
- **Evidence-Based**: Include specific metrics and industry benchmarks
- **Actionable**: Concrete next steps and implementation pathways

### Content Structure per Page
- **Clear Title**: Descriptive, benefit-oriented page titles
- **Key Messages**: 3-5 main points maximum per page
- **Supporting Evidence**: Metrics, examples, and proof points
- **Visual Support**: Interactive charts, diagrams, or images that reinforce the message
- **Call to Action**: Where appropriate, clear next steps
- **Navigation**: Clear indicators of current position and next/previous pages

### Writing Style
- **Concise**: Brief, impactful bullet points
- **Professional**: Healthcare executive-appropriate tone
- **Specific**: Concrete examples and quantified benefits
- **Compelling**: Engaging language that motivates action

## Technical Integration Requirements

### Web Framework Configuration
- **Technology Stack**: HTML5, CSS3, ES6+ JavaScript
- **Navigation**: Keyboard shortcuts, touch gestures, and button controls
- **Header/Footer**: Consistent CSSI branding and "Company Confidential" marking
- **Progress Indicator**: Visual presentation progress and page counter
- **Routing**: Semantic URLs for direct page access (`/page_introduction`, `/page_challenges`, etc.)

### Asset Management
- **Shared Assets**: Logo, color definitions, and common images in `shared/` directory
- **Slide-Specific Assets**: Charts and diagrams generated as needed
- **Image Quality**: High-resolution images optimized for projection
- **File Organization**: Clear naming conventions and organized directory structure

### LLM Code Generation Workflow
- **Specification Input**: Each `page_<subject>/spec.md` contains rich requirements for LLM
- **Generated Artifacts**: LLM produces HTML, CSS, and JavaScript for each page
- **Template Consistency**: LLM follows shared design system and component patterns
- **Asset Integration**: Generated code references shared assets and maintains branding
- **Quality Validation**: Generated code follows web standards and accessibility guidelines

### Build Process
- **Individual Development**: Each page can be built and tested independently
- **Master Assembly**: Build script combines all pages with shared assets
- **Version Control**: Clean separation allows for targeted updates
- **Error Handling**: Robust build process with validation and clear error reporting
- **Deployment**: Automated deployment to Digital Ocean droplet

## Digital Ocean Hosting Requirements

### Infrastructure Specifications
- **Server Environment**: Optimized for Digital Ocean droplet hosting
- **Static Site Hosting**: Efficient serving of HTML/CSS/JS assets
- **Performance**: Fast loading times with CDN considerations
- **SSL/HTTPS**: Secure hosting with proper certificate management
- **Domain Configuration**: Professional domain setup and DNS management

### Deployment Pipeline
- **Build Automation**: Streamlined deployment process from local development
- **Asset Optimization**: Minification and compression for production
- **Cache Management**: Proper cache headers and asset versioning
- **Error Monitoring**: Basic monitoring and error logging

## Web-Specific Features

### Interactive Elements
- **Touch Navigation**: Swipe gestures for mobile devices
- **Keyboard Shortcuts**: Arrow keys, spacebar, and standard presentation controls
- **URL Routing**: Direct access to individual pages via semantic URLs
- **Browser History**: Proper back/forward button support
- **Fullscreen Mode**: Option for distraction-free presentation view

### Responsive Breakpoints
- **Mobile**: 320px - 768px (portrait and landscape)
- **Tablet**: 768px - 1024px (portrait and landscape)  
- **Desktop**: 1024px+ (standard monitors and projectors)
- **Large Displays**: 1920px+ (conference room displays)

### Performance Requirements
- **Initial Load**: Under 3 seconds on 3G connection
- **Page Transitions**: Smooth animations under 300ms
- **Image Optimization**: WebP format with fallbacks
- **Font Loading**: Efficient web font loading with fallbacks
- **JavaScript**: Progressive enhancement, works without JS

## Quality Standards

### Content Review
- **Accuracy**: All metrics and claims verified against reliable sources
- **Relevance**: Content directly supports the presentation objectives
- **Clarity**: Complex concepts explained in accessible terms
- **Consistency**: Unified voice and messaging throughout

### Visual Review
- **Professional Appearance**: Polished, executive-ready visual quality
- **Brand Compliance**: Consistent with CSSI and healthcare industry standards
- **Readability**: All text and visuals clearly visible in presentation environments
- **Device Compatibility**: Optimized for various display types and sizes

### Technical Review
- **Cross-Browser**: Consistent functionality across modern browsers
- **Performance**: Fast loading times and smooth animations on all devices
- **Mobile Optimization**: Excellent experience on smartphones and tablets
- **Maintainability**: Clean, semantic HTML and modular CSS/JS
- **Extensibility**: Easy to modify and extend for future iterations
- **Hosting**: Optimized for Digital Ocean droplet environment
