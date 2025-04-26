#!/usr/bin/env python3
"""
generate_blog_index.py

Reads src/blog/blog_index.json and generates blog/index.html using a styled template,
only including posts whose HTML files exist, and injecting a Call-to-Action.

Template: src/includes/blog_index_template.html must include:
  <!-- POST_LIST goes here -->
  <!-- CTA_PLACEHOLDER -->

Outputs: blog/index.html
"""

import json
from pathlib import Path
from datetime import datetime


def main():
    # Determine repo root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    # Paths
    index_json = repo_root / 'src' / 'blog' / 'blog_index.json'
    template_html = repo_root / 'src' / 'includes' / 'blog_index_template.html'
    cta_html_path = repo_root / 'src' / 'includes' / 'blog_cta.html'
    output_html = repo_root / 'blog' / 'index.html'

    # Sanity checks
    if not index_json.exists():
        print(f"❌ {index_json} not found. Cannot generate blog index.")
        return
    if not template_html.exists():
        print(f"❌ {template_html} not found. Cannot apply template.")
        return

    # Load metadata
    with index_json.open('r', encoding='utf-8') as f:
        data = json.load(f)

    # Read CTA fragment if available
    cta_html = ''
    if cta_html_path.exists():
        cta_html = cta_html_path.read_text(encoding='utf-8')

    # Build list entries only for existing HTML posts
    posts = sorted(data.get('posts', []), key=lambda p: p.get('date', ''), reverse=True)
    list_items = []
    for post in posts:
        year = post.get('year')
        month = post.get('month')
        slug = post.get('slug')
        title = post.get('title')
        date = post.get('date')
        # Path to the generated HTML
        post_html = repo_root / 'blog' / year / month / f"{slug}.html"
        if post_html.exists():
            # Format date nicely
            try:
                date_str = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
            except Exception:
                date_str = date
            href = f"/blog/{year}/{month}/{slug}.html"
            list_items.append(
                f"      <li>"
                f"<a href=\"{href}\">{title}</a> "
                f"<span class=\"blog-date\">– {date_str}</span>"
                f"</li>"
            )

    # Combine into a list
    post_list_html = '<ul class="blog-list">\n' + '\n'.join(list_items) + '\n    </ul>'

    # Load template and inject
    template = template_html.read_text(encoding='utf-8')
    final_html = template.replace('<!-- POST_LIST goes here -->', post_list_html)
    final_html = final_html.replace('<!-- CTA_PLACEHOLDER -->', cta_html)

    # Write output
    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(final_html, encoding='utf-8')

    print(f"✅ Styled blog index generated at: {output_html}")


if __name__ == '__main__':
    main()
