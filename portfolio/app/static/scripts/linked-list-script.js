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

// Automatically hide the validation message after 5 seconds
document.addEventListener('DOMContentLoaded', () => {
    const validationBox = document.getElementById('validation-box');
    if (validationBox && validationBox.innerText.trim() !== "") {
        setTimeout(() => {
            validationBox.innerHTML = ''; // Clear the content
            validationBox.classList.add('hidden'); // Optionally hide the box
        }, 5000); // Message persists for 5 seconds
    }
});