m4_define(`PAGE_TITLE', `Contact Us - Common Sense Systems')m4_dnl
m4_include(`src/includes/head.m4')m4_dnl
m4_include(`src/includes/navigation.m4')m4_dnl
<body>
    MAIN_NAVIGATION(`contact')

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>Get in Touch</h1>
                    <p>Choose how you'd like to connect with us. Talk to our AI assistant for immediate help, or schedule a personal meeting with John to discuss your business needs.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Options Section -->
    <section class="contact-options">
        <div class="container">
            <div class="options-grid">
                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path>
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                            <line x1="12" y1="19" x2="12" y2="23"></line>
                        </svg>
                    </div>
                    <h3>Talk to Our AI Assistant</h3>
                    <p>Get immediate answers to your questions about our services, process, and how we can help your business. See our widget in the lower right corner our pages.</p>
                </div>
                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                    </div>
                    <h3>Schedule a Meeting with John</h3>
                    <p>Book a one-on-one consultation to discuss your business needs and explore how we can help you achieve your goals.</p>
                    <a href="https://calendly.com/john-sambrook/60-minute-meeting" target="_blank" class="btn">Book Meeting</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
m4_include(`src/includes/footer.m4')m4_dnl

    <!-- Voice agent -->
m4_include(`src/includes/voice_agent.m4')m4_dnl

    <!-- JavaScript for mobile menu toggle -->
m4_include(`src/includes/mobile.m4')m4_dnl
</body>
</html>
