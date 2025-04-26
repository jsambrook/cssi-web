#!/usr/bin/env python3
"""
generate_blog_index.py

Generates blog/index.html by injecting blog links into a full HTML layout template.

Ensures styling by wrapping content in the .blog-index section used in styles.css.
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent

    # Adjust if running from src/bin
    if (root_dir / 'src').exists():
        root_dir = root_dir.parent

    index_json_path = root_dir / 'src' / 'blog' / 'blog_index.json'
    template_path = root_dir / 'src' / 'includes' / 'blog_index_template.html'
    output_path = root_dir / 'blog' / 'index.html'

    if not index_json_path.exists():
        print(f"❌ {index_json_path} not found. Cannot generate blog index.")
        return

    if not template_path.exists():
        print(f"❌ {template_path} not found.")
        return

    with open(index_json_path) as f:
        index_data = json.load(f)

    posts = sorted(index_data['posts'], key=lambda p: p['date'], reverse=True)

    # Generate styled <ul> list for blog posts
    post_list_html = ''
    for post in posts:
        title = post['title']
        slug = post['slug']
        year = post['year']
        month = post['month']
        date = datetime.strptime(post['date'], "%Y-%m-%d").strftime("%B %d, %Y")
        link = f"/blog/{year}/{month}/{slug}.html"
        post_list_html += f'      <li>\n'
        post_list_html += f'        <a href="{link}">{title}</a>\n'
        post_list_html += f'        <span class="blog-date">{date}</span>\n'
        post_list_html += f'      </li>\n'

    full_list_html = f'<ul class="blog-list">\n{post_list_html}    </ul>'

    with open(template_path) as f:
        template = f.read()

    # Insert into .blog-index section
    full_content = template.replace('<!-- POST_LIST goes here -->', full_list_html)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(full_content)

    print(f"✅ Styled blog index generated at: {output_path}")

if __name__ == "__main__":
    main()
