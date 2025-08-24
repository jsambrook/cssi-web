#!/usr/bin/env python3

"""
Quick link checker for the blog index to identify potential 404s
"""

import os
import re
from pathlib import Path

def check_blog_links():
    """Check all links in the blog index for 404s"""
    blog_index = Path("blog/index.html")
    
    if not blog_index.exists():
        print(f"Blog index not found at {blog_index}")
        return False
    
    with open(blog_index, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all href links in the blog index
    href_pattern = r'href="([^"]*)"'
    links = re.findall(href_pattern, content)
    
    # Look for blog post links: either relative paths like "2025/08/..." or absolute paths with "/blog/"
    blog_links = [link for link in links if 
                  (('/blog/' in link and not link.startswith('http')) or 
                   (link.startswith(('2020/', '2021/', '2022/', '2023/', '2024/', '2025/')) and link.endswith('index.html')))]
    
    print(f"Checking {len(blog_links)} blog post links...")
    
    missing_links = []
    for link in blog_links:
        # Convert relative path to file system path
        if link.startswith('/'):
            file_path = Path('.' + link)
        else:
            # Relative link - prepend blog directory
            file_path = Path('blog') / link
        
        if not file_path.exists():
            missing_links.append((link, str(file_path)))
    
    if missing_links:
        print(f"\nFound {len(missing_links)} broken links:")
        for link, file_path in missing_links:
            print(f"  404: {link} -> {file_path}")
        return False
    else:
        print("✓ All blog links are valid!")
        return True

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    check_blog_links()