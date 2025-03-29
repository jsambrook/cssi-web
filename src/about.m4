m4_define(`PAGE_TITLE', `About Us - Common Sense Systems')m4_dnl
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
                    <h1>About Common Sense</h1>
                    <p>More than 28 years of innovation in software engineering and business process improvement</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Content Section -->
    <section class="about-content">
        <div class="container">
            <div class="about-grid">
                <div class="about-section">
                    <h2>Innovating with AI & Business Intelligence</h2>
                    <p>Founded in 1996 as a software engineering services company, Common Sense has invested 28 years contributing to life-saving medical technologies including ultrasound systems and automatic defibrillators. In late 2024, we pivoted to business process improvement through targeted AI and workflow applications, helping business owners deliver superior service while finding greater satisfaction in their operations. This evolution builds on our decades of experience in software engineering and the Theory of Constraints.</p>
                </div>
                <div class="about-section">
                    <h2>My Commitment to You</h2>
                    <p>I'm passionate about implementing effective, lasting solutions to challenging business and automation problems. My approach is simple: if it's not win-win, it's no deal. Your success drives my business. When needed, I collaborate with trusted industry colleagues, always with your full knowledge and agreement. I also provide coaching for individuals and small business teams, combining technical expertise with the soft skills necessary for practice improvement. Resume available upon request.</p>
                    <p class="cta-text">Please contact us anytime to arrange a meeting.</p>
                    <a href="contact.html" class="btn">Get in Touch</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-company">
                    <h3>Common Sense</h3>
                    <p>We help businesses leverage automation and AI to work smarter, optimize processes, and achieve sustainable growth.</p>
                </div>
                <div class="footer-links">
                    <h4>Company</h4>
                    <ul>
                        <li><a href="about.html" class="active">About Us</a></li>
                        <li><a href="team.html">Team</a></li>
                        <li><a href="payments.html">Payments</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="ai-integration.html">AI Integration</a></li>
                        <li><a href="process-automation.html">Process Automation</a></li>
                        <li><a href="revenue-improvement.html">Revenue Improvement</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Contact</h4>
                    <ul>
                        <li><a href="mailto:contact@common-sense.com">contact@common-sense.com</a></li>
                        <li><a href="tel:+12066597951">main: (206) 659-7951</a></li>
                        <li><a href="tel:+14255019074">john: (425) 501-9074</a></li>
                        <li><a href="https://maps.google.com/?q=11227+NE+128+ST,+Unit+I-102,+Kirkland,+WA+98034">11227 NE 128 ST, Unit I-102</a></li>
                        <li><a href="https://maps.google.com/?q=Kirkland,+WA+98034">Kirkland, WA 98034</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 1996-2025 Common Sense Systems, Inc. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <elevenlabs-convai agent-id="XRQKG0KZygCOvX9xpVv2"></elevenlabs-convai>
	<script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>

    <!-- JavaScript for mobile menu toggle -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const menuToggle = document.querySelector('.menu-toggle');
            const navLinks = document.querySelector('.nav-links');

            menuToggle.addEventListener('click', function() {
                navLinks.classList.toggle('active');

                // Animate hamburger to X
                const spans = menuToggle.querySelectorAll('span');
                spans[0].style.transform = spans[0].style.transform === 'rotate(45deg) translate(5px, 5px)' ? '' : 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = spans[1].style.opacity === '0' ? '1' : '0';
                spans[2].style.transform = spans[2].style.transform === 'rotate(-45deg) translate(7px, -6px)' ? '' : 'rotate(-45deg) translate(7px, -6px)';
            });

            // Close menu when clicking on a link
            const links = navLinks.querySelectorAll('a');
            links.forEach(link => {
                link.addEventListener('click', () => {
                    navLinks.classList.remove('active');

                    // Reset hamburger
                    const spans = menuToggle.querySelectorAll('span');
                    spans[0].style.transform = '';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = '';
                });
            });
        });
    </script>
</body>
</html>
