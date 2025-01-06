// Clear button for clearing all contents
function clearAll() {
    document.getElementById('inputBox').value = '';
    document.querySelector('.postfix-result').innerHTML = '<span class="placeholder-text">Your postfix expression will appear here...</span>';
}

// Function to toggle between eye and eye-slash icons
// Uses Font Awesome classes for smooth transition
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

// Detect page refresh and reset the cookie
window.addEventListener("beforeunload", function() {
    document.cookie = "linked_list_data=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
});

// For modal contents
document.querySelector('.infix-to-postfix-text h1').addEventListener('click', () => {
    document.getElementById('howToUseModal').classList.add('active');
    document.querySelector('.modal-content').classList.add('active');
});

document.getElementById('closeModal').addEventListener('click', () => {
    document.getElementById('howToUseModal').classList.remove('active');
    document.querySelector('.modal-content').classList.remove('active');
});

document.querySelector('.modal-overlay').addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        document.getElementById('howToUseModal').classList.remove('active');
        document.querySelector('.modal-content').classList.remove('active');
    }
});