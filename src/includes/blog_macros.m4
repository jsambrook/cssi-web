m4_dnl Blog post header macro
m4_define(`BLOG_POST_HEADER', `
    <header class="blog-header">
        <h1>$1</h1>
        <div class="blog-meta">
            <span class="blog-date">$2</span>
            m4_ifelse(`$3', `', `', `<span class="blog-tags">$3</span>')
        </div>
    </header>
')m4_dnl

m4_dnl Blog post navigation
m4_define(`BLOG_POST_NAV', `
    <nav class="blog-nav">
        <a href="/blog/index.html" class="blog-nav-link">&larr; Back to Blog</a>
        m4_ifelse(`$1', `', `', `<a href="$1" class="blog-nav-link prev">&larr; Previous Post</a>')
        m4_ifelse(`$2', `', `', `<a href="$2" class="blog-nav-link next">Next Post &rarr;</a>')
    </nav>
')m4_dnl

m4_dnl Blog post template
m4_define(`BLOG_POST_LAYOUT', `
m4_define(`PAGE_TITLE', `$1 | Blog | Common Sense Systems')m4_dnl
m4_include(`src/includes/head.m4')m4_dnl
m4_include(`src/includes/navigation.m4')m4_dnl
<body>
    MAIN_NAVIGATION(`blog')

    <main class="blog-post">
        <article class="container">
            BLOG_POST_HEADER(`$1', `$2', `$3')
            
            <div class="blog-content">
                $4
            </div>
            
            BLOG_POST_NAV(`$5', `$6')
        </article>
    </main>

    m4_include(`src/includes/footer.m4')m4_dnl
    m4_include(`src/includes/mobile.m4')m4_dnl
</body>
</html>
')m4_dnl
