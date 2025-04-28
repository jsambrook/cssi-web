#!/bin/bash
# test_blog_system.sh
#
# A script to test the blog publishing system with a sample blog post
#
# This script:
# 1. Sets up the necessary directory structure
# 2. Copies the sample blog post to the drafts directory
# 3. Publishes the blog post
# 4. Generates the blog index

set -e  # Exit on error

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

echo "🔧 Setting up test environment..."

# Create necessary directories
mkdir -p "$REPO_ROOT/blog"
mkdir -p "$REPO_ROOT/src/blog/drafts"
mkdir -p "$REPO_ROOT/src/assets/img/blog"
mkdir -p "$REPO_ROOT/src/includes"

# Create a simple blog index JSON if it doesn't exist
if [ ! -f "$REPO_ROOT/src/blog/blog_index.json" ]; then
    echo '{"posts":[]}' > "$REPO_ROOT/src/blog/blog_index.json"
    echo "✅ Created empty blog index JSON"
fi

# Copy the sample blog post to the drafts directory
echo "📝 Copying sample blog post to drafts directory..."
cp "$SCRIPT_DIR/sample_blog_post.md" "$REPO_ROOT/src/blog/drafts/"
SAMPLE_POST="$REPO_ROOT/src/blog/drafts/sample_blog_post.md"

# Ensure scripts are executable
chmod +x "$SCRIPT_DIR/blog_publisher.py"
chmod +x "$SCRIPT_DIR/generate_blog_index.py"

# Publish the blog post
echo "🔄 Publishing blog post..."
"$SCRIPT_DIR/blog_publisher.py" --input "$SAMPLE_POST" --verbose

# Generate the blog index
echo "📋 Generating blog index..."
"$SCRIPT_DIR/generate_blog_index.py"

echo "🎉 Test completed successfully!"
echo ""
echo "You can view the blog post at: $REPO_ROOT/blog/2025/04/ai-transforming-small-business-operations.html"
echo "You can view the blog index at: $REPO_ROOT/blog/index.html"
