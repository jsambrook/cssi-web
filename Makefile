# Makefile
SRC_DIR = src
# Build directly to website root
BUILD_DIR = .

# Find all .m4 files in the source directory
M4_FILES = $(wildcard $(SRC_DIR)/*.m4)
# Convert the .m4 filenames to .html for the root directory
HTML_FILES = $(patsubst $(SRC_DIR)/%.m4,$(BUILD_DIR)/%.html,$(M4_FILES))

# M4 command configuration
M4 = m4
M4FLAGS = -P -I $(SRC_DIR)/includes

# The default target builds all HTML files
all: $(HTML_FILES)

# Rule to convert .m4 files to .html
$(BUILD_DIR)/%.html: $(SRC_DIR)/%.m4 $(SRC_DIR)/includes/head.m4
	$(M4) $(M4FLAGS) $< > $@

# Clean up generated files
clean:
	rm -f $(HTML_FILES)

# Target to rebuild everything from scratch
rebuild: clean all
