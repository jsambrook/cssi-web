# Instructions for Regenerating AI Voice Agent Architecture Diagram

## Overview
Create an interactive SVG diagram showing an AI voice agent architecture. The diagram should be professional, interactive, and suitable for client presentations. The final SVG should be self-contained with embedded CSS and JavaScript.

## Canvas Specifications
- **SVG ViewBox**: `0 0 1200 900` (to accommodate all components)
- **Background**: Clean white background
- **Title**: "AI Voice Agent Architecture" centered at top

## Components to Include

### 1. User's Phone
- **Position**: Left side (x: 50, y: 200)
- **Size**: 100×160 pixels, rounded corners (rx: 20)
- **Color**: Blue gradient (#4a90e2 to #357abd)
- **Icon**: 📱 emoji
- **Labels**: "User's Phone"
- **Tooltip**: "User's smartphone initiating voice call"

### 2. Twilio
- **Position**: Left-center (x: 250, y: 230)
- **Size**: 120×100 pixels, rounded corners (rx: 15)
- **Color**: Red gradient (#f22f46 to #c21e3a)
- **Icon**: ☁️ emoji
- **Labels**: "Twilio", "Voice API"
- **Tooltip**: "Twilio handles telephony and WebRTC connections"

### 3. ElevenLabs Voice Agent
- **Position**: Center (x: 450, y: 200)
- **Size**: 140×160 pixels, rounded corners (rx: 15)
- **Color**: Purple gradient (#8b5cf6 to #7c3aed)
- **Icon**: 🎙️ emoji
- **Labels**: "ElevenLabs", "Voice Agent", "STT Processing", "Audio Handling"
- **Tooltip**: "ElevenLabs hosts the voice agent with STT/TTS capabilities"

### 4. System Prompt
- **Position**: Top-right (x: 700, y: 80)
- **Size**: 140×120 pixels, rounded corners (rx: 15)
- **Color**: Dark purple gradient (#7c2d92 to #5b1a6b)
- **Icon**: 📝 emoji
- **Labels**: "System", "Prompt", "Instructions", "Personality"
- **Tooltip**: "System prompt defines LLM behavior, personality, and instructions"

### 5. Claude 4 Sonnet
- **Position**: Right-center (x: 700, y: 250)
- **Size**: 140×160 pixels, rounded corners (rx: 15)
- **Color**: Orange gradient (#d97706 to #b45309)
- **Icon**: 🧠 emoji
- **Labels**: "Claude 4", "Sonnet", "Language Model", "Reasoning Engine"
- **Tooltip**: "Claude 4 Sonnet processes natural language and generates responses"

### 6. Knowledge Base
- **Position**: Far right (x: 950, y: 250)
- **Size**: 140×160 pixels, rounded corners (rx: 15)
- **Color**: Green gradient (#059669 to #047857)
- **Icon**: 📚 emoji
- **Labels**: "Knowledge", "Base", "Vector Database", "RAG System"
- **Tooltip**: "Vector database with RAG for contextual information retrieval"

### 7. TTS Model
- **Position**: Bottom-right (x: 700, y: 550)
- **Size**: 140×120 pixels, rounded corners (rx: 15)
- **Color**: Red gradient (#dc2626 to #b91c1c)
- **Icon**: 🔊 emoji
- **Labels**: "TTS Model", "Text-to-Speech", "Voice Synthesis"
- **Tooltip**: "Text-to-Speech model converts text responses to natural speech"

## Flow Connections & Labels

### Flow Sequence (with IDs for JavaScript control):
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

## Visual Styling Requirements

### Colors & Gradients
- Use linear gradients for all component backgrounds
- Components should have matching stroke colors (darker versions of fill)
- Flow lines: #666 gray, 2px width
- Active flow lines: #4ade80 green, 3px width with glow effect

### Typography
- **Font**: Arial, sans-serif
- **Title**: 24px, bold, dark gray (#1f2937)
- **Component text**: White, bold, centered
- **Labels**: 12px, dark gray (#333), centered
- **Tooltips**: 12px, white text on dark background

### Interactive Effects
- **Hover**: Scale components to 105%, add glow filter
- **Tooltips**: Dark background (#1f2937), rounded corners, positioned above components
- **Flow animations**: Dashed lines with moving dash offset animation

## JavaScript Functionality

### Required Interactive Features:
1. **Hover Effects**: Show tooltips on component hover
2. **Click Highlighting**: Clicking components highlights their connected flow paths
3. **Auto-Animation**: Continuous cycling through flow sequence (1-second intervals)
4. **Flow Mapping**: Define which flows connect to each component

### Component-to-Flow Mapping:
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

### Animation Sequence:
Start auto-animation 2 seconds after page load, cycling through flows: flow0 → flow1 → flow2 → flow3 → flow4 → flow5 → flow6 → flow7 → flow8 → flow9 → repeat

## Technical Requirements

### SVG Structure:
- Include all gradients and filters in `<defs>` section
- Use embedded `<style>` for CSS animations and transitions
- Include arrow markers for flow lines
- Embed JavaScript in `<script>` section with CDATA wrapper

### Accessibility:
- Ensure proper contrast ratios
- Include descriptive tooltips for all components
- Make diagram keyboard-navigable if possible

### Browser Compatibility:
- Use standard SVG features supported across modern browsers
- Avoid experimental CSS properties
- Test interactive features work without external libraries

## Final Notes
- The diagram should be completely self-contained (no external dependencies)
- Optimize for both desktop and mobile viewing
- Ensure professional appearance suitable for client presentations
- All text should be legible and components clearly distinguishable
- Flow lines should clearly indicate data direction with arrow markers