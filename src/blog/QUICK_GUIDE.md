# Quick Guide: Adding a New Blog Post

## 1. Create the blog post file

```bash
# Create directory for the month (if needed)
mkdir -p src/blog/YYYY/MM

# Create the M4 file
touch src/blog/YYYY/MM/your-post-name.m4
```

## 2. Write your post using this template

```m4
m4_include(`src/includes/blog_macros.m4')m4_dnl
BLOG_POST_LAYOUT(
    `Your Post Title Here',
    `April 25, 2025',
    `ai, automation, business',
    `
    <p>Your opening paragraph here...</p>

    <h2>First Subheading</h2>
    <p>Content for the first section...</p>

    <h2>Second Subheading</h2>
    <p>Content for the second section...</p>

    <ul>
        <li>Bullet point 1</li>
        <li>Bullet point 2</li>
    </ul>

    <h2>Conclusion</h2>
    <p>Your closing thoughts...</p>
    ',
    `',
    `'
)m4_dnl
```

## 3. Update the blog index

Edit `src/includes/blog_posts.m4` and add your post to the appropriate section:

```m4
ADD_BLOG_POST(`2025', `04', `your-post-name', `Your Post Title', `April 25, 2025')
```

## 4. Build the site

```bash
make all
```

## 5. Preview

Open `/blog/YYYY/MM/your-post-name.html` in your browser to preview.

## Tips

- Use semantic HTML tags (h2, h3, p, ul, etc.)
- Keep URLs lowercase and hyphenated
- Add images to `/assets/img/blog/`
- Run `make clean && make all` if changes don't appear
