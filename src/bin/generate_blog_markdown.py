#!/usr/bin/env python3
"""
generate_blog_markdown.py

Takes a short meta-description and uses AI (OpenAI or Claude) to generate a
Markdown file for a blog article, using company context from a TXT file.

Today's real date is used consistently across metadata, filenames, and prompt content.

Also saves a .current_blog.md file pointing to the generated Markdown file.

Usage:
    ./generate_blog_markdown.py "How AI assistants help accountants manage client communication"
    ./generate_blog_markdown.py --prompt /path/to/prompt_file.txt "Blog topic"
    ./generate_blog_markdown.py --provider claude --model claude-3-sonnet-20240229 "Blog topic"
"""

import argparse
import os
import json
import requests
import subprocess
import re
from pathlib import Path
import datetime
import time
from urllib.parse import urlparse

# Import OpenAI conditionally to avoid hard dependency
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog article in Markdown from a meta-description using AI")
    parser.add_argument('description', help='Short meta-description of the blog post topic')
    parser.add_argument('--prompt', help='Path to a custom prompt template file')
    parser.add_argument('--context-file', default='../includes/common-sense-systems.txt', help='Path to company context file')
    parser.add_argument('--output-dir', default='../blog/drafts', help='Where to save the generated Markdown file')
    parser.add_argument('--provider', default='openai', choices=['openai', 'claude'], help='AI provider to use')
    parser.add_argument('--model', default='gpt-4-turbo', help='Model name (default: gpt-4-turbo for OpenAI, claude-3-sonnet-20240229 for Claude)')
    parser.add_argument('--skip-reference-check', action='store_true', help='Skip reference URL validation (faster but might include invalid links)')
    return parser.parse_args()

def build_prompt(description: str, context_md: str, today_str: str) -> str:
    return f"""
Today's date is {today_str}.

You are an expert in researching, writing, and business process
improvement and management and execution. Your job is writing
compelling blog articles for Common Sense Systems, Inc., usually known
more simply as "Common Sense."

Your goal is to create the most compelling blog articles that you can
for your readers. To do so, you consider all of the things that go
into the most high-performing blog articles.

The blog articles you write are backed up by research you do. You
write from a position of evidence and this comes through in the
articles you write. You don't make claims that aren't backed up in
some way unless they are extremely obvious and accepted by virtually
everyone in business.

You are writing for an audience of business owners, startup founders,
and other people that want to make a difference in the world in one
way or another.

They are, in general, busy, practical people that are looking for ways
to improve the satisfaction they get from operating their businesses
or being employed in the jobs they are in or for pursuing their
mission in life, whatever it may be.

Common Sense Systems, Inc. (or simply "Common Sense" when the context is clear) is in the business of providing these individuals with
compelling solutions that help them achieve their goals much more
easily through the use of AI and workflow automation.

The blog articles you write are typically between 800 and 1500 words
in length. They contain references to back up claims that you make.

When you write a blog post, you must return the article in Markdown format with YAML frontmatter.
The frontmatter must include these fields:
---
title: "An engaging title for the post"
description: "A 1-2 sentence summary of the post content"
date: "{today_str}"
author: "Common Sense Systems, Inc."
slug: "url-friendly-version-of-title"
tags: ["tag1", "tag2", "tag3"]
category: "AI for Business"
status: "draft"
---

After the frontmatter, write the full blog post in proper Markdown format:
1. Use ## for main section headings and ### for subsections
2. Use proper Markdown formatting for lists, emphasis, links, etc.
3. Include citations using [1], [2], etc. in the text
4. At the end of the post, include a section for references:
   ## References
   1. Reference title. Source name. Year. URL

Also include a section at the end for a featured image prompt:
## Image Prompt
Title: Title for the featured image
Description: A detailed description for generating an image that complements the post
Usage: Featured image for blog post

The article must:
- Appeal to busy professionals and small business owners
- Be fact-based and persuasive without exaggeration or hype
- Show the benefits of AI assistants without sounding like a sales pitch
- Use a small business scenario (e.g. massage therapist, real estate agent, accountant)
- Be properly formatted in Markdown with good structure and readability
- Use realistic data and examples that would apply to actual businesses

Today's description is:
"{description}"

You may use the following company context when writing the blog post:

{context_md}
"""


def call_ai(prompt: str, provider: str, model: str) -> str:
    """Call AI using the specified provider and model"""

    # For OpenAI
    if provider == 'openai':
        if not OPENAI_AVAILABLE:
            raise ImportError("OpenAI package not installed. Install with: pip install openai")

        openai.api_key = os.getenv('OPENAI_API_KEY')
        if not openai.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")

        # Support for both new and old OpenAI Python library
        if hasattr(openai, 'chat'):
            # New API style (v1.0+)
            response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a Markdown-generating assistant for business blog posts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        else:
            # Legacy API style (pre-v1.0)
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a Markdown-generating assistant for business blog posts."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content

    # For Claude
    elif provider == 'claude':
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        # If no model specified, use a default Claude model
        if model == 'gpt-4-turbo':  # This is the default in the arg parser
            model = 'claude-3-sonnet-20240229'

        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }

        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 4000,
            "temperature": 0.7
        }

        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )

        if response.status_code != 200:
            raise Exception(f"Claude API error: {response.status_code}\n{response.text}")

        response_json = response.json()

        try:
            return response_json["content"][0]["text"]
        except (KeyError, IndexError) as e:
            print(f"Error parsing Claude response: {e}")
            print(f"Response structure: {response_json.keys()}")

            # Try alternative response format (Claude API might change)
            if "completion" in response_json:
                return response_json["completion"]
            elif "response" in response_json:
                return response_json["response"]
            else:
                print(f"Full response: {response_json}")
                raise ValueError(f"Could not extract text from Claude response: {e}")

    else:
        raise ValueError(f"Unknown provider: {provider}")


def verify_url(url, timeout=5):
    """Check if a URL is accessible using curl with more thorough validation"""
    try:
        # First check if URL is well-formed
        parsed = urlparse(url)
        if not all([parsed.scheme, parsed.netloc]):
            return False, "Invalid URL format"

        # Check for common issues in URLs
        if parsed.scheme not in ['http', 'https']:
            return False, "Invalid URL scheme (must be http or https)"

        # Check for unusual characters that might cause issues
        if any(c in url for c in [' ', '"', "'", '<', '>', '{', '}', '|', '\\', '^', '`']):
            return False, "URL contains invalid characters"

        # Reject localhost, IP addresses, and suspicious domains
        domain = parsed.netloc.lower()
        if (domain.startswith('localhost') or
            domain == '127.0.0.1' or
            domain.startswith('192.168.') or
            domain.startswith('10.') or
            domain.endswith('.local')):
            return False, "URL points to local or private address"

        # Validate common URL patterns and detect potentially unstable pages
        if re.search(r'temporary|temp|tmp', url.lower()):
            return False, "URL appears to be a temporary resource"

        # Use curl to check URL validity - more reliable than Python requests for some sites
        # Add user agent to avoid being blocked
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

        result = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "-A", user_agent, "--max-time", str(timeout), url],
            capture_output=True,
            text=True
        )

        status_code = int(result.stdout.strip())

        # Check specifically for common error codes
        if status_code == 404:
            return False, "Page not found (404)"
        elif status_code == 403:
            return False, "Access forbidden (403)"
        elif status_code == 401:
            return False, "Authentication required (401)"
        elif status_code == 429:
            return False, "Too many requests (429)"
        elif status_code >= 500:
            return False, f"Server error ({status_code})"
        elif status_code >= 400:
            return False, f"Client error ({status_code})"

        return status_code < 400, f"HTTP Status: {status_code}"
    except Exception as e:
        return False, str(e)


def is_ai_related(text):
    """Check if text appears to be related to AI, ML, or similar technologies"""
    ai_keywords = [
        'ai', 'artificial intelligence', 'machine learning', 'ml', 'deep learning',
        'neural network', 'nlp', 'natural language processing', 'computer vision',
        'chatbot', 'language model', 'llm', 'gpt', 'claude', 'automation', 'robotics',
        'data science', 'predictive analytics', 'algorithm'
    ]

    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ai_keywords)


def extract_yaml_frontmatter(markdown_text):
    """Extract and parse YAML frontmatter from markdown text"""
    if markdown_text.startswith('---'):
        end_marker = markdown_text.find('---', 3)
        if end_marker != -1:
            frontmatter = markdown_text[3:end_marker].strip()
            # Basic YAML parsing (for simple frontmatter without complex nesting)
            metadata = {}
            lines = frontmatter.split('\n')
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()

                    # Handle lists in YAML (e.g., tags: ["tag1", "tag2"])
                    if value.startswith('[') and value.endswith(']'):
                        # Very simple parsing for list values
                        items = value[1:-1].split(',')
                        value = [item.strip().strip('"\'') for item in items]
                    elif value.startswith('"') and value.endswith('"'):
                        # Remove quotes from quoted strings
                        value = value[1:-1]

                    metadata[key] = value

            return metadata

    return {}


def extract_references(markdown_text):
    """Extract references from markdown text"""
    references = []

    # Look for the References section
    ref_section_match = re.search(r'##\s*References\s*\n(.*?)(\n##|$)', markdown_text, re.DOTALL)

    if ref_section_match:
        ref_section = ref_section_match.group(1)

        # Extract each reference entry
        ref_pattern = r'(\d+)\.\s*(.*?)(?=\n\d+\.|$)'
        ref_matches = re.findall(ref_pattern, ref_section, re.DOTALL)

        for ref_id, ref_content in ref_matches:
            ref_id = int(ref_id)
            ref_content = ref_content.strip()

            # Try to extract the components (title, source, year, url)
            url_match = re.search(r'https?://[^\s]+', ref_content)
            url = url_match.group(0) if url_match else ""

            # Remove the URL from content for further processing
            if url:
                ref_content = ref_content.replace(url, "").strip()

            # Try to extract year (4 consecutive digits)
            year_match = re.search(r'\b(19\d\d|20\d\d)\b', ref_content)
            year = year_match.group(1) if year_match else ""

            # Remove year from content if found
            if year:
                ref_content = ref_content.replace(year, "").strip()

            # Split remaining content into title and source
            parts = ref_content.split('.')
            if len(parts) >= 2:
                title = parts[0].strip()
                source = '.'.join(parts[1:]).strip()
            else:
                title = ref_content
                source = ""

            # Remove trailing dots and spaces
            title = title.rstrip('.')
            source = source.rstrip('.')

            reference = {
                "id": ref_id,
                "title": title,
                "source": source,
                "year": year,
                "url": url
            }

            references.append(reference)

    return references


def extract_image_prompt(markdown_text):
    """Extract image prompt section from markdown text"""
    image_prompt = {}

    # Look for the Image Prompt section
    prompt_section_match = re.search(r'##\s*Image\s*Prompt\s*\n(.*?)($)', markdown_text, re.DOTALL)

    if prompt_section_match:
        prompt_section = prompt_section_match.group(1)

        # Extract title
        title_match = re.search(r'Title:\s*(.*?)(?=\n|$)', prompt_section)
        if title_match:
            image_prompt['title'] = title_match.group(1).strip()

        # Extract description
        desc_match = re.search(r'Description:\s*(.*?)(?=\nUsage:|$)', prompt_section, re.DOTALL)
        if desc_match:
            image_prompt['description'] = desc_match.group(1).strip()

        # Extract usage
        usage_match = re.search(r'Usage:\s*(.*?)(?=\n|$)', prompt_section)
        if usage_match:
            image_prompt['usage'] = usage_match.group(1).strip()

    return image_prompt


def verify_references(references):
    """Verify references and check URLs"""
    valid_refs = []
    invalid_refs = []

    print("🔍 Verifying reference URLs and recency...")

    for ref in references:
        ref_id = ref.get("id")
        url = ref.get("url", "")

        if not url:
            print(f"  ⚠️ Warning: Reference [{ref_id}] has no URL")
            invalid_refs.append(ref)
            continue

        # Check recency for AI-related content
        year_str = ref.get("year", "")
        ref_is_ai_related = is_ai_related(ref.get("title", "")) or is_ai_related(ref.get("source", ""))

        if ref_is_ai_related and year_str and year_str.isdigit():
            year = int(year_str)
            if year < 2022:
                print(f"  ⚠️ Outdated: Reference [{ref_id}] from {year} is too old for AI content")
                ref["outdated"] = True

        # Verify URL
        print(f"  Checking: [{ref_id}] {url}")
        is_valid, message = verify_url(url)

        if is_valid:
            print(f"  ✅ Valid: {url}")
            valid_refs.append(ref)
        else:
            print(f"  ❌ Invalid: {url} - {message}")
            invalid_refs.append(ref)

    print(f"📊 References summary: {len(valid_refs)} valid, {len(invalid_refs)} invalid")
    return valid_refs, invalid_refs


def replace_invalid_references(markdown_text, invalid_refs):
    """Modify markdown text to indicate invalid references"""
    modified_text = markdown_text

    # Add a note about invalid references at the end of the references section
    if invalid_refs:
        ref_section_match = re.search(r'(##\s*References\s*\n.*?)(\n##|$)', markdown_text, re.DOTALL)
        if ref_section_match:
            ref_section = ref_section_match.group(1)
            end_position = ref_section_match.end(1)

            invalid_ids = [str(ref["id"]) for ref in invalid_refs]
            note = f"\n\n**Note**: References {', '.join(invalid_ids)} need verification. URLs may be inaccessible or outdated."

            # Insert the note at the end of the references section
            modified_text = markdown_text[:end_position] + note + markdown_text[end_position:]

    return modified_text


def process_custom_prompt(prompt_template: str, description: str, context_md: str, today_str: str) -> str:
    """Process a custom prompt template by replacing placeholders with actual values"""
    # Define standard replacement mappings
    replacements = {
        '{description}': description,
        '{today_str}': today_str,
        '{context_md}': context_md,
        '{date}': today_str,
        '{company}': 'Common Sense Systems, Inc.',
        '{company_short}': 'Common Sense',
        '{{ topic }}': description,
        '{{ date }}': today_str,
        '{{ tags }}': '"AI", "Business", "Automation"',  # Default tags if not specified
        '{{ category }}': '"AI for Business"',  # Default category
        '{{ small_business_example }}': 'small business',  # Default example
        '{{ company }}': 'Common Sense Systems, Inc.',
        '{{ company_short }}': 'Common Sense',
        '{{ days }}': '30'  # Default days for news
    }

    # Handle special case for recent news from RSS feed
    if '{{ recent_news }}' in prompt_template:
        # Check if we have recent AI news from the RSS fetcher
        news_json_path = Path(__file__).resolve().parent.parent / "blog" / "prompts" / "recent_ai_news.json"

        # If we don't have the news or it's older than 6 hours, try to generate it
        if not news_json_path.exists() or (time.time() - news_json_path.stat().st_mtime > 6 * 3600):
            try:
                print("📰 Fetching recent AI news from RSS feeds...")
                rss_fetcher_path = Path(__file__).resolve().parent.parent / "blog" / "prompts" / "ai_news_rss_fetcher.py"

                if rss_fetcher_path.exists():
                    subprocess.run([str(rss_fetcher_path)], check=True)
                    print("✅ RSS news fetched successfully")
                else:
                    print(f"⚠️ RSS fetcher script not found at {rss_fetcher_path}")
            except Exception as e:
                print(f"❌ Error fetching RSS news: {e}")

        # Load news items from json if it exists
        if news_json_path.exists():
            try:
                with open(news_json_path, 'r') as f:
                    news_data = json.load(f)

                # Format news data as a nice markdown list for the prompt
                news_md = "## Recent News Items:\n\n"

                # Add categorized news items
                for category, items in news_data.get("categories", {}).items():
                    news_md += f"### {category.replace('_', ' ').title()} News:\n\n"
                    for item in items[:5]:  # Limit to 5 items per category
                        news_md += f"- **{item['title']}** ({item['date']}, {item['source']})\n"
                        news_md += f"  {item['summary'][:150]}...\n"
                        news_md += f"  Source: {item['link']}\n\n"
                    news_md += "\n"

                replacements['{{ recent_news }}'] = news_md
                replacements['{{ days }}'] = str(news_data.get("timeframe_days", 30))

                print(f"✅ Incorporated {len(news_data.get('all_items', []))} recent news items into prompt")
            except Exception as e:
                print(f"❌ Error loading RSS news data: {e}")
                replacements['{{ recent_news }}'] = "*No recent news data available*"
        else:
            replacements['{{ recent_news }}'] = "*No recent news data available*"

    # Apply all replacements
    result = prompt_template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)

    return result


def save_blog_metadata(metadata, references, image_prompt):
    """Save blog metadata in JSON format for future reference"""
    blog_data = {
        "metadata": metadata,
        "references": references,
        "image": image_prompt
    }
    return blog_data


def main():
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent

    # Resolve paths
    context_path = (script_dir / args.context_file).resolve()
    output_dir = (script_dir / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get today's real date
    today = datetime.date.today()
    today_str = today.isoformat()  # '2025-04-25'
    year_str = today.strftime('%Y')
    month_str = today.strftime('%m')

    # Read context
    with open(context_path, 'r') as f:
        context_md = f.read()

    # Build prompt - either custom or default
    if args.prompt:
        prompt_path = Path(args.prompt).resolve()
        if not prompt_path.exists():
            raise FileNotFoundError(f"Custom prompt file not found: {prompt_path}")

        with open(prompt_path, 'r') as f:
            prompt_template = f.read()

        # Process the custom prompt with all possible placeholders
        prompt = process_custom_prompt(prompt_template, args.description, context_md, today_str)
    else:
        prompt = build_prompt(args.description, context_md, today_str)

    # Determine provider-specific message
    provider_name = "OpenAI" if args.provider == "openai" else "Claude"
    print(f"📡 Sending request to {provider_name}...")

    # Call the appropriate AI provider
    markdown_response = call_ai(prompt, provider=args.provider, model=args.model)

    # Extract metadata, references, and image prompt from the Markdown
    metadata = extract_yaml_frontmatter(markdown_response)
    references = extract_references(markdown_response)
    image_prompt = extract_image_prompt(markdown_response)

    # Ensure metadata has required fields
    metadata.setdefault('title', f"Blog Post: {args.description}")
    metadata.setdefault('date', today_str)
    metadata.setdefault('author', "Common Sense Systems, Inc.")

    # Generate slug if not present
    if 'slug' not in metadata:
        # Create a slug from title (lowercase, replace spaces with hyphens, remove special chars)
        title = metadata.get('title', args.description)
        slug = re.sub(r'[^a-z0-9-]', '', title.lower().replace(' ', '-'))
        metadata['slug'] = slug

    # Add year and month to metadata
    metadata['year'] = year_str
    metadata['month'] = month_str

    # Verify references if needed
    if not args.skip_reference_check and references:
        valid_refs, invalid_refs = verify_references(references)

        # Modify the markdown if there are invalid references
        if invalid_refs:
            markdown_response = replace_invalid_references(markdown_response, invalid_refs)

    # Build output filename
    slug = metadata['slug']
    output_file = output_dir / f"{today_str}-{slug}.md"

    # Save the markdown
    with open(output_file, 'w') as f:
        f.write(markdown_response)

    print(f"✅ Blog Markdown saved to: {output_file}")

    # Save blog metadata for future reference
    metadata_file = output_dir / f"{today_str}-{slug}.json"
    with open(metadata_file, 'w') as f:
        json.dump(save_blog_metadata(metadata, references, image_prompt), f, indent=2)

    print(f"✅ Blog metadata saved to: {metadata_file}")

    # Save pointer to current blog markdown
    pointer_file = output_dir / '.current_blog.md'
    with open(pointer_file, 'w') as f:
        f.write(f"{output_file.name}\n")
    print(f"🧭 Pointer file updated at: {pointer_file}")


if __name__ == '__main__':
    main()
