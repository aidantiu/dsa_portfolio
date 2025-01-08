// Dropdown for stations
document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.station-select select');

    dropdowns.forEach(dropdown => {
        // Add click listener to toggle active state
        dropdown.addEventListener('click', function() {
            // Remove active class from all dropdowns
            dropdowns.forEach(d => d.classList.remove('active'));
            // Add active class to clicked dropdown
            this.classList.add('active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.station-select')) {
                dropdowns.forEach(d => d.classList.remove('active'));
            }
        });
    });
});