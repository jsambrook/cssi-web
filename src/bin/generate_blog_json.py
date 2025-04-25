#!/usr/bin/env python3
"""
generate_blog_json.py

Takes a short meta-description and uses OpenAI to generate a JSON representation
of a full blog article and image prompt, using company context from a TXT file.

Today's real date is used consistently across metadata, filenames, and prompt content.

Usage:
    ./generate_blog_json.py --description "How AI assistants help accountants manage client communication"
"""

import argparse
import os
import openai
from pathlib import Path
import datetime
import json


def parse_args():
    parser = argparse.ArgumentParser(description="Generate blog article JSON from a meta-description using OpenAI")
    parser.add_argument('--description', required=True, help='Short meta-description of the blog post topic')
    parser.add_argument('--context-file', default='../includes/common-sense-systems.txt', help='Path to company context file')
    parser.add_argument('--output-dir', default='../blog/drafts', help='Where to save the generated JSON file')
    parser.add_argument('--model', default='gpt-4-turbo', help='OpenAI model name')
    return parser.parse_args()


def build_prompt(description: str, context_md: str, today_str: str) -> str:
    return f"""
You are an expert business writer and AI strategist working for a company called Common Sense Systems.

Today's date is {today_str}.

Your job is to generate a JSON representation of a blog post and image prompt that will be used to publish a daily article
on the company's website. The JSON must match this structure exactly:

{{
  "metadata": {{
    "title": "...",
    "slug": "...",
    "author": "Common Sense Systems",
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

    # Build and send prompt
    prompt = build_prompt(args.description, context_md, today_str)
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


if __name__ == '__main__':
    main()
