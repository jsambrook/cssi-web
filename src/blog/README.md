# Blog System Documentation

This directory contains the M4 source files for the blog section of the website.

## Structure

- `index.m4` - The main blog index page that lists all posts
- `2025/` - Year directory containing monthly subdirectories
  - `04/` - April posts
    - `power-of-simplicity.m4` - Example blog post

## Creating a New Blog Post

1. Create the appropriate year/month directory if it doesn't exist:
   ```bash
   mkdir -p src/blog/YYYY/MM
   ```

2. Create a new `.m4` file for your post:
   ```bash
   touch src/blog/YYYY/MM/your-post-name.m4
   ```

3. Use the blog post template:
   ```m4
   m4_include(`src/includes/blog_macros.m4')m4_dnl
   BLOG_POST_LAYOUT(
       `Your Post Title',
       `Month DD, YYYY',
       `tag1, tag2, tag3',
       `
       <p>Your content here...</p>
       <h2>Subheading</h2>
       <p>More content...</p>
       ',
       `optional-prev-post-url',
       `optional-next-post-url'
   )m4_dnl
   ```

4. Update the blog index by editing `src/includes/blog_posts.m4`:
   - Add your post to the appropriate month/year section
   - If creating a new month/year, use the appropriate macros:
     ```m4
     BLOG_YEAR_SECTION(`YYYY')
     BLOG_MONTH_SECTION(`Month')
     ADD_BLOG_POST(`YYYY', `MM', `filename', `Post Title', `Month DD, YYYY')
     ```

5. Build the site:
   ```bash
   make all
   # or just build blog files:
   make blog
   ```

## Blog Post Macros

The `BLOG_POST_LAYOUT` macro accepts the following parameters:
1. Title - The post title
2. Date - Publication date
3. Tags - Comma-separated list of tags
4. Content - The main content of the post
5. Previous post URL - Optional link to previous post
6. Next post URL - Optional link to next post

## Best Practices

- Use semantic HTML in your blog content
- Add appropriate headings (h2, h3, etc.)
- Include images in `/assets/img/blog/` directory
- Keep URLs consistent: `/blog/YYYY/MM/post-name.html`
- Update the blog index immediately after creating a new post

## Troubleshooting

If your blog post doesn't appear:
1. Check that the `.m4` file is correctly formatted
2. Ensure you've updated `blog_posts.m4`
3. Run `make clean && make all` to rebuild everything
4. Check that the M4 include paths are correct
