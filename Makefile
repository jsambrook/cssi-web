# Makefile

# Set up PATH to ensure we can find what we depend on.
export PATH := /opt/homebrew/Cellar/pyenv-virtualenv/HEAD-e8c8fd9/shims:\
	           /Users/john/.pyenv/shims:\
               /Users/john/.pyenv/bin:\
               .:\
               /Users/john/bin:\
               /Users/john/git/cssi/bin:\
               /Users/john/git/cssi-dev-env/bin:\
               /opt/homebrew/opt/postgresql@16/bin:\
               /opt/homebrew/bin:\
               /opt/homebrew/opt/ruby/bin:\
               /opt/homebrew/sbin:\
               /usr/local/bin:\
               /bin:\
               /usr/bin:\
               /usr/sbin:\
               /sbin:\
               /Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin:\
               /Users/john/.local/bin:\
               /Library/TeX/texbin:

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

# Blog cache file for dependency tracking
BLOG_CACHE_FILE = $(BLOG_SRC_DIR)/.blog_cache.json

# Custom scripts
HTML_TO_MARKDOWN = ~/git/cssi-ai/html-to-markdown/html-to-markdown.py
SUMMARIZE_ARTICLE = ~/git/cssi-ai/summarize-article/summarize-article.py

# Find static HTML files (not in blog directory and not in src directory)
STATIC_HTML_FILES := $(shell find $(BUILD_DIR) -path "$(BLOG_BUILD_DIR)" -prune -o -path "$(SRC_DIR)" -prune -o -name "*.html" -print)

# Find blog HTML files if the blog directory exists
BLOG_HTML_FILES := $(shell find $(BLOG_BUILD_DIR) -name "*.html" 2>/dev/null || echo "")

# Find all blog post source files
BLOG_POST_SOURCES := $(shell find $(BLOG_CONTENT_DIR) -name "index.md" 2>/dev/null || echo "")

# Determine blog post output files (transform src/blog/content/YYYY/MM/post-slug/index.md to blog/YYYY/MM/post-slug/index.html)
BLOG_POST_OUTPUTS := $(patsubst $(BLOG_CONTENT_DIR)/%/index.md,$(BLOG_BUILD_DIR)/%/index.html,$(BLOG_POST_SOURCES))

# Blog index file
BLOG_INDEX = $(BLOG_BUILD_DIR)/index.html

# Content file for LLM training
CONTENT_FILE = $(BUILD_DIR)/website-content.txt

# VNU HTML Validator configuration
VNU = vnu
VNU_FLAGS = --errors-only --format text
# We need to get rid of the va*.html files someday soon, or make them useful
#VNU_FILES := $(filter-out va-japanese-acupuncture.html,$(filter-out va-sundays.html,$(shell ls -1 *.html)))
VNU_FILES := $(shell ls -1 *.html | grep -v "^va")

# Default target builds blog posts, blog index, generates sitemap, validates HTML, and creates content file
all: blog sitemap validate content-file

# Check for Python
check-python:
	@echo "🔍 Checking for Python installation..."
	@if ! command -v python >/dev/null 2>&1; then \
		echo "❌ ERROR: Python is required but not found in PATH."; \
		echo "   Please install Python or ensure it's in your PATH."; \
		echo ""; \
		echo "   Current PATH: $PATH"; \
		exit 1; \
	else \
		echo "✅ Python found at: $(which python)"; \
	fi

# Target to validate HTML files
validate:
	@echo "🔍 Validating HTML files..."
	@if command -v $(VNU) >/dev/null 2>&1; then \
		$(VNU) $(VNU_FLAGS) $(VNU_FILES) && { \
			echo "✅ HTML validation passed!"; \
		} || { \
			echo "❌ HTML validation failed!"; \
			exit 1; \
		}; \
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

# Check for HTML-to-Markdown converter
check-html-to-markdown:
	@echo "🔍 Checking for HTML-to-Markdown converter..."
	@if [ ! -f $(HTML_TO_MARKDOWN) ]; then \
		echo "❌ ERROR: HTML-to-Markdown converter not found at $(HTML_TO_MARKDOWN)"; \
		echo "   Please check if the repository is properly cloned."; \
		exit 1; \
	else \
		echo "✅ HTML-to-Markdown converter found"; \
	fi

# Check for article summarizer
check-summarize-article:
	@echo "🔍 Checking for article summarizer..."
	@if [ ! -f $(SUMMARIZE_ARTICLE) ]; then \
		echo "❌ ERROR: Article summarizer not found at $(SUMMARIZE_ARTICLE)"; \
		echo "   Please check if the repository is properly cloned."; \
		exit 1; \
	else \
		echo "✅ Article summarizer found"; \
	fi

# Generate a content file with all HTML converted to Markdown
content-file: check-python check-html-to-markdown check-summarize-article
	@echo "📄 Generating website content file..."
	@echo "" > $(CONTENT_FILE)

	@echo "🔄 Processing regular HTML files..."
	@for file in $(find . -name "*.html" | grep -v "$(SRC_DIR)/" | grep -v "$(BLOG_BUILD_DIR)" | sort); do \
		echo "  - Converting $file to Markdown..."; \
		printf "\n--- Markdown synthesized from $file ---\n" >> $(CONTENT_FILE); \
		$(HTML_TO_MARKDOWN) --input-file $file --output-file - >> $(CONTENT_FILE); \
		printf "\n\n" >> $(CONTENT_FILE); \
	done

	@echo "📝 Processing blog HTML files..."
	@for file in $(find $(BLOG_BUILD_DIR) -name "*.html" | sort); do \
		echo "  - Summarizing blog article: $file..."; \
		printf "\n--- Blog summary synthesized from $file ---\n" >> $(CONTENT_FILE); \
		$(SUMMARIZE_ARTICLE) --input-file $file --output-file - >> $(CONTENT_FILE); \
		printf "\n\n" >> $(CONTENT_FILE); \
	done

	@echo "✅ Content file generated at $(CONTENT_FILE)!"

# ========================================
# Blog System Targets
# ========================================

# Check for pandoc installation
check-pandoc:
	@echo "🔍 Checking for pandoc installation..."
	@if ! command -v pandoc >/dev/null 2>&1; then \
		echo "❌ ERROR: pandoc is required but not found in PATH."; \
		echo "   Please install pandoc or ensure it's in your PATH."; \
		echo "   macOS: brew install pandoc"; \
		echo "   Linux: apt-get install pandoc / yum install pandoc"; \
		echo ""; \
		echo "   Current PATH: $$PATH"; \
		exit 1; \
	else \
		echo "✅ pandoc found at: $$(which pandoc)"; \
	fi

# Process all blog posts and update the index
blog: check-python check-pandoc
	@echo "📝 Processing blog posts and updating index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --cache-file=$(BLOG_CACHE_FILE)
	@echo "✅ Blog processing complete!"

# Rule for creating the blog index, which depends on all blog posts
$(BLOG_INDEX): check-python check-pandoc $(BLOG_POST_OUTPUTS)
	@echo "📝 Updating blog index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --rebuild-index --cache-file=$(BLOG_CACHE_FILE)
	@touch $(BLOG_INDEX)
	@echo "✅ Blog index updated!"

# Pattern rule for blog posts (only rebuilds when necessary)
$(BLOG_BUILD_DIR)/%/index.html: check-python check-pandoc $(BLOG_CONTENT_DIR)/%/index.md
	@echo "📝 Processing blog post: $<"
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --post "$*" --cache-file=$(BLOG_CACHE_FILE)
	@echo "✅ Blog post processed: $@"

# Process a specific blog post (forces rebuild)
blog-post: check-python check-pandoc
ifndef POST
	$(error POST is required. Usage: make blog-post POST="2025/04/post-slug")
endif
	@echo "📝 Processing blog post: $(POST)"
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --post "$(POST)" --force --cache-file=$(BLOG_CACHE_FILE)
	@echo "✅ Blog post processed!"

# Only regenerate the blog index
blog-index: check-python check-pandoc
	@echo "📝 Regenerating blog index..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --rebuild-index --cache-file=$(BLOG_CACHE_FILE)
	@echo "✅ Blog index regenerated!"

# Force rebuild all blog posts (ignores cache)
blog-rebuild: check-python check-pandoc
	@echo "📝 Rebuilding all blog posts..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --force --cache-file=$(BLOG_CACHE_FILE)
	@echo "✅ All blog posts rebuilt!"

# Check which posts would be rebuilt (dry run)
blog-check: check-python check-pandoc
	@echo "📝 Checking which blog posts need rebuilding..."
	python $(BLOG_SRC_DIR)/scripts/process_blog.py --dry-run --cache-file=$(BLOG_CACHE_FILE)

# Clean the blog cache file
clean-cache:
	@echo "🧹 Cleaning blog build cache..."
	rm -f $(BLOG_CACHE_FILE)
	@echo "✅ Blog cache cleaned!"

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

# Clean content file
clean-content:
	@echo "🧹 Cleaning generated content file..."
	rm -f $(CONTENT_FILE)
	@echo "✅ Content file cleaned!"

# Clean all generated files
clean: clean-sitemap clean-blog clean-cache clean-content
	@echo "✅ All generated files cleaned!"

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Process all blog posts, generate sitemap, validate HTML, and create content file (default)"
	@echo "  blog         - Process all blog posts and update the index"
	@echo "  blog-post    - Process a specific blog post (requires POST=path/to/post)"
	@echo "  blog-index   - Only regenerate the blog index"
	@echo "  blog-rebuild - Force rebuild all blog posts (ignores cache)"
	@echo "  blog-check   - Check which posts would be rebuilt (dry run)"
	@echo "  sitemap      - Generate sitemap.xml"
	@echo "  validate     - Validate all HTML files with VNU validator"
	@echo "  content-file - Generate website-content.txt from all HTML files"
	@echo "  clean-cache  - Clean the blog cache file"
	@echo "  clean-sitemap- Remove generated sitemap.xml"
	@echo "  clean-blog   - Remove all generated blog files"
	@echo "  clean-content- Remove generated content file"
	@echo "  clean        - Remove all generated files"
	@echo "  help         - Show this help message"

# Define all phony targets
.PHONY: all validate sitemap content-file blog blog-post blog-index blog-rebuild blog-check clean-cache clean-sitemap clean-blog clean-content clean help check-pandoc check-python check-html-to-markdown check-summarize-article
