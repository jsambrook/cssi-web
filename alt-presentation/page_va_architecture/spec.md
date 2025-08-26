# Voice Agent Architecture Page Specification

## Page Overview
This page provides EvergreenHealth executives with a detailed visualization of how AI voice agents work internally. The page demonstrates technical sophistication while remaining accessible to healthcare leadership, showcasing the comprehensive architecture that powers modern voice AI solutions.

## Content Requirements

### Page Title
**"Inside a Typical AI Voice Agent"**
- Large, prominent display using EvergreenHealth green (#006633)
- Professional, healthcare-executive appropriate typography
- Centered above the diagram

### Main Visual Element: Interactive SVG Diagram
The centerpiece of this page is a comprehensive, interactive SVG diagram showing the complete architecture of an AI voice agent system.

#### SVG Diagram Specifications
- **Canvas Size**: 1200×900 pixels (viewBox: `0 0 1200 900`)
- **Background**: Clean white background
- **Title**: "AI Voice Agent Architecture" centered at top of diagram
- **Position**: Centered on page with responsive scaling

#### Required Components (7 total):

1. **User's Phone**
   - Position: Left side (x: 50, y: 200)
   - Size: 100×160 pixels, rounded corners (rx: 20)
   - Color: Blue gradient (#4a90e2 to #357abd)
   - Icon: 📱 emoji
   - Labels: "User's Phone"
   - Tooltip: "User's smartphone initiating voice call"

2. **Twilio**
   - Position: Left-center (x: 250, y: 230)
   - Size: 120×100 pixels, rounded corners (rx: 15)
   - Color: Red gradient (#f22f46 to #c21e3a)
   - Icon: ☁️ emoji
   - Labels: "Twilio", "Voice API"
   - Tooltip: "Twilio handles telephony and WebRTC connections"

3. **ElevenLabs Voice Agent**
   - Position: Center (x: 450, y: 200)
   - Size: 140×160 pixels, rounded corners (rx: 15)
   - Color: Purple gradient (#8b5cf6 to #7c3aed)
   - Icon: 🎙️ emoji
   - Labels: "ElevenLabs", "Voice Agent", "STT Processing", "Audio Handling"
   - Tooltip: "ElevenLabs hosts the voice agent with STT/TTS capabilities"

4. **System Prompt**
   - Position: Top-right (x: 700, y: 80)
   - Size: 140×120 pixels, rounded corners (rx: 15)
   - Color: Dark purple gradient (#7c2d92 to #5b1a6b)
   - Icon: 📝 emoji
   - Labels: "System", "Prompt", "Instructions", "Personality"
   - Tooltip: "System prompt defines LLM behavior, personality, and instructions"

5. **Claude 4 Sonnet**
   - Position: Right-center (x: 700, y: 250)
   - Size: 140×160 pixels, rounded corners (rx: 15)
   - Color: Orange gradient (#d97706 to #b45309)
   - Icon: 🧠 emoji
   - Labels: "Claude 4", "Sonnet", "Language Model", "Reasoning Engine"
   - Tooltip: "Claude 4 Sonnet processes natural language and generates responses"

6. **Knowledge Base**
   - Position: Far right (x: 950, y: 250)
   - Size: 140×160 pixels, rounded corners (rx: 15)
   - Color: Green gradient (#059669 to #047857)
   - Icon: 📚 emoji
   - Labels: "Knowledge", "Base", "Vector Database", "RAG System"
   - Tooltip: "Vector database with RAG for contextual information retrieval"

7. **TTS Model**
   - Position: Bottom-right (x: 700, y: 550)
   - Size: 140×120 pixels, rounded corners (rx: 15)
   - Color: Red gradient (#dc2626 to #b91c1c)
   - Icon: 🔊 emoji
   - Labels: "TTS Model", "Text-to-Speech", "Voice Synthesis"
   - Tooltip: "Text-to-Speech model converts text responses to natural speech"

#### Data Flow Connections (10 total):
1. **flow0**: System Prompt → Claude (vertical line, "Configuration")
2. **flow1**: Phone → Twilio (horizontal line, "Voice Call")
3. **flow2**: Twilio → ElevenLabs (horizontal line, "Audio Stream")
4. **flow3**: ElevenLabs → Claude (diagonal line, "Text Query")
5. **flow4**: Claude → Knowledge Base (horizontal line, "RAG Query")
6. **flow5**: Knowledge Base → Claude (horizontal line, "Context Data")
7. **flow6**: Claude → TTS (vertical line, "Response Text")
8. **flow7**: TTS → ElevenLabs (curved path, "Audio Response")
9. **flow8**: ElevenLabs → Twilio (horizontal line, "Speech Output")
10. **flow9**: Twilio → Phone (horizontal line, "Voice Response")

### Interactive Features Required:

#### JavaScript Functionality:
- **Hover Effects**: Components scale to 105% with glow on hover, show tooltips
- **Click Highlighting**: Clicking components highlights their connected flow paths
- **Auto-Animation**: Continuous cycling through flow sequence (1-second intervals)
- **Flow Mapping**: Define component-to-flow relationships:
  ```javascript
  const flowMap = {
    'phone': ['flow1', 'flow9'],
    'twilio': ['flow1', 'flow2', 'flow8', 'flow9'],
    'elevenlabs': ['flow2', 'flow3', 'flow7', 'flow8'],
    'system-prompt': ['flow0'],
    'claude': ['flow0', 'flow3', 'flow4', 'flow5', 'flow6'],
    'knowledge-base': ['flow4', 'flow5'],
    'tts': ['flow6', 'flow7']
  };
  ```
- **Animation Sequence**: Start 2 seconds after load, cycle: flow0→flow1→flow2→flow3→flow4→flow5→flow6→flow7→flow8→flow9→repeat

### Visual Design Requirements

#### Color Scheme
- **Background**: Clean white (#FFFFFF)
- **Page Title**: EvergreenHealth green (#006633)
- **Component Gradients**: As specified above
- **Flow Lines**: #666 gray (2px width), #4ade80 green when active (3px with glow)
- **Typography**: Arial sans-serif, white text on components, dark gray (#1f2937) for titles

#### Layout
- **Centered Design**: Diagram centered on page with generous whitespace
- **Responsive**: Must scale appropriately for mobile, tablet, and desktop
- **Professional**: Clean, technical but accessible to healthcare executives

#### Branding Elements
- **CSSI Logo**: Common Sense logo symbol in upper-left corner (already in template)
- **Company Confidential**: Footer marking
- **EvergreenHealth Colors**: Use brand colors for page title and accents

## Technical Specifications

### Generated Files
- **page_va_architecture.html**: Complete standalone HTML page with embedded SVG
- **SVG Requirements**: Self-contained with embedded CSS and JavaScript
- **No External Dependencies**: All functionality must work without external libraries

### SVG Technical Requirements
- **Structure**: Include gradients/filters in `<defs>`, embedded `<style>` and `<script>`
- **Accessibility**: Proper contrast ratios, descriptive tooltips, keyboard navigation
- **Browser Compatibility**: Standard SVG features, modern browser support
- **Optimization**: Works on both desktop and mobile

### Performance Requirements
- Fast loading with optimized SVG
- Smooth animations and transitions
- Interactive features work reliably
- Professional presentation quality

### Accessibility
- Proper heading hierarchy (h1 for page title)
- Alt text and tooltips for all diagram components
- Keyboard navigation support where possible
- High contrast ratios throughout

## Content Tone
- **Technical but Accessible**: Sophisticated enough for IT leaders, clear for healthcare executives
- **Professional**: Appropriate for C-level healthcare audience
- **Educational**: Helps executives understand voice AI complexity and sophistication
- **Trustworthy**: Demonstrates CSSI's deep technical knowledge

## Navigation Requirements

### Page Position
- **Current Page**: 2 of 8
- **Progress**: 25% (2/8 * 100)

### Navigation Links
- **Previous Page**: `../page_home/page_home.html` (Home page)
- **Next Page**: [To be defined when next page is created]
- **Page Order**: Home → Voice Agent Architecture → [Future Pages]

## Success Criteria
This page should effectively communicate:
1. The sophisticated, multi-component nature of modern voice AI systems
2. How different technologies integrate to create seamless voice experiences
3. The technical depth and complexity that CSSI manages for clients
4. The professional, enterprise-grade nature of the voice agent architecture
5. Clear understanding of data flow and processing in voice AI systems

## Interactive Experience Goals
- **Engagement**: Executives can explore the diagram interactively
- **Understanding**: Clear visualization of complex technical relationships
- **Professional**: Polished, client-presentation quality
- **Educational**: Learn through interaction and animation
- **Memorable**: Sophisticated technical demonstration that reinforces CSSI expertise