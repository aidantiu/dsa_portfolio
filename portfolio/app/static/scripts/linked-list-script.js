// Function to toggle dropdown visibility
function toggleDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId); // Target the clicked dropdown
    dropdown.classList.toggle('show'); // Show/Hide the dropdown

    // Close other dropdowns if they are open
    const otherDropdown = dropdownId === 'addDropdown' ? 'deleteDropdown' : 'addDropdown';
    const other = document.getElementById(otherDropdown);
    if (other && other.classList.contains('show')) {
        other.classList.remove('show');
    }
}

// Close the dropdowns when clicking outside
window.onclick = function (event) {
    if (!event.target.matches('.dropdown-btn') && !event.target.matches('#inputData') && !event.target.closest('.dropdown-content')) {
        const dropdowns = document.getElementsByClassName('dropdown-content');
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
};

// Add delay functionality to the input field for reading the number after typing
let typingTimer;
const typingDelay = 1000; // 1 second delay after typing stops

const inputField = document.getElementById('inputData');
inputField.addEventListener('input', function () {
    clearTimeout(typingTimer); // Clear the previous timer
    typingTimer = setTimeout(function () {
        const inputVal = inputField.value.trim();
        if (inputVal !== "") {
            console.log("User input: " + inputVal);
        }
    }, typingDelay);
});


// SHow validation box 
document.addEventListener('DOMContentLoaded', function() {
    const validationBox = document.getElementById('validation-wrapper');

    if (validationBox.innerHTML.trim() !== '') {
        validationBox.style.display = 'flex';
    }

    // Close validation box after 5 seconds
    setTimeout(() => {
        validationBox.style.display = 'none';
    }, 5000);
});

// Detect page refresh and reset the cookie
window.addEventListener("beforeunload", function() {
    document.cookie = "linked_list_data=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
});

// For how-to-use modal button
// Show modal on button click
document.getElementById('showHowToUse').addEventListener('click', () => {
    document.getElementById('howToUseModal').classList.add('active');
    document.querySelector('.modal-content').classList.add('active');
});

// Close modal with X button
document.getElementById('closeModal').addEventListener('click', () => {
    document.getElementById('howToUseModal').classList.remove('active');
    document.querySelector('.modal-content').classList.remove('active');
});

// Close modal when clicking overlay
document.querySelector('.modal-overlay').addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        document.getElementById('howToUseModal').classList.remove('active');
        document.querySelector('.modal-content').classList.remove('active');
    }
});