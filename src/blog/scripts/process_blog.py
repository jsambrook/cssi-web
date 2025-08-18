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

Dependency Tracking:
The script now tracks dependencies to avoid rebuilding files unnecessarily:
- Uses a cache file to store timestamps of processed files
- Only rebuilds posts when the source file has changed
- Only rebuilds the index when posts have changed

Usage Examples:
    # Process all blog posts with default settings
    python3 process_blog.py

    # Process all blog posts, forcing rebuild regardless of timestamps
    python3 process_blog.py --force

    # Process only posts containing "my-awesome-post" in their path
    # (typically matches a specific post by its slug directory name)
    python3 process_blog.py --post "my-awesome-post"

    # Example: For a post in src/blog/content/2024/05/my-awesome-post/index.md
    # The command would be:
    python3 process_blog.py --post "my-awesome-post"

    # Show what posts would be processed without making changes
    python3 process_blog.py --post "my-awesome-post" --dry-run

    # Process posts interactively, confirming each post before processing
    python3 process_blog.py --year 2024 -i

    # Process posts from a specific year
    python3 process_blog.py --year 2024

    # Process posts from a specific month (requires --year)
    python3 process_blog.py --year 2024 --month 05

    # Only rebuild the index without regenerating posts
    python3 process_blog.py --rebuild-index

    # Specify custom directories
    python3 process_blog.py --content-root ./content --output-root ./public --template-dir ./templates

    # Log to a specific file
    python3 process_blog.py --log-file /path/to/blog_process.log

    # Increase log verbosity
    python3 process_blog.py --log-level DEBUG

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
import logging
import sys
import json
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
    "gen_json_ld_path": "/Users/john/git/cssi-ai/gen-json-ld/gen-json-ld.py",
    "pandoc_args": [
        "--standalone",
        "--template=./src/blog/templates/blog_template.html",
        "--css=/css/styles.css",
        "--highlight-style=pygments",
        "--mathjax"
    ],
    # Add cache file path for dependency tracking
    "cache_file": ".blog_cache.json"
}

# Cache to store file modification timestamps
# Structure: {file_path: {"mtime": last_modified_time, "output": output_file_path}}
CACHE = {}

def setup_logging(log_file=None, log_level="INFO"):
    """Set up logging configuration

    Args:
        log_file: Optional path to log file. If None, logs to a default location
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Convert string log level to logging constant
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # Clear any existing handlers (in case this function is called multiple times)
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler (always enabled)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # File handler
    if log_file:
        # User-specified log file
        log_path = Path(log_file)
    else:
        # Default log file in the same directory as the script
        script_dir = Path(__file__).parent
        log_path = script_dir / "process_blog.log"

    try:
        # Create directory if it doesn't exist
        log_path.parent.mkdir(parents=True, exist_ok=True)

        # Add file handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

        # Only log this if we're not at DEBUG level to avoid confusion
        if numeric_level > logging.DEBUG:
            root_logger.info(f"Logging to file: {log_path}")
    except Exception as e:
        root_logger.error(f"Failed to set up file logging to {log_path}: {e}")

def load_cache():
    """Load dependency cache from file"""
    global CACHE
    cache_path = Path(CONFIG["cache_file"])

    if cache_path.exists():
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                CACHE = json.load(f)
            logging.debug(f"Loaded cache with {len(CACHE)} entries")
        except Exception as e:
            logging.warning(f"Failed to load cache from {cache_path}: {e}")
            CACHE = {}
    else:
        logging.debug(f"No cache file found at {cache_path}, starting with empty cache")
        CACHE = {}

def save_cache():
    """Save dependency cache to file"""
    cache_path = Path(CONFIG["cache_file"])

    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(CACHE, f, indent=2)
        logging.debug(f"Saved cache with {len(CACHE)} entries")
    except Exception as e:
        logging.error(f"Failed to save cache to {cache_path}: {e}")

def needs_rebuild(md_file, output_file=None):
    """Determine if a file needs to be rebuilt

    A file needs rebuilding if any of these conditions are true:
    1. It's not in the cache (never been processed)
    2. It's been modified since last processing
    3. The output file doesn't exist
    4. The template is newer than the output file

    Args:
        md_file: Path to the markdown file
        output_file: Optional path to the output file

    Returns:
        bool: True if the file needs to be rebuilt, False otherwise
    """
    md_file_str = str(md_file)  # Convert Path to string for cache key

    # Get current file modification time
    try:
        current_mtime = os.path.getmtime(md_file)
    except OSError as e:
        logging.error(f"Error getting modification time for {md_file}: {e}")
        return True  # Rebuild if we can't determine mtime

    # Check if file is in cache
    if md_file_str not in CACHE:
        logging.debug(f"File not in cache, needs rebuild: {md_file}")
        return True

    # Check if file has been modified
    cached_mtime = CACHE[md_file_str].get("mtime", 0)
    if current_mtime > cached_mtime:
        logging.debug(f"File modified since last build, needs rebuild: {md_file}")
        return True

    # Determine output file path if not provided
    if not output_file:
        if "output" in CACHE[md_file_str]:
            output_file = CACHE[md_file_str]["output"]
        else:
            # We don't know the output path, rebuild to be safe
            logging.debug(f"Output path unknown, needs rebuild: {md_file}")
            return True

    # Check if output file exists
    if not os.path.exists(output_file):
        logging.debug(f"Output file doesn't exist, needs rebuild: {md_file}")
        return True

    # Check if template is newer than output file
    template_path = os.path.join(CONFIG["template_dir"], "blog_template.html")
    try:
        template_mtime = os.path.getmtime(template_path)
        output_mtime = os.path.getmtime(output_file)
        if template_mtime > output_mtime:
            logging.debug(f"Template newer than output, needs rebuild: {md_file}")
            return True
    except OSError as e:
        logging.warning(f"Error comparing template and output times: {e}")
        # Continue with other checks

    # Check if JSON-LD script is newer than output file
    try:
        script_mtime = os.path.getmtime(CONFIG["gen_json_ld_path"])
        output_mtime = os.path.getmtime(output_file)
        if script_mtime > output_mtime:
            logging.debug(f"JSON-LD script newer than output, needs rebuild: {md_file}")
            return True
    except OSError as e:
        logging.warning(f"Error comparing JSON-LD script time: {e}")
        # Continue with other checks

    # All checks passed, no need to rebuild
    logging.debug(f"File unchanged, no rebuild needed: {md_file}")
    return False

def update_cache(md_file, output_file):
    """Update cache with file information

    Args:
        md_file: Path to the markdown file
        output_file: Path to the output file
    """
    md_file_str = str(md_file)  # Convert Path to string for cache key

    try:
        mtime = os.path.getmtime(md_file)
        CACHE[md_file_str] = {
            "mtime": mtime,
            "output": output_file
        }
        logging.debug(f"Updated cache for {md_file}")
    except OSError as e:
        logging.error(f"Error updating cache for {md_file}: {e}")

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
            # Handle unexpected structure - should not happen with new error checking
            output_dir = os.path.join(CONFIG["output_root"], metadata["slug"])
            output_assets = os.path.join(output_dir, "assets")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Check if assets need to be copied - compare directory timestamps
        should_copy = True
        if os.path.exists(output_assets):
            try:
                # Get the latest modification time of any file in source assets
                latest_source_mtime = max(
                    os.path.getmtime(os.path.join(root, file))
                    for root, _, files in os.walk(source_assets)
                    for file in files
                )

                # Get the latest modification time of any file in output assets
                latest_output_mtime = max(
                    os.path.getmtime(os.path.join(root, file))
                    for root, _, files in os.walk(output_assets)
                    for file in files
                )

                # Only copy if source is newer than output
                if latest_source_mtime <= latest_output_mtime:
                    should_copy = False
                    logging.debug(f"Assets unchanged, skipping copy: {source_assets}")
            except (OSError, ValueError) as e:
                # If there's any error (e.g., no files in directory), copy to be safe
                logging.debug(f"Error checking asset timestamps, will copy: {e}")
                should_copy = True

        if should_copy:
            # Copy assets directory
            if os.path.exists(output_assets):
                shutil.rmtree(output_assets)
            shutil.copytree(source_assets, output_assets)
            logging.info(f"Copied assets: {source_assets} -> {output_assets}")
        else:
            logging.info(f"Assets up to date, skipping: {source_assets}")

def generate_html(md_file, metadata):
    """Generate HTML from markdown using pandoc

    Converts markdown to HTML using Pandoc, handling JSON-LD
    structured data generation and including metadata.

    Args:
        md_file: Path to the markdown file
        metadata: Dictionary containing post metadata

    Returns:
        str: Path to the generated HTML file, or None if generation failed
    """
    # Determine output path
    rel_path = os.path.relpath(md_file, CONFIG["content_root"])
    dir_parts = os.path.dirname(rel_path).split(os.sep)

    if len(dir_parts) >= 3:
        year, month, slug = dir_parts[0], dir_parts[1], dir_parts[2]
        output_dir = os.path.join(CONFIG["output_root"], year, month, slug)
        output_file = os.path.join(output_dir, "index.html")
    else:
        output_dir = os.path.join(CONFIG["output_root"], metadata["slug"])
        output_file = os.path.join(output_dir, "index.html")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Generate JSON-LD structured data using gen-json-ld.py
    json_ld_file = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
    json_ld_file.close()

    try:
        # Call gen-json-ld.py to generate the JSON-LD markup
        # Convert Path objects to strings for subprocess
        json_ld_cmd = [
            CONFIG["gen_json_ld_path"],
            str(md_file),  # Convert Path to string
            "--output",
            json_ld_file.name
        ]

        logging.info(f"Generating JSON-LD structured data for {md_file}")
        subprocess.run(json_ld_cmd, check=True)
        logging.debug(f"JSON-LD generated: {json_ld_file.name}")

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
        # Convert Path objects to strings for subprocess
        cmd = [
            "pandoc",
            f"--include-in-header={json_ld_file.name}",
            str(md_file),  # Convert Path to string
            "-o",
            str(output_file)  # Convert Path to string
        ] + CONFIG["pandoc_args"] + metadata_args

        logging.debug(f"PANDOC COMMAND: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        logging.info(f"Generated HTML: {output_file}")

        # Copy assets if they exist
        copy_assets(md_file, metadata)

        # Update cache with the new file information
        update_cache(md_file, output_file)

        return output_file
    except subprocess.CalledProcessError as e:
        logging.error(f"Error generating HTML for {md_file}: {e}")
        return None
    finally:
        # Clean up the temporary file
        try:
            os.unlink(json_ld_file.name)
            logging.debug(f"Cleaned up temporary file: {json_ld_file.name}")
        except Exception as e:
            logging.warning(f"Could not delete temporary file {json_ld_file.name}: {e}")

def generate_index(posts):
    """Generate blog index.html from posts metadata with improved formatting"""
    index_template = os.path.join(CONFIG["template_dir"], "blog_index_template.html")
    output_file = os.path.join(CONFIG["output_root"], "index.html")

    # Check if index needs rebuilding
    index_needs_rebuild = True

    # If the index exists, check if it's newer than the template
    if os.path.exists(output_file):
        try:
            index_mtime = os.path.getmtime(output_file)
            template_mtime = os.path.getmtime(index_template)

            # If the template hasn't changed and we have a special cache entry for the index
            if template_mtime <= index_mtime and "_index_last_build" in CACHE:
                # Check if any posts have been modified since the last index build
                last_index_build = CACHE["_index_last_build"]

                # If no posts have been modified or added since the last index build
                if all(CACHE.get(str(post["source_file"]), {}).get("mtime", float('inf')) <= last_index_build
                       for post in posts if "source_file" in post):
                    index_needs_rebuild = False
                    logging.debug("Index is up to date, skipping rebuild")
        except OSError as e:
            logging.warning(f"Error checking index timestamps: {e}")
            # Rebuild to be safe
            index_needs_rebuild = True

    if not index_needs_rebuild:
        logging.info("Blog index is up to date, skipping rebuild")
        return output_file

    logging.info("Rebuilding blog index")
    logging.info(f"DEBUG: Generating index at absolute path: {os.path.abspath(output_file)}")

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

    # Update index build timestamp in cache
    CACHE["_index_last_build"] = datetime.now().timestamp()

    logging.info(f"Generated blog index with {len(posts)} posts")
    return output_file

def process_blog(posts_filter=None, interactive=False, dry_run=False, force=False):
    """Process all blog articles and generate index

    Args:
        posts_filter: Optional filter function to process only certain posts
        interactive: If True, prompt for confirmation before processing each post
        dry_run: If True, only show what would be processed without making changes
        force: If True, rebuild all posts regardless of timestamps
    """
    content_root = Path(CONFIG["content_root"])
    posts_metadata = []
    error_files = []
    any_posts_changed = False

    # Find all markdown files
    md_files = list(content_root.glob('**/*.md'))

    if not md_files:
        logging.warning(f"No markdown files found in {content_root}")
        return

    # Filter files if needed
    if posts_filter:
        md_files = [f for f in md_files if posts_filter(f)]

    # Dry run mode - just show what would be processed
    if dry_run:
        # For dry run with dependency checking, show which files would actually be processed
        if not force:
            would_process = []
            for md_file in md_files:
                if needs_rebuild(md_file):
                    would_process.append(md_file)

            logging.info(f"DRY RUN: Would process {len(would_process)} out of {len(md_files)} posts:")
            for md_file in would_process:
                logging.info(f"  - {md_file}")
        else:
            logging.info(f"DRY RUN with FORCE: Would process all {len(md_files)} posts:")
            for md_file in md_files:
                logging.info(f"  - {md_file}")

        logging.info("No changes were made (dry run)")
        return

    # Show how many files matched if in interactive mode
    if interactive and md_files:
        # For interactive mode with dependency checking, first filter for posts that need rebuilding
        if not force:
            md_files = [f for f in md_files if needs_rebuild(f)]

        logging.info(f"Found {len(md_files)} posts to process")

    # Process each markdown file
    for md_file in md_files:
        # Check if file needs rebuilding
        if not force and not needs_rebuild(md_file):
            logging.info(f"Skipping unchanged file: {md_file}")

            # Still need the metadata for the index
            try:
                metadata = extract_metadata(md_file)

                # Add source file info for later index checks
                metadata["source_file"] = md_file

                if metadata.get("status") != "draft":
                    # Get the output file path from cache
                    md_file_str = str(md_file)
                    if md_file_str in CACHE and "output" in CACHE[md_file_str]:
                        posts_metadata.append(metadata)
            except Exception as e:
                logging.error(f"Error extracting metadata from unchanged file {md_file}: {e}")

            continue

        # Prompt for confirmation in interactive mode
        if interactive:
            confirm = input(f"Process {md_file}? [y/n/q/a] (yes/no/quit/all): ").lower()
            if confirm in ('q', 'quit'):
                logging.info("User aborted processing")
                return
            elif confirm in ('a', 'all'):
                # Turn off interactive mode for remaining files
                interactive = False
            elif confirm not in ('y', 'yes'):
                logging.info(f"Skipping {md_file}")
                continue

        logging.info(f"Processing: {md_file}")
        any_posts_changed = True

        try:
            # Extract metadata - will raise an error if front matter is missing or invalid
            metadata = extract_metadata(md_file)

            # Add source file info for later index checks
            metadata["source_file"] = md_file

            # Only process if not draft
            if metadata.get("status") != "draft":
                # Generate HTML
                html_file = generate_html(md_file, metadata)

                if html_file:
                    posts_metadata.append(metadata)
        except ValueError as e:
            # Log the error and add to the list of files with errors
            logging.error(f"ERROR: {e}")
            error_files.append((md_file, str(e)))
            continue
        except Exception as e:
            # Log other unexpected errors
            logging.error(f"UNEXPECTED ERROR processing {md_file}: {e}")
            error_files.append((md_file, f"Unexpected error: {str(e)}"))
            continue

    # If we encountered any errors, show a summary and exit
    if error_files:
        logging.error("\n======== ERROR SUMMARY ========")
        logging.error(f"Encountered errors in {len(error_files)} file(s):")
        for file_path, error_msg in error_files:
            logging.error(f"  - {file_path}: {error_msg}")
        logging.error("\nPlease fix these errors and run the script again.")
        sys.exit(1)

    # Generate index if any posts were changed or if specifically forced
    if any_posts_changed or force or posts_filter:
        if posts_metadata:
            generate_index(posts_metadata)
        else:
            logging.warning("No posts to index")
    else:
        logging.info("No posts changed, skipping index regeneration")

    # Save the updated cache
    save_cache()

def main():
    """Main entry point with command line argument parsing"""
    parser = argparse.ArgumentParser(description='Process blog markdown files to HTML and generate index')
    parser.add_argument('--content-root', help='Root directory for blog content')
    parser.add_argument('--output-root', help='Root directory for generated output')
    parser.add_argument('--template-dir', help='Directory containing templates')
    parser.add_argument('--site-url', help='Base URL for the website')
    parser.add_argument('--gen-json-ld-path', help='Path to gen-json-ld.py script')
    parser.add_argument('--post', help='Process only posts containing this string in their path (usually matches the slug directory)')
    parser.add_argument('--year', help='Process only posts from a specific year')
    parser.add_argument('--month', help='Process only posts from a specific month (requires --year)')
    parser.add_argument('--rebuild-index', action='store_true', help='Only rebuild the index, don\'t regenerate posts')
    parser.add_argument('-i', '--interactive', action='store_true',
                      help='Prompt for confirmation before processing each post')
    parser.add_argument('--dry-run', action='store_true',
                      help='Show what would be processed without making any changes')
    parser.add_argument('--force', action='store_true',
                      help='Force rebuild of all posts regardless of timestamps')
    parser.add_argument('--cache-file', help='Path to dependency cache file')

    # Add logging arguments
    parser.add_argument('--log-file', help='Path to log file (default: ./process_blog.log)')
    parser.add_argument('--log-level',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                       default='INFO',
                       help='Set the logging level (default: INFO)')

    args = parser.parse_args()

    # Setup logging first thing
    setup_logging(args.log_file, args.log_level)

    # Log the start of execution with key parameters
    logging.info("Starting blog processing")
    logging.debug(f"Arguments: {vars(args)}")

    # Update config from command line args
    if args.content_root:
        CONFIG["content_root"] = args.content_root
        logging.debug(f"Using content root: {CONFIG['content_root']}")
    if args.output_root:
        CONFIG["output_root"] = args.output_root
        logging.debug(f"Using output root: {CONFIG['output_root']}")
    if args.template_dir:
        CONFIG["template_dir"] = args.template_dir
        logging.debug(f"Using template directory: {CONFIG['template_dir']}")
    if args.site_url:
        CONFIG["site_url"] = args.site_url
        logging.debug(f"Using site URL: {CONFIG['site_url']}")
    if args.gen_json_ld_path:
        CONFIG["gen_json_ld_path"] = args.gen_json_ld_path
        logging.debug(f"Using gen-json-ld.py path: {CONFIG['gen_json_ld_path']}")
    if args.cache_file:
        CONFIG["cache_file"] = args.cache_file
        logging.debug(f"Using cache file: {CONFIG['cache_file']}")

    # Update pandoc args with new template path if template_dir changed
    if args.template_dir:
        for i, arg in enumerate(CONFIG["pandoc_args"]):
            if arg.startswith("--template="):
                CONFIG["pandoc_args"][i] = f"--template={os.path.join(args.template_dir, 'blog_template.html')}"
                logging.debug(f"Updated pandoc template path: {CONFIG['pandoc_args'][i]}")

    # Load dependency cache
    load_cache()

    # Handle filters
    if args.rebuild_index:
        # Just rebuild the index from existing posts
        logging.info("Rebuilding index only from existing posts")

        # Show dry run message if applicable
        if args.dry_run:
            logging.info("DRY RUN: Would rebuild the index only")
            logging.info("No changes were made (dry run)")
            return

        all_posts = []
        for root, dirs, files in os.walk(CONFIG["output_root"]):
            for file in files:
                if file == "index.html" and root != CONFIG["output_root"]:
                    # This is a blog post, read its metadata
                    try:
                        file_path = os.path.join(root, file)
                        logging.debug(f"Extracting metadata from existing post: {file_path}")

                        with open(file_path, 'r', encoding='utf-8') as f:
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
                                logging.debug(f"Using directory structure for date: {year}-{month}-01")
                            else:
                                date = datetime.now()
                                logging.warning(f"Could not determine date for {file_path}, using current date")

                        categories_match = re.search(r'<meta name="categories" content="(.*?)"', content)
                        categories_str = categories_match.group(1) if categories_match else "Uncategorized"
                        categories = [c.strip() for c in categories_str.split(",")]

                        tags_match = re.search(r'<meta name="tags" content="(.*?)"', content)
                        tags_str = tags_match.group(1) if tags_match and tags_match.group(1) else ""
                        tags = [t.strip() for t in tags_str.split(",")] if tags_str else []

                        # Get relative path for URLs
                        rel_path = os.path.relpath(file_path, CONFIG["output_root"])

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
                            "html_path": f"/blog/{rel_path}"
                        })
                        logging.debug(f"Added post to index: {title}")
                    except Exception as e:
                        logging.error(f"Error processing existing post {os.path.join(root, file)}: {e}")
                        continue

        if all_posts:
            generate_index(all_posts)

            # Update index build timestamp in cache
            CACHE["_index_last_build"] = datetime.now().timestamp()
            save_cache()
        else:
            logging.warning("No existing posts found to rebuild index")
    else:
        # Process posts with filters
        filter_func = None

        if args.post:
            def post_filter(f):
                return args.post in str(f)
            filter_func = post_filter
            logging.info(f"Processing posts matching: {args.post}")
        elif args.year:
            if args.month:
                def year_month_filter(f):
                    parts = os.path.relpath(f, CONFIG["content_root"]).split(os.sep)
                    return len(parts) >= 3 and parts[0] == args.year and parts[1] == args.month
                filter_func = year_month_filter
                logging.info(f"Processing posts from year/month: {args.year}/{args.month}")
            else:
                def year_filter(f):
                    parts = os.path.relpath(f, CONFIG["content_root"]).split(os.sep)
                    return len(parts) >= 3 and parts[0] == args.year
                filter_func = year_filter
                logging.info(f"Processing posts from year: {args.year}")

        # Interactive mode is ignored in dry-run mode
        process_blog(
            filter_func,
            args.interactive and not args.dry_run,
            args.dry_run,
            args.force
        )

    logging.info("Blog processing completed")

if __name__ == "__main__":
    main()
