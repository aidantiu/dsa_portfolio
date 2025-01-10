// Hover effect for station select options
document.querySelectorAll('.station-select option:hover').forEach(option => {
    option.addEventListener('mouseover', function() {
        this.style.color = '#fff';
    });
    option.addEventListener('mouseout', function() {
        this.style.color = '#d62323';
    });
});

// Hover effect for station nodes
document.addEventListener('DOMContentLoaded', () => {
    const stationNodes = document.querySelectorAll('.station-node');
    
    stationNodes.forEach(node => {
        node.addEventListener('mouseenter', () => {
            node.style.transform = 'scale(1.05)';
            node.style.boxShadow = '0 0 15px rgba(107, 0, 161, 0.5)';
        });

        node.addEventListener('mouseleave', () => {
            node.style.transform = 'scale(1)';
            node.style.boxShadow = 'none';
        });
    });
});

// Output Info Section Hidden by Default
document.addEventListener('DOMContentLoaded', function() {
    const viewOutputButton = document.getElementById('view-output-btn');
    const outputSection = document.getElementById('output');
    const eyeIcon = viewOutputButton.querySelector('i');

    viewOutputButton.addEventListener('click', function(e) {
        e.preventDefault();
        outputSection.classList.toggle('visible');
        eyeIcon.classList.toggle('fa-eye');
        eyeIcon.classList.toggle('fa-eye-slash');
    });
});

// Toggle eye icon 
