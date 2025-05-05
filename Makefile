# Makefile

# Source directory
SRC_DIR = src

# Build directly to website root
BUILD_DIR = .

# Blog source directory
BLOG_SRC_DIR = $(SRC_DIR)/blog

# Blog build directory
BLOG_BUILD_DIR = $(BUILD_DIR)/blog

# Blog content directory
BLOG_CONTENT_DIR = $(BLOG_SRC_DIR)/content

# Find static HTML files (not in blog directory and not in src directory)
STATIC_HTML_FILES := $(shell find $(BUILD_DIR) -path "$(BLOG_BUILD_DIR)" -prune -o -path "$(SRC_DIR)" -prune -o -name "*.html" -print)

# Find blog HTML files if the blog directory exists
BLOG_HTML_FILES := $(shell find $(BLOG_BUILD_DIR) -name "*.html" 2>/dev/null || echo "")

# Find all blog post source files
BLOG_POST_SOURCES := $(shell find $(BLOG_CONTENT_DIR) -name "index.md" 2>/dev/null || echo "")

# Determine blog post output files (transform src/blog/content/YYYY/MM/post-slug/index.md to blog/YYYY/MM/post-slug/index.html)
BLOG_POST_OUTPUTS := $(patsubst $(BLOG_CONTENT_DIR)/%/index.md,$(BLOG_BUILD_DIR)/%/index.html,$(BLOG_POST_SOURCES))

# VNU HTML Validator configuration
VNU = vnu
VNU_FLAGS = --errors-only --format text
# We need to get rid of the va*.html files someday soon, or make them useful
VNU_FILES := $(filter-out va-1.html,$(filter-out va.html,$(shell ls -1 *.html)))

# Default target builds blog posts, blog index, generates sitemap, and validates HTML
all: blog sitemap validate

# Target to validate HTML files
validate:
	@echo "🔍 Validating HTML files..."
	@if command -v $(VNU) >/dev/null 2>&1; then \
		$(VNU) $(VNU_FLAGS) $(VNU_FILES); \
	 	if [ $$? -eq 0 ]; then \
	 		echo "✅ HTML validation passed!"; \
	 	else \
	 		echo "❌ HTML validation failed!"; \
	 		exit 1; \
	 	fi \
	 else \
	 	echo "⚠️ VNU validator ($(VNU)) not found. Skipping validation."; \
	 	echo "   To use this target, install the validator with:"; \
	 	echo "   brew install vnu (macOS with Homebrew)"; \
	 	echo "   or download from https://github.com/validator/validator/releases"; \
	 fi

# Generate sitemap.xml
sitemap:
	@echo "🌎 Generating sitemap.xml..."
	python $(SRC_DIR)/scripts/generate_sitemap.py --site-url="https://common-sense.com" --static-dir="$(BUILD_DIR)" --output-file="$(BUILD_DIR)/sitemap.xml" --debug
	@echo "✅ Sitemap generated!"

# ========================================
# Blog System Targets
# ========================================

# Process all blog posts and update the index
blog:
	@echo "📝 Processing all blog posts and updating index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py
	@echo "✅ Blog processing complete!"

# Process a specific blog post
blog-post:
ifndef POST
	$(error POST is required. Usage: make blog-post POST="2025/04/post-slug")
endif
	@echo "📝 Processing blog post: $(POST)"
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --post "$(POST)"
	@echo "✅ Blog post processed!"

# Only regenerate the blog index
blog-index:
	@echo "📝 Regenerating blog index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --rebuild-index
	@echo "✅ Blog index regenerated!"

# Clean generated sitemap
clean-sitemap:
	@echo "🧹 Cleaning generated sitemap..."
	rm -f $(BUILD_DIR)/sitemap.xml
	@echo "✅ Sitemap cleaned!"

# Clean blog output files
clean-blog:
	@echo "🧹 Cleaning generated blog files..."
	rm -rf $(BLOG_BUILD_DIR)
	@echo "✅ Blog files cleaned!"

# Clean all generated files
clean: clean-sitemap clean-blog
	@echo "✅ All generated files cleaned!"

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Process all blog posts, generate sitemap, and validate HTML (default)"
	@echo "  blog         - Process all blog posts and update the index"
	@echo "  blog-post    - Process a specific blog post (requires POST=path/to/post)"
	@echo "  blog-index   - Only regenerate the blog index"
	@echo "  sitemap      - Generate sitemap.xml"
	@echo "  validate     - Validate all HTML files with VNU validator"
	@echo "  clean-sitemap- Remove generated sitemap.xml"
	@echo "  clean-blog   - Remove all generated blog files"
	@echo "  clean        - Remove all generated files"
	@echo "  help         - Show this help message"

# Define all phony targets
.PHONY: all validate sitemap blog blog-post blog-index clean-sitemap clean-blog clean help
