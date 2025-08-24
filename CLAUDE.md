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

### Blog Processing Best Practices

#### Efficient Blog Operations (Updated 2025-08-24)
The blog processing system has been optimized for efficiency. Normal operations now process only changed files:

**✅ Standard Workflow:**
- `python3 src/blog/scripts/process_blog.py` - Processes only changed posts + smart index rebuild (~8 seconds)
- `python3 check_links.py` - Validate all 121+ blog links are working

**🔧 Force Options (Use Sparingly):**
- `--force-posts` - Rebuild all posts but smart index (recommended over `--force`)
- `--force-index` - Rebuild index only from existing posts (~1 second)  
- `--force` - Rebuild everything (120+ posts + index, ~18 minutes - use only when templates change)

**🚨 Troubleshooting:**
- **Posts not appearing**: Check `python3 check_links.py` finds 121+ links
- **Cache issues**: Delete `src/blog/.blog_cache.json` and retry
- **Index broken**: Use `--force-index` to rebuild from existing posts
- **Template changes**: Use `--force` to rebuild everything with new templates

**Performance Expectations:**
- New post addition: ~8 seconds (1 post + index)
- No changes: ~2 seconds (dependency check only)
- Force index rebuild: ~1 second
- Full rebuild: ~18 minutes (use sparingly)

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