#!/usr/bin/env python3
"""
generate_blog_json.py

Takes a short meta-description and uses OpenAI to generate a JSON representation
of a full blog article and image prompt, using company context from a Markdown file.

Usage:
    ./generate_blog_json.py --description "How AI assistants help massage therapists"
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
    parser.add_argument('--context-file', default='../includes/common-sense-systems.txt', help='Path to XML-ish context file')
    parser.add_argument('--output-dir', default='../blog/drafts', help='Where to save the generated JSON file')
    parser.add_argument('--model', default='gpt-4-turbo', help='OpenAI model name')
    return parser.parse_args()

def clean_openai_response(text: str) -> str:
    """Remove code fences from OpenAI JSON responses if present"""
    if text.startswith("```json"):
        text = text.lstrip("```json").strip()
    if text.startswith("```"):
        text = text.lstrip("```").strip()
    if text.endswith("```"):
        text = text.rstrip("```").strip()
    return text

def build_prompt(description: str, context_md: str) -> str:
    return f"""
You are an expert business writer and AI strategist working for a company called Common Sense Systems.

Your job is to generate a JSON representation of a blog post and image prompt that will be used to publish a daily article
on the company's website. The JSON must match this structure:

{{
  "metadata": {{
    "title": "...",
    "slug": "...",
    "author": "Common Sense Systems",
    "date": "YYYY-MM-DD",
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


def main():
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    context_path = (script_dir / args.context_file).resolve()
    output_dir = (script_dir / args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(context_path, 'r') as f:
        context_md = f.read()

    prompt = build_prompt(args.description, context_md)
    print("📡 Sending request to OpenAI...")

    raw_response = call_openai(prompt, model=args.model)
    cleaned_response = clean_openai_response(raw_response)
    try:
        blog_json = json.loads(cleaned_response)
    except json.JSONDecodeError:
        raise ValueError("OpenAI response was not valid JSON. Got:\n\n" + raw_response)

    # Derive output path
    slug = blog_json['metadata']['slug']
    date = blog_json['metadata']['date']
    output_file = output_dir / f"{date}-{slug}.json"

    with open(output_file, 'w') as f:
        json.dump(blog_json, f, indent=2)

    print(f"✅ Blog JSON saved to: {output_file}")


if __name__ == '__main__':
    main()
