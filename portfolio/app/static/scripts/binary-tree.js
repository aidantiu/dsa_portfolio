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
    let isDragging = false;
    let startX, startY, scrollLeft, scrollTop;

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


