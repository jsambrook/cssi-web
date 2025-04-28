#!/usr/bin/env python3
"""
generate_blog_index.py

Reads src/blog/blog_index.json, filters out posts without HTML files,
injects the post list into blog_index_template.html, fills in the CTA,
appends the site footer, and writes blog/index.html.

Usage:
    ./generate_blog_index.py
"""

import json
from pathlib import Path
from datetime import datetime

def collect_categories_and_tags(posts, repo_root):
    """
    Extracts categories and tags from the blog posts.

    Returns a tuple of (categories, tags) where each is a dictionary mapping
    the category/tag name to a count of posts.
    """
    categories = {}
    tags = {}

    for p in posts:
        # Get categories and tags from the post metadata
        category = p.get('category', '')
        post_tags = p.get('tags', [])

        # Count categories
        if category:
            categories[category] = categories.get(category, 0) + 1

        # Count tags
        for tag in post_tags:
            # Ensure tag is a string
            tag_str = str(tag).strip('"\'[]')
            tags[tag_str] = tags.get(tag_str, 0) + 1

    return categories, tags


def build_filter_section(categories, tags):
    """Builds HTML for category and tag filters with mobile-friendly design"""
    if not categories and not tags:
        return ""

    html = '<div class="filter-container">\n'
    html += '  <div class="filter-toggles">\n'
    html += '    <button id="toggle-filters" class="filter-toggle-btn">Filter Posts <span class="toggle-icon">+</span></button>\n'
    html += '    <button id="clear-filters" class="filter-clear-btn">Clear Filters</button>\n'
    html += '  </div>\n'

    html += '  <div class="blog-filters" id="filter-panel">\n'

    # Add categories filter
    if categories:
        html += '    <div class="filter-section category-filter">\n'
        html += '      <h3>Categories</h3>\n'
        html += '      <ul>\n'
        for cat, count in sorted(categories.items()):
            html += f'        <li><a href="#" data-category="{cat}">{cat} <span class="count">({count})</span></a></li>\n'
        html += '      </ul>\n'
        html += '    </div>\n'

    # Add tags filter
    if tags:
        html += '    <div class="filter-section tag-filter">\n'
        html += '      <h3>Tags</h3>\n'
        html += '      <div class="tag-cloud">\n'
        for tag, count in sorted(tags.items()):
            html += f'        <a href="#" data-tag="{tag}" class="tag">{tag} <span class="count">({count})</span></a>\n'
        html += '      </div>\n'
        html += '    </div>\n'

    html += '  </div>\n'
    html += '  <div class="active-filters" id="active-filters"></div>\n'
    html += '</div>\n'

    # Add filter functionality with mobile-friendly enhancements
    html += """
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Toggle filter panel visibility (mobile-friendly)
  const toggleBtn = document.getElementById('toggle-filters');
  const filterPanel = document.getElementById('filter-panel');
  const activeFilters = document.getElementById('active-filters');

  // Initialize and maintain active filters state
  let activeFiltersState = {
    category: null,
    tags: []
  };

  // Toggle filter panel
  toggleBtn.addEventListener('click', function() {
    filterPanel.classList.toggle('expanded');
    this.classList.toggle('active');

    // Toggle icon
    const icon = this.querySelector('.toggle-icon');
    icon.textContent = filterPanel.classList.contains('expanded') ? '−' : '+';
  });

  // Update active filters UI
  function updateActiveFiltersUI() {
    activeFilters.innerHTML = '';

    if (activeFiltersState.category) {
      const pill = document.createElement('span');
      pill.className = 'filter-pill category-pill';
      pill.textContent = activeFiltersState.category;

      const removeBtn = document.createElement('button');
      removeBtn.className = 'remove-filter';
      removeBtn.innerHTML = '&times;';
      removeBtn.setAttribute('data-type', 'category');
      removeBtn.setAttribute('data-value', activeFiltersState.category);

      pill.appendChild(removeBtn);
      activeFilters.appendChild(pill);
    }

    activeFiltersState.tags.forEach(tag => {
      const pill = document.createElement('span');
      pill.className = 'filter-pill tag-pill';
      pill.textContent = tag;

      const removeBtn = document.createElement('button');
      removeBtn.className = 'remove-filter';
      removeBtn.innerHTML = '&times;';
      removeBtn.setAttribute('data-type', 'tag');
      removeBtn.setAttribute('data-value', tag);

      pill.appendChild(removeBtn);
      activeFilters.appendChild(pill);
    });

    // Show/hide based on if we have active filters
    if (activeFiltersState.category || activeFiltersState.tags.length > 0) {
      activeFilters.style.display = 'flex';
    } else {
      activeFilters.style.display = 'none';
    }
  }

  // Apply all current filters
  function applyAllFilters() {
    document.querySelectorAll('.blog-list li').forEach(item => {
      let shouldShow = true;

      // Check category filter
      if (activeFiltersState.category &&
          !item.getAttribute('data-categories').includes(activeFiltersState.category)) {
        shouldShow = false;
      }

      // Check tag filters
      if (shouldShow && activeFiltersState.tags.length > 0) {
        const itemTags = item.getAttribute('data-tags').split(',');
        let hasAnyTag = false;

        activeFiltersState.tags.forEach(tag => {
          if (itemTags.includes(tag)) {
            hasAnyTag = true;
          }
        });

        if (!hasAnyTag) shouldShow = false;
      }

      item.style.display = shouldShow ? '' : 'none';
    });

    // Update URL with filter state for sharing
    updateURL();
  }

  // Category filtering
  document.querySelectorAll('.category-filter a').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const category = this.getAttribute('data-category');

      // Toggle active class
      document.querySelectorAll('.category-filter a').forEach(a => a.classList.remove('active'));
      this.classList.add('active');

      // Update active filters state
      activeFiltersState.category = category;
      updateActiveFiltersUI();
      applyAllFilters();

      // On mobile, collapse filter panel after selection
      if (window.innerWidth < 768) {
        filterPanel.classList.remove('expanded');
        toggleBtn.classList.remove('active');
        toggleBtn.querySelector('.toggle-icon').textContent = '+';
      }
    });
  });

  // Tag filtering
  document.querySelectorAll('.tag-filter a').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const tag = this.getAttribute('data-tag');

      // Toggle this tag in active filters
      if (this.classList.contains('active')) {
        // Remove tag
        this.classList.remove('active');
        activeFiltersState.tags = activeFiltersState.tags.filter(t => t !== tag);
      } else {
        // Add tag
        this.classList.add('active');
        activeFiltersState.tags.push(tag);
      }

      updateActiveFiltersUI();
      applyAllFilters();
    });
  });

  // Remove filter when clicking X on filter pill
  activeFilters.addEventListener('click', function(e) {
    if (e.target.classList.contains('remove-filter')) {
      const type = e.target.getAttribute('data-type');
      const value = e.target.getAttribute('data-value');

      if (type === 'category') {
        activeFiltersState.category = null;
        document.querySelectorAll('.category-filter a').forEach(a => a.classList.remove('active'));
      } else if (type === 'tag') {
        activeFiltersState.tags = activeFiltersState.tags.filter(t => t !== value);
        document.querySelector(`.tag-filter a[data-tag="${value}"]`).classList.remove('active');
      }

      updateActiveFiltersUI();
      applyAllFilters();
    }
  });

  // Clear filters button
  document.getElementById('clear-filters').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelectorAll('.category-filter a, .tag-filter a').forEach(a => a.classList.remove('active'));
    activeFiltersState = { category: null, tags: [] };
    updateActiveFiltersUI();

    document.querySelectorAll('.blog-list li').forEach(item => {
      item.style.display = '';
    });

    // Clear URL parameters
    history.replaceState({}, document.title, window.location.pathname);
  });

  // Update URL with current filter state
  function updateURL() {
    const params = new URLSearchParams();

    if (activeFiltersState.category) {
      params.append('category', activeFiltersState.category);
    }

    if (activeFiltersState.tags.length > 0) {
      params.append('tags', activeFiltersState.tags.join(','));
    }

    const newURL = params.toString()
      ? `${window.location.pathname}?${params.toString()}`
      : window.location.pathname;

    history.replaceState({}, document.title, newURL);
  }

  // Initialize from URL parameters (if any)
  function initFromURL() {
    const params = new URLSearchParams(window.location.search);

    if (params.has('category')) {
      const category = params.get('category');
      const categoryLink = document.querySelector(`.category-filter a[data-category="${category}"]`);

      if (categoryLink) {
        categoryLink.classList.add('active');
        activeFiltersState.category = category;
      }
    }

    if (params.has('tags')) {
      const tagList = params.get('tags').split(',');

      tagList.forEach(tag => {
        const tagLink = document.querySelector(`.tag-filter a[data-tag="${tag}"]`);

        if (tagLink) {
          tagLink.classList.add('active');
          activeFiltersState.tags.push(tag);
        }
      });
    }

    // If we have any active filters, apply them
    if (activeFiltersState.category || activeFiltersState.tags.length > 0) {
      updateActiveFiltersUI();
      applyAllFilters();
    }
  }

  // Initialize from URL
  initFromURL();
});
</script>
"""

    return html


def get_metadata_from_json(post_path, repo_root):
    """
    Try to get post metadata either from:
    1. A JSON file with the same name in the drafts directory
    2. A JSON metadata file with the same name as the MD file
    """
    # Extract date and slug from the HTML path
    parts = post_path.name.split('.')
    if len(parts) < 2:
        return {}

    # Remove .html extension
    slug = parts[0]

    # Check if the slug contains a date
    date_parts = []
    if '-' in slug:
        date_parts = slug.split('-')
        if len(date_parts) >= 3 and len(date_parts[0]) == 4:
            year = date_parts[0]
            month = date_parts[1]
            # Rebuild the slug without the date
            slug = '-'.join(date_parts[3:])
            date = f"{year}-{month}-{date_parts[2]}"
        else:
            # Try parent directories for date
            year = post_path.parent.name  # Month directory
            month = post_path.parent.parent.name  # Year directory
            date = None  # We don't have the day
    else:
        # Try parent directories for date
        month = post_path.parent.name
        year = post_path.parent.parent.name
        date = None

    # First, try to find a matching JSON file in the drafts directory
    json_paths = []

    # Most specific search: look for a JSON file with matching date and slug
    if date:
        # Check drafts directory for JSON with same name pattern
        json_path = repo_root / 'src' / 'blog' / 'drafts' / f"{date}-{slug}.json"
        json_paths.append(json_path)

    # Also check for a JSON with just the slug (without date)
    json_paths.append(repo_root / 'src' / 'blog' / 'drafts' / f"{slug}.json")

    # Try to find any JSON file with matching slug pattern
    drafts_dir = repo_root / 'src' / 'blog' / 'drafts'
    if drafts_dir.exists():
        for json_file in drafts_dir.glob(f"*-{slug}.json"):
            if json_file not in json_paths:
                json_paths.append(json_file)

    # Try each potential JSON path
    for json_path in json_paths:
        if json_path.exists():
            try:
                data = json.loads(json_path.read_text(encoding='utf-8'))

                # Check if this is the metadata format from generate_blog_markdown.py
                if 'metadata' in data:
                    return data['metadata']

                # Check for older JSON format
                if 'metadata' not in data and 'content_html' in data:
                    return data.get('metadata', {})

                # Otherwise, use the whole JSON
                return data
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue

    # If we couldn't find a JSON file, create basic metadata
    basic_metadata = {
        "title": slug.replace('-', ' ').title(),
        "slug": slug,
        "date": date if date else f"{year}-{month}-01",
        "year": year,
        "month": month,
        "category": "Uncategorized",
        "tags": []
    }

    return basic_metadata


def main():
    # Locate script and repo root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    # Paths
    index_json = repo_root / 'src' / 'blog' / 'blog_index.json'
    template_html = repo_root / 'src' / 'includes' / 'blog_index_template.html'
    cta_html_file = repo_root / 'src' / 'includes' / 'blog_cta.html'
    footer_file = repo_root / 'src' / 'includes' / 'site_footer.html'
    output_html = repo_root / 'blog' / 'index.html'

    # Sanity checks
    if not index_json.exists():
        print(f"❌ {index_json} not found. Creating an empty blog index.")
        index_json.parent.mkdir(parents=True, exist_ok=True)
        index_json.write_text('{"posts":[]}', encoding='utf-8')

    if not template_html.exists():
        print(f"❌ {template_html} not found. Creating a basic template...")
        # Create a basic template if one doesn't exist
        template_html.parent.mkdir(parents=True, exist_ok=True)
        template_html.write_text("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog - Common Sense Systems, Inc.</title>
  <link rel="stylesheet" href="/css/styles.css">
  <!-- CSS_PLACEHOLDER -->
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

  <main class="container">
    <h1>Blog Articles</h1>
    <!-- POST_LIST goes here -->
  </main>

  <!-- CTA_PLACEHOLDER -->

</body>
</html>""", encoding='utf-8')
        print(f"✅ Created basic template at: {template_html}")

    # Load metadata
    try:
        data = json.loads(index_json.read_text(encoding='utf-8'))
        posts = sorted(data.get('posts', []), key=lambda p: p['date'], reverse=True)
    except (json.JSONDecodeError, FileNotFoundError):
        print(f"❌ Error reading or parsing {index_json}. Creating a new index.")
        posts = []

    # Collect all HTML files in the blog directory (find actual posts)
    html_files = []
    blog_dir = repo_root / 'blog'

    # Skip if blog directory doesn't exist
    if blog_dir.exists():
        # Recursively find all HTML files in the blog directory
        for html_file in blog_dir.glob('**/*.html'):
            # Skip index.html files
            if html_file.name != 'index.html':
                html_files.append(html_file)

    # Update posts list with any HTML files not in the index
    for html_file in html_files:
        # Extract relative path from blog directory
        rel_path = html_file.relative_to(blog_dir)
        parts = list(rel_path.parts)

        # Skip if we don't have at least year/month/file.html
        if len(parts) < 3:
            continue

        # Get year, month, and slug
        year = parts[0]
        month = parts[1]
        slug = html_file.stem  # Filename without extension

        # Check if this post is already in the index
        existing = [p for p in posts if p.get('slug') == slug and
                   p.get('year') == year and p.get('month') == month]

        if not existing:
            # This is a new HTML file, get its metadata
            metadata = get_metadata_from_json(html_file, repo_root)

            # Ensure we have the correct year, month, slug
            metadata['year'] = year
            metadata['month'] = month
            metadata['slug'] = slug

            # Add to posts list
            posts.append(metadata)

    # Remove posts that don't have corresponding HTML files
    valid_posts = []
    for p in posts:
        year = p.get('year', '')
        month = p.get('month', '')
        slug = p.get('slug', '')

        html_path = blog_dir / year / month / f"{slug}.html"
        if html_path.exists():
            # Ensure post has complete metadata
            if not p.get('title'):
                # Try to get full metadata
                metadata = get_metadata_from_json(html_path, repo_root)
                if metadata.get('title'):
                    # Update with better metadata
                    p.update(metadata)

            valid_posts.append(p)

    # Sort posts by date (newest first)
    valid_posts = sorted(valid_posts, key=lambda p: p.get('date', ''), reverse=True)

    # Save the updated blog index
    data = {"posts": valid_posts}
    index_json.write_text(json.dumps(data, indent=2), encoding='utf-8')

    # Collect categories and tags from posts
    categories, tags = collect_categories_and_tags(valid_posts, repo_root)

    # Build list items for the blog index page
    lines = []
    for p in valid_posts:
        year, month, slug = p.get('year', ''), p.get('month', ''), p.get('slug', '')
        html_path = blog_dir / year / month / f"{slug}.html"
        if not html_path.exists():
            continue

        # Get formatted date
        try:
            date_obj = datetime.strptime(p.get('date', ''), "%Y-%m-%d")
            date_str = date_obj.strftime("%B %d, %Y")
        except ValueError:
            date_str = p.get('date', '')

        # Get path to blog post
        href = f"/blog/{year}/{month}/{slug}.html"

        # Get category and tags
        category = p.get('category', '')
        post_tags = p.get('tags', [])

        # Handle tags in different formats
        if isinstance(post_tags, list):
            tag_attr = ",".join(str(tag).strip('"\'') for tag in post_tags)
        elif isinstance(post_tags, str):
            # Handle comma-separated string
            tag_attr = post_tags.replace('"', '').replace("'", "")
        else:
            tag_attr = ""

        # Create list item with data attributes for filtering
        lines.append(
            f'      <li data-categories="{category}" data-tags="{tag_attr}">'
            f'<a href="{href}">{p.get("title", slug.replace("-", " ").title())}</a> <span class="blog-date">– {date_str}</span>'
            f'</li>'
        )

    # Create filter HTML if we have categories or tags
    filter_html = build_filter_section(categories, tags) if (categories or tags) else ""

    # Simplified post list structure without redundant clear button (now in filter HTML)
    post_list = (
        f'{filter_html}\n'
        '<ul class="blog-list">\n'
        + "\n".join(lines) +
        "\n    </ul>"
    )

    # Read the template
    template = template_html.read_text(encoding='utf-8')

    # Add responsive CSS for filtering
    css_styles = """
<style>
  /* Overall filter container */
  .filter-container {
    margin-bottom: 2rem;
    position: relative;
  }

  /* Filter toggle buttons row */
  .filter-toggles {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: center;
  }

  /* Toggle button for mobile */
  .filter-toggle-btn {
    padding: 0.5rem 1rem;
    background-color: #f8f8f8;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 500;
    transition: all 0.2s ease;
  }

  .filter-toggle-btn .toggle-icon {
    margin-left: 8px;
    font-weight: bold;
  }

  .filter-toggle-btn:hover {
    background-color: #f0f0f0;
  }

  .filter-toggle-btn.active {
    background-color: #e6f2ff;
    border-color: #99ccff;
  }

  /* Clear filters button */
  .filter-clear-btn {
    background: transparent;
    border: none;
    color: #666;
    cursor: pointer;
    font-size: 0.9rem;
    text-decoration: underline;
    padding: 0.5rem;
  }

  .filter-clear-btn:hover {
    color: #333;
  }

  /* Filter panel - collapsed by default on mobile */
  .blog-filters {
    display: none;
    flex-direction: column;
    gap: 1.5rem;
    background-color: #f9f9f9;
    border-radius: 4px;
    padding: 1rem;
    margin-bottom: 1rem;
    border: 1px solid #eee;
  }

  /* When expanded */
  .blog-filters.expanded {
    display: flex;
  }

  /* Individual filter sections */
  .filter-section {
    margin-bottom: 1rem;
  }

  .filter-section h3 {
    margin-top: 0;
    margin-bottom: 0.75rem;
    font-size: 1.1rem;
    color: #333;
  }

  /* Category filters */
  .category-filter ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .category-filter li {
    margin-bottom: 0.5rem;
  }

  .category-filter a {
    color: #333;
    text-decoration: none;
    display: inline-block;
    padding: 0.3rem 0;
    font-size: 1rem;
  }

  /* Tag cloud */
  .tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .tag {
    background-color: #f0f0f0;
    padding: 0.5rem 0.75rem;
    border-radius: 4px;
    font-size: 0.9rem;
    color: #333;
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s ease;
  }

  /* Active state for filters */
  .category-filter a.active, .tag-filter a.active, .tag.active {
    font-weight: 600;
    color: #0066cc;
    position: relative;
  }

  .tag.active {
    background-color: #e6f2ff;
    border-color: #99ccff;
  }

  /* Count indicators */
  .count {
    font-size: 0.85em;
    color: #666;
    font-weight: normal;
  }

  /* Active filters display */
  .active-filters {
    display: none;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  /* Filter pills */
  .filter-pill {
    background-color: #e6f2ff;
    color: #0066cc;
    padding: 0.4rem 0.75rem;
    border-radius: 100px;
    display: inline-flex;
    align-items: center;
    font-size: 0.9rem;
  }

  .filter-pill .remove-filter {
    background: none;
    border: none;
    color: #0066cc;
    cursor: pointer;
    font-size: 1.1rem;
    margin-left: 0.4rem;
    line-height: 1;
  }

  /* Desktop styles */
  @media (min-width: 768px) {
    .blog-filters {
      display: flex;
      flex-direction: row;
    }

    .filter-toggle-btn {
      display: none;
    }

    .filter-section {
      flex: 1;
    }

    .tag {
      padding: 0.4rem 0.6rem;
    }
  }

  /* Ensure the blog list is responsive */
  .blog-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .blog-list li {
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
  }

  .blog-list a {
    color: #333;
    text-decoration: none;
    font-weight: 500;
    font-size: 1.1rem;
    display: block;
    margin-bottom: 0.25rem;
  }

  .blog-list a:hover {
    color: #0066cc;
  }

  .blog-date {
    color: #666;
    font-size: 0.9rem;
  }
</style>
"""

    # Check if we need to inject CSS
    if '<!-- CSS_PLACEHOLDER -->' in template:
        filled = template.replace('<!-- CSS_PLACEHOLDER -->', css_styles)
    else:
        filled = template.replace('</head>', f'{css_styles}\n</head>')

    # Inject post list
    if '<!-- POST_LIST goes here -->' in filled:
        filled = filled.replace('<!-- POST_LIST goes here -->', post_list)
    else:
        # Try to find the main content area and append
        main_tag = filled.find('<main')
        if main_tag != -1:
            end_main_tag = filled.find('</main>', main_tag)
            if end_main_tag != -1:
                filled = filled[:end_main_tag] + post_list + filled[end_main_tag:]
            else:
                print("⚠️ Could not find closing </main> tag. Appending to end of document.")
                filled = filled + "\n" + post_list
        else:
            print("⚠️ Could not find <main> tag. Appending to end of document.")
            filled = filled + "\n" + post_list

    # Inject CTA (if present)
    cta_html = ''
    if cta_html_file.exists():
        cta_html = cta_html_file.read_text(encoding='utf-8')

    if '<!-- CTA_PLACEHOLDER -->' in filled:
        filled = filled.replace('<!-- CTA_PLACEHOLDER -->', cta_html)

    # Append full footer just before </body>
    footer_html = ''
    if footer_file.exists():
        footer_html = footer_file.read_text(encoding='utf-8')

    final_html = filled.replace('</body>', f'{footer_html}\n</body>')

    # Write out
    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(final_html, encoding='utf-8')

    print(f"✅ Blog index generated at: {output_html}")
    print(f"📊 Listed {len(lines)} blog posts")


if __name__ == "__main__":
    main()
