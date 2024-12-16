// Clear button for clearing all contents
function clearAll() {
    document.getElementById('inputBox').value = '';
    document.querySelector('.postfix-result').innerHTML = '<span class="placeholder-text">Your postfix expression will appear here...</span>';
}

// Function to toggle between eye and eye-slash icons
// Uses Font Awesome classes for smooth transition
function toggleView() {
    const icon = document.querySelector('.toggle-button i');
    icon.classList.toggle('fa-eye');
    icon.classList.toggle('fa-eye-slash');
}