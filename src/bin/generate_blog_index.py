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

def collect_categories_and_tags(posts, repo_root):
    """
    Extracts categories and tags from the blog posts.
    
    Returns a tuple of (categories, tags) where each is a dictionary mapping 
    the category/tag name to a count of posts.
    """
    categories = {}
    tags = {}
    
    for p in posts:
        # Read the actual post file to get categories and tags
        year, month, slug = p['year'], p['month'], p['slug']
        json_path = repo_root / 'src' / 'blog' / 'drafts' / f"{p['date']}-{slug}.json"
        
        if json_path.exists():
            try:
                post_data = json.loads(json_path.read_text(encoding='utf-8'))
                
                # Extract category
                category = post_data.get('metadata', {}).get('category')
                if category:
                    categories[category] = categories.get(category, 0) + 1
                
                # Extract tags
                post_tags = post_data.get('metadata', {}).get('tags', [])
                for tag in post_tags:
                    tags[tag] = tags.get(tag, 0) + 1
            except (json.JSONDecodeError, KeyError):
                # Skip if there's an issue with the JSON file
                continue
    
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
    
    # Collect categories and tags from posts
    categories, tags = collect_categories_and_tags(posts, repo_root)

    # Build list items only for posts whose HTML exists
    lines = []
    for p in posts:
        year, month, slug = p['year'], p['month'], p['slug']
        html_path = repo_root / 'blog' / year / month / f"{slug}.html"
        if not html_path.exists():
            continue
            
        # Get categories and tags for this post
        json_path = repo_root / 'src' / 'blog' / 'drafts' / f"{p['date']}-{slug}.json"
        post_category = ""
        post_tags = []
        
        if json_path.exists():
            try:
                post_data = json.loads(json_path.read_text(encoding='utf-8'))
                post_category = post_data.get('metadata', {}).get('category', "")
                post_tags = post_data.get('metadata', {}).get('tags', [])
            except (json.JSONDecodeError, KeyError):
                pass
        
        date_str = datetime.strptime(p['date'], "%Y-%m-%d").strftime("%B %d, %Y")
        href = f"/blog/{year}/{month}/{slug}.html"
        
        # Create list item with data attributes for filtering
        tag_attr = ",".join(post_tags) if post_tags else ""
        category_attr = post_category if post_category else ""
        
        lines.append(
            f'      <li data-categories="{category_attr}" data-tags="{tag_attr}">'
            f'<a href="{href}">{p["title"]}</a> <span class="blog-date">– {date_str}</span>'
            f'</li>'
        )

    # Create filter HTML if we have categories or tags
    filter_html = build_filter_section(categories, tags) if categories or tags else ""
    
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

    # Inject CSS
    filled = template.replace('</head>', f'{css_styles}\n</head>')
    
    # Inject post list
    filled = filled.replace('<!-- POST_LIST goes here -->', post_list)

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
