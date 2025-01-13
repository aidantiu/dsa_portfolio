// Actions for buttons
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


// SHow validation box and search indicator if there is a message
document.addEventListener('DOMContentLoaded', function() {
    const validationBox = document.querySelector('#validation-box div');
    
    // Only set timeout if there's a message
    if (validationBox.innerHTML.trim() !== '') {
        setTimeout(() => {
            validationBox.innerHTML = '';  // Clear content but keep box
        }, 5000);
    }
});

// Close dropdowns when clicking outside
window.onclick = function (event) {
    const dropdowns = document.querySelectorAll('.binary-tree-simulator-dropdown-content');
    dropdowns.forEach(dropdown => {
        if (!dropdown.contains(event.target) && !event.target.matches('.binary-tree-simulator-dropdown-btn')) {
            dropdown.classList.remove('show');
        }
    });
};

// When user clicks a node, highlight it and set the selected node value
function selectNode(value) {
    // Remove highlight from previously selected node
    const previouslySelected = document.querySelector('.node.highlighted');
    if (previouslySelected) {
        previouslySelected.classList.remove('highlighted');
    }

    // Highlight the clicked node
    const selectedNode = document.querySelector(`.node[onclick="selectNode('${value}')"]`);
    if (selectedNode) {
        selectedNode.classList.add('highlighted');
    }

    // Set the selected node value in the hidden input field
    document.getElementById('selected_node').value = value;
}

// Add drag scroll functionality
document.addEventListener('DOMContentLoaded', () => {
    const svg = document.querySelector('.tree-svg');
    const container = document.querySelector('.tree-structure-container');
    const rootNode = document.querySelector('#node-0');
    let isDragging = false;
    let startX, startY, scrollLeft, scrollTop;

    // Center on root node (0) when page loads with tons of nodes
    if (rootNode) {
        const rootRect = rootNode.getBoundingClientRect();
        const containerRect = container.getBoundingClientRect();
        const svgRect = svg.getBoundingClientRect();
        
        // Calculate center position
        const centerX = (svgRect.width - containerRect.width) / 2;
        const centerY = rootRect.top - containerRect.top - 20; // Adjust for top padding
        
        // Add small delay to ensure proper positioning
        setTimeout(() => {
            container.scrollLeft = centerX;
            container.scrollTop = centerY;
        }, 100);
    }

    container.addEventListener('mousedown', (e) => {
        isDragging = true;
        container.style.cursor = 'grabbing';
        startX = e.pageX - container.offsetLeft;
        startY = e.pageY - container.offsetTop;
        scrollLeft = container.scrollLeft;
        scrollTop = container.scrollTop;
    });

    container.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX - container.offsetLeft;
        const y = e.pageY - container.offsetTop;
        const moveX = x - startX;
        const moveY = y - startY;
        container.scrollLeft = scrollLeft - moveX;
        container.scrollTop = scrollTop - moveY;
    });

    container.addEventListener('mouseup', () => {
        isDragging = false;
        container.style.cursor = 'grab';
    });

    container.addEventListener('mouseleave', () => {
        isDragging = false;
        container.style.cursor = 'grab';
    });

    // Prevent click events during drag
    container.addEventListener('click', (e) => {
        if (container.style.cursor === 'grabbing') {
            e.stopPropagation();
        }
    });
});

// Traverse the tree and highlight nodes
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.tree-structure-container');
    const searchPath = JSON.parse(container.dataset.searchPath || '[]');
    const searchFound = JSON.parse(container.dataset.searchFound || 'false');

    if (searchPath.length > 0) {
        animateSearch(searchPath, searchFound);
    }
});

function animateSearch(path, found) {
    const DELAY = 1000;
    const CHECK_DELAY = 500;
    const NOT_FOUND_DURATION = 1000;
    const RESET_DELAY = 2000;
    const totalTime = (path.length * DELAY) + (found ? 0 : NOT_FOUND_DURATION) + RESET_DELAY;

    // Hide validation box at start
    const validationBox = document.getElementById('validation-box');
    validationBox.style.display = 'none';

    // Show search indicator
    const searchIndicator = document.getElementById('search-indicator');
    searchIndicator.style.display = 'flex';

    // Reset all nodes to default color at start of new search
    document.querySelectorAll('.node circle').forEach(circle => {
        circle.setAttribute('fill', '#D9D9D9');
    });

    // Animate each node in the path
    path.forEach((nodeId, index) => {
        setTimeout(() => {
            const nodeCircle = document.querySelector(`#node-${nodeId} circle`);
            if (nodeCircle) {
                // First show blue for searching
                nodeCircle.setAttribute('fill', '#2196F3');
                
                // After checking, change color based on result
                setTimeout(() => {
                    if (found && index === path.length - 1) {
                        // Found node - green (permanent)
                        nodeCircle.setAttribute('fill', '#4CAF50');
                    } else {
                        // Not the target node - yellow (permanent)
                        nodeCircle.setAttribute('fill', '#FFEB3B');
                    }
                }, CHECK_DELAY);
            }
        }, index * DELAY);
    });

    // If node not found, flash red on all nodes
    if (!found) {
        setTimeout(() => {
            document.querySelectorAll('.node circle').forEach(circle => {
                circle.setAttribute('fill', '#F44336');
            });
        }, path.length * DELAY);
    }

    // Reset all nodes to default after animation completes
    setTimeout(() => {
        document.querySelectorAll('.node circle').forEach(circle => {
            circle.setAttribute('fill', '#D9D9D9');
        });
        validationBox.style.display = 'flex';
        searchIndicator.style.display = 'none';
    }, totalTime);
}

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
})

// For the dropdown buton showing the caret
document.querySelectorAll('.binary-tree-simulator-dropdown-btn').forEach(button => {
    button.addEventListener('click', function() {
        const dropdown = this.closest('.binary-tree-simulator-dropdown');
        dropdown.classList.toggle('active');
        
        // Close other dropdowns
        document.querySelectorAll('.binary-tree-simulator-dropdown.active').forEach(otherDropdown => {
            if (otherDropdown !== dropdown) {
                otherDropdown.classList.remove('active');
            }
        });
    });
});

// Close dropdowns when clicking outside
document.addEventListener('click', function(e) {
    if (!e.target.closest('.binary-tree-simulator-dropdown')) {
        document.querySelectorAll('.binary-tree-simulator-dropdown.active').forEach(dropdown => {
            dropdown.classList.remove('active');
        });
    }
});