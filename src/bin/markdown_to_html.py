#!/usr/bin/env python3
"""
markdown_to_html.py

Converts Markdown blog posts to HTML using Pandoc templates.
Updates the blog index and creates directories as needed.

Usage:
    ./markdown_to_html.py --input path/to/blog/drafts/YYYY-MM-DD-title.md
    ./markdown_to_html.py --input path/to/blog/drafts/YYYY-MM-DD-title.md --template path/to/template.html
"""

import argparse
import yaml
import json
import subprocess
import re
from pathlib import Path
from datetime import datetime
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description="Convert Markdown blog post to HTML using Pandoc")
    parser.add_argument('--input', required=True, help='Path to the input Markdown file')
    parser.add_argument('--template', default='blog-template.html', help='Pandoc template to use (relative to script directory)')
    parser.add_argument('--cta', default='../includes/blog_cta.html', help='Path to CTA HTML fragment')
    parser.add_argument('--footer', default='../includes/site_footer.html', help='Path to footer HTML fragment')
    return parser.parse_args()


def extract_frontmatter(markdown_path):
    """Extract YAML frontmatter from a Markdown file."""
    content = markdown_path.read_text(encoding='utf-8')

    # Extract the YAML frontmatter between --- markers
    if content.startswith('---'):
        end_marker = content.find('---', 3)
        if end_marker != -1:
            frontmatter = content[3:end_marker].strip()
            try:
                # Try using PyYAML for more robust parsing
                metadata = yaml.safe_load(frontmatter)
                return metadata
            except Exception as e:
                print(f"Warning: YAML parsing error: {e}")
                # Fall back to manual parsing
                metadata = {}
                for line in frontmatter.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()
                return metadata

    return {}


def extract_image_prompt(markdown_text):
    """Extract image prompt section from markdown text"""
    image_prompt = {}

    # Look for the Image Prompt section
    prompt_section_match = re.search(r'##\s*Image\s*Prompt\s*\n(.*?)($)', markdown_text, re.DOTALL)

    if prompt_section_match:
        prompt_section = prompt_section_match.group(1)

        # Extract title
        title_match = re.search(r'Title:\s*(.*?)(?=\n|$)', prompt_section)
        if title_match:
            image_prompt['title'] = title_match.group(1).strip()

        # Extract description
        desc_match = re.search(r'Description:\s*(.*?)(?=\nUsage:|$)', prompt_section, re.DOTALL)
        if desc_match:
            image_prompt['description'] = desc_match.group(1).strip()

        # Extract usage
        usage_match = re.search(r'Usage:\s*(.*?)(?=\n|$)', prompt_section)
        if usage_match:
            image_prompt['usage'] = usage_match.group(1).strip()

    return image_prompt


def extract_references(markdown_text):
    """Extract references from markdown text to pass to Pandoc template"""
    references = []

    # Look for the References section
    ref_section_match = re.search(r'##\s*References\s*\n(.*?)(\n##|$)', markdown_text, re.DOTALL)

    if ref_section_match:
        ref_section = ref_section_match.group(1)

        # Extract each reference entry
        ref_pattern = r'(\d+)\.\s*(.*?)(?=\n\d+\.|$)'
        ref_matches = re.findall(ref_pattern, ref_section, re.DOTALL)

        for ref_id, ref_content in ref_matches:
            ref_id = int(ref_id)
            ref_content = ref_content.strip()

            # Try to extract the components (title, source, year, url)
            url_match = re.search(r'https?://[^\s]+', ref_content)
            url = url_match.group(0) if url_match else ""

            # Remove the URL from content for further processing
            if url:
                ref_content = ref_content.replace(url, "").strip()

            # Try to extract year (4 consecutive digits)
            year_match = re.search(r'\b(19\d\d|20\d\d)\b', ref_content)
            year = year_match.group(1) if year_match else ""

            # Remove year from content if found
            if year:
                ref_content = ref_content.replace(year, "").strip()

            # Split remaining content into title and source
            parts = ref_content.split('.')
            if len(parts) >= 2:
                title = parts[0].strip()
                source = '.'.join(parts[1:]).strip()
            else:
                title = ref_content
                source = ""

            # Remove trailing dots and spaces
            title = title.rstrip('.')
            source = source.rstrip('.')

            reference = {
                "id": ref_id,
                "title": title,
                "source": source,
                "year": year,
                "url": url
            }

            references.append(reference)

    return references


def update_blog_index(index_path, metadata):
    """Update the blog index with metadata from the new post."""
    entry = {
        "title": metadata.get("title", "Untitled"),
        "slug": metadata.get("slug", "untitled"),
        "date": metadata.get("date", datetime.now().strftime('%Y-%m-%d')),
        "year": metadata.get("year", datetime.now().strftime('%Y')),
        "month": metadata.get("month", datetime.now().strftime('%m')),
        "category": metadata.get("category", "Uncategorized"),
        "tags": metadata.get("tags", [])
    }

    # Create or update the index
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if index_path.exists():
        try:
            data = json.loads(index_path.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in {index_path}. Creating new index.")
            data = {"posts": []}
    else:
        data = {"posts": []}

    # Check if the post already exists in the index
    existing = [i for i, p in enumerate(data.get("posts", []))
               if p.get("slug") == entry["slug"] and p.get("date") == entry["date"]]

    if existing:
        # Update existing entry
        for i in existing:
            data["posts"][i] = entry
    else:
        # Add new entry
        data["posts"].append(entry)

    # Sort by date (newest first)
    data["posts"] = sorted(data["posts"], key=lambda p: p.get("date", ""), reverse=True)

    # Write the updated index
    index_path.write_text(json.dumps(data, indent=2), encoding='utf-8')


def write_image_prompt(prompt_data, output_path):
    """Write image prompt to a text file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open('w', encoding='utf-8') as f:
        f.write(f"Title: {prompt_data.get('title', '')}\n\n")
        f.write(f"Description:\n{prompt_data.get('description', '')}\n\n")
        f.write(f"Usage: {prompt_data.get('usage', 'Featured image')}\n")


def convert_markdown_to_html(input_path, output_path, template_path, metadata, references=None, cta_path=None, footer_path=None):
    """Convert Markdown to HTML using Pandoc with a template."""
    # Set up Pandoc command
    pandoc_cmd = [
        "pandoc",
        str(input_path),
        "--from=markdown",
        "--to=html5",
        f"--template={str(template_path)}",
        f"--output={str(output_path)}",
        "--standalone"
    ]

    # Add metadata variables
    for key, value in metadata.items():
        if isinstance(value, list):
            # For list values (like tags), create a metadata file
            continue  # We'll handle this differently
        elif isinstance(value, (str, int, float)):
            pandoc_cmd.append(f"--variable={key}:{value}")

    # Format date for display
    if 'date' in metadata:
        try:
            date_obj = datetime.strptime(metadata['date'], '%Y-%m-%d')
            formatted_date = date_obj.strftime('%B %d, %Y')
            pandoc_cmd.append(f"--variable=date:{formatted_date}")
        except (ValueError, TypeError):
            print(f"Warning: Invalid date format: {metadata.get('date')}")

    # Handle tags special case
    if 'tags' in metadata and metadata['tags']:
        tags = metadata['tags']
        if isinstance(tags, list):
            # Format as comma-separated string
            tags_str = ', '.join(tags)
            pandoc_cmd.append(f"--variable=tags:{tags_str}")
            # Also add as keywords for meta tag
            pandoc_cmd.append(f"--variable=keywords:{tags_str}")
        elif isinstance(tags, str):
            pandoc_cmd.append(f"--variable=tags:{tags}")
            pandoc_cmd.append(f"--variable=keywords:{tags}")

    # Add references if available
    if references:
        # Create a temporary JSON file with references
        temp_dir = Path.cwd() / "temp"
        temp_dir.mkdir(exist_ok=True)
        refs_file = temp_dir / "refs.json"
        with open(refs_file, 'w') as f:
            json.dump({"references": references}, f)

        pandoc_cmd.append(f"--metadata-file={refs_file}")

    # Add CTA and footer HTML if available
    if cta_path and Path(cta_path).exists():
        cta_html = Path(cta_path).read_text(encoding='utf-8')
        # Create a temporary file with CTA HTML
        temp_dir = Path.cwd() / "temp"
        temp_dir.mkdir(exist_ok=True)
        cta_file = temp_dir / "cta.html"
        cta_file.write_text(cta_html)
        pandoc_cmd.append(f"--variable=cta_html:{cta_html}")

    if footer_path and Path(footer_path).exists():
        footer_html = Path(footer_path).read_text(encoding='utf-8')
        pandoc_cmd.append(f"--variable=footer_html:{footer_html}")

    # Run Pandoc
    try:
        subprocess.run(pandoc_cmd, check=True)
        print(f"✅ Successfully converted Markdown to HTML: {output_path}")

        # Clean up temporary files
        if references:
            refs_file.unlink(missing_ok=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error converting Markdown to HTML: {e}")

        # If Pandoc isn't installed, show a helpful message
        if e.returncode == 127:  # Command not found
            print("\nPandoc appears to be missing. Install Pandoc with one of these commands:")
            print("- Ubuntu/Debian: sudo apt-get install pandoc")
            print("- macOS (Homebrew): brew install pandoc")
            print("- Windows: Install from https://pandoc.org/installing.html")

        return False


def main():
    args = parse_args()

    # Get script directory and input path
    script_dir = Path(__file__).resolve().parent
    input_path = Path(args.input).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"Input Markdown file not found: {input_path}")

    # Get repo root (assumed to be two levels up from script dir)
    repo_root = script_dir.parent.parent

    # Read the input Markdown file
    markdown_text = input_path.read_text(encoding='utf-8')

    # Extract metadata, references, and image prompt
    metadata = extract_frontmatter(input_path)
    references = extract_references(markdown_text)
    image_prompt = extract_image_prompt(markdown_text)

    # Set default values for required fields
    metadata.setdefault('slug', input_path.stem.split('-', 3)[-1])
    metadata.setdefault('year', datetime.now().strftime('%Y'))
    metadata.setdefault('month', datetime.now().strftime('%m'))

    # Resolve template path
    if args.template.startswith('/'):
        template_path = Path(args.template)
    else:
        template_path = script_dir / args.template

    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")

    # Resolve CTA and footer paths
    cta_path = script_dir / args.cta if not args.cta.startswith('/') else Path(args.cta)
    footer_path = script_dir / args.footer if not args.footer.startswith('/') else Path(args.footer)

    # Define output paths
    year = metadata.get('year')
    month = metadata.get('month')
    slug = metadata.get('slug')

    html_dir = repo_root / "blog" / year / month
    html_dir.mkdir(parents=True, exist_ok=True)
    html_path = html_dir / f"{slug}.html"

    image_prompt_dir = repo_root / "src" / "assets" / "img" / "blog" / year / month
    image_prompt_path = image_prompt_dir / f"{slug}-image.txt"

    index_path = repo_root / "src" / "blog" / "blog_index.json"

    # Convert Markdown to HTML
    success = convert_markdown_to_html(
        input_path=input_path,
        output_path=html_path,
        template_path=template_path,
        metadata=metadata,
        references=references,
        cta_path=cta_path,
        footer_path=footer_path
    )

    if success:
        # Update blog index
        update_blog_index(index_path, metadata)
        print(f"✅ Blog index updated at: {index_path}")

        # Write image prompt if available
        if image_prompt:
            write_image_prompt(image_prompt, image_prompt_path)
            print(f"✅ Image prompt saved to: {image_prompt_path}")

        print(f"✅ Blog post generated successfully: {html_path}")
    else:
        print("❌ Failed to generate blog post")


if __name__ == "__main__":
    main()
