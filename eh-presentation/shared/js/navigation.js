/**
 * EvergreenHealth AI Presentation - Navigation System
 * Handles presentation navigation, keyboard shortcuts, and page routing
 */

class PresentationNavigator {
  constructor() {
    this.pages = [
      'page_home/page_home',
      'page_healthcare_challenge/page_healthcare_challenge',
      'page_eh_org_facts/page_eh_org_facts',
      'page_eh_fin_facts/page_eh_fin_facts',
      'page_challenges_and_trends/page_challenges_and_trends',
      'page_introducing_voice_agents/page_introducing_voice_agents',
      'page_about_cssi/page_about_cssi',
      'page_compassionate_intermediaries/page_compassionate_intermediaries',
      'page_workforce_solution/page_workforce_solution',
      'page_our_services/page_our_services',
      'page_references/page_references',
      'page_va_architecture/page_va_architecture'
    ];
    
    this.currentPageIndex = this.getCurrentPageIndex();
    this.totalPages = this.pages.length;
    
    this.init();
  }
  
  init() {
    this.setupKeyboardNavigation();
    this.setupTouchNavigation();
    this.setupProgressIndicator();
    this.setupNavigationButtons();
    this.updatePageCounter();
  }
  
  getCurrentPageIndex() {
    const currentPath = window.location.pathname;
    // Extract the directory and file name (e.g., "page_home/page_home.html")
    const pathParts = currentPath.split('/');
    const fileName = pathParts.pop() || '';
    const directory = pathParts.pop() || '';
    
    if (fileName && directory) {
      const pagePath = `${directory}/${fileName.replace('.html', '')}`;
      const index = this.pages.indexOf(pagePath);
      return index !== -1 ? index : 0;
    }
    
    return 0;
  }
  
  setupKeyboardNavigation() {
    document.addEventListener('keydown', (event) => {
      switch (event.key) {
        case 'ArrowRight':
        case ' ': // Spacebar
        case 'PageDown':
          event.preventDefault();
          this.nextPage();
          break;
        case 'ArrowLeft':
        case 'PageUp':
          event.preventDefault();
          this.previousPage();
          break;
        case 'Home':
          event.preventDefault();
          this.goToPage(0);
          break;
        case 'End':
          event.preventDefault();
          this.goToPage(this.totalPages - 1);
          break;
        case 'f':
        case 'F11':
          if (event.key === 'f') {
            event.preventDefault();
            this.toggleFullscreen();
          }
          break;
        case 'Escape':
          if (document.fullscreenElement) {
            document.exitFullscreen();
          }
          break;
      }
    });
  }
  
  setupTouchNavigation() {
    let touchStartX = 0;
    let touchEndX = 0;
    const minSwipeDistance = 50;
    
    document.addEventListener('touchstart', (event) => {
      touchStartX = event.changedTouches[0].screenX;
    }, { passive: true });
    
    document.addEventListener('touchend', (event) => {
      touchEndX = event.changedTouches[0].screenX;
      this.handleSwipe(touchStartX, touchEndX, minSwipeDistance);
    }, { passive: true });
  }
  
  handleSwipe(startX, endX, minDistance) {
    const distance = endX - startX;
    
    if (Math.abs(distance) >= minDistance) {
      if (distance > 0) {
        // Swipe right - go to previous page
        this.previousPage();
      } else {
        // Swipe left - go to next page
        this.nextPage();
      }
    }
  }
  
  setupNavigationButtons() {
    // Previous button
    const prevButton = document.querySelector('.nav-prev');
    if (prevButton && !prevButton.disabled) {
      prevButton.addEventListener('click', () => this.previousPage());
    }
    
    // Next button
    const nextButton = document.querySelector('.nav-next');
    if (nextButton && !nextButton.disabled) {
      nextButton.addEventListener('click', () => this.nextPage());
    }
    
    // Home button
    const homeButton = document.querySelector('.nav-home');
    if (homeButton && !homeButton.disabled) {
      homeButton.addEventListener('click', () => this.goToPage(0));
    }
  }
  
  setupProgressIndicator() {
    const progressFill = document.querySelector('.progress-fill');
    if (progressFill) {
      const progress = ((this.currentPageIndex + 1) / this.totalPages) * 100;
      progressFill.style.width = `${progress}%`;
    }
  }
  
  updatePageCounter() {
    const pageCounter = document.querySelector('.page-counter');
    if (pageCounter) {
      pageCounter.textContent = `${this.currentPageIndex + 1} of ${this.totalPages}`;
    }
  }
  
  nextPage() {
    // Check if next button is disabled in HTML
    const nextButton = document.querySelector('.nav-next');
    if (nextButton && nextButton.disabled) {
      return; // Don't navigate if button is explicitly disabled
    }
    
    if (this.currentPageIndex < this.totalPages - 1) {
      this.goToPage(this.currentPageIndex + 1);
    }
  }
  
  previousPage() {
    if (this.currentPageIndex > 0) {
      this.goToPage(this.currentPageIndex - 1);
    }
  }
  
  goToPage(pageIndex) {
    if (pageIndex >= 0 && pageIndex < this.totalPages) {
      const pagePath = this.pages[pageIndex];
      const url = `../${pagePath}.html`;
      
      // Use history API for smooth navigation
      if (window.location.pathname !== url) {
        window.location.href = url;
      }
    }
  }
  
  toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.log(`Error attempting to enable fullscreen: ${err.message}`);
      });
    } else {
      document.exitFullscreen();
    }
  }
  
  // Public API for manual navigation
  static getInstance() {
    if (!window.presentationNavigator) {
      window.presentationNavigator = new PresentationNavigator();
    }
    return window.presentationNavigator;
  }
}

// Utility functions for common presentation needs
const PresentationUtils = {
  // Animate elements on page load
  animateOnLoad(selector, delay = 0) {
    const elements = document.querySelectorAll(selector);
    elements.forEach((element, index) => {
      element.style.opacity = '0';
      element.style.transform = 'translateY(20px)';
      element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      
      setTimeout(() => {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0)';
      }, delay + (index * 100));
    });
  },
  
  // Add loading state to buttons
  setButtonLoading(button, loading = true) {
    if (loading) {
      button.disabled = true;
      button.innerHTML = '<span class="loading-spinner"></span> Loading...';
    } else {
      button.disabled = false;
      button.innerHTML = button.dataset.originalText || 'Continue';
    }
  },
  
  // Smooth scroll to element
  scrollToElement(selector, offset = 0) {
    const element = document.querySelector(selector);
    if (element) {
      const elementPosition = element.getBoundingClientRect().top + window.pageYOffset;
      window.scrollTo({
        top: elementPosition - offset,
        behavior: 'smooth'
      });
    }
  },
  
  // Show/hide elements with animation
  toggleElement(selector, show = true) {
    const element = document.querySelector(selector);
    if (element) {
      if (show) {
        element.style.display = 'block';
        element.style.opacity = '0';
        element.style.transform = 'scale(0.95)';
        element.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        
        requestAnimationFrame(() => {
          element.style.opacity = '1';
          element.style.transform = 'scale(1)';
        });
      } else {
        element.style.opacity = '0';
        element.style.transform = 'scale(0.95)';
        
        setTimeout(() => {
          element.style.display = 'none';
        }, 300);
      }
    }
  }
};

// Initialize navigation when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  // Initialize navigation
  const navigator = PresentationNavigator.getInstance();
  
  // Add smooth animations to page content
  PresentationUtils.animateOnLoad('.page-content > *', 200);
  
  // Add keyboard shortcut hints for development
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    console.log('Presentation Navigation:');
    console.log('→ / Space: Next page');
    console.log('← : Previous page');
    console.log('Home: First page');
    console.log('End: Last page');
    console.log('F: Toggle fullscreen');
    console.log('ESC: Exit fullscreen');
  }
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { PresentationNavigator, PresentationUtils };
}