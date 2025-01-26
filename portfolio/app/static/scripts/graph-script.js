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

// Output Info Section and Toggle Button
document.addEventListener('DOMContentLoaded', function() {
    const viewOutputButton = document.getElementById('view-output-btn');
    const outputSection = document.getElementById('output');
    const eyeIcon = viewOutputButton.querySelector('i');
    const form = document.querySelector('form');
    const sourceStation = document.getElementById('source-station');
    const destinationStation = document.getElementById('destination-station');
    const validationBox = document.querySelector('#validation-box div');

    // Show output initially if there's already data
    if (outputSection.querySelector('.path-container') || 
        outputSection.querySelector('.journey-container')) {
        outputSection.classList.add('visible');
        eyeIcon.classList.remove('fa-eye');
        eyeIcon.classList.add('fa-eye-slash');
    }

    // Handle form submission
    form.addEventListener('submit', function(e) {
        // Check if stations are selected
        if (!sourceStation.value || !destinationStation.value) {
            e.preventDefault();
            validationBox.innerHTML = '<img src="/static/icons/exclamation-circle.svg" alt="Error"><p>Please select both stations</p>';
            outputSection.classList.remove('visible');
            eyeIcon.classList.add('fa-eye');
            eyeIcon.classList.remove('fa-eye-slash');
            return false;
        }

        // Check if same station selected
        if (sourceStation.value === destinationStation.value) {
            e.preventDefault();
            validationBox.innerHTML = '<img src="/static/icons/exclamation-circle.svg" alt="Error"><p>Please select different stations</p>';
            outputSection.classList.remove('visible');
            eyeIcon.classList.add('fa-eye');
            eyeIcon.classList.remove('fa-eye-slash');
            return false;
        }

        // If validation passes, show output section
        outputSection.classList.add('visible');
        eyeIcon.classList.remove('fa-eye');
        eyeIcon.classList.add('fa-eye-slash');
    });

    // Toggle button functionality
    viewOutputButton.addEventListener('click', function(e) {
        e.preventDefault();
        outputSection.classList.toggle('visible');
        eyeIcon.classList.toggle('fa-eye');
        eyeIcon.classList.toggle('fa-eye-slash');
    });
});

// Add zoom functionality
document.addEventListener('DOMContentLoaded', function() {
    const graphBox = document.querySelector('.graph-box');
    const mapImage = graphBox.querySelector('img');
    let scale = 1;
    let isDragging = false;
    let startX, startY, translateX = 0, translateY = 0;
    const ZOOM_SPEED = 0.1;
    const MAX_ZOOM = 4;
    const MIN_ZOOM = 0.5;

    // Create zoom controls
    const zoomControls = document.createElement('div');
    zoomControls.className = 'zoom-controls';
    zoomControls.innerHTML = `
        <button class="zoom-in"><i class="fas fa-plus"></i></button>
        <button class="zoom-out"><i class="fas fa-minus"></i></button>
        <button class="zoom-reset"><i class="fas fa-undo"></i></button>
    `;
    graphBox.appendChild(zoomControls);

    // Zoom with mouse wheel
    graphBox.addEventListener('wheel', function(e) {
        e.preventDefault();
        const rect = mapImage.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        const delta = e.deltaY > 0 ? -1 : 1;
        const newScale = scale + (delta * ZOOM_SPEED);
        
        if (newScale >= MIN_ZOOM && newScale <= MAX_ZOOM) {
            scale = newScale;
            updateTransform(mouseX, mouseY);
        }
    });

    // Pan functionality
    graphBox.addEventListener('mousedown', function(e) {
        isDragging = true;
        startX = e.clientX - translateX;
        startY = e.clientY - translateY;
        mapImage.style.cursor = 'grabbing';
    });

    document.addEventListener('mousemove', function(e) {
        if (!isDragging) return;
        translateX = e.clientX - startX;
        translateY = e.clientY - startY;
        updateTransform();
    });

    document.addEventListener('mouseup', function() {
        isDragging = false;
        mapImage.style.cursor = 'grab';
    });

    // Zoom controls functionality
    document.querySelector('.zoom-in').addEventListener('click', () => {
        if (scale < MAX_ZOOM) {
            scale += ZOOM_SPEED;
            updateTransform();
        }
    });

    document.querySelector('.zoom-out').addEventListener('click', () => {
        if (scale > MIN_ZOOM) {
            scale -= ZOOM_SPEED;
            updateTransform();
        }
    });

    document.querySelector('.zoom-reset').addEventListener('click', () => {
        scale = 1;
        translateX = 0;
        translateY = 0;
        updateTransform();
    });

    function updateTransform(mouseX, mouseY) {
        mapImage.style.transformOrigin = 'center center';
        mapImage.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
    }
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

// Notification Timer
document.addEventListener('DOMContentLoaded', () => {
    const notification = document.getElementById('notification');
    if (notification) {
        setTimeout(() => {
            notification.style.display = 'none'; // Hides the notification
        }, 5000); // 5 seconds
    }
});