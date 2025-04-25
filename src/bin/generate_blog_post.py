#!/usr/bin/env python3
"""
generate_blog_post.py

Reads a JSON definition of a blog article and generates:
1. A standalone .html file for the blog post
2. Updates src/blog/blog_index.json
3. A graphics prompt text file

Usage:
    ./generate_blog_post.py --input path/to/article.json
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog post HTML from JSON input")
    parser.add_argument('--input', required=True, help='Path to the input JSON file (relative to script)')
    return parser.parse_args()


def generate_html_content(metadata, content):
    """Generate full HTML page for a blog post."""
    title = metadata['title']
    date_str = datetime.strptime(metadata['date'], '%Y-%m-%d').strftime('%B %d, %Y')
    tags = ', '.join(metadata['tags'])
    introduction = content['introduction']
    body = content['body']
    conclusion = content['conclusion']

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <meta name="description" content="{title}">
  <meta name="keywords" content="{tags}">
  <meta name="author" content="{metadata['author']}">
</head>
<body>
  <article>
    <h1>{title}</h1>
    <p><em>Published on {date_str}</em></p>
    {introduction}
    {body}
    {conclusion}
  </article>
</body>
</html>
"""
    return html


def write_html_file(html_path, html_content):
    html_path.parent.mkdir(parents=True, exist_ok=True)
    with open(html_path, 'w') as f:
        f.write(html_content)


def update_blog_index_json(blog_index_path, metadata):
    """Append a blog entry into blog_index.json safely."""
    post_entry = {
        "title": metadata['title'],
        "slug": metadata['slug'],
        "date": metadata['date'],
        "year": metadata['year'],
        "month": metadata['month']
    }

    blog_index_path.parent.mkdir(parents=True, exist_ok=True)
    if blog_index_path.exists():
        with open(blog_index_path, 'r') as f:
            index_data = json.load(f)
    else:
        index_data = {"posts": []}

    index_data["posts"].append(post_entry)

    with open(blog_index_path, 'w') as f:
        json.dump(index_data, f, indent=2)


def write_graphics_prompt(graphics, image_prompt_path):
    image_prompt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(image_prompt_path, 'w') as f:
        f.write(f"Title: {graphics['title']}\n\n")
        f.write(f"Description:\n{graphics['description']}\n\n")
        f.write(f"Usage: {graphics['usage']}\n")


def main():
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent

    input_path = (script_dir / args.input).resolve()
    with open(input_path, 'r') as f:
        data = json.load(f)

    metadata = data['metadata']
    content = data['content_html']
    graphics = data.get('graphics_prompt', {})

    year = metadata['year']
    month = metadata['month']
    slug = metadata['slug']

    html_content = generate_html_content(metadata, content)

    html_path = root_dir / 'blog' / year / month / f"{slug}.html"
    blog_index_path = root_dir / 'blog' / 'blog_index.json'
    image_prompt_path = root_dir / 'assets' / 'img' / 'blog' / year / month / f"{slug}-image.txt"

    write_html_file(html_path, html_content)
    update_blog_index_json(blog_index_path, metadata)

    if graphics:
        write_graphics_prompt(graphics, image_prompt_path)

    print(f"✅ Blog HTML generated at: {html_path}")
    print(f"✅ Graphics prompt saved to: {image_prompt_path}")
    print(f"✅ Blog index metadata updated at: {blog_index_path}")


if __name__ == '__main__':
    main()
