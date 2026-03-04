# CC Prompt: Review and Publish "The Compass and the Toolkit"

## Task

Review and publish the blog post draft at:
`src/content/blog/compass-and-toolkit-toc-lean-healthcare.md`

## Context

This is a blog post arguing that healthcare should use TOC (Theory of Constraints) as a strategic compass to identify where to focus, and Lean as the tactical toolkit to eliminate waste at that focus point. It is fair to Lean throughout and does not set it up as a straw man. The target audience is broad: healthcare leaders, process improvement practitioners, and consultants.

## Review Checklist

1. **Read BRAND-GUIDELINES.md first.** The TOC vs. Lean section has specific guidance on tone and framing. Verify the draft follows it.

2. **Read the existing related posts** for consistency of voice and to avoid redundancy:
   - `non-value-added-work-lean.md` (credits Lean, argues for three-category model)
   - `physics-of-patient-flow.md` (discharge as constraint)
   - `the-cath-lab-is-empty-at-2am.md` (space utilization)
   - `why-is-hc-so-stuck.md`
   - `hidden-conflicts.md`
     Check for any overlap that should be addressed with cross-links or differentiation.

3. **Verify all external links resolve.** There are five source links in the post:
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC10868449/ (ophthalmology TOC case)
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC8812771/ (systematic review)
   - https://onlinelibrary.wiley.com/doi/10.1155/2020/8875902 (Lean failure rates)
   - https://www.industryweek.com/operations/continuous-improvement/article/21144299/why-do-so-many-lean-efforts-fail (Industry Week survey)
   - https://pmc.ncbi.nlm.nih.gov/articles/PMC4833201/ (Saskatchewan study)
   - https://www.synchronix.com/comparing-toc-and-lean/comparing-lean-and-six-sigma-and-the-impact-of-theory-of-constraints/ (21-plant case study)

4. **Check the internal link** to `/resources/toc-lean-integration`. This page does not exist yet. Either:
   - Create a placeholder at the appropriate location, or
   - Comment out the link and leave a TODO

5. **Style and tone review:**
   - No em-dashes (use commas or restructure instead)
   - Opens with a concrete scene, not an abstraction
   - No defensive tone
   - Fair to Lean throughout
   - Claims are backed by linked sources

6. **Frontmatter check:**
   - `draft: true` is set. When ready to publish, change to `draft: false` or remove the field, depending on how the Astro config handles it.
   - Verify `tags` are consistent with existing tag taxonomy in the blog
   - `imageAlt` is present but no `image` field. Generate or assign an appropriate image if the site requires one for blog posts.

7. **TL;DR section** is present at the top, consistent with other posts in the blog.

## Publishing

When the review is complete and any issues are resolved:

1. Remove `draft: true` (or set to `false`)
2. Commit with message: `blog: add "The Compass and the Toolkit" - TOC and Lean integration for healthcare`
3. Verify it builds cleanly with `npm run build` or the project's build command

## Notes

- This post is the first of a planned three-piece set: this healthcare post, a small business post (not yet drafted), and an evergreen reference page on TOC/Lean integration (not yet created). The internal link to `/resources/toc-lean-integration` anticipates that reference page.
- The 21-plant study (Synchronix) is a practitioner case study, not peer-reviewed academic research. The draft acknowledges this explicitly. Do not elevate the language around it.
- The ophthalmology case honestly notes that the improvement was not sustained. This is intentional. Do not remove it.
