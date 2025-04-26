#!/usr/bin/env python3
"""
generate_blog_json.py

Takes a short meta-description and uses AI (OpenAI or Claude) to generate a JSON representation
of a full blog article and image prompt, using company context from a TXT file.

Today's real date is used consistently across metadata, filenames, and prompt content.

Also saves a .current_blog.json file pointing to the generated JSON file.

Usage:
    ./generate_blog_json.py "How AI assistants help accountants manage client communication"
    ./generate_blog_json.py --prompt /path/to/prompt_file.txt "Blog topic"
    ./generate_blog_json.py --provider claude --model claude-3-sonnet-20240229 "Blog topic"
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
    parser = argparse.ArgumentParser(description="Generate blog article JSON from a meta-description using AI")
    parser.add_argument('description', help='Short meta-description of the blog post topic')
    parser.add_argument('--prompt', help='Path to a custom prompt template file')
    parser.add_argument('--context-file', default='../includes/common-sense-systems.txt', help='Path to company context file')
    parser.add_argument('--output-dir', default='../blog/drafts', help='Where to save the generated JSON file')
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
write from a position of evidence And this comes through in the
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

When you write a blog article, you return the article in a JSON
representation. That representation contains the article itself And a
prompt for an image generator that will generate marketing images to
go with the blog article.

The JSON you write must match this structure exactly:

{{
  "metadata": {{
    "title": "...",
    "slug": "...",
    "author": "Common Sense Systems, Inc.",
    "date": "{today_str}",
    "tags": ["tag1", "tag2", ...],
    "category": "AI for Business",
    "status": "draft",
    "year": "YYYY",
    "month": "MM"
  }},
  "content_html": {{
    "introduction": "<p>...</p>",
    "body": "<h2>...</h2><p>...</p>",
    "conclusion": "<h2>...</h2><p>...</p>"
  }},
  "graphics_prompt": {{
    "title": "...",
    "description": "...",
    "usage": "..."
  }}
}}

The article must:
- Appeal to busy professionals and small business owners
- Be fact-based and persuasive without exaggeration or hype
- Show the benefits of AI assistants without sounding like a sales pitch
- Use a small business scenario (e.g. massage therapist, real estate agent, accountant)

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
                    {"role": "system", "content": "You are a JSON-generating assistant for business blog posts."},
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
                    {"role": "system", "content": "You are a JSON-generating assistant for business blog posts."},
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
            
        return response.json()["content"][0]["text"]
    
    else:
        raise ValueError(f"Unknown provider: {provider}")
        
def call_openai(prompt: str, model: str) -> str:
    """Legacy function for backward compatibility"""
    return call_ai(prompt, provider='openai', model=model)


def clean_openai_response(text: str) -> str:
    """Remove code fences from OpenAI JSON responses if present"""
    if text.startswith("```json"):
        text = text.lstrip("```json").strip()
    if text.startswith("```"):
        text = text.lstrip("```").strip()
    if text.endswith("```"):
        text = text.rstrip("```").strip()
    return text


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

def extract_and_verify_references(blog_json):
    """Extract references from the blog JSON and verify their URLs and recency"""
    valid_refs = []
    invalid_refs = []
    citations_in_text = []
    
    # Determine if the blog post is AI-related
    is_blog_ai_related = False
    
    title = blog_json.get("metadata", {}).get("title", "")
    tags = blog_json.get("metadata", {}).get("tags", [])
    
    # Check if title or tags suggest AI content
    if is_ai_related(title) or any(is_ai_related(tag) for tag in tags):
        is_blog_ai_related = True
        print("ℹ️ This appears to be an AI-related blog post; enforcing recency requirements")
    
    # Check if the blog post has references
    if "references" in blog_json and blog_json["references"]:
        print("🔍 Verifying reference URLs and recency...")
        
        # Find all citation patterns in the content to track which ones are used
        content_text = ""
        # Add introduction text
        if "introduction" in blog_json.get("content", {}):
            content_text += blog_json["content"]["introduction"] + " "
            
        # Add body text from all sections
        for section in blog_json.get("content", {}).get("body", []):
            for para in section.get("paragraphs", []):
                content_text += para + " "
                
        # Add conclusion
        if "conclusion" in blog_json.get("content", {}):
            content_text += blog_json["content"]["conclusion"]
            
        # Find all citation patterns like [1], [2], etc.
        citation_pattern = r'\[(\d+)\]'
        citations_in_text = [int(match) for match in re.findall(citation_pattern, content_text)]
        
        # Check if text around citations is AI-related
        if not is_blog_ai_related:
            for citation_id in citations_in_text:
                # Find context around citation (50 chars before and after)
                citation_marker = f"[{citation_id}]"
                pos = content_text.find(citation_marker)
                if pos >= 0:
                    start = max(0, pos - 50)
                    end = min(len(content_text), pos + len(citation_marker) + 50)
                    context = content_text[start:end]
                    
                    if is_ai_related(context):
                        is_blog_ai_related = True
                        print(f"ℹ️ Citation [{citation_id}] appears in AI-related context")
        
        # Check each reference URL
        for ref in blog_json["references"]:
            ref_id = ref.get("id")
            
            # Skip references not cited in the text
            if ref_id not in citations_in_text:
                print(f"ℹ️ Reference [{ref_id}] not cited in text, skipping verification")
                continue
                
            url = ref.get("url", "")
            if not url:
                invalid_refs.append(ref)
                continue
            
            # Check recency for AI-related content
            year_str = ref.get("year", "")
            
            # Check if this specific reference is about AI
            ref_is_ai_related = is_ai_related(ref.get("title", "")) or is_ai_related(ref.get("source", ""))
            
            # Apply recency check for AI-related references in AI-related blogs
            if (is_blog_ai_related or ref_is_ai_related) and year_str and year_str.isdigit():
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
        
        # Check for outdated AI references
        outdated_refs = [ref for ref in valid_refs if ref.get("outdated")]
        if outdated_refs:
            print(f"⚠️ Found {len(outdated_refs)} outdated references for AI content")
            for ref in outdated_refs:
                invalid_refs.append(ref)
                valid_refs.remove(ref)
    
    return valid_refs, invalid_refs, citations_in_text

def fix_invalid_references(blog_json, provider, model, invalid_refs, citations_in_text):
    """Fix blog post content with invalid or outdated references by asking the AI to revise it"""
    if not invalid_refs:
        return blog_json
    
    # Separate outdated from invalid references for clearer instructions
    outdated_refs = [ref for ref in invalid_refs if ref.get("outdated")]
    bad_url_refs = [ref for ref in invalid_refs if not ref.get("outdated")]
    
    has_outdated = len(outdated_refs) > 0
    has_invalid = len(bad_url_refs) > 0
    
    print("🔄 Revising blog post to fix references...")
    
    # Create a prompt to fix the content
    invalid_ids = [ref["id"] for ref in invalid_refs]
    outdated_ids = [ref["id"] for ref in outdated_refs]
    bad_url_ids = [ref["id"] for ref in bad_url_refs]
    
    prompt = f"""You need to revise a blog post to address reference issues. 

The blog post contains citations that need to be revised:
{json.dumps(invalid_refs, indent=2)}

"""

    if has_outdated and has_invalid:
        prompt += f"""These include:
- Outdated references (too old for AI topics): {outdated_ids}
- References with invalid or inaccessible URLs: {bad_url_ids}
"""
    elif has_outdated:
        prompt += f"These are outdated references (pre-2022) used for AI-related topics: {outdated_ids}\n"
    elif has_invalid:
        prompt += f"These references have invalid or inaccessible URLs: {bad_url_ids}\n"

    prompt += f"""
These citations have the form [1], [2], etc. in the text.

Please revise the blog post to:
1. Remove references to these problematic sources (citations {invalid_ids})
"""
    
    if has_outdated:
        prompt += f"""2. Replace outdated AI references ({outdated_ids}) with newer, up-to-date statistics and information from the past 2 years
3. Make sure any claims about AI capabilities or adoption reflect the current state of technology (2022 or newer)
"""
    else:
        prompt += "2. Remove any statements that were only supported by these invalid sources\n"
        
    prompt += f"""
{4 if has_outdated else 3}. Rephrase any sentences to remove the need for these specific citations
{5 if has_outdated else 4}. Keep the overall flow and quality of the content
{6 if has_outdated else 5}. DO NOT change any valid citations

Here is the original blog post content:
{json.dumps(blog_json["content"], indent=2)}

Respond with ONLY a JSON object containing the revised content, with the same structure as the original.
"""

    # Call AI to revise the content
    print("📡 Sending revision request to AI...")
    
    # Wait a moment to avoid rate limits
    time.sleep(1)
    
    revised_content = call_ai(prompt, provider=provider, model=model)
    revised_content = clean_openai_response(revised_content)
    
    try:
        # Parse the revised content
        revised_json = json.loads(revised_content)
        
        # Update the blog JSON with the revised content
        blog_json["content"] = revised_json
        
        # Filter out invalid references
        blog_json["references"] = [ref for ref in blog_json.get("references", []) if ref["id"] not in invalid_ids]
        
        print("✅ Blog post revised successfully to remove invalid references")
    except json.JSONDecodeError:
        print("❌ Failed to parse revised content - keeping original content")
        print(f"Received: {revised_content[:200]}...")
    
    return blog_json

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
        '{{ company_short }}': 'Common Sense'
    }
    
    # Apply all replacements
    result = prompt_template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)
        
    return result


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
    raw_response = call_ai(prompt, provider=args.provider, model=args.model)
    cleaned_response = clean_openai_response(raw_response)

    try:
        blog_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        raise ValueError(f"{provider_name} response was not valid JSON. Got:\n\n" + raw_response)
        
    # Verify references and fix invalid ones using a second pass (unless skipped)
    if not args.skip_reference_check:
        valid_refs, invalid_refs, citations_in_text = extract_and_verify_references(blog_json)
        
        # If any invalid references are found, ask the AI to fix the content
        if invalid_refs:
            blog_json = fix_invalid_references(blog_json, args.provider, args.model, invalid_refs, citations_in_text)
    else:
        print("ℹ️ Skipping reference URL validation as requested")

    # Correct the date metadata
    blog_json['metadata']['date'] = today_str
    blog_json['metadata']['year'] = year_str
    blog_json['metadata']['month'] = month_str

    # Build output filename
    slug = blog_json['metadata']['slug']
    output_file = output_dir / f"{today_str}-{slug}.json"

    with open(output_file, 'w') as f:
        json.dump(blog_json, f, indent=2)

    print(f"✅ Blog JSON saved to: {output_file}")

    # Save pointer to current blog JSON
    pointer_file = output_dir / '.current_blog.json'
    with open(pointer_file, 'w') as f:
        f.write(f"{output_file.name}\n")
    print(f"🧭 Pointer file updated at: {pointer_file}")


if __name__ == '__main__':
    main()
