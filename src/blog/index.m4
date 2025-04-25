m4_define(`PAGE_TITLE', `Blog | Common Sense Systems')m4_dnl
m4_include(`src/includes/head.m4')m4_dnl
m4_include(`src/includes/navigation.m4')m4_dnl
m4_include(`src/includes/blog_posts.m4')m4_dnl
<body>
    MAIN_NAVIGATION(`blog')

    <main>
        <section class="blog-index container">
            <h1>Blog</h1>
            <p>Welcome to the Common Sense Systems blog. Here we share insights on process automation, AI integration, and business optimization.</p>

            <hr>

            <!-- Blog posts are managed in src/includes/blog_posts.m4 -->
            BLOG_POSTS

        </section>
    </main>

    <!-- CTA Section -->
    <section id="contact" class="cta">
        <div class="container">
            <h2>Ready to Transform Your Business?</h2>
            <p>Let's discuss how our process automation and AI solutions can help you achieve your business goals.</p>
            <a href="/contact.html" class="btn">Schedule a Consultation</a>
        </div>
    </section>

    m4_include(`src/includes/footer.m4')m4_dnl
    m4_include(`src/includes/mobile.m4')m4_dnl
</body>
</html>
