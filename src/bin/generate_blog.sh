#!/bin/bash
# generate_blog.sh - Generate a blog post from a description
#
# This script combines the markdown generation and HTML conversion steps
# into a single command for easier use.
#
# Usage:
#   ./generate_blog.sh "How AI assistants help accountants manage client communication"

set -e  # Exit on error

# Check if a description was provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 \"Blog post description\""
    echo "Example: $0 \"How AI assistants help accountants manage client communication\""
    exit 1
fi

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DESCRIPTION="$1"
PROVIDER=${2:-claude}  # Use Claude by default, allow override as second parameter
MODEL=${3:-claude-3-sonnet-20240229}  # Default model

# Step 1: Generate the Markdown file
echo "🤖 Generating blog post content using $PROVIDER..."
python3 "$SCRIPT_DIR/generate_blog_markdown.py" --provider "$PROVIDER" --model "$MODEL" "$DESCRIPTION"

# Get the path to the generated Markdown file
CURRENT_BLOG_FILE=$(cat "$SCRIPT_DIR/../blog/drafts/.current_blog.md")
MARKDOWN_PATH="$SCRIPT_DIR/../blog/drafts/$CURRENT_BLOG_FILE"

if [ ! -f "$MARKDOWN_PATH" ]; then
    echo "❌ Error: Markdown file not found at $MARKDOWN_PATH"
    exit 1
fi

echo "✅ Markdown file generated: $MARKDOWN_PATH"

# Step 2: Convert Markdown to HTML
echo "🔄 Converting Markdown to HTML using Pandoc..."
python3 "$SCRIPT_DIR/markdown_to_html.py" --input "$MARKDOWN_PATH"

echo "🎉 Blog post generation complete!"
echo "To view your blog post, check the HTML file in the blog directory."

# Extract the slug from the markdown filename
SLUG=$(basename "$MARKDOWN_PATH" | cut -d'-' -f4- | sed 's/\.md$//')
YEAR=$(basename "$MARKDOWN_PATH" | cut -d'-' -f1)
MONTH=$(basename "$MARKDOWN_PATH" | cut -d'-' -f2)

echo "📝 Blog post URL: /blog/$YEAR/$MONTH/$SLUG.html"
echo ""
echo "Next steps:"
echo "1. Check the HTML output and make any desired edits"
echo "2. Generate an image using the image prompt file"
echo "3. Update your blog index if needed"
