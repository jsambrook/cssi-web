# Blog Publishing System

A simple, robust system for publishing Markdown blog posts to your website. This system handles converting Markdown to HTML, processing images, and maintaining a blog index with category and tag filtering.

## Overview

This system consists of two main components:

1. **Blog Publisher (`blog_publisher.py`)**: Converts Markdown files to HTML blog posts
2. **Blog Index Generator (`generate_blog_index.py`)**: Generates the blog index page

## Features

- Supports standard Markdown syntax
- Processes images and places them in the correct directories
- Extracts metadata from YAML frontmatter
- Handles categories and tags for filtering
- Creates a responsive blog index with filtering capabilities
- Works with your existing site structure and styling

## Requirements

- Python 3.6+
- Pandoc (for Markdown to HTML conversion)
- PyYAML (for parsing YAML frontmatter)

## Installation

1. Place the scripts in your `/src/bin/` directory
2. Make them executable:
   ```bash
   chmod +x blog_publisher.py
   chmod +x generate_blog_index.py
   ```
3. Install dependencies:
   ```bash
   pip install pyyaml
   ```
4. Install Pandoc:
   ```bash
   # Ubuntu/Debian
   sudo apt-get install pandoc

   # macOS
   brew install pandoc

   # Windows
   # Download from https://pandoc.org/installing.html
   ```

## Usage

### Creating a Blog Post

1. Create a Markdown file with YAML frontmatter:
   ```markdown
   ---
   title: "Your Blog Post Title"
   description: "A brief description of your post"
   date: "2025-04-28"
   author: "Your Name"
   tags: ["Tag1", "Tag2"]
   category: "Your Category"
   slug: "your-post-slug"
   ---

   # Your Blog Post Title

   Your content here...
   ```

2. Include images in your Markdown using standard syntax:
   ```markdown
   ![Image description](images/your-image.jpg)
   ```

3. Publish the post:
   ```bash
   ./blog_publisher.py --input path/to/your-post.md
   ```

### Regenerating the Blog Index

```bash
./generate_blog_index.py
```

## Directory Structure

The system uses the following directory structure:

```
/
├── blog/
│   ├── index.html              # Generated blog index
│   ├── YYYY/                   # Year directory
│   │   ├── MM/                 # Month directory
│   │   │   └── post-slug.html  # Generated blog post
├── src/
│   ├── assets/
│   │   ├── img/
│   │   │   ├── blog/
│   │   │   │   ├── YYYY/
│   │   │   │   │   ├── MM/
│   │   │   │   │   │   └── post-slug/    # Post images
│   ├── bin/
│   │   ├── blog_publisher.py
│   │   ├── generate_blog_index.py
│   │   └── templates/
│   │       └── blog-template.html        # Pandoc template
│   ├── blog/
│   │   ├── blog_index.json               # Blog metadata
│   │   └── drafts/                       # Your markdown files
│   ├── includes/
│   │   ├── blog_cta.html                 # Optional CTA
│   │   ├── blog_index_template.html      # Index template
│   │   └── site_footer.html              # Optional footer
```

## Customization

### Templates

The system uses two templates:

1. **Blog Post Template**: Located at `src/bin/templates/blog-template.html` (created automatically if missing)
2. **Blog Index Template**: Located at `src/includes/blog_index_template.html` (created automatically if missing)

You can customize these templates to match your site's design.

### Additional Elements

The system can include these additional elements:

1. **Call to Action (CTA)**: Located at `src/includes/blog_cta.html`
2. **Footer**: Located at `src/includes/site_footer.html`

## Advanced Options

For more options, use the help flag:

```bash
./blog_publisher.py --help
./generate_blog_index.py --help
```

## Troubleshooting

If you encounter issues:

1. **Missing Template**: Templates are automatically created in the default locations
2. **Pandoc Not Found**: Ensure Pandoc is installed and in your PATH
3. **Image Processing Issues**: Make sure images are in the correct location relative to your Markdown file
4. **Metadata Problems**: Verify your YAML frontmatter syntax is correct

## License

This software is provided as is with no warranty. Feel free to modify it to suit your needs.
