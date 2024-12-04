// FOR ADDING Caret Symbol
// Add event listener to the caret to toggle dropdown visibility
const addCaret = document.querySelector('.insert-btn');
const addDropdown = document.querySelector('.dropdown-content');

addCaret.addEventListener('click', function(event) {
    event.stopPropagation(); // Prevent event from bubbling up to the button
    addDropdown.classList.toggle('active'); // Toggle dropdown visibility
});

// Close the dropdown if clicked outside the button or dropdown content
document.addEventListener('click', function(event) {
    if (!addDropdown.contains(event.target) && !addCaret.contains(event.target)) {
        addDropdown.classList.remove('active');
    }
});

// Make the dropdown content disappear when the cursor is not on the button or dropdown content
addCaret.addEventListener('mouseleave', function() {
    if (!addDropdown.contains(document.querySelector(':hover'))) {
        addDropdown.classList.remove('active');
    }
});

addDropdown.addEventListener('mouseleave', function() {
    if (!addDropdown.contains(document.querySelector(':hover'))) {
        addDropdown.classList.remove('active');
    }
});

function toggleDropdown() {
    var dropdown = document.querySelector('.dropdown');
    dropdown.classList.toggle('active');
}

// FOR DELETING Caret Symbol