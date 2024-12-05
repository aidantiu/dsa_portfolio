// Toggle function for Add dropdown
function toggleDropdown() {
    const addDropdownbtn = document.getElementById('dropdown-add');
    const addDropdown = document.getElementById('addDropdown');
    const deleteDropdown = document.getElementById('deleteDropdown');
    
    // If Add dropdown is clicked, toggle visibility
    addDropdown.classList.toggle('show');
    addDropdownbtn.classList.toggle('active');

    // Close Delete dropdown if it's open
    if (deleteDropdown.classList.contains('show')) {
        deleteDropdown.classList.remove('show');
        const deleteDropdownbtn = document.getElementById('dropdown-del');
        deleteDropdownbtn.classList.remove('active');
    }
}

// Toggle function for Delete dropdown
function toggleDeleteDropdown() {
    const deleteDropdownbtn = document.getElementById('dropdown-del');
    const deleteDropdown = document.getElementById('deleteDropdown');
    const addDropdown = document.getElementById('addDropdown');
    
    // If Delete dropdown is clicked, toggle visibility
    deleteDropdown.classList.toggle('show');
    deleteDropdownbtn.classList.toggle('active');
    
    // Close Add dropdown if it's open
    if (addDropdown.classList.contains('show')) {
        addDropdown.classList.remove('show');
        const addDropdownbtn = document.getElementById('dropdown-add');
        addDropdownbtn.classList.remove('active');
    }
}

// Update the Add button text and toggle the active class when an option is selected
function updateAddButtonText(option) {
    const addButtonText = document.getElementById('add-button-text');  // Target Add button text
    addButtonText.textContent = option;
    const addDropdown = document.getElementById('addDropdown');
    const addDropdownbtn = document.getElementById('dropdown-add');
    
    // Toggle active class on the Add button
    addDropdownbtn.classList.toggle('active');
    
    // Hide dropdown after selection
    addDropdown.classList.remove('show');
}

// Update the Delete button text and toggle the active class when an option is selected
function updateDeleteButtonText(option) {
    const deleteButtonText = document.getElementById('delete-button-text');  // Target Delete button text
    deleteButtonText.textContent = option;
    const deleteDropdown = document.getElementById('deleteDropdown');
    const deleteDropdownbtn = document.getElementById('dropdown-del');
    
    // Toggle active class on the Delete button
    deleteDropdownbtn.classList.toggle('active');
    
    // Hide dropdown after selection
    deleteDropdown.classList.remove('show');
}

// Option click handlers for Add dropdown
document.getElementById('addAtBeginning').addEventListener('click', function() {
    updateAddButtonText('Insert at Beginning');
});

document.getElementById('addAtEnd').addEventListener('click', function() {
    updateAddButtonText('Insert at End');
});

// Option click handlers for Delete dropdown
document.getElementById('deleteAtBeginning').addEventListener('click', function() {
    updateDeleteButtonText('Delete at Beginning');
});

document.getElementById('deleteAtEnd').addEventListener('click', function() {
    updateDeleteButtonText('Delete at End');
});
