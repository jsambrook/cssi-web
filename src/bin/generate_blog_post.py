#!/usr/bin/env python3
"""
generate_blog_post.py

Reads a JSON definition of a blog article and generates:
1. A .m4 file with the post content formatted for M4 macros
2. An update to src/includes/blog_posts.m4
3. A graphics prompt text file

Run from inside the src/bin directory. All paths are resolved relative to src/.

Usage:
    ./generate_blog_post.py --input ../blog/drafts/article.json
"""

import json
import os
import argparse
from pathlib import Path
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog post files from JSON input")
    parser.add_argument('--input', required=True, help='Path to the input JSON file (relative to script)')
    return parser.parse_args()


def sanitize_html(html: str) -> str:
    """Escape backticks and wrap in correct M4 format if needed"""
    return html.replace("`", "&#96;")


def generate_m4_content(metadata, content):
    title = metadata['title']
    date_str = datetime.strptime(metadata['date'], '%Y-%m-%d').strftime('%B %d, %Y')
    tags = ', '.join(metadata['tags'])
    intro = sanitize_html(content['introduction'])
    body = sanitize_html(content['body'])
    conclusion = sanitize_html(content['conclusion'])

    return f"""m4_include(`src/includes/blog_macros.m4')m4_dnl
BLOG_POST_LAYOUT(
    `{title}',
    `{date_str}',
    `{tags}',
    `
    {intro}
    {body}
    {conclusion}
    ',
    ``,
    ``)m4_dnl
"""


def write_m4_file(m4_path, m4_content):
    m4_path.parent.mkdir(parents=True, exist_ok=True)
    with open(m4_path, 'w') as f:
        f.write(m4_content)


def update_blog_index(blog_index_path, metadata):
    title = metadata['title']
    year = metadata['year']
    month = metadata['month']
    slug = metadata['slug']
    date_str = datetime.strptime(metadata['date'], '%Y-%m-%d').strftime('%B %d, %Y')
    entry = f"ADD_BLOG_POST(`{year}', `{month}', `{slug}', `{title}', `{date_str}')\n"

    with open(blog_index_path, 'a') as f:
        f.write(entry)


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

    m4_path = root_dir / 'blog' / year / month / f"{slug}.m4"
    blog_index_path = root_dir / 'includes' / 'blog_posts.m4'
    image_prompt_path = root_dir / 'assets' / 'img' / 'blog' / year / month / f"{slug}-image.txt"

    m4_content = generate_m4_content(metadata, content)
    write_m4_file(m4_path, m4_content)
    update_blog_index(blog_index_path, metadata)

    if graphics:
        write_graphics_prompt(graphics, image_prompt_path)

    print(f"✅ Blog post generated at: {m4_path}")
    print(f"✅ Graphics prompt saved to: {image_prompt_path}")
    print(f"✅ Blog index updated at: {blog_index_path}")


if __name__ == '__main__':
    main()
