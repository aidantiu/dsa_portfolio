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
    // Prevent closing dropdown if the input or dropdown is clicked
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
    typingTimer = setTimeout(function() {
        const inputVal = inputField.value;
        if (inputVal !== "") {
            // Process the number input here (e.g., call a function to read it)
            console.log("User input: " + inputVal);  // Replace with your function to handle the number
        }
    }, typingDelay);
});

// Show Search Result when the search button is clicked
function showSearchResult() {
    const searchResultBox = document.getElementById('search-result-box');

    // If there is a result from the server, display the search result box
    if (searchResultBox) {
        searchResultBox.classList.remove('hidden');
        searchResultBox.classList.add('visible');
    }
}

// Attach event listener to the "Search" button
document.querySelector('button[name="action"][value="search"]').addEventListener('click', function () {
    showSearchResult();
});

    // Prevent form submission if the input field is empty when searching
    document.getElementById('searchButton').addEventListener('click', function (event) {
        const inputField = document.getElementById('inputData');
        if (inputField.value.trim() === "") {
            event.preventDefault();  // Prevent form submission
            alert('Please enter a value to search.');
        }
    });

document.addEventListener('DOMContentLoaded', () => {
    const validationBox = document.getElementById('validation-box');

    if (validationBox.classList.contains('visible')) {
        setTimeout(() => {
            validationBox.classList.remove('visible');
        }, 5000); // Message persists for 5 seconds
    }
});