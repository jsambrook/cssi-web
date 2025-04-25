#!/usr/bin/env python3
"""
generate_blog_index.py

Reads src/blog/blog_index.json and generates blog/index.html with a list of all blog posts.
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent

    blog_index_json = root_dir / 'src' / 'blog' / 'blog_index.json'
    output_html = root_dir / 'blog' / 'index.html'

    if not blog_index_json.exists():
        print("❌ blog_index.json not found. Cannot generate blog index.")
        return

    with open(blog_index_json, 'r') as f:
        data = json.load(f)

    posts = sorted(data["posts"], key=lambda p: p["date"], reverse=True)

    output_html.parent.mkdir(parents=True, exist_ok=True)

    with open(output_html, 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Blog - Common Sense Systems</title>
</head>
<body>
  <h1>Blog Articles</h1>
  <ul>
""")
        for post in posts:
            title = post["title"]
            year = post["year"]
            month = post["month"]
            slug = post["slug"]
            date_str = datetime.strptime(post["date"], "%Y-%m-%d").strftime("%B %d, %Y")
            f.write(f'    <li><a href="/blog/{year}/{month}/{slug}.html">{title}</a> - {date_str}</li>\n')

        f.write("""  </ul>
</body>
</html>""")

    print(f"✅ Blog index generated at: {output_html}")

if __name__ == "__main__":
    main()
