# CLAUDE.md - Common Sense Systems Static Website

## Build Commands
- `make` - Build all static HTML pages (default)
- `make pages` - Build only static site pages
- `make clean` - Prune drafts and remove generated HTML
- `make rebuild` - Clean and rebuild everything
- `make blog-today DESCRIPTION="Blog description"` - Generate today's blog post
- `make blog-index` - Regenerate blog index from metadata
- `make prune-drafts` - Remove draft files older than 30 days
- `make help` - Show all available commands

### Blog Index Gotcha
**Important**: When adding new blog posts, the blog index may not update properly due to caching. If a new post doesn't appear at the top of the blog index:
1. Delete the cache file: `rm src/blog/.blog_cache.json`
2. Force rebuild the index: `make blog-index`
3. Commit and push the updated `blog/index.html`

This ensures new posts appear chronologically at the top of the blog list.

## Code Style Guidelines
- **Python**: Follow PEP 8 style guide with docstrings for all scripts and functions
- **M4**: Use consistent macro naming (uppercase for macros) with m4_dnl for clean output
- **HTML**: Use semantic HTML with proper indentation
- **File Structure**: Maintain `/blog/YYYY/MM/slug.html` pattern for all posts

## Naming Conventions
- **Functions**: Use snake_case for Python functions
- **Variables**: Use descriptive lowercase names with underscores
- **Files**: Use lowercase with hyphens for HTML/M4 files
- **Blog slugs**: Use hyphenated-lowercase-names

## Error Handling
- Use try/except blocks with specific exception types
- Validate inputs and provide meaningful error messages
- Check file existence before reading/writing

## Project Workflow
1. For blog posts, use `make blog-today DESCRIPTION="..."` to generate JSON draft
2. For code changes, test locally before committing
3. Run `make clean && make` to verify all pages build correctly
4. Commit changes with descriptive messages

## Dependencies
- Python 3.8+ with OpenAI API
- GNU Make
- M4 macro processor

Remember to set OPENAI_API_KEY environment variable for blog generation.