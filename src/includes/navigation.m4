m4_dnl Navigation template for all pages
m4_define(`MAIN_NAVIGATION', `
    <header>
        <div class="container">
            <nav>
                <a href="/index.html" class="logo">
                    <span>Common Sense Systems, Inc.</span>
                </a>
                <ul class="nav-links">
                    <li><a href="/index.html" m4_ifelse($1, `home', `class="active"')>Home</a></li>
                    <li><a href="/index.html#services" m4_ifelse($1, `services', `class="active"')>Services</a></li>
                    <li><a href="/blog/index.html" m4_ifelse($1, `blog', `class="active"')>Blog</a></li>
                    <li><a href="/contact.html" m4_ifelse($1, `contact', `class="active"')>Contact</a></li>
                </ul>
                <div class="menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </nav>
        </div>
    </header>
')m4_dnl
