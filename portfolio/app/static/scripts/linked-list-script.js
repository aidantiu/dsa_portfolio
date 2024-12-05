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
    if (!event.target.matches('.dropdown-btn')) {
        const dropdowns = document.getElementsByClassName('dropdown-content');
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
};

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