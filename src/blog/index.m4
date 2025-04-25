m4_dnl — blog index page — include site wrapper
m4_include(`src/includes/head.m4')dnl

<body>
  m4_include(`src/includes/navigation.m4')dnl

  <main class="container blog-listing">
    <h1>Blog Articles</h1>

    m4_dnl — this macro spits out your <ul>…</ul> listing
    BLOG_POSTS
  </main>

  m4_include(`src/includes/footer.m4')dnl
  m4_include(`src/includes/mobile.m4')dnl
</body>
</html>
