#!/usr/bin/env python3

#!/usr/bin/env python3

"""
Process Blog - A Static Blog Generator for Markdown Content

This script processes markdown files with YAML front matter to generate a static blog site.
It converts markdown to HTML using Pandoc, extracts and normalizes metadata, and creates
a filterable index page.

The script performs the following operations:
1. Recursively finds markdown files in the content directory
2. Extracts YAML front matter metadata from each file
3. Generates HTML using Pandoc with custom templates
4. Adds JSON-LD structured data for SEO
5. Copies associated assets (images, etc.) for each post
6. Generates a filterable index page with category and tag navigation

Usage Examples:
    # Process all blog posts with default settings
    python3 process_blog.py

    # Process posts from a specific year
    python3 process_blog.py --year 2024

    # Process a specific post only
    python3 process_blog.py --post "my-awesome-post"

    # Only rebuild the index without regenerating posts
    python3 process_blog.py --rebuild-index

    # Specify custom directories
    python3 process_blog.py --content-root ./content --output-root ./public --template-dir ./templates

Requirements:
    - Pandoc must be installed and available in PATH
    - Proper directory structure (YEAR/MONTH/SLUG format recommended)
    - gen-json-ld.py script must be available for structured data generation
"""

import os
import re
import yaml
import shutil
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import argparse
import html

# Configuration
CONFIG = {
    "content_root": "./src/blog/content",
    "output_root": "./blog",
    "template_dir": "./src/blog/templates",
    "site_url": "https://common-sense.com",
    "pandoc_args": [
        "--standalone",
        "--template=./src/blog/templates/blog_template.html",
        "--css=/css/styles.css",
        "--highlight-style=pygments",
        "--mathjax"
    ]
}

def extract_metadata(md_file):
    """Extract YAML front matter from markdown file

    Reads the file and extracts the YAML front matter between the opening and
    closing '---' markers. If the front matter is missing or invalid, raises
    an error with a clear explanation.

    Args:
        md_file: Path to the markdown file

    Returns:
        dict: Parsed metadata from the YAML front matter

    Raises:
        ValueError: If the file has no front matter or the YAML is invalid
    """
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for YAML front matter (between --- markers)
    front_matter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

    if not front_matter_match:
        raise ValueError(f"Missing YAML front matter in {md_file}. All blog posts must begin with front matter enclosed by '---' markers.")

    # Extract and parse the YAML
    yaml_content = front_matter_match.group(1)
    try:
        metadata = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML front matter in {md_file}: {e}")

    # Verify required fields
    required_fields = ['title', 'date', 'author', 'categories', 'tags']
    missing_fields = [field for field in required_fields if field not in metadata]

    if missing_fields:
        raise ValueError(f"Missing required fields in front matter of {md_file}: {', '.join(missing_fields)}")

    # Add derived paths based on file location
    rel_path = os.path.relpath(md_file, CONFIG["content_root"])
    dir_parts = os.path.dirname(rel_path).split(os.sep)

    # Add path information if the file is in the expected directory structure
    if len(dir_parts) >= 3:  # Should be YEAR/MONTH/SLUG format
        year, month, slug = dir_parts[0], dir_parts[1], dir_parts[2]
        metadata["year"] = year
        metadata["month"] = month
        metadata["slug"] = slug
        metadata["url"] = f"/blog/{year}/{month}/{slug}/"
        metadata["html_path"] = f"/blog/{year}/{month}/{slug}/index.html"
    else:
        raise ValueError(f"Blog post {md_file} is not in the expected directory structure: YEAR/MONTH/SLUG")

    # Ensure date is a datetime object for sorting
    if isinstance(metadata["date"], str):
        try:
            metadata["date"] = datetime.strptime(metadata["date"], "%Y-%m-%d")
        except ValueError as e:
            raise ValueError(f"Invalid date format in {md_file}. Expected YYYY-MM-DD: {e}")

    # Format categories and tags for display with proper spacing
    metadata["categories_display"] = ", ".join(metadata["categories"])
    metadata["tags_display"] = ", ".join(metadata["tags"])

    return metadata

def copy_assets(md_file, metadata):
    """Copy assets directory if it exists"""
    source_dir = os.path.dirname(md_file)
    source_assets = os.path.join(source_dir, "assets")

    if os.path.exists(source_assets) and os.path.isdir(source_assets):
        # Determine output path
        rel_path = os.path.relpath(md_file, CONFIG["content_root"])
        dir_parts = os.path.dirname(rel_path).split(os.sep)

        if len(dir_parts) >= 3:
            year, month, slug = dir_parts[0], dir_parts[1], dir_parts[2]
            output_dir = os.path.join(CONFIG["output_root"], year, month, slug)
            output_assets = os.path.join(output_dir, "assets")
        else:
            # Handle unexpected structure
            output_dir = os.path.join(CONFIG["output_root"], metadata["slug"])
            output_assets = os.path.join(output_dir, "assets")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Copy assets directory
        if os.path.exists(output_assets):
            shutil.rmtree(output_assets)
        shutil.copytree(source_assets, output_assets)
        print(f"Copied assets: {source_assets} -> {output_assets}")

def generate_html(md_file, metadata):
    """Generate HTML from markdown using pandoc with improved metadata handling"""
    # Determine output path
    rel_path = os.path.relpath(md_file, CONFIG["content_root"])
    dir_parts = os.path.dirname(rel_path).split(os.sep)

    if len(dir_parts) >= 3:
        year, month, slug = dir_parts[0], dir_parts[1], dir_parts[2]
        output_dir = os.path.join(CONFIG["output_root"], year, month, slug)
        output_file = os.path.join(output_dir, "index.html")
    else:
        # Handle unexpected structure
        output_dir = os.path.join(CONFIG["output_root"], metadata["slug"])
        output_file = os.path.join(output_dir, "index.html")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate JSON-LD structured data using gen-json-ld.py
    json_ld_file = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
    json_ld_file.close()

    try:
        # Call gen-json-ld.py to generate the JSON-LD markup
        json_ld_cmd = [
            "/Users/john/git/cssi-ai/gen-json-ld/gen-json-ld.py",
            md_file,
            "--output",
            json_ld_file.name
        ]

        print(f"Generating JSON-LD structured data...")
        subprocess.run(json_ld_cmd, check=True)
        print(f"JSON-LD generated: {json_ld_file.name}")

        # Prepare metadata for pandoc as variables
        metadata_args = []
        for key, value in metadata.items():
            if isinstance(value, list):
                # Join lists with comma and space for better display
                value = ", ".join(value)
            elif isinstance(value, datetime):
                value = value.strftime("%B %d, %Y")  # Format date as "April 28, 2025"

            if value:  # Ignore empty values
                metadata_args.extend(["--metadata", f"{key}={value}"])

        # Run pandoc with JSON-LD included in header
        cmd = ["pandoc", f"--include-in-header={json_ld_file.name}", md_file, "-o", output_file] + CONFIG["pandoc_args"] + metadata_args

        print(f"PANDOC COMMAND: {cmd}")

        subprocess.run(cmd, check=True)
        print(f"Generated HTML: {output_file}")

        # Copy assets if they exist
        copy_assets(md_file, metadata)

        return output_file
    except subprocess.CalledProcessError as e:

        subprocess.run(cmd, check=True)
        print(f"Generated HTML: {output_file}")

        # Copy assets if they exist
        copy_assets(md_file, metadata)

        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error generating HTML for {md_file}: {e}")
        return None
    finally:
        # Clean up the temporary file
        try:
            pass
            #os.unlink(json_ld_file.name)
        except Exception as e:
            print(f"Warning: Could not delete temporary file {json_ld_file.name}: {e}")

def generate_index(posts):
    """Generate blog index.html from posts metadata with improved formatting"""
    index_template = os.path.join(CONFIG["template_dir"], "blog_index_template.html")
    output_file = os.path.join(CONFIG["output_root"], "index.html")

    with open(index_template, 'r', encoding='utf-8') as f:
        template = f.read()

    # Sort posts by date (newest first)
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)

    # Count categories and tags
    category_counts = {}
    tag_counts = {}

    for post in sorted_posts:
        # Count categories
        for category in post["categories"]:
            category_counts[category] = category_counts.get(category, 0) + 1

        # Count tags
        for tag in post["tags"]:
            if tag:  # Skip empty tags
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

    # Generate category filter HTML
    category_html = '<ul>\n'
    for category, count in sorted(category_counts.items()):
        category_html += f'        <li><a href="#" data-category="{html.escape(category)}">{html.escape(category)} <span class="count">({count})</span></a></li>\n'
    category_html += '      </ul>'

    # Generate tag filter HTML
    tag_html = '<div class="tag-cloud">\n'
    for tag, count in sorted(tag_counts.items()):
        tag_html += f'        <a href="#" data-tag="{html.escape(tag)}" class="tag">{html.escape(tag)} <span class="count">({count})</span></a>\n'
    tag_html += '      </div>'

    # Generate blog posts list HTML with properly formatted categories and tags
    posts_html = '<ul class="blog-list">\n'
    for post in sorted_posts:
        date_str = post["date"].strftime("%B %d, %Y")

        # Ensure categories and tags are properly formatted for data attributes
        categories_attr = ",".join(post["categories"]) if isinstance(post["categories"], list) else post["categories"]
        tags_attr = ",".join(post["tags"]) if isinstance(post["tags"], list) and post["tags"] else ""

        posts_html += f'      <li data-categories="{html.escape(categories_attr)}" data-tags="{html.escape(tags_attr)}"><a href="{html.escape(post["html_path"])}">{html.escape(post["title"])}</a> <span class="blog-date">– {date_str}</span></li>\n'
    posts_html += '    </ul>'

    # Replace placeholders in template
    result = template.replace('<!-- CATEGORIES_PLACEHOLDER -->', category_html)
    result = result.replace('<!-- TAGS_PLACEHOLDER -->', tag_html)
    result = result.replace('<!-- POSTS_PLACEHOLDER -->', posts_html)

    # Write the new index.html
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"Generated blog index with {len(posts)} posts")
    return output_file

def process_blog(posts_filter=None):
    """Process all blog articles and generate index

    Args:
        posts_filter: Optional filter function to process only certain posts
    """
    content_root = Path(CONFIG["content_root"])
    posts_metadata = []
    error_files = []

    # Find all markdown files
    md_files = list(content_root.glob('**/*.md'))

    if not md_files:
        print(f"No markdown files found in {content_root}")
        return

    # Filter files if needed
    if posts_filter:
        md_files = [f for f in md_files if posts_filter(f)]

    # Process each markdown file
    for md_file in md_files:
        print(f"Processing: {md_file}")

        try:
            # Extract metadata - will raise an error if front matter is missing or invalid
            metadata = extract_metadata(md_file)

            # Only process if not draft
            if metadata.get("status") != "draft":
                # Generate HTML
                html_file = generate_html(md_file, metadata)

                if html_file:
                    posts_metadata.append(metadata)
        except ValueError as e:
            # Log the error and add to the list of files with errors
            print(f"ERROR: {e}")
            error_files.append((md_file, str(e)))
            continue
        except Exception as e:
            # Log other unexpected errors
            print(f"UNEXPECTED ERROR processing {md_file}: {e}")
            error_files.append((md_file, f"Unexpected error: {str(e)}"))
            continue

    # If we encountered any errors, show a summary and exit
    if error_files:
        print("\n======== ERROR SUMMARY ========")
        print(f"Encountered errors in {len(error_files)} file(s):")
        for file_path, error_msg in error_files:
            print(f"  - {file_path}: {error_msg}")
        print("\nPlease fix these errors and run the script again.")
        sys.exit(1)

    # Generate index
    if posts_metadata:
        generate_index(posts_metadata)
    else:
        print("No posts to index")

def main():
    """Main entry point with command line argument parsing"""
    parser = argparse.ArgumentParser(description='Process blog markdown files to HTML and generate index')
    parser.add_argument('--content-root', help='Root directory for blog content')
    parser.add_argument('--output-root', help='Root directory for generated output')
    parser.add_argument('--template-dir', help='Directory containing templates')
    parser.add_argument('--site-url', help='Base URL for the website')
    parser.add_argument('--post', help='Process only a specific post directory')
    parser.add_argument('--year', help='Process only posts from a specific year')
    parser.add_argument('--month', help='Process only posts from a specific month (requires --year)')
    parser.add_argument('--rebuild-index', action='store_true', help='Only rebuild the index, don\'t regenerate posts')
    args = parser.parse_args()

    # Update config from command line args
    if args.content_root:
        CONFIG["content_root"] = args.content_root
    if args.output_root:
        CONFIG["output_root"] = args.output_root
    if args.template_dir:
        CONFIG["template_dir"] = args.template_dir
    if args.site_url:
        CONFIG["site_url"] = args.site_url

    # Update pandoc args with new template path if template_dir changed
    if args.template_dir:
        for i, arg in enumerate(CONFIG["pandoc_args"]):
            if arg.startswith("--template="):
                CONFIG["pandoc_args"][i] = f"--template={os.path.join(args.template_dir, 'blog_template.html')}"

    # Handle filters
    if args.rebuild_index:
        # Just rebuild the index from existing posts
        all_posts = []
        for root, dirs, files in os.walk(CONFIG["output_root"]):
            for file in files:
                if file == "index.html" and root != CONFIG["output_root"]:
                    # This is a blog post, read its metadata
                    try:
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Extract metadata from meta tags
                        title_match = re.search(r'<title>(.*?) – Common Sense Systems</title>', content)
                        title = title_match.group(1) if title_match else "Untitled"

                        date_match = re.search(r'<meta name="date" content="(.*?)"', content)
                        date_str = date_match.group(1) if date_match else ""

                        try:
                            date = datetime.strptime(date_str, "%Y-%m-%d")
                        except (ValueError, TypeError):
                            # Use directory structure
                            parts = root.split(os.sep)
                            if len(parts) >= 3:
                                year, month = parts[-3], parts[-2]
                                date = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
                            else:
                                date = datetime.now()

                        categories_match = re.search(r'<meta name="categories" content="(.*?)"', content)
                        categories_str = categories_match.group(1) if categories_match else "Uncategorized"
                        categories = [c.strip() for c in categories_str.split(",")]

                        tags_match = re.search(r'<meta name="tags" content="(.*?)"', content)
                        tags_str = tags_match.group(1) if tags_match and tags_match.group(1) else ""
                        tags = [t.strip() for t in tags_str.split(",")] if tags_str else []

                        # Get relative path for URLs
                        rel_path = os.path.relpath(os.path.join(root, file), CONFIG["output_root"])

                        # Add properly formatted display versions
                        categories_display = ", ".join(categories)
                        tags_display = ", ".join(tags)

                        all_posts.append({
                            "title": title,
                            "date": date,
                            "categories": categories,
                            "tags": tags,
                            "categories_display": categories_display,
                            "tags_display": tags_display,
                            "html_path": f"/{rel_path}"
                        })
                    except Exception as e:
                        print(f"Error processing existing post {os.path.join(root, file)}: {e}")
                        continue

        if all_posts:
            generate_index(all_posts)
        else:
            print("No existing posts found to rebuild index")
    else:
        # Process posts with filters
        filter_func = None

        if args.post:
            def post_filter(f):
                return args.post in str(f)
            filter_func = post_filter
        elif args.year:
            if args.month:
                def year_month_filter(f):
                    parts = os.path.relpath(f, CONFIG["content_root"]).split(os.sep)
                    return len(parts) >= 3 and parts[0] == args.year and parts[1] == args.month
                filter_func = year_month_filter
            else:
                def year_filter(f):
                    parts = os.path.relpath(f, CONFIG["content_root"]).split(os.sep)
                    return len(parts) >= 3 and parts[0] == args.year
                filter_func = year_filter

        process_blog(filter_func)

if __name__ == "__main__":
    main()
