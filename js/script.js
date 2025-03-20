document.addEventListener('DOMContentLoaded', function() {
  // Code for Mobile Toggle Menu
  function setupMobileToggleMenu() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
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
    } else {
      console.error("Menu toggle or nav links not found");
    }
  }

  // Function to fetch and insert HTML content
  async function loadSection(url, placeholderId) {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Failed to load ${url}: ${response.status}`);
      }
      const html = await response.text();
      document.getElementById(placeholderId).innerHTML = html;
    } catch (error) {
      console.error(error);
      document.getElementById(placeholderId).innerHTML = "<p>Failed to load section.</p>"; // Placeholder for error message
    }
  }

  // Load all sections and setup menu after they're loaded
  async function initializePage() {
    try {
      // Load all sections concurrently with proper paths
      await Promise.all([
        loadSection('/header.html', 'header-placeholder'),
        loadSection('/hero.html', 'hero-placeholder'),
        loadSection('/services.html', 'services-placeholder'),
        loadSection('/process.html', 'process-placeholder'),
        loadSection('/testimonials.html', 'testimonials-placeholder'),
        loadSection('/cta.html', 'cta-placeholder'),
        loadSection('/footer.html', 'footer-placeholder')
      ]);

      // Setup Mobile Toggle Menu after all content is loaded
      setupMobileToggleMenu();
    } catch (error) {
      console.error('Failed to initialize page:', error);
    }
  }

  // Start the initialization process
  initializePage();
});
