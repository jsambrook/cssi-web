Publish the blog post at src/content/blog/where-does-the-money-come-from.md. Follow these steps in order:

1. Read and follow BRAND-GUIDELINES.md for all content and formatting standards.

2. Read the blog post draft and its imageAlt frontmatter field. Use Nano Banana Pro to generate a hero image guided by the imageAlt description. The image should be clean, minimalist, and analytical -- no stock imagery, no clip art, no marketing gloss. Use brand orange (#fe811b) as an accent color with dark charcoal (#292929) on white background. Save the final image as a .webp file to public/images/content/ with a descriptive filename matching the post slug. Then insert an <img> tag referencing the image immediately after the TL;DR section's horizontal rule, before the first body paragraph. Include descriptive alt text, explicit width and height attributes, loading="lazy", and decoding="async". Do not publish without a hero image.

3. Remove `draft: true` from the frontmatter to mark the post as published.

4. Run `npm run build` and verify a clean build with no errors before committing. If the build fails, fix the issue and rebuild.

5. Commit with a descriptive message and deploy using ./deploy.sh.
