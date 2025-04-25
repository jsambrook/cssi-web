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

# Find all blog .m4 files recursively
BLOG_M4_FILES = $(shell find $(BLOG_SRC_DIR) -name '*.m4')
# Convert blog .m4 filenames to .html, preserving directory structure
BLOG_HTML_FILES = $(patsubst $(BLOG_SRC_DIR)/%.m4,$(BLOG_BUILD_DIR)/%.html,$(BLOG_M4_FILES))

# M4 command configuration
M4 = m4
M4FLAGS = -P -I $(SRC_DIR)/includes

# The default target builds all HTML files
all: $(HTML_FILES) $(BLOG_HTML_FILES)

# Rule to convert .m4 files to .html
$(BUILD_DIR)/%.html: $(SRC_DIR)/%.m4 $(SRC_DIR)/includes/head.m4
	@mkdir -p $(dir $@)
	$(M4) $(M4FLAGS) $< > $@

# Rule for blog files
$(BLOG_BUILD_DIR)/%.html: $(BLOG_SRC_DIR)/%.m4 $(SRC_DIR)/includes/head.m4 $(SRC_DIR)/includes/blog_macros.m4
	@mkdir -p $(dir $@)
	$(M4) $(M4FLAGS) $< > $@

# Clean up generated files
clean:
	rm -f $(HTML_FILES)
	rm -f $(BLOG_HTML_FILES)

# Target to rebuild everything from scratch
rebuild: clean all

# Target for blog only
blog: $(BLOG_HTML_FILES)

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Build all HTML files (default)"
	@echo "  blog      - Build only blog files"
	@echo "  clean     - Remove all generated HTML files"
	@echo "  rebuild   - Clean and rebuild all files"
	@echo "  help      - Show this help message"

.PHONY: all clean rebuild blog help
