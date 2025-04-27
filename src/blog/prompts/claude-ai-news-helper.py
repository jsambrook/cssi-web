#!/usr/bin/env python3
"""
claude-ai-news-helper.py - A utility to help with AI news source verification

This script checks if the source URLs listed in claude-ai-news.txt are accessible
and provides additional suggestions for reliable sources.
"""

import subprocess
import re
import sys
import time
from urllib.parse import urlparse

def extract_urls_from_prompt(prompt_file):
    """Extract URLs from the AI news prompt file"""
    with open(prompt_file, 'r') as f:
        content = f.read()
    
    # Extract URLs using regex
    url_pattern = r'https?://[^\s)"]+'
    urls = re.findall(url_pattern, content)
    return urls

def verify_url(url, timeout=5):
    """Check if a URL is accessible using curl"""
    try:
        # First check if URL is well-formed
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            return False, "Invalid URL format"
        
        print(f"Checking: {url}")
        # Use curl to check URL validity
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        
        result = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L", 
             "-A", user_agent, "--max-time", str(timeout), url],
            capture_output=True,
            text=True
        )
        
        status_code = int(result.stdout.strip())
        
        if status_code < 400:
            print(f"✅ Valid: {url}")
            return True, f"HTTP Status: {status_code}"
        else:
            print(f"❌ Invalid: {url} - HTTP Status: {status_code}")
            return False, f"HTTP Status: {status_code}"
    except Exception as e:
        print(f"❌ Error: {url} - {str(e)}")
        return False, str(e)

def main():
    prompt_file = "../prompts/claude-ai-news.txt"
    
    print("AI News Source Validator")
    print("=======================")
    
    # Extract URLs from the prompt file
    urls = extract_urls_from_prompt(prompt_file)
    print(f"Found {len(urls)} URLs in the prompt file\n")
    
    # Verify each URL
    valid_count = 0
    invalid_count = 0
    invalid_urls = []
    
    for url in urls:
        is_valid, message = verify_url(url)
        if is_valid:
            valid_count += 1
        else:
            invalid_count += 1
            invalid_urls.append((url, message))
        
        # Avoid rate limiting
        time.sleep(0.5)
    
    # Print summary
    print("\nVerification Summary:")
    print(f"✅ Valid URLs: {valid_count}")
    print(f"❌ Invalid URLs: {invalid_count}")
    
    if invalid_urls:
        print("\nInvalid URLs:")
        for url, message in invalid_urls:
            print(f"❌ {url} - {message}")
        
        print("\nConsider replacing these invalid URLs in the prompt file.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())