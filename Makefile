# Makefile

SRC_DIR = src
# Build directly to website root
BUILD_DIR = .
BLOG_SRC_DIR = $(SRC_DIR)/blog
BLOG_BUILD_DIR = $(BUILD_DIR)/blog

# Find all .m4 files in the source directory
M4_FILES = $(wildcard $(SRC_DIR)/*.m4)
# Convert the .m4 filenames to .html for the root directory
HTML_FILES = $(patsubst $(SRC_DIR)/%.m4,$(BUILD_DIR)/%.html,$(M4_FILES))

# M4 command configuration
M4 = m4
M4FLAGS = -P -I $(SRC_DIR)/includes

# The default target builds all static HTML pages (no blog posts here)
all: $(HTML_FILES) sitemap

# Rule to convert .m4 files to .html
$(BUILD_DIR)/%.html: $(SRC_DIR)/%.m4 $(SRC_DIR)/includes/head.m4
	@mkdir -p $(dir $@)
	$(M4) $(M4FLAGS) $< > $@

# Clean up generated files
clean:
	rm -f $(HTML_FILES)
	rm -f $(BUILD_DIR)/blog/**/*.html

# Target to rebuild everything from scratch
rebuild: clean all

# Target for static site pages only
pages: $(HTML_FILES)

# Generate sitemap.xml
sitemap:
	@echo "🌎 Generating sitemap.xml..."
	python $(SRC_DIR)/scripts/generate_sitemap.py --site-url="https://common-sense.com" --static-dir="$(BUILD_DIR)" --output-file="$(BUILD_DIR)/sitemap.xml" --debug
	@echo "✅ Sitemap generated!"

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Build all static HTML pages (default)"
	@echo "  pages        - Build only static site pages"
	@echo "  clean        - Remove all generated HTML files"
	@echo "  rebuild      - Clean and rebuild all static pages"
	@echo "  blog         - Process all blog posts and update the index"
	@echo "  blog-post    - Process a specific blog post (requires POST=path/to/post)"
	@echo "  blog-index   - Only regenerate the blog index"
	@echo "  sitemap      - Generate sitemap.xml"
	@echo "  help         - Show this help message"

# ========================================
# New Blog System Targets
# ========================================

.PHONY: blog blog-post blog-index clean pages rebuild sitemap help

# Process all blog posts and update the index
blog:
	@echo "📝 Processing all blog posts and updating index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py
	@echo "✅ Blog processing complete!"
	@echo "🌎 Updating sitemap..."
	make sitemap

# Process a specific blog post
blog-post:
ifndef POST
	$(error POST is required. Usage: make blog-post POST="2025/04/post-slug")
endif
	@echo "📝 Processing blog post: $(POST)"
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --post "$(POST)"
	@echo "✅ Blog post processed!"
	@echo "🌎 Updating sitemap..."
	make sitemap

# Only regenerate the blog index
blog-index:
	@echo "📝 Regenerating blog index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --rebuild-index
	@echo "✅ Blog index regenerated!"
	@echo "🌎 Updating sitemap..."
	make sitemap
