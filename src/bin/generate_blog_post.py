#!/usr/bin/env python3
"""
generate_blog_post.py

Reads a JSON definition of a blog article and generates:
1. A standalone .html file for the blog post under /blog/YYYY/MM/
2. Updates src/blog/blog_index.json
3. Writes a graphics prompt text file under src/assets/img/blog/YYYY/MM/
4. Appends the CTA fragment from src/includes/blog_cta.html if present
5. Appends the full site footer from src/includes/site_footer.html

Usage:
    ./generate_blog_post.py --input path/to/blog/drafts/YYYY-MM-DD-title.json
"""

import json
import argparse
from pathlib import Path
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog post HTML from JSON input")
    parser.add_argument('--input', required=True, help='Path to the input JSON file (relative to script)')
    return parser.parse_args()


def generate_html_content(metadata, content, cta_html=None, footer_html=None):
    title = metadata['title']
    date_str = datetime.strptime(metadata['date'], '%Y-%m-%d').strftime('%B %d, %Y')
    tags = ', '.join(metadata['tags'])
    introduction = content['introduction']
    body = content['body']
    conclusion = content['conclusion']

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{title}">
  <meta name="keywords" content="{tags}">
  <meta name="author" content="{metadata['author']}">
  <link rel="stylesheet" href="/css/styles.css">
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

  <main class="container blog-post">
    <article>
      <h1>{title}</h1>
      <div class="blog-meta">
        <span class="blog-date">{date_str}</span>
        <span class="blog-tags">{tags}</span>
      </div>
      {introduction}
      {body}
      {conclusion}
    </article>
  </main>

  {cta_html or ""}

  {footer_html or ""}

</body>
</html>
"""


def write_html_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def update_blog_index_json(index_path: Path, metadata: dict):
    entry = {
        "title": metadata["title"],
        "slug": metadata["slug"],
        "date": metadata["date"],
        "year": metadata["year"],
        "month": metadata["month"]
    }
    index_path.parent.mkdir(parents=True, exist_ok=True)
    if index_path.exists():
        data = json.loads(index_path.read_text(encoding='utf-8'))
    else:
        data = {"posts": []}
    data["posts"].append(entry)
    index_path.write_text(json.dumps(data, indent=2), encoding='utf-8')


def write_graphics_prompt(graphics: dict, prompt_path: Path):
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    with prompt_path.open('w', encoding='utf-8') as f:
        f.write(f"Title: {graphics['title']}\n\n")
        f.write(f"Description:\n{graphics['description']}\n\n")
        f.write(f"Usage: {graphics['usage']}\n")


def main():
    args = parse_args()

    # compute repo root two levels up from src/bin
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    input_path = (script_dir / args.input).resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Input JSON file not found: {input_path}")

    data = json.loads(input_path.read_text(encoding='utf-8'))
    metadata = data["metadata"]
    content = data["content_html"]
    graphics = data.get("graphics_prompt")

    year, month, slug = metadata["year"], metadata["month"], metadata["slug"]

    # define paths
    html_path = repo_root / "blog" / year / month / f"{slug}.html"
    index_json_path = repo_root / "src" / "blog" / "blog_index.json"
    graphics_path = repo_root / "src" / "assets" / "img" / "blog" / year / month / f"{slug}-image.txt"
    cta_path = repo_root / "src" / "includes" / "blog_cta.html"
    footer_path = repo_root / "src" / "includes" / "site_footer.html"

    # load optional fragments
    cta_html = cta_path.read_text(encoding='utf-8') if cta_path.exists() else None
    footer_html = footer_path.read_text(encoding='utf-8') if footer_path.exists() else None

    # generate full HTML and write
    html_content = generate_html_content(metadata, content, cta_html=cta_html, footer_html=footer_html)
    write_html_file(html_path, html_content)

    # update index and graphics prompt
    update_blog_index_json(index_json_path, metadata)
    if graphics:
        write_graphics_prompt(graphics, graphics_path)

    print(f"✅ Blog HTML generated at: {html_path}")
    print(f"✅ Graphics prompt saved to: {graphics_path}")
    print(f"✅ Blog index metadata updated at: {index_json_path}")

if __name__ == '__main__':
    main()
