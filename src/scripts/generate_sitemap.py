#!/usr/bin/env python3

import os
import re
from datetime import datetime
import argparse
from pathlib import Path
import xml.dom.minidom as minidom
import xml.etree.ElementTree as ET

# Default configuration
CONFIG = {
    "site_url": "https://common-sense.com",
    "output_file": "sitemap.xml",
    "static_dir": ".",
    "blog_dir": "blog",
    "exclude_patterns": [
        r"^\.git/.*",  # Git directory
        r"^\.DS_Store$",  # macOS files
        r"^Makefile$",  # Makefile
        r"^CLAUDE\.md$",  # Claude markdown file
        r"^\.gitignore$",  # Git ignore file
        r".*\.(md|m4|py|json|txt)$",  # Source files (excluding html files)
        r"^src/.*",  # Source directory
        r"^assets/.*\.(scss|less)$",  # Source SCSS/LESS files
        r"^node_modules/.*"  # Node modules
    ],
    "default_priority": {
        "home": 1.0,
        "main_pages": 0.8,
        "blog_index": 0.8,
        "service_pages": 0.7,
        "blog_posts": 0.6
    },
    "debug": False
}

def should_exclude(path, exclude_patterns, debug=False):
    """Check if path should be excluded based on patterns"""
    rel_path = path if isinstance(path, str) else str(path)
    
    for pattern in exclude_patterns:
        if re.search(pattern, rel_path):
            if debug:
                print(f"  Excluding {rel_path} (matched pattern: {pattern})")
            return True
    return False

def get_lastmod(file_path):
    """Get the last modification date of a file in YYYY-MM-DD format"""
    try:
        mtime = os.path.getmtime(file_path)
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    except Exception as e:
        if CONFIG["debug"]:
            print(f"  Error getting last modified date for {file_path}: {e}")
        return datetime.now().strftime("%Y-%m-%d")

def get_priority(url_path, config):
    """Determine priority based on URL path"""
    if url_path == "/" or url_path == "/index.html":
        return config["default_priority"]["home"]
    elif url_path == "/blog/index.html" or url_path == "/blog/":
        return config["default_priority"]["blog_index"]
    elif re.match(r"^/blog/.*", url_path):
        return config["default_priority"]["blog_posts"]
    elif re.match(r"^/.*\.(html|htm)$", url_path) and not re.match(r"^/assets/", url_path):
        if re.match(r"^/(about|contact)\.(html|htm)$", url_path):
            return config["default_priority"]["main_pages"]
        else:
            return config["default_priority"]["service_pages"]
    else:
        return 0.5  # Default for other files

def generate_sitemap(config):
    """Generate sitemap.xml from website directory structure"""
    print(f"Generating sitemap for {config['site_url']}...")
    debug = config["debug"]
    
    # Check if static_dir exists
    static_dir = Path(config["static_dir"])
    if not static_dir.exists():
        print(f"Error: Static directory '{static_dir}' does not exist!")
        return None
    
    # Create XML root element
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Track processed URLs to avoid duplicates
    processed_urls = set()
    
    if debug:
        print(f"Scanning directory: {static_dir}")
    
    # Get a list of all files to debug what we're finding
    if debug:
        all_files = []
        for root, _, files in os.walk(static_dir):
            for file in files:
                all_files.append(os.path.join(root, file))
        print(f"Found {len(all_files)} total files")
    
    # Process static files
    html_files_found = 0
    for root, dirs, files in os.walk(static_dir):
        # Create normalized path for comparison
        rel_root = os.path.relpath(root, static_dir)
        if rel_root == ".":
            rel_root = ""
            
        if debug:
            print(f"Processing directory: {rel_root or '/'}")
        
        # Skip excluded directories
        orig_dirs_len = len(dirs)
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(rel_root, d), config["exclude_patterns"], debug)]
        if debug and orig_dirs_len != len(dirs):
            print(f"  Skipped {orig_dirs_len - len(dirs)} excluded directories")
        
        for file in files:
            file_path = os.path.join(root, file)
            rel_file_path = os.path.join(rel_root, file)
            
            # Skip excluded files
            if should_exclude(rel_file_path, config["exclude_patterns"], debug):
                continue
            
            # Only include HTML files
            if not file.endswith(('.html', '.htm')):
                if debug:
                    print(f"  Skipping non-HTML file: {rel_file_path}")
                continue
            
            html_files_found += 1
            if debug:
                print(f"  Processing HTML file: {rel_file_path}")
            
            # Get relative path from website root
            rel_path = os.path.relpath(file_path, config["static_dir"])
            
            # Convert backslashes to forward slashes for URLs on all platforms
            url_path = "/" + rel_path.replace("\\", "/")
            
            # Handle index.html files
            if file == "index.html":
                # Convert /dir/index.html to /dir/
                url_path = os.path.dirname(url_path) + "/"
                if url_path == "//":  # Root index
                    url_path = "/"
            
            # Skip if URL was already processed
            if url_path in processed_urls:
                if debug:
                    print(f"  Skipping duplicate URL: {url_path}")
                continue
            
            if debug:
                print(f"  Adding URL: {url_path}")
                
            processed_urls.add(url_path)
            
            # Create URL element
            url_element = ET.SubElement(urlset, "url")
            
            # Add location
            loc = ET.SubElement(url_element, "loc")
            loc.text = config["site_url"] + url_path
            
            # Add last modified date
            lastmod = ET.SubElement(url_element, "lastmod")
            lastmod.text = get_lastmod(file_path)
            
            # Add priority
            priority = ET.SubElement(url_element, "priority")
            priority.text = str(get_priority(url_path, config))
    
    if debug:
        print(f"Found {html_files_found} HTML files, added {len(processed_urls)} unique URLs to sitemap")
    
    # If no URLs were processed, create a minimal sitemap with just the homepage
    if not processed_urls:
        print("Warning: No URLs were found. Creating a minimal sitemap with just the homepage.")
        
        # Add homepage
        url_element = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_element, "loc")
        loc.text = config["site_url"] + "/"
        lastmod = ET.SubElement(url_element, "lastmod")
        lastmod.text = datetime.now().strftime("%Y-%m-%d")
        priority = ET.SubElement(url_element, "priority")
        priority.text = str(config["default_priority"]["home"])
        
        # Add about.html if it exists
        about_file = os.path.join(static_dir, "about.html")
        if os.path.exists(about_file):
            url_element = ET.SubElement(urlset, "url")
            loc = ET.SubElement(url_element, "loc")
            loc.text = config["site_url"] + "/about.html"
            lastmod = ET.SubElement(url_element, "lastmod")
            lastmod.text = get_lastmod(about_file)
            priority = ET.SubElement(url_element, "priority")
            priority.text = str(config["default_priority"]["main_pages"])
    
    # Convert to pretty XML
    rough_string = ET.tostring(urlset, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    # Clean up pretty XML (remove empty lines)
    clean_lines = [line for line in pretty_xml.split('\n') if line.strip()]
    clean_xml = '\n'.join(clean_lines)
    
    # Write to file
    with open(config["output_file"], 'w', encoding='utf-8') as f:
        f.write(clean_xml)
    
    print(f"Generated sitemap with {len(processed_urls)} URLs")
    return config["output_file"]

def main():
    """Main entry point with command line argument parsing"""
    parser = argparse.ArgumentParser(description='Generate sitemap.xml for website')
    parser.add_argument('--site-url', help='Base URL for the website')
    parser.add_argument('--output-file', help='Output sitemap file path')
    parser.add_argument('--static-dir', help='Root directory for static files')
    parser.add_argument('--blog-dir', help='Directory containing blog files')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()
    
    # Update config from command line args
    if args.site_url:
        CONFIG["site_url"] = args.site_url
    if args.output_file:
        CONFIG["output_file"] = args.output_file
    if args.static_dir:
        CONFIG["static_dir"] = args.static_dir
    if args.blog_dir:
        CONFIG["blog_dir"] = args.blog_dir
    if args.debug:
        CONFIG["debug"] = True
    
    generate_sitemap(CONFIG)

if __name__ == "__main__":
    main()
