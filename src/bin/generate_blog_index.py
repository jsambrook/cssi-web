#!/usr/bin/env python3
"""
generate_blog_index.py

Reads src/blog/blog_index.json, filters out posts without HTML files,
injects the post list into blog_index_template.html, fills in the CTA,
appends the site footer, and writes blog/index.html.
"""

import json
from pathlib import Path
from datetime import datetime

def main():
    # Locate script and repo root
    script_dir = Path(__file__).resolve().parent
    repo_root  = script_dir.parent.parent

    # Paths
    index_json    = repo_root / 'src' / 'blog' / 'blog_index.json'
    template_html = repo_root / 'src' / 'includes' / 'blog_index_template.html'
    cta_html_file = repo_root / 'src' / 'includes' / 'blog_cta.html'
    footer_file   = repo_root / 'src' / 'includes' / 'site_footer.html'
    output_html   = repo_root / 'blog' / 'index.html'

    # Sanity checks
    if not index_json.exists():
        print(f"❌ {index_json} not found. Cannot generate blog index.")
        return
    if not template_html.exists():
        print(f"❌ {template_html} not found. Cannot generate blog index.")
        return

    # Load metadata
    data = json.loads(index_json.read_text(encoding='utf-8'))
    posts = sorted(data.get('posts', []), key=lambda p: p['date'], reverse=True)

    # Build list items only for posts whose HTML exists
    lines = []
    for p in posts:
        year, month, slug = p['year'], p['month'], p['slug']
        html_path = repo_root / 'blog' / year / month / f"{slug}.html"
        if not html_path.exists():
            continue
        date_str = datetime.strptime(p['date'], "%Y-%m-%d").strftime("%B %d, %Y")
        href     = f"/blog/{year}/{month}/{slug}.html"
        lines.append(f'      <li><a href="{href}">{p["title"]}</a> <span class="blog-date">– {date_str}</span></li>')

    post_list = (
        '<ul class="blog-list">\n'
        + "\n".join(lines) +
        "\n    </ul>"
    )

    # Read the template
    template = template_html.read_text(encoding='utf-8')

    # Inject post list
    filled = template.replace('<!-- POST_LIST goes here -->', post_list)

    # Inject CTA (if present)
    cta_html = cta_html_file.read_text(encoding='utf-8') if cta_html_file.exists() else ''
    filled = filled.replace('<!-- CTA_PLACEHOLDER -->', cta_html)

    # Append full footer just before </body>
    footer_html = footer_file.read_text(encoding='utf-8') if footer_file.exists() else ''
    final_html  = filled.replace('</body>', f'{footer_html}\n</body>')

    # Write out
    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(final_html, encoding='utf-8')

    print(f"✅ Styled blog index generated at: {output_html}")


if __name__ == "__main__":
    main()
