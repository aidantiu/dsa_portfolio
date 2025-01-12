// For dropdowns in Double-ended queue
document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropdown-btn');
        
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            dropdowns.forEach(d => {
                if (d !== dropdown) {
                    d.classList.remove('active');
                }
            });
            dropdown.classList.toggle('active');
        });
    });

    

    // Close dropdowns when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.dropdown')) {
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('active');
            });
        }
    });
});

// SHow validation box and search indicator if there is a message
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