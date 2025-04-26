#!/usr/bin/env python3
"""
generate_blog_json.py

Takes a short meta-description and uses OpenAI to generate a JSON representation
of a full blog article and image prompt, using company context from a TXT file.

Today's real date is used consistently across metadata, filenames, and prompt content.

Also saves a .current_blog.json file pointing to the generated JSON file.

Usage:
    ./generate_blog_json.py "How AI assistants help accountants manage client communication"
    ./generate_blog_json.py --prompt /path/to/prompt_file.txt "Blog topic"
"""

import argparse
import os
import openai
from pathlib import Path
import datetime
import json


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog article JSON from a meta-description using OpenAI")
    parser.add_argument('description', help='Short meta-description of the blog post topic')
    parser.add_argument('--prompt', help='Path to a custom prompt template file')
    parser.add_argument('--context-file', default='../includes/common-sense-systems.txt', help='Path to company context file')
    parser.add_argument('--output-dir', default='../blog/drafts', help='Where to save the generated JSON file')
    parser.add_argument('--model', default='gpt-4-turbo', help='OpenAI model name')
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


def call_openai(prompt: str, model: str) -> str:
    openai.api_key = os.getenv('OPENAI_API_KEY')
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a JSON-generating assistant for business blog posts."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content


def clean_openai_response(text: str) -> str:
    """Remove code fences from OpenAI JSON responses if present"""
    if text.startswith("```json"):
        text = text.lstrip("```json").strip()
    if text.startswith("```"):
        text = text.lstrip("```").strip()
    if text.endswith("```"):
        text = text.rstrip("```").strip()
    return text


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
        
    print(f"Generated prompt: \n{prompt}\n")

    print("📡 Sending request to OpenAI...")

    raw_response = call_openai(prompt, model=args.model)
    cleaned_response = clean_openai_response(raw_response)

    try:
        blog_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        raise ValueError("OpenAI response was not valid JSON. Got:\n\n" + raw_response)

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
