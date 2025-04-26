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

# Clean up generated files (prune drafts first)
clean: prune-drafts
	rm -f $(HTML_FILES)
	rm -f $(BUILD_DIR)/blog/**/*.html

# Target to rebuild everything from scratch
rebuild: clean all

# Target for static site pages only
pages: $(HTML_FILES)

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Build all static HTML pages (default)"
	@echo "  pages        - Build only static site pages"
	@echo "  clean        - Prune and remove all generated HTML files"
	@echo "  rebuild      - Prune, clean and rebuild all static pages"
	@echo "  blog-today   - Generate today's blog post using OpenAI (default)"  # requires DESCRIPTION
	@echo "  blog-claude  - Generate today's blog post using Claude"  # requires DESCRIPTION
	@echo "  blog-index   - Regenerate blog/index.html from metadata"
	@echo "  blog-reset   - Reset blog system to pristine/empty state (⚠️ DESTRUCTIVE)"
	@echo "  prune-drafts - Prune old files from the drafts directory"
	@echo "  help         - Show this help message"

# ========================================
# Blog Automation Targets
# ========================================

TODAY := $(shell date +"%Y-%m-%d")
DRAFTS_DIR := src/blog/drafts

.PHONY: blog-today blog-claude blog-index blog-reset prune-drafts clean pages rebuild help

# Prune the drafts folder
prune-drafts:
	@echo "🗑️  Pruning old blog drafts..."
	# keep only the last 30 days of drafts
	find $(DRAFTS_DIR) -name '*.json' -mtime +30 -delete
	@echo "✅ Old drafts pruned."

# Generate today's blog post using OpenAI (default)
blog-today: prune-drafts
ifndef DESCRIPTION
	$(error DESCRIPTION is required. Usage: make blog-today DESCRIPTION=\"Short description here\")
endif
	@echo "📝 Generating blog post for today: $(TODAY)"
	cd src/bin && ./generate_blog_json.py "$(DESCRIPTION)"
	@CURRENT_JSON=$$(cat $(DRAFTS_DIR)/.current_blog.json); \
	echo "🔍 Using generated JSON file: $$CURRENT_JSON"; \
	cd src/bin && ./generate_blog_post.py --input ../blog/drafts/$$CURRENT_JSON
	@echo "✅ Blog post generated and HTML written!"
	@$(MAKE) blog-index

# Generate today's blog post using Claude
blog-claude: prune-drafts
ifndef DESCRIPTION
	$(error DESCRIPTION is required. Usage: make blog-claude DESCRIPTION=\"Short description here\")
endif
	@echo "📝 Generating blog post using Claude for today: $(TODAY)"
	cd src/bin && ./generate_blog_json.py --provider claude --prompt ../blog/claude-prompt.txt "$(DESCRIPTION)"
	@CURRENT_JSON=$$(cat $(DRAFTS_DIR)/.current_blog.json); \
	echo "🔍 Using generated JSON file: $$CURRENT_JSON"; \
	cd src/bin && ./generate_blog_post.py --input ../blog/drafts/$$CURRENT_JSON
	@echo "✅ Blog post generated and HTML written!"
	@$(MAKE) blog-index

# Regenerate the blog index page
blog-index:
	cd src/bin && ./generate_blog_index.py
	@echo "✅ Blog index rebuilt!"

# Reset the blog system to a pristine, empty state
blog-reset:
	@echo "🛑 WARNING: This will delete ALL blog posts, drafts, and related files!"
	@echo "    This action cannot be undone. Are you sure? (Type 'yes' to proceed)"
	@read -r confirmation; \
	if [ "$$confirmation" = "yes" ]; then \
		echo "🗑️  Deleting all blog HTML files..."; \
		rm -rf $(BUILD_DIR)/blog/20*; \
		echo "🗑️  Removing all blog drafts..."; \
		rm -rf $(BLOG_SRC_DIR)/drafts/*.json; \
		echo "🗑️  Deleting blog images and prompts..."; \
		rm -rf $(SRC_DIR)/assets/img/blog/20*; \
		echo "🗑️  Resetting blog index..."; \
		echo '{"posts":[]}' > $(BLOG_SRC_DIR)/blog_index.json; \
		echo "🔄 Regenerating empty blog index..."; \
		cd src/bin && ./generate_blog_index.py; \
		echo "✅ Blog system has been reset to a pristine state."; \
	else \
		echo "❌ Reset cancelled."; \
	fi
