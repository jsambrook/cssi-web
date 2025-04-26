#!/usr/bin/env python3
"""
generate_blog_index.py

Reads src/blog/blog_index.json and generates blog/index.html by injecting
your styled template and the up-to-date list of posts.

Fixes root detection so it always finds:
 - src/blog/blog_index.json
 - src/includes/blog_index_template.html
and writes to
 - blog/index.html
regardless of where it's run from.
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    # Where this script lives: .../cssi-web/src/bin
    script_dir = Path(__file__).resolve().parent
    # Repo root: one more level up
    repo_root = script_dir.parent.parent

    index_json = repo_root / 'src' / 'blog' / 'blog_index.json'
    template_html = repo_root / 'src' / 'includes' / 'blog_index_template.html'
    output_html   = repo_root / 'blog' / 'index.html'

    # Sanity checks
    if not index_json.exists():
        print(f"❌ {index_json} not found. Cannot generate blog index.")
        return
    if not template_html.exists():
        print(f"❌ {template_html} not found. Cannot apply template.")
        return

    # Load metadata
    data = json.loads(index_json.read_text(encoding='utf-8'))
    posts = sorted(data.get('posts', []), key=lambda p: p['date'], reverse=True)

    # Build the <ul class="blog-list">...</ul>
    lines = []
    for p in posts:
        date_str = datetime.strptime(p['date'], "%Y-%m-%d").strftime("%B %d, %Y")
        href = f"/blog/{p['year']}/{p['month']}/{p['slug']}.html"
        lines.append(f'      <li>')
        lines.append(f'        <a href="{href}">{p["title"]}</a>')
        lines.append(f'        <span class="blog-date">– {date_str}</span>')
        lines.append(f'      </li>')
    post_list = "<ul class=\"blog-list\">\n" + "\n".join(lines) + "\n    </ul>"

    # Read your template and inject
    template = template_html.read_text(encoding='utf-8')
    final = template.replace('<!-- POST_LIST goes here -->', post_list)

    # Write out
    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(final, encoding='utf-8')
    print(f"✅ Styled blog index generated at: {output_html}")

if __name__ == "__main__":
    main()
