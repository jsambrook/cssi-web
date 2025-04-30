# BLOG ARTICLE GENERATION GUIDELINES

## Blog Format and Structure

Generate a complete blog article using Markdown format that follows these requirements:

1. **YAML Front Matter**: Begin with YAML front matter enclosed by triple dashes (---) containing:
   - title: "Article Title" (clear, engaging, under 70 characters)
   - date: YYYY-MM-DD (use today's date)
   - author: "Author Name" (default: "Common Sense Systems")
   - categories: ["Primary Category"] (choose 1-2 most relevant categories)
   - tags: ["Tag1", "Tag2", "Tag3", "Tag4"] (4-6 specific keywords)
   - summary: "A concise 1-2 sentence description of the article" (under 160 characters)
   - featuredImage: "assets/header-image.jpg" (always use this path)
   - status: "published"

2. **Content Structure**:
   - Start with a compelling introduction (2-3 paragraphs)
   - Use H2 (##) for main sections and H3 (###) for subsections
   - Include 4-6 main sections with descriptive headings
   - End with a clear conclusion/summary section
   - Total length should be 1200-1800 words

3. **Formatting**:
   - Use paragraph breaks for readability (no walls of text)
   - Use bullet points or numbered lists where appropriate
   - Include 1-2 blockquotes for emphasis where relevant
   - Use bold or italic text for emphasis (sparingly)

4. **Images**:
   - Reference the header image at appropriate places: ![Descriptive Alt Text](assets/header-image.jpg)
   - Additional images should use naming pattern: ![Alt Text](assets/image-descriptive-name.jpg)
   - Always include alt text that describes the image content

5. **Technical Elements** (if applicable):
   - Use code blocks with language specification for code snippets: ```python
   - Use tables for structured data comparison
   - Use proper Markdown hyperlinks: [Link Text](https://example.com)

## Content Quality Guidelines

1. **Voice and Tone**:
   - Professional but conversational
   - Knowledgeable but not overly technical
   - Write for small to medium business owners/operators
   - Be helpful, practical, and solution-oriented

2. **Content Focus**:
   - Focus on actionable insights and practical applications
   - Include examples, case studies, or scenarios
   - Address real business problems and solutions
   - Provide specific, concrete recommendations

3. **SEO Optimization**:
   - Use the target keyword in first paragraph, conclusion, and 2-3 H2 headings
   - Include LSI keywords naturally throughout the text
   - Write descriptive meta summary that includes the primary keyword
   - Aim for multiple long-tail keyword phrases

4. **Content Types**:
   - How-to guides
   - Industry trend analysis
   - Technology guides relevant to small business
   - Case studies and success stories
   - Product/service overviews
   - Problem-solution articles

5. **Credibility Markers**:
   - Include statistics with proper attribution
   - Reference recognized industry sources
   - Include expert insights or quotes where appropriate
   - Mention specific tools, platforms, or technologies by name

## Technical Requirements

1. This blog uses a static file system with specific directory structure
2. All assets must be referenced from the "assets" directory
3. The markdown file will be processed by Pandoc to generate HTML
4. Code syntax highlighting is supported
5. Math formulas using MathJax are supported
6. Ensure all links are properly formatted and functional
7. Use relative paths for internal links

## Primary Categories

Choose from these main categories:
- AI for Business
- Process Automation
- Cloud Computing
- Small Business Technology
- Digital Transformation
- Data Analytics
- Productivity
- Business Strategy
- Software Solutions
- Industry Trends

## Common Tags

Choose relevant tags from this list (or suggest new ones):
- AI
- Automation
- Small Business
- Process Improvement
- Cloud Services
- Data Security
- Remote Work
- Productivity Tools
- Cost Reduction
- Customer Experience
- Integration
- Digital Strategy
- Analytics
- Collaboration
- Efficiency
- ROI
- Technology Adoption
- Scalability
