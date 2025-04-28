def convert_markdown_to_html(input_path, output_path, template_path, metadata, references=None, cta_path=None, footer_path=None):
    """Convert Markdown to HTML using Pandoc with a template."""
    # Read the original markdown content
    markdown_content = input_path.read_text(encoding='utf-8')

    # Extract any image prompt data before cleaning
    image_prompt = extract_image_prompt(markdown_content)

    # Check if the first heading matches the title in metadata
    first_heading_is_title = False
    title = metadata.get('title', '')

    # Look for the first H1 heading in the markdown
    heading_match = re.search(r'^#\s+(.*?)$', markdown_content, re.MULTILINE)
    if heading_match and heading_match.group(1).strip() == title:
        first_heading_is_title = True

    # Clean the markdown content
    cleaned_markdown = clean_markdown(markdown_content)

    # Write the cleaned markdown to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(cleaned_markdown)

    try:
        # Set up Pandoc command
        pandoc_cmd = [
            "pandoc",
            temp_file_path,
            "--from=markdown-yaml_metadata_block",  # Exclude YAML metadata block
            "--to=html5",
            f"--template={str(template_path)}",
            f"--output={str(output_path)}",
            "--standalone"
        ]

        # Add metadata variables
        for key, value in metadata.items():
            if isinstance(value, list):
                # For list values (like tags), create a metadata file
                continue  # We'll handle this differently
            elif isinstance(value, (str, int, float)):
                pandoc_cmd.append(f"--variable={key}:{value}")

        # Add our first_heading_is_title variable
        pandoc_cmd.append(f"--variable=first_heading_is_title:{str(first_heading_is_title).lower()}")

        # Format date for display
        if 'date' in metadata:
            try:
                date_obj = datetime.strptime(metadata['date'], '%Y-%m-%d')
                formatted_date = date_obj.strftime('%B %d, %Y')
                pandoc_cmd.append(f"--variable=date:{formatted_date}")
            except (ValueError, TypeError):
                print(f"Warning: Invalid date format: {metadata.get('date')}")

        # Handle tags special case
        if 'tags' in metadata and metadata['tags']:
            tags = metadata['tags']
            if isinstance(tags, list):
                # Format as comma-separated string
                tags_str = ', '.join(tags)
                pandoc_cmd.append(f"--variable=tags:{tags_str}")
                # Also add as keywords for meta tag
                pandoc_cmd.append(f"--variable=keywords:{tags_str}")
            elif isinstance(tags, str):
                pandoc_cmd.append(f"--variable=tags:{tags}")
                pandoc_cmd.append(f"--variable=keywords:{tags}")

        # Add references if available
        if references:
            # Create a temporary JSON file with references
            temp_dir = Path.cwd() / "temp"
            temp_dir.mkdir(exist_ok=True)
            refs_file = temp_dir / "refs.json"
            with open(refs_file, 'w') as f:
                json.dump({"references": references}, f)

            pandoc_cmd.append(f"--metadata-file={refs_file}")

        # Add CTA and footer HTML if available
        if cta_path and Path(cta_path).exists():
            cta_html = Path(cta_path).read_text(encoding='utf-8')
            pandoc_cmd.append(f"--variable=cta_html:{cta_html}")

        if footer_path and Path(footer_path).exists():
            footer_html = Path(footer_path).read_text(encoding='utf-8')
            pandoc_cmd.append(f"--variable=footer_html:{footer_html}")

        # Run Pandoc
        try:
            subprocess.run(pandoc_cmd, check=True)
            print(f"✅ Successfully converted Markdown to HTML: {output_path}")

            # Clean up temporary files
            if references:
                refs_file.unlink(missing_ok=True)

            return image_prompt
        except subprocess.CalledProcessError as e:
            print(f"❌ Error converting Markdown to HTML: {e}")

            # If Pandoc isn't installed, show a helpful message
            if e.returncode == 127:  # Command not found
                print("\nPandoc appears to be missing. Install Pandoc with one of these commands:")
                print("- Ubuntu/Debian: sudo apt-get install pandoc")
                print("- macOS (Homebrew): brew install pandoc")
                print("- Windows: Install from https://pandoc.org/installing.html")

            return None
    finally:
        # Clean up the temporary file
        Path(temp_file_path).unlink(missing_ok=True)
