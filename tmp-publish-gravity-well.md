Publish the blog post at src/content/blog/the-gravity-well-in-the-conference-room.md. Follow these steps in order:

1. Read and follow BRAND-GUIDELINES.md for all content and formatting standards.

2. Read the blog post draft and its imageAlt frontmatter field. Use Nano Banana Pro to generate a hero image guided by the imageAlt description. The image should be clean, minimalist, and analytical -- no stock imagery, no clip art, no marketing gloss. Use brand orange (#fe811b) as an accent color with dark charcoal (#292929) on white background. Save the final image as a .webp file to public/images/content/ with a descriptive filename matching the post slug. Then insert an <img> tag referencing the image immediately after the TL;DR section's horizontal rule, before the first body paragraph. Include descriptive alt text, explicit width and height attributes, loading="lazy", and decoding="async". Do not publish without a hero image.

3. The post contains a link to the Wikipedia article on gravity wells. Verify the link works. Also add at least one internal link to a related post on the site. Good candidates include:
   - /insights/the-meeting-that-went-differently/ (the board meeting where Sam first appeared)
   - /insights/the-other-calculation/ (Park's throughput discovery)
   - /insights/where-does-the-money-come-from/ (the surplus/profit reframe)
     Place internal links where they are contextually natural within the body text.

4. Remove `draft: true` from the frontmatter to mark the post as published.

5. Run `npm run build` and verify a clean build with no errors before committing. If the build fails, fix the issue and rebuild.

6. Commit with a descriptive message and deploy using ./deploy.sh.
