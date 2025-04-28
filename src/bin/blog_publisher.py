#!/usr/bin/env python3
"""
blog_publisher.py

A simple system to convert Markdown blog posts to HTML and publish them to your blog.
This script handles:
- Extracting metadata from Markdown frontmatter
- Processing Markdown content with Pandoc
- Managing image paths and copying images to the correct location
- Updating the blog index

Usage:
    ./blog_publisher.py --input path/to/your-markdown-file.md [--template path/to/template.html]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import yaml
from datetime import datetime
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Convert Markdown blog post to HTML and update blog index")
    parser.add_argument('--input', required=True, help='Path to the input Markdown file')
    parser.add_argument('--template', default=None, help='Path to the HTML template (relative to script directory)')
    parser.add_argument('--cta', default=None, help='Path to CTA HTML fragment')
    parser.add_argument('--footer', default=None, help='Path to footer HTML fragment')
    parser.add_argument('--rebuild-index', action='store_true', help='Rebuild the blog index')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show verbose output')
    return parser.parse_args()


def log(message, verbose=False):
    """Log messages based on verbosity setting"""
    if verbose:
        print(f"DEBUG: {message}")


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    if not content.startswith('---'):
        return {}, content

    end_marker = content.find('---', 3)
    if end_marker == -1:
        return {}, content

    frontmatter_text = content[3:end_marker].strip()
    remaining_content = content[end_marker + 3:].strip()

    try:
        metadata = yaml.safe_load(frontmatter_text)
        return metadata, remaining_content
    except Exception as e:
        print(f"Warning: Error parsing YAML frontmatter: {e}")
        # Basic fallback parser
        metadata = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        return metadata, remaining_content


def find_images_in_markdown(markdown_text):
    """Find all image references in the Markdown content"""
    # Standard Markdown image syntax: ![alt text](path/to/image.jpg)
    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(image_pattern, markdown_text)


def process_images(markdown_text, input_file_path, output_image_dir, verbose=False):
    """Process images in the Markdown content and copy them to the output directory"""
    images = find_images_in_markdown(markdown_text)
    if not images:
        return markdown_text

    input_dir = input_file_path.parent
    output_image_dir.mkdir(parents=True, exist_ok=True)

    # Process each image
    for alt_text, image_path in images:
        # Resolve the image path relative to the Markdown file
        image_path = image_path.strip()
        source_path = input_dir / image_path

        if source_path.exists():
            # Create a web-friendly filename
            target_filename = source_path.name
            target_path = output_image_dir / target_filename

            # Copy the image to the target directory
            shutil.copy2(source_path, target_path)
            log(f"Copied image: {source_path} -> {target_path}", verbose)

            # Generate the new web path for the image
            relative_path = f"/assets/img/blog/{output_image_dir.relative_to(output_image_dir.parents[2])}/{target_filename}"

            # Replace the image path in the Markdown
            old_tag = f"![{alt_text}]({image_path})"
            new_tag = f"![{alt_text}]({relative_path})"
            markdown_text = markdown_text.replace(old_tag, new_tag)
            log(f"Updated image path: {image_path} -> {relative_path}", verbose)
        else:
            print(f"Warning: Image not found: {source_path}")

    return markdown_text


def create_default_template():
    """Create a default HTML template if none is provided"""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$title$ - Common Sense Systems, Inc.</title>
  <meta name="description" content="$description$">
  $if(keywords)$
  <meta name="keywords" content="$keywords$">
  $endif$
  <meta name="author" content="$author$">
  <link rel="stylesheet" href="/css/styles.css">
  <style>
    /* Blog-specific styles */
    .blog-content {
      max-width: 800px;
      margin: 20px auto;
      line-height: 1.6;
    }

    .blog-content h1 {
      margin-bottom: 10px;
    }

    .blog-meta {
      color: #666;
      margin-bottom: 30px;
    }

    .blog-content h2 {
      margin-top: 40px;
      margin-bottom: 15px;
    }

    .blog-content p {
      margin-bottom: 20px;
    }

    .blog-content img {
      max-width: 100%;
      height: auto;
      margin: 20px 0;
    }

    .references {
      margin-top: 40px;
      padding-top: 20px;
      border-top: 1px solid #eee;
      font-size: 0.9em;
    }

    .references li {
      margin-bottom: 10px;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <header>
    <div class="container">
      <nav>
        <a href="/index.html" class="logo"><span>Common Sense Systems, Inc.</span></a>
        <ul class="nav-links">
          <li><a href="/index.html">Home</a></li>
          <li><a href="/index.html#services">Services</a></li>
          <li><a href="/blog/index.html" class="active">Blog</a></li>
          <li><a href="/contact.html">Contact</a></li>
        </ul>
        <div class="menu-toggle"><span></span><span></span><span></span></div>
      </nav>
    </div>
  </header>

  <main class="container blog-content">
    <article>
      <h1>$title$</h1>
      <div class="blog-meta">
        <span class="blog-date">$date$</span>
        $if(tags)$
        <span class="blog-tags">$for(tags)$$tags$$sep$, $endfor$</span>
        $endif$
      </div>

      $body$
    </article>
  </main>

  $if(cta_html)$
  $cta_html$
  $endif$

  $if(footer_html)$
  $footer_html$
  $endif$
</body>
</html>"""


def update_blog_index(index_path, post_metadata, verbose=False):
    """Update the blog index with the new post's metadata"""
    # Ensure required metadata is present
    year = post_metadata.get('year', datetime.now().strftime('%Y'))
    month = post_metadata.get('month', datetime.now().strftime('%m'))
    slug = post_metadata.get('slug', '')
    title = post_metadata.get('title', 'Untitled')
    date = post_metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
    category = post_metadata.get('category', 'Uncategorized')
    tags = post_metadata.get('tags', [])

    # Ensure tags is a list
    if isinstance(tags, str):
        # Handle comma-separated values or quoted string
        tags = [tag.strip().strip('"\'') for tag in re.split(r',\s*', tags)]

    # Create entry for this post
    entry = {
        "title": title,
        "slug": slug,
        "date": date,
        "year": year,
        "month": month,
        "category": category,
        "tags": tags
    }

    # Create or load the index
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if index_path.exists():
        try:
            data = json.loads(index_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in {index_path}. Creating new index.")
            data = {"posts": []}
    else:
        data = {"posts": []}

    # Update or add the post entry
    existing = [i for i, p in enumerate(data.get("posts", []))
                if p.get("slug") == slug and p.get("date") == date]

    if existing:
        # Update existing entry
        for i in existing:
            data["posts"][i] = entry
            log(f"Updated existing post in index: {title}", verbose)
    else:
        # Add new entry
        data["posts"].append(entry)
        log(f"Added new post to index: {title}", verbose)

    # Sort by date (newest first)
    data["posts"] = sorted(data["posts"], key=lambda p: p.get("date", ""), reverse=True)

    # Write the updated index
    index_path.write_text(json.dumps(data, indent=2), encoding='utf-8')
    log(f"Wrote updated index to {index_path}", verbose)

    return True


def convert_markdown_to_html(input_path, output_path, template_path, metadata, processed_content, cta_path=None, footer_path=None, verbose=False):
    """Convert Markdown content to HTML using pandoc"""
    # Create a temporary file with the processed content
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        temp_path = temp_file.name
        temp_file.write(processed_content)

    try:
        # Prepare pandoc command
        pandoc_cmd = [
            "pandoc",
            temp_path,
            "--from=markdown-yaml_metadata_block",  # Explicitly exclude YAML frontmatter
            "--to=html5",
            f"--template={template_path}",
            "--standalone",
            f"--output={output_path}"
        ]

        # Add variables from metadata
        for key, value in metadata.items():
            if isinstance(value, (str, int, float)):
                if key == 'date':
                    # Format date for display
                    try:
                        date_obj = datetime.strptime(value, '%Y-%m-%d')
                        formatted_date = date_obj.strftime('%B %d, %Y')
                        pandoc_cmd.append(f"--variable={key}:{formatted_date}")
                    except (ValueError, TypeError):
                        pandoc_cmd.append(f"--variable={key}:{value}")
                else:
                    pandoc_cmd.append(f"--variable={key}:{value}")

        # Add tags as keywords
        if 'tags' in metadata and metadata['tags']:
            tags = metadata['tags']
            if isinstance(tags, list):
                tags_str = ', '.join(str(tag) for tag in tags)
                pandoc_cmd.append(f"--variable=tags:{tags_str}")
                pandoc_cmd.append(f"--variable=keywords:{tags_str}")
            else:
                pandoc_cmd.append(f"--variable=tags:{tags}")
                pandoc_cmd.append(f"--variable=keywords:{tags}")

        # Add CTA and footer
        if cta_path and Path(cta_path).exists():
            cta_html = Path(cta_path).read_text(encoding='utf-8')
            pandoc_cmd.append(f"--variable=cta_html:{cta_html}")

        if footer_path and Path(footer_path).exists():
            footer_html = Path(footer_path).read_text(encoding='utf-8')
            pandoc_cmd.append(f"--variable=footer_html:{footer_html}")

        # Print command for debugging
        if verbose:
            print(f"Pandoc command: {' '.join(pandoc_cmd)}")

        # Run pandoc
        result = subprocess.run(pandoc_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error running pandoc: {result.stderr}")
            return False

        return True
    finally:
        # Clean up temporary files
        if Path(temp_path).exists():
            Path(temp_path).unlink()


def regenerate_blog_index(script_dir, repo_root, verbose=False):
    """Regenerate the blog index by running the blog index generator script"""
    index_script = script_dir / "generate_blog_index.py"

    if not index_script.exists():
        print(f"Warning: Blog index generator script not found at {index_script}")
        return False

    try:
        result = subprocess.run(["python3", str(index_script)], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Error regenerating blog index: {result.stderr}")
            return False

        if verbose:
            print(f"Blog index regeneration output: {result.stdout}")

        return True
    except Exception as e:
        print(f"Error running blog index generator: {e}")
        return False


def main():
    args = parse_args()
    verbose = args.verbose

    # Get script directory and paths
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    input_path = Path(args.input).resolve()

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1

    # Set up template path
    if args.template:
        if args.template.startswith('/'):
            template_path = Path(args.template)
        else:
            template_path = script_dir / args.template
    else:
        # Create a default template
        template_dir = script_dir / "templates"
        template_dir.mkdir(exist_ok=True)
        template_path = template_dir / "blog-template.html"
        if not template_path.exists():
            template_path.write_text(create_default_template())

    if not template_path.exists():
        print(f"Error: Template not found: {template_path}")
        return 1

    # Set up CTA and footer paths
    cta_path = None
    if args.cta:
        cta_path = Path(args.cta)
    else:
        default_cta = script_dir.parent / "includes" / "blog_cta.html"
        if default_cta.exists():
            cta_path = default_cta

    footer_path = None
    if args.footer:
        footer_path = Path(args.footer)
    else:
        default_footer = script_dir.parent / "includes" / "site_footer.html"
        if default_footer.exists():
            footer_path = default_footer

    # Read and process the Markdown file
    content = input_path.read_text(encoding='utf-8')

    # Extract frontmatter
    metadata, content_without_frontmatter = extract_frontmatter(content)

    # Ensure required metadata is present
    if 'title' not in metadata:
        # Try to extract title from H1 or first line
        title_match = re.search(r'^#\s+(.*?)$', content_without_frontmatter, re.MULTILINE)
        if title_match:
            metadata['title'] = title_match.group(1).strip()
        else:
            metadata['title'] = input_path.stem.split('-')[-1].replace('-', ' ').title()

    # Ensure we have date, year, month
    if 'date' not in metadata:
        # Try to extract from filename (YYYY-MM-DD-title.md)
        filename_parts = input_path.stem.split('-')
        if len(filename_parts) >= 3 and len(filename_parts[0]) == 4:
            metadata['date'] = f"{filename_parts[0]}-{filename_parts[1]}-{filename_parts[2]}"
        else:
            metadata['date'] = datetime.now().strftime('%Y-%m-%d')

    date_parts = metadata['date'].split('-')
    metadata['year'] = date_parts[0]
    metadata['month'] = date_parts[1]

    # Ensure slug is present
    if 'slug' not in metadata:
        # Use the last part of the filename, or create from title
        if '-' in input_path.stem:
            metadata['slug'] = input_path.stem.split('-')[-1]
        else:
            title_slug = re.sub(r'[^a-z0-9-]', '', metadata['title'].lower().replace(' ', '-'))
            metadata['slug'] = title_slug

    # Set up output paths
    year = metadata['year']
    month = metadata['month']
    slug = metadata['slug']

    blog_dir = repo_root / "blog" / year / month
    blog_dir.mkdir(parents=True, exist_ok=True)
    output_path = blog_dir / f"{slug}.html"

    image_dir = repo_root / "src" / "assets" / "img" / "blog" / year / month / slug

    # Process images in the Markdown
    processed_content = process_images(content_without_frontmatter, input_path, image_dir, verbose)

    # Convert Markdown to HTML
    log(f"Converting {input_path} to {output_path}", verbose)
    success = convert_markdown_to_html(
        input_path=input_path,
        output_path=output_path,
        template_path=template_path,
        metadata=metadata,
        processed_content=processed_content,
        cta_path=cta_path,
        footer_path=footer_path,
        verbose=verbose
    )

    if not success:
        print(f"Error: Failed to convert {input_path} to HTML")
        return 1

    print(f"✅ Successfully converted Markdown to HTML: {output_path}")

    # Update blog index
    index_path = repo_root / "src" / "blog" / "blog_index.json"
    if update_blog_index(index_path, metadata, verbose):
        print(f"✅ Blog index updated at: {index_path}")

    # Regenerate full blog index if requested
    if args.rebuild_index:
        if regenerate_blog_index(script_dir, repo_root, verbose):
            print(f"✅ Blog index regenerated")

    print(f"✅ Blog post publishing complete: {output_path}")
    return 0


if __name__ == "__main__":
    exit(main())
