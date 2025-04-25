m4_dnl Blog post header macro
m4_define(`BLOG_POST_HEADER', `
    <header class="blog-header">
        <h1>$1</h1>
        <div class="blog-meta">
            <span class="blog-date">$2</span>
            <span class="blog-tags">$3</span>
        </div>
    </header>
')m4_dnl

m4_dnl Blog post navigation
m4_define(`BLOG_POST_NAV', `
    <nav class="blog-nav">
        <a href="/blog/index.html" class="blog-nav-link">&larr; Back to Blog</a>
    </nav>
')m4_dnl

m4_dnl Simple blog post layout
m4_define(`BLOG_POST_LAYOUT_SIMPLE', `
<main class="blog-post">
    <article class="container">
        BLOG_POST_HEADER(`$1', `$2', `$3')
        <div class="blog-content">
            $4
        </div>
        BLOG_POST_NAV
    </article>
</main>
')m4_dnl
