/**
 * Detects scroll direction and toggles the visibility of the navbar.
 * Adds 'navbar-hidden' class to the navbar when scrolling down,
 * and removes it when scrolling up.
 */
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        // Scroll down
        navbar.classList.add('navbar-hidden');
    } else {
        // Scroll up
        navbar.classList.remove('navbar-hidden');
    }
    lastScrollTop = scrollTop;
});