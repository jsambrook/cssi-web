m4_dnl Blog post metadata and listing
m4_dnl Usage: Use these macros to manage blog post listings and metadata
m4_dnl
m4_dnl Define blog posts with their metadata
m4_define(`BLOG_POSTS', `m4_dnl
    <h2>2025</h2>
    <h3>April</h3>
    <ul class="blog-list">
        <li>
            <a href="/blog/2025/04/power-of-simplicity.html">The Power of Simplicity in Embedded Systems</a>
            <span class="blog-date">April 25, 2025</span>
        </li>
    </ul>
')m4_dnl

m4_dnl Define a macro for adding a new blog post to the index
m4_dnl Usage: ADD_BLOG_POST(`year', `month', `filename', `title', `date')
m4_define(`ADD_BLOG_POST', `
        <li>
            <a href="/blog/$1/$2/$3.html">$4</a>
            <span class="blog-date">$5</span>
        </li>
')m4_dnl

m4_dnl Define a macro for starting a new month section
m4_define(`BLOG_MONTH_SECTION', `
    <h3>$1</h3>
    <ul class="blog-list">
')m4_dnl

m4_dnl Define a macro for starting a new year section
m4_define(`BLOG_YEAR_SECTION', `
    <h2>$1</h2>
')m4_dnl
ADD_BLOG_POST(`2023', `12', `enhancing-client-communication-for-accountants-with-ai-assistants', `Enhancing Client Communication for Accountants with AI Assistants', `December 05, 2023')
ADD_BLOG_POST(`2025', `04', `ai-assistants-acupuncturists-client-bookings', `How AI Assistants Help Acupuncturists Manage Client Bookings', `April 25, 2025')
