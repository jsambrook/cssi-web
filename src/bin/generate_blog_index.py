#!/usr/bin/env python3
"""
generate_blog_index.py

Generates a comprehensive blog index page by:
1. Scanning the blog directory for HTML files
2. Extracting metadata from corresponding JSON files
3. Creating a filtered, categorized, and tagged index
4. Generating the blog/index.html file with proper styling and filtering

This script is designed to be robust against various issues and can handle
missing or malformed metadata gracefully.
"""

import json
import re
import os
from pathlib import Path
from datetime import datetime


def extract_title_from_html(html_path):
    """Extract the title from an HTML file if metadata is missing"""
    try:
        content = html_path.read_text(encoding='utf-8')
        # Look for the title tag
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            return title_match.group(1).replace(' - Common Sense Systems, Inc.', '').strip()

        # Look for h1 tag
        h1_match = re.search(r'<h1>(.*?)</h1>', content)
        if h1_match:
            return h1_match.group(1).strip()

        # Fall back to filename
        return html_path.stem.replace('-', ' ').title()
    except Exception:
        return html_path.stem.replace('-', ' ').title()


def get_post_metadata(html_path, repo_root):
    """Get metadata for a blog post from multiple potential sources"""
    # Start with basic metadata from the path
    year = html_path.parent.name  # Month directory
    month = html_path.parent.parent.name  # Year directory
    slug = html_path.stem

    # Default metadata
    metadata = {
        "title": slug.replace('-', ' ').title(),
        "slug": slug,
        "date": f"{year}-{month}-01",  # Default to first of month if no exact date
        "year": year,
        "month": month,
        "category": "Uncategorized",
        "tags": []
    }

    # Check for metadata sources in this order:
    # 1. Look for JSON file in drafts with same date-slug pattern
    # 2. Look for any JSON file with matching slug
    # 3. Extract title from HTML if nothing else works

    # Search for JSON files in drafts directory with matching patterns
    drafts_dir = repo_root / "src" / "blog" / "drafts"
    if drafts_dir.exists():
        # First try to find exact match with date pattern
        for json_file in drafts_dir.glob(f"*-{slug}.json"):
            try:
                data = json.loads(json_file.read_text(encoding='utf-8'))

                # Handle different JSON structures
                if "metadata" in data:
                    # New format with metadata key
                    metadata.update(data["metadata"])
                    return metadata
                elif "content" in data or "content_html" in data:
                    # Old format with inline metadata
                    for key in ["title", "slug", "date", "author", "category", "tags"]:
                        if key in data:
                            metadata[key] = data[key]
                    return metadata
                else:
                    # Assume whole file is metadata
                    metadata.update(data)
                    return metadata
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue

    # If we got here, we need to extract the title from the HTML
    metadata["title"] = extract_title_from_html(html_path)

    return metadata


def collect_categories_and_tags(posts):
    """Collect unique categories and tags with their post counts"""
    categories = {}
    tags = {}

    for post in posts:
        # Process category
        category = post.get("category", "Uncategorized")
        categories[category] = categories.get(category, 0) + 1

        # Process tags
        post_tags = post.get("tags", [])
        if isinstance(post_tags, str):
            # Handle comma-separated string format
            post_tags = [tag.strip() for tag in post_tags.split(",")]

        for tag in post_tags:
            tag_str = str(tag).strip('"\'[]')
            if tag_str:  # Skip empty tags
                tags[tag_str] = tags.get(tag_str, 0) + 1

    return categories, tags


def format_date(date_str):
    """Format a date string from YYYY-MM-DD to Month DD, YYYY"""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return date_str


def build_filter_section(categories, tags):
    """Generate HTML for the filter UI if categories or tags exist"""
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

    return html


def generate_filter_javascript():
    """Generate the JavaScript for the filter UI"""
    return """
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Toggle filter panel visibility
  const toggleBtn = document.getElementById('toggle-filters');
  const filterPanel = document.getElementById('filter-panel');
  const activeFilters = document.getElementById('active-filters');

  // Initialize active filters state
  let activeFiltersState = {
    category: null,
    tags: []
  };

  // Toggle filter panel
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function() {
      filterPanel.classList.toggle('expanded');
      this.classList.toggle('active');

      // Toggle icon
      const icon = this.querySelector('.toggle-icon');
      icon.textContent = filterPanel.classList.contains('expanded') ? '−' : '+';
    });
  }

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
  if (activeFilters) {
    activeFilters.addEventListener('click', function(e) {
      if (e.target.classList.contains('remove-filter')) {
        const type = e.target.getAttribute('data-type');
        const value = e.target.getAttribute('data-value');

        if (type === 'category') {
          activeFiltersState.category = null;
          document.querySelectorAll('.category-filter a').forEach(a => a.classList.remove('active'));
        } else if (type === 'tag') {
          activeFiltersState.tags = activeFiltersState.tags.filter(t => t !== value);
          const tagLink = document.querySelector(`.tag-filter a[data-tag="${value}"]`);
          if (tagLink) tagLink.classList.remove('active');
        }

        updateActiveFiltersUI();
        applyAllFilters();
      }
    });
  }

  // Clear filters button
  const clearBtn = document.getElementById('clear-filters');
  if (clearBtn) {
    clearBtn.addEventListener('click', function(e) {
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
  }

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

  // Initialize from URL parameters
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


def generate_filter_css():
    """Generate the CSS for the filter UI"""
    return """
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

  /* Blog list styling */
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


def create_default_template():
    """Create a default blog index template if none exists"""
    return """<!DOCTYPE html>
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
</html>"""


def main():
    # Locate script and repo root
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    # Define paths
    blog_dir = repo_root / "blog"
    template_path = repo_root / "src" / "includes" / "blog_index_template.html"
    cta_path = repo_root / "src" / "includes" / "blog_cta.html"
    footer_path = repo_root / "src" / "includes" / "site_footer.html"
    index_json_path = repo_root / "src" / "blog" / "blog_index.json"
    output_path = blog_dir / "index.html"

    # Ensure blog directory exists
    blog_dir.mkdir(parents=True, exist_ok=True)

    # Create template if it doesn't exist
    if not template_path.exists():
        print(f"Creating default template at {template_path}")
        template_path.parent.mkdir(parents=True, exist_ok=True)
        template_path.write_text(create_default_template(), encoding='utf-8')

    # Load index.json if it exists
    if index_json_path.exists():
        try:
            data = json.loads(index_json_path.read_text(encoding='utf-8'))
            index_posts = data.get("posts", [])
        except (json.JSONDecodeError, UnicodeDecodeError):
            print(f"Warning: Invalid JSON in {index_json_path}. Creating new index.")
            index_posts = []
    else:
        index_posts = []

    # Find all HTML files in the blog directory
    html_files = []
    for year_dir in blog_dir.glob("[0-9][0-9][0-9][0-9]"):
        if year_dir.is_dir():
            for month_dir in year_dir.glob("[0-9][0-9]"):
                if month_dir.is_dir():
                    for html_file in month_dir.glob("*.html"):
                        # Skip index.html files
                        if html_file.name != "index.html":
                            html_files.append(html_file)

    # Build complete posts list
    all_posts = []

    # First add posts from the index that have HTML files
    for post in index_posts:
        year = post.get("year", "")
        month = post.get("month", "")
        slug = post.get("slug", "")

        if not year or not month or not slug:
            continue

        html_path = blog_dir / year / month / f"{slug}.html"

        if html_path.exists() and html_path in html_files:
            # This post exists and is in the index
            all_posts.append(post)
            html_files.remove(html_path)  # Remove from list to avoid duplicates

    # Now process any HTML files not in the index
    for html_path in html_files:
        metadata = get_post_metadata(html_path, repo_root)
        all_posts.append(metadata)

    # Sort posts by date (newest first)
    all_posts = sorted(all_posts, key=lambda p: p.get("date", ""), reverse=True)

    # Update the index.json file
    index_json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_json_path, 'w', encoding='utf-8') as f:
        json.dump({"posts": all_posts}, f, indent=2)

    print(f"Updated blog index metadata at {index_json_path}")

    # Collect categories and tags
    categories, tags = collect_categories_and_tags(all_posts)

    # Build list items for the HTML index
    post_items = []
    for post in all_posts:
        title = post.get("title", "Untitled")
        date = post.get("date", "")
        year = post.get("year", "")
        month = post.get("month", "")
        slug = post.get("slug", "")
        category = post.get("category", "Uncategorized")

        # Handle tags in different formats
        post_tags = post.get("tags", [])
        if isinstance(post_tags, str):
            # Handle comma-separated string format
            tag_list = [tag.strip() for tag in post_tags.split(",")]
        else:
            tag_list = post_tags

        # Create tag string for data attribute
        tag_attr = ",".join(str(tag).strip('"\'[]') for tag in tag_list)

        # Format date
        formatted_date = format_date(date)

        # Build HTML
        post_items.append(
            f'      <li data-categories="{category}" data-tags="{tag_attr}">'
            f'<a href="/blog/{year}/{month}/{slug}.html">{title}</a> '
            f'<span class="blog-date">– {formatted_date}</span>'
            f'</li>'
        )

    # Build filter section if we have categories or tags
    filter_html = build_filter_section(categories, tags) if categories or tags else ""

    # Combine filter and post list
    post_list_html = (
        f'{filter_html}\n'
        '<ul class="blog-list">\n'
        + "\n".join(post_items) +
        "\n    </ul>"
    )

    # Read the template
    template = template_path.read_text(encoding='utf-8')

    # Add CSS styles
    if '<!-- CSS_PLACEHOLDER -->' in template:
        filled = template.replace('<!-- CSS_PLACEHOLDER -->', generate_filter_css())
    else:
        filled = template.replace('</head>', f'{generate_filter_css()}\n</head>')

    # Add JavaScript before closing body tag
    filled = filled.replace('</body>', f'{generate_filter_javascript()}\n</body>')

    # Add post list
    if '<!-- POST_LIST goes here -->' in filled:
        filled = filled.replace('<!-- POST_LIST goes here -->', post_list_html)
    else:
        # Try to find a suitable location
        main_tag = filled.find('<main')
        if main_tag != -1:
            end_main_tag = filled.find('</main>', main_tag)
            if end_main_tag != -1:
                # Find the end of the first h1 tag after main
                h1_start = filled.find('<h1', main_tag, end_main_tag)
                if h1_start != -1:
                    h1_end = filled.find('</h1>', h1_start, end_main_tag)
                    if h1_end != -1:
                        # Insert after the h1
                        filled = filled[:h1_end + 5] + '\n' + post_list_html + filled[h1_end + 5:]
                    else:
                        # Fall back to inserting at the end of main
                        filled = filled[:end_main_tag] + '\n' + post_list_html + filled[end_main_tag:]
                else:
                    # Fall back to inserting at the end of main
                    filled = filled[:end_main_tag] + '\n' + post_list_html + filled[end_main_tag:]
            else:
                # Fall back to inserting at the end of the document
                filled = filled + '\n' + post_list_html
        else:
            # Fall back to inserting at the end of the document
            filled = filled + '\n' + post_list_html

    # Add CTA (if present)
    cta_html = ''
    if cta_path.exists():
        cta_html = cta_path.read_text(encoding='utf-8')

    if '<!-- CTA_PLACEHOLDER -->' in filled:
        filled = filled.replace('<!-- CTA_PLACEHOLDER -->', cta_html)

    # Add footer (if present)
    footer_html = ''
    if footer_path.exists():
        footer_html = footer_path.read_text(encoding='utf-8')

    final_html = filled.replace('</body>', f'{footer_html}\n</body>')

    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"✅ Blog index generated at: {output_path}")
    print(f"📊 Listed {len(post_items)} blog posts")


if __name__ == "__main__":
    main()
