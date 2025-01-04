function toggleDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle('show');

    // Close other dropdowns
    const otherDropdowns = document.querySelectorAll('.binary-tree-simulator-dropdown-content');
    otherDropdowns.forEach(d => {
        if (d !== dropdown && d.classList.contains('show')) {
            d.classList.remove('show');
        }
    });
}

// Close dropdowns when clicking outside
window.onclick = function (event) {
    const dropdowns = document.querySelectorAll('.binary-tree-simulator-dropdown-content');
    dropdowns.forEach(dropdown => {
        if (!dropdown.contains(event.target) && !event.target.matches('.binary-tree-simulator-dropdown-btn')) {
            dropdown.classList.remove('show');
        }
    });
};