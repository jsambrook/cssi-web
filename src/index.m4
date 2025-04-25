m4_define(`PAGE_TITLE', `Common Sense - Process Automation & AI Agency')m4_dnl
m4_include(`src/includes/head.m4')m4_dnl
m4_include(`src/includes/navigation.m4')m4_dnl
<body>
    MAIN_NAVIGATION(`home')

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <div class="hero-text">
                    <h1>Process Automation & AI Solutions for Your Business</h1>
                    <p>We help businesses streamline operations and leverage artificial intelligence to work smarter, not harder.</p>
                    <div class="hero-buttons">
                        <a href="#contact" class="btn">Get Started</a>
                        <a href="#services" class="btn secondary">Our Services</a>
                    </div>
                </div>
                <div class="hero-image">
                    <img src="/assets/img/business_automation_1_500x400.jpg" alt="Business process automation solutions for increased efficiency">
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <div class="section-title">
                <h2>Our Services</h2>
                <p>We offer tailored solutions to optimize your business processes and integrate AI to drive growth.</p>
            </div>
            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon">AI</div>
                    <h3>AI Integration</h3>
                    <p>Implement artificial intelligence solutions to optimize decision-making and automate complex tasks.</p>
                    <a href="ai-integration.html" class="btn secondary">Learn More</a>
                </div>
                <div class="service-card">
                    <div class="service-icon">BPA</div>
                    <h3>Business Process Automation</h3>
                    <!-- <p>Streamline workflows and reduce manual tasks with custom automation solutions.</p> -->
                    <p>Reclaim your workday with custom automation solutions that eliminate tedious tasks and simplify complex processes.</p>
                    <a href="process-automation.html" class="btn secondary">Learn More</a>
                </div>
                <div class="service-card">
                    <div class="service-icon">RI</div>
                    <h3>Revenue Improvement</h3>
                    <p>Implement targeted strategies to boost your bottom line through optimized pricing, sales processes, and cost reduction.</p>
                    <a href="revenue-improvement.html" class="btn secondary">Learn More</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Process Section -->
    <section id="process" class="process">
        <div class="container">
            <div class="section-title">
                <h2>Our Process</h2>
                <p>A proven methodology that delivers consistent results for businesses of all sizes.</p>
            </div>
            <div class="process-steps">
                <div class="process-step">
                    <div class="step-number">1</div>
                    <h3>Discovery</h3>
                    <p>We start by understanding your business, identifying pain points, and defining clear objectives.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">2</div>
                    <h3>Analysis</h3>
                    <p>Our experts analyze your current processes and systems to identify optimization opportunities.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">3</div>
                    <h3>Implementation</h3>
                    <p>We develop and deploy customized solutions tailored to your specific business needs.</p>
                </div>
                <div class="process-step">
                    <div class="step-number">4</div>
                    <h3>Optimization</h3>
                    <p>Continuous improvement and refinement to ensure long-term success and adaptability.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials">
        <div class="container">
            <div class="section-title">
                <h2>Success Stories</h2>
                <p>Hear from businesses that have transformed their operations with our solutions.</p>
            </div>
            <div class="testimonial-grid">
                <div class="testimonial-card">
                    <div class="testimonial-text">
                        <p>Common Sense helped us automate our customer onboarding process, reducing the time from days to minutes while improving accuracy.</p>
                    </div>
                    <div class="testimonial-author">
                        <div class="author-image">
                            <img src="/assets/img/round_icons/icon_4.png" alt="Client photo">
                        </div>
                        <div class="author-info">
                            <!-- <h4>Sarah Johnson</h4> -->
                            <p>VP of People, Tech Start-Up</p>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-text">
                      <p>The AI solution they implemented has simplified our day to day workload a lot. Things run more smoothly, the chaos is reduced, and people are happier.</p>
                    </div>
                    <div class="testimonial-author">
                        <div class="author-image">
                            <img src="/assets/img/round_icons/icon_6.png" alt="Client photo">
                        </div>
                        <div class="author-info">
                            <!-- <h4>Michael Rodriguez</h4> -->
                            <p>Owner, Landscape Company</p>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-text">
                        <p>Working with Common Sense was seamless. They understood our unique challenges and delivered solutions that exceeded our expectations.</p>
                    </div>
                    <div class="testimonial-author">
                        <div class="author-image">
                            <img src="/assets/img/round_icons/icon_10.png" alt="Client photo">
                        </div>
                        <div class="author-info">
                            <!-- <h4>Lisa Chen</h4> -->
                            <p>Owner, Printing Company</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section id="contact" class="cta">
        <div class="container">
            <h2>Ready to Transform Your Business?</h2>
            <p>Let's discuss how our process automation and AI solutions can help you achieve your business goals.</p>
            <a href="contact.html" class="btn">Schedule a Consultation</a>
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
