m4_define(`PAGE_TITLE', `Payments - Common Sense Systems')m4_dnl
m4_include(`src/includes/head.m4')m4_dnl
<body>
    <!-- Header -->
    <header>
        <div class="container">
            <nav>
                <a href="index.html" class="logo">
                    <span>Common Sense Systems, Inc.</span>
                </a>
                <ul class="nav-links">
                    <li><a href="index.html#services">Services</a></li>
                    <li><a href="index.html#process">Our Process</a></li>
                    <li><a href="index.html#testimonials">Success Stories</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="payments.html" class="active">Payments</a></li>
                </ul>
                <div class="menu-toggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>Make a Payment</h1>
                    <p>Select the appropriate payment option below for services rendered. All payments are securely processed through Stripe.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Payment Options Section -->
    <section class="payment-options">
        <div class="container">
            <div class="options-grid">
                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="5" width="20" height="14" rx="2"></rect>
                            <line x1="2" y1="10" x2="22" y2="10"></line>
                        </svg>
                    </div>
                    <h3>60 Minute Business Consultation</h3>
                    <p>Payment for a 60 minute business consultation meeting.</p>
                    <a href="https://buy.stripe.com/9AQeYKgas19D2di000" class="btn payment-btn">Pay</a>
                </div>

                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path>
                        </svg>
                    </div>
                    <h3>30 Minute Business Consultation</h3>
                    <p>Payment for a 30 minute business consultation meeting.</p>
                    <a href="https://buy.stripe.com/aEUg2ObUc2dHg48fZ0" class="btn payment-btn">Pay</a>
                </div>

                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 10h-4V4h-4v6H6l6 6 6-6z"></path>
                            <path d="M6 16v4h12v-4"></path>
                        </svg>
                    </div>
                    <h3>60 Minute Personal Consultation</h3>
                    <p>Payment for 60 minute personal consultation meeting.</p>
                    <a href="https://buy.stripe.com/aEUaIu3nG6tX3hmfZ3" class="btn payment-btn">Pay</a>
                </div>

                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="22 12 16 12 14 15 10 15 8 12 2 12"></polyline>
                            <path d="M5.45 5.11L2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"></path>
                        </svg>
                    </div>
                    <h3>30 Minute Personal Consultation</h3>
                    <p>Payment for 30 minute personal consultation meeting.</p>
                    <a href="https://buy.stripe.com/28ocQCaQ8bOhcRWfZ2" class="btn payment-btn">Pay</a>
                </div>

                <div class="option-card">
                    <div class="option-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
                            <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
                            <path d="M9 14h6"></path>
                            <path d="M9 18h6"></path>
                            <path d="M9 10h6"></path>
                        </svg>
                    </div>
                    <h3>Manage Your Subscription</h3>
                    <p>View and manage your subscription details, update payment methods, or download invoices.</p>
                    <a href="https://billing.stripe.com/p/login/bIYeVX1khda6axa3cc" class="btn payment-btn">Customer Portal</a>
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
