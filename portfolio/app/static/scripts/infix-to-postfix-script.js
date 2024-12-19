// Clear button for clearing all contents
function clearAll() {
    document.getElementById('inputBox').value = '';
    document.querySelector('.postfix-result').innerHTML = '<span class="placeholder-text">Your postfix expression will appear here...</span>';
}

// Function to toggle between eye and eye-slash icons
// Uses Font Awesome classes for smooth transition
/* filepath: /c:/Users/flore/Jace's Coding Projects/dsa_portfolio/portfolio/app/static/scripts/infix-to-postfix.js */
function toggleView() {
    const splitContainer = document.querySelector('.split-container');
    const icon = document.querySelector('.toggle-button i');
    
    splitContainer.classList.toggle('active');
    
    if (splitContainer.classList.contains('active')) {
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}