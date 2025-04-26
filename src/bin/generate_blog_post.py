#!/usr/bin/env python3
"""
generate_blog_post.py

Reads a JSON definition of a blog article and generates:
1. A standalone .html blog post
2. Updates blog/blog_index.json
3. Generates a graphics prompt file for image generation

Usage:
    ./generate_blog_post.py --input path/to/blog/drafts/YYYY-MM-DD-title.json
"""

import json
import argparse
from pathlib import Path
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog post HTML from JSON input")
    parser.add_argument('--input', required=True, help='Path to the input JSON file')
    return parser.parse_args()


def generate_html_content(metadata, content):
    """Generate full HTML page for the blog post."""
    title = metadata['title']
    date_str = datetime.strptime(metadata['date'], '%Y-%m-%d').strftime('%B %d, %Y')
    tags = ', '.join(metadata['tags'])
    intro = content['introduction']
    body = content['body']
    conclusion = content['conclusion']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <meta name="description" content="{title}">
  <meta name="keywords" content="{tags}">
  <meta name="author" content="{metadata['author']}">
  <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
  <main class="blog-post">
    <article class="container">
      <header class="blog-header">
        <h1>{title}</h1>
        <div class="blog-meta">
          <span class="blog-date">{date_str}</span>
          <span class="blog-tags">{tags}</span>
        </div>
      </header>
      <div class="blog-content">
        {intro}
        {body}
        {conclusion}
      </div>
      <nav class="blog-nav">
        <a href="/blog/index.html" class="blog-nav-link">&larr; Back to Blog</a>
      </nav>
    </article>
  </main>
</body>
</html>
"""


def write_html_file(html_path, html_content):
    html_path.parent.mkdir(parents=True, exist_ok=True)
    with open(html_path, 'w') as f:
        f.write(html_content)


def update_blog_index_json(blog_index_path, metadata):
    """Append a blog entry to blog_index.json (safe and idempotent)."""
    new_entry = {
        "title": metadata["title"],
        "slug": metadata["slug"],
        "date": metadata["date"],
        "year": metadata["year"],
        "month": metadata["month"]
    }

    blog_index_path.parent.mkdir(parents=True, exist_ok=True)
    if blog_index_path.exists():
        with open(blog_index_path, "r") as f:
            index_data = json.load(f)
    else:
        index_data = {"posts": []}

    # Avoid duplicates
    if not any(p["slug"] == new_entry["slug"] and p["date"] == new_entry["date"] for p in index_data["posts"]):
        index_data["posts"].append(new_entry)

    with open(blog_index_path, "w") as f:
        json.dump(index_data, f, indent=2)


def write_graphics_prompt(graphics, image_path):
    image_path.parent.mkdir(parents=True, exist_ok=True)
    with open(image_path, "w") as f:
        f.write(f"Title: {graphics['title']}\n\n")
        f.write(f"Description:\n{graphics['description']}\n\n")
        f.write(f"Usage: {graphics['usage']}\n")


def main():
    args = parse_args()
    input_path = Path(args.input).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r") as f:
        data = json.load(f)

    metadata = data["metadata"]
    content = data["content_html"]
    graphics = data.get("graphics_prompt", {})

    # Project root is two levels up from src/bin/
    root_dir = Path(__file__).resolve().parents[2]

    year = metadata["year"]
    month = metadata["month"]
    slug = metadata["slug"]

    html_content = generate_html_content(metadata, content)

    # 💡 Write HTML post to public-facing blog/ dir
    html_path = root_dir / 'blog' / year / month / f"{slug}.html"
    index_path = root_dir / 'src' / 'blog' / 'blog_index.json'
    image_path = root_dir / 'src' / 'assets'
