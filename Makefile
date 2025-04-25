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
all: $(HTML_FILES)

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

# Help target
help:
	@echo "Available targets:"
	@echo "  all         - Build all static HTML pages (default)"
	@echo "  pages       - Build only static site pages"
	@echo "  clean       - Remove all generated HTML files"
	@echo "  rebuild     - Clean and rebuild all static pages"
	@echo "  blog-today  - Generate today's blog post (requires DESCRIPTION=\"...\")"
	@echo "  blog-index  - Regenerate blog/index.html from metadata"
	@echo "  help        - Show this help message"

# ========================================
# Blog Automation Targets
# ========================================

TODAY := $(shell date +"%Y-%m-%d")
DRAFTS_DIR := src/blog/drafts

.PHONY: blog-today

blog-today:
ifndef DESCRIPTION
	$(error DESCRIPTION is required. Usage: make blog-today DESCRIPTION="Short description here")
endif
	@echo "📝 Generating blog post for today: $(TODAY)"
	cd src/bin && ./generate_blog_json.py --description "$(DESCRIPTION)"
	@CURRENT_JSON=$$(cat $(DRAFTS_DIR)/.current_blog.json); \
	echo "🔍 Using generated JSON file: $$CURRENT_JSON"; \
	cd src/bin && ./generate_blog_post.py --input ../blog/drafts/$$CURRENT_JSON
	@echo "✅ Blog post generated and HTML written!"
	@$(MAKE) blog-index

.PHONY: blog-index

blog-index:
	cd src/bin && ./generate_blog_index.py
	@echo "✅ Blog index rebuilt!"
