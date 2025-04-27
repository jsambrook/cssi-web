#!/usr/bin/env python3
"""
ai_news_rss_fetcher.py - Fetch recent AI news from RSS feeds

This script fetches AI news from reliable RSS feeds, filters for recent items,
and generates a JSON file with the latest news that can be incorporated into
the Claude AI news prompt.

Usage:
    ./ai_news_rss_fetcher.py [--days 30] [--output /path/to/output.json]
"""

import argparse
import datetime
import feedparser
import json
import re
import sys
import time
from dateutil import parser as date_parser
from pathlib import Path
from urllib.parse import urlparse

# List of reliable AI news RSS feeds
AI_RSS_FEEDS = [
    {
        "name": "The Verge AI",
        "url": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
        "source": "The Verge"
    },
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
        "source": "TechCrunch"
    },
    {
        "name": "VentureBeat AI",
        "url": "https://venturebeat.com/category/ai/feed/",
        "source": "VentureBeat"
    },
    {
        "name": "Wired AI",
        "url": "https://www.wired.com/feed/tag/artificial-intelligence/latest/rss",
        "source": "Wired"
    },
    {
        "name": "MIT Technology Review",
        "url": "https://www.technologyreview.com/feed/",
        "source": "MIT Technology Review"
    },
    {
        "name": "AI News",
        "url": "https://www.artificialintelligence-news.com/feed/",
        "source": "AI News"
    },
    {
        "name": "Ars Technica AI",
        "url": "https://arstechnica.com/tag/artificial-intelligence/feed/",
        "source": "Ars Technica"
    },
    {
        "name": "VB AI",
        "url": "https://venturebeat.com/ai/feed/",
        "source": "VentureBeat"
    }
]

def parse_args():
    parser = argparse.ArgumentParser(description="Fetch recent AI news from RSS feeds")
    parser.add_argument("--days", type=int, default=30, 
                        help="Number of days to look back for news (default: 30)")
    parser.add_argument("--output", default="recent_ai_news.json",
                        help="Path to output JSON file")
    parser.add_argument("--min-items", type=int, default=15,
                        help="Minimum number of news items to collect (default: 15)")
    return parser.parse_args()

def parse_feed_date(entry):
    """Extract and parse the publication date from a feed entry"""
    # Try common date fields
    for date_field in ['published', 'pubDate', 'updated', 'updated_parsed', 
                       'published_parsed', 'created']:
        if date_field in entry and entry[date_field]:
            try:
                # Handle both string dates and time structs
                if isinstance(entry[date_field], str):
                    date = date_parser.parse(entry[date_field])
                    return date.replace(tzinfo=None)  # Remove timezone to avoid comparison issues
                else:
                    # Assume it's a time struct
                    date = datetime.datetime.fromtimestamp(time.mktime(entry[date_field]))
                    return date.replace(tzinfo=None)  # Remove timezone to avoid comparison issues
            except Exception as e:
                print(f"      Error parsing date field '{date_field}': {e}")
                continue
                
    # If we get here, look in entry.get('dc_date')
    if 'dc_date' in entry and entry['dc_date']:
        try:
            date = date_parser.parse(entry['dc_date'])
            return date.replace(tzinfo=None)  # Remove timezone to avoid comparison issues
        except Exception as e:
            print(f"      Error parsing dc_date: {e}")
            pass
            
    # As a last resort, try to find a date in the title or description
    date_pattern = r'\b(20\d{2}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]20\d{2})\b'
    
    # Check title
    if 'title' in entry:
        date_match = re.search(date_pattern, entry['title'])
        if date_match:
            try:
                return date_parser.parse(date_match.group(0))
            except Exception:
                pass
                
    # Check description/summary
    for field in ['description', 'summary', 'content']:
        if field in entry and entry[field]:
            date_match = re.search(date_pattern, str(entry[field]))
            if date_match:
                try:
                    return date_parser.parse(date_match.group(0))
                except Exception:
                    continue
    
    # If all else fails, return None to indicate we couldn't determine the date
    return None

def extract_domain(url):
    """Extract domain from URL for source attribution"""
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # Remove www. prefix if present
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

def fetch_ai_news(days_back=30, min_items=15):
    """Fetch AI news items from RSS feeds, filtering for recent items"""
    today = datetime.datetime.now()
    cutoff_date = today - datetime.timedelta(days=days_back)
    
    all_recent_items = []
    
    print(f"🔍 Fetching AI news from {len(AI_RSS_FEEDS)} RSS feeds...")
    
    for feed_info in AI_RSS_FEEDS:
        try:
            print(f"  Fetching: {feed_info['name']} ({feed_info['url']})")
            feed = feedparser.parse(feed_info['url'])
            
            if not feed.entries:
                print(f"    ⚠️ No entries found in feed")
                continue
                
            recent_count = 0
            for entry in feed.entries:
                # Get publication date
                pub_date = parse_feed_date(entry)
                
                # Skip if we couldn't determine the date
                if not pub_date:
                    continue
                    
                # Skip if older than cutoff date
                if pub_date < cutoff_date:
                    continue
                
                # Extract needed information
                news_item = {
                    "title": entry.get('title', 'Unknown title'),
                    "link": entry.get('link', ''),
                    "date": pub_date.strftime('%Y-%m-%d'),
                    "source": feed_info.get('source', extract_domain(feed_info['url'])),
                    "summary": entry.get('summary', '')[:300]  # Truncate long summaries
                }
                
                # Clean up the summary (remove HTML)
                news_item['summary'] = re.sub(r'<[^>]+>', '', news_item['summary'])
                
                all_recent_items.append(news_item)
                recent_count += 1
            
            print(f"    ✅ Found {recent_count} recent items")
            
        except Exception as e:
            print(f"    ❌ Error fetching {feed_info['name']}: {e}")
    
    # Sort items by date (most recent first)
    all_recent_items.sort(key=lambda x: x['date'], reverse=True)
    
    # If we don't have enough items, relax the date constraint
    if len(all_recent_items) < min_items:
        print(f"⚠️ Only found {len(all_recent_items)} items, extending search period...")
        
        # To avoid infinite recursion, cap the maximum days back
        if days_back >= 180:  # 6 months is as far back as we'll go
            print(f"⚠️ Reached maximum search period of 180 days, returning what we have")
            return all_recent_items
            
        # Double the search period and try again
        return fetch_ai_news(days_back=days_back*2, min_items=min_items)
        
    print(f"✅ Found {len(all_recent_items)} total recent AI news items")
    return all_recent_items

def generate_news_json(items, output_path):
    """Generate a JSON file with the recent news items"""
    # Create categories for the news
    categories = {
        "large_language_models": [],
        "multimodal_ai": [],
        "generative_ai": [],
        "ai_applications": [],
        "ai_research": [],
        "ai_business": [],
        "ai_policy": []
    }
    
    # Categorize items based on keywords
    category_keywords = {
        "large_language_models": ["llm", "language model", "gpt", "claude", "llama", "bard", "mistral", "falcon"],
        "multimodal_ai": ["multimodal", "vision", "image", "audio", "video", "speech"],
        "generative_ai": ["generative", "generate", "diffusion", "stable diffusion", "midjourney", "dall-e"],
        "ai_applications": ["application", "chatbot", "assistant", "tool", "product", "launch"],
        "ai_research": ["research", "paper", "study", "algorithm", "hugging face", "model", "neural"],
        "ai_business": ["startup", "funding", "acquisition", "investment", "market", "company", "partnership"],
        "ai_policy": ["policy", "regulation", "law", "governance", "ethics", "safety", "eu", "congress"]
    }
    
    # Limit to 5 items per category
    max_per_category = 5
    
    # Categorize each item
    for item in items:
        # Combine title and summary for keyword matching
        text = (item.get('title', '') + ' ' + item.get('summary', '')).lower()
        
        # Check each category
        assigned = False
        for category, keywords in category_keywords.items():
            if len(categories[category]) >= max_per_category:
                continue
                
            for keyword in keywords:
                if keyword.lower() in text:
                    categories[category].append(item)
                    assigned = True
                    break
                    
            if assigned:
                break
                
        # If not assigned to any category, put in the smallest category
        if not assigned:
            smallest_category = min(categories.items(), key=lambda x: len(x[1]))[0]
            categories[smallest_category].append(item)
    
    # Create the output JSON
    output = {
        "fetch_date": datetime.datetime.now().isoformat(),
        "timeframe_days": args.days,
        "categories": {}
    }
    
    # Add categories with items to output
    for category, cat_items in categories.items():
        if cat_items:
            output["categories"][category] = cat_items
    
    # Also include a flat list of all items
    output["all_items"] = items[:30]  # Limit to top 30 overall
    
    # Write to file
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
        
    print(f"✅ AI news JSON saved to: {output_path}")
    
    # Print a summary
    print("\nSummary of recent AI news:")
    for category, cat_items in categories.items():
        if cat_items:
            print(f"  {category.replace('_', ' ').title()}: {len(cat_items)} items")
    
    return output_path

def main():
    args = parse_args()
    output_dir = Path(args.output).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Ensure today is timezone-naive to avoid comparison issues
        global today
        today = datetime.datetime.now().replace(tzinfo=None)
        
        # Fetch news
        items = fetch_ai_news(days_back=args.days, min_items=args.min_items)
        
        # If we found any items, generate JSON
        if items:
            json_path = generate_news_json(items, args.output)
            print(f"\n✅ Successfully saved {len(items)} news items to {json_path}")
        else:
            print("\n❌ No news items found, no JSON file generated")
            return 1
            
    except Exception as e:
        print(f"\n❌ Error: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return 1
        
    return 0

if __name__ == "__main__":
    args = parse_args()
    sys.exit(main())