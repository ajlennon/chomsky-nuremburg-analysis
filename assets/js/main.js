// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const navTrigger = document.getElementById('nav-trigger');
    const menuIcon = document.querySelector('.menu-icon');
    
    if (navTrigger && menuIcon) {
        menuIcon.addEventListener('click', function() {
            navTrigger.checked = !navTrigger.checked;
        });
    }
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (navTrigger && navTrigger.checked) {
            if (!event.target.closest('.site-nav')) {
                navTrigger.checked = false;
            }
        }
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

