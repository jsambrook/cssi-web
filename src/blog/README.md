# Blog Management System

A simple, static file-based blog system for Common Sense Systems, Inc. This system uses Markdown files with YAML front matter to generate HTML blog posts and an index page.

## Directory Structure

```
/website-root
  /blog                  # Published blog content (generated)
    /index.html          # Generated index page
    /2025/04/...         # Generated blog posts

  /src                   # Source files
    /blog                # Blog source files
      /templates         # Templates
        blog_template.html
        blog_index_template.html
      /scripts           # Python scripts
        process_blog.py
      /content           # Raw markdown content
        /2025
          /04
            /post-slug
              /index.md      # Markdown source (always named index.md)
              /assets        # Source assets
```

## How to Add a New Blog Post

1. Create a directory structure for your post:
   ```
   src/blog/content/YEAR/MONTH/post-slug/
   ```
   Example: `src/blog/content/2025/04/ai-transforming-small-business/`

2. Create a Markdown file named `index.md` in the post directory:
   ```
   src/blog/content/2025/04/ai-transforming-small-business/index.md
   ```

3. Add YAML front matter at the top of your Markdown file:
   ```markdown
   ---
   title: "How AI is Transforming Small Business Operations"
   date: 2025-04-28
   author: "John Smith"
   categories: ["AI for Business"]
   tags: ["AI", "Automation", "Small Business", "Process Improvement"]
   summary: "Learn how small businesses can leverage AI to automate tasks and improve efficiency."
   featuredImage: "assets/header-image.jpg"
   status: "published"
   ---

   Content starts here...
   ```

4. Add images and other assets to an `assets` directory:
   ```
   src/blog/content/2025/04/ai-transforming-small-business/assets/header-image.jpg
   ```

5. Generate the blog by running:
   ```bash
   python src/blog/scripts/process_blog.py
   ```

## Front Matter Options

| Field | Description | Example |
|-------|-------------|---------|
| `title` | The post title (required) | `"How AI is Transforming Small Business Operations"` |
| `date` | Publication date (YYYY-MM-DD) | `2025-04-28` |
| `author` | Author name | `"John Smith"` |
| `categories` | Primary categories (array) | `["AI for Business"]` |
| `tags` | More specific tags (array) | `["AI", "Automation", "Small Business"]` |
| `summary` | Brief description for SEO and previews | `"Learn how small businesses can leverage AI..."` |
| `featuredImage` | Path to header image (relative to post) | `"assets/header-image.jpg"` |
| `status` | Publication status | `"published"` or `"draft"` |
| `lastUpdated` | Last modification date | `2025-04-29` |
| `relatedPosts` | Array of related post slugs | `["cloud-computing-guide", "digital-transformation"]` |

## Post Generation Process

The Python script handles:

1. Finding all Markdown files in the content directory
2. Extracting metadata from YAML front matter
3. Converting Markdown to HTML using Pandoc
4. Copying asset files to the output directory
5. Generating the blog index page with filtering capabilities

## Advanced Usage

### Command Line Options

The `process_blog.py` script supports several command line options:

```bash
# Process all posts
python src/blog/scripts/process_blog.py

# Process only a specific post
python src/blog/scripts/process_blog.py --post "ai-transforming-small-business"

# Process posts from a specific time period
python src/blog/scripts/process_blog.py --year 2025 --month 04

# Only rebuild the index (without regenerating posts)
python src/blog/scripts/process_blog.py --rebuild-index

# Use custom directories
python src/blog/scripts/process_blog.py --content-root "./content" --output-root "./public/blog"
```

### Blog Post Features

- **Formatting**: Standard Markdown formatting (headings, lists, links, etc.)
- **Code blocks**: Syntax highlighted code snippets
- **Images**: Include images with `![Alt text](assets/image.jpg)`
- **Math**: MathJax support for mathematical formulas

## Maintenance

### Modifying Templates

To change the appearance of blog posts or the index page, edit the template files:

- `src/blog/templates/blog_template.html` - Template for individual posts
- `src/blog/templates/blog_index_template.html` - Template for the index page

### Adding New Categories or Tags

Categories and tags are generated automatically based on the front matter in your posts. To add a new category or tag, simply include it in a post's front matter.

### Workflow for Updates

1. Make changes to your Markdown files
2. Run `python src/blog/scripts/process_blog.py`
3. Commit both the source files and generated HTML to version control
4. Deploy to your web server

## Requirements

- Python 3.6+
- PyYAML
- Pandoc (for Markdown to HTML conversion)

Install the required Python packages:
```bash
pip install pyyaml
```

## Troubleshooting

- **Missing metadata**: If front matter is missing or malformed, default values will be used
- **Image paths**: Ensure images paths are relative to the post directory
- **Draft posts**: Posts with `status: "draft"` will be skipped during generation

## Best Practices

1. **Consistent naming**: Use kebab-case for directory names and file names (`like-this-example`)
2. **Image optimization**: Optimize images before adding them to reduce page load times
3. **Front matter**: Include all recommended front matter fields for better SEO and site functionality
4. **Backup**: Regularly backup your content directory
5. **Version control**: Keep both source and generated files in version control

## Support

For questions or assistance with the blog system, contact the web development team.
