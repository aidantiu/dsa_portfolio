function toggleDropdown(dropdownId) {
    const dropdown = document.getElementById(dropdownId);
    dropdown.classList.toggle('show');

    // Close other dropdowns
    const dropdowns = document.getElementsByClassName('dropdown-content');
    Array.from(dropdowns).forEach(d => {
        if (d.id !== dropdownId && d.classList.contains('show')) {
            d.classList.remove('show');
        }
    });
}


// Close dropdowns when clicking outside
window.onclick = function(event) {
    if (!event.target.closest('.speed-dropdown-btn')) {
        const dropdowns = document.getElementsByClassName('dropdown-content');
        Array.from(dropdowns).forEach(dropdown => {
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            }
        });
    }
};

// Animation for sorting algorithms
let array = [];
let isSorting = false;
let isPaused = false;
let sortingInterval;
let currentStep = { i: 0, j: 0 };
let currentAlgorithm = '';
let baseSpeed = 100;
let speedMultiplier = parseFloat(document.getElementById('speed_value').value) || 1;
let sortedIndices = [];

// Update speed function
function setSpeed(multiplier) {
    speedMultiplier = multiplier;
    // Update UI with full button content
    const speedBtn = document.querySelector('.speed-dropdown-btn');
    speedBtn.innerHTML = `<span>${multiplier.toFixed(2)}x</span><i class="fas fa-fast-forward"></i>`;
    
    // Update hidden input
    document.getElementById('speed_value').value = multiplier;
    
    // Handle active sorting
    if (isSorting) {
        clearInterval(sortingInterval);
        startSort(currentAlgorithm);
    }
    
    // Close dropdown after selection
    const dropdown = document.getElementById('speedDropdown');
    if (dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
    }
}

// Initialize speed on page load
window.onload = function() {
    document.querySelector('.pause-stop').style.display = 'none'; // Hide pause/stop controls on load
    try {
        const savedSpeed = document.getElementById('speed_value').value;
        if (savedSpeed) {
            const speed = parseFloat(savedSpeed);
            if (!isNaN(speed) && speed > 0) {
                setSpeed(speed);
            } else {
                setSpeed(1); // Default to 1x if invalid
            }
        }
    } catch (error) {
        console.error('Error initializing speed:', error);
        setSpeed(1); // Fallback to default
    }
};

// Update form submit handling
document.querySelector('form').addEventListener('submit', function(e) {
    // Ensure speed value is included in form submission
    document.getElementById('speed_value').value = speedMultiplier;
});


// Helper functions
function getArrayFromDOM() {
    return Array.from(document.getElementsByClassName('array-element'))
        .map(el => parseInt(el.querySelector('p').textContent));
}

// Add isSorted check function
function isSorted(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}

// Update visualization function
function updateArrayView(arr, comparing = [], swapping = [], sorted = false) {
    const elements = document.getElementsByClassName('array-element');
    
    for (let i = 0; i < elements.length; i++) {
        const element = elements[i];
        
        element.style.transition = 'all 0.3s ease';
        element.style.height = `${arr[i] + 150}px`;
        element.querySelector('p').textContent = arr[i];
        
        // Default state
        element.style.background = 'linear-gradient(to bottom, #007bff, #0056b3)';
        element.style.transform = 'scale(1)';
        
        // Comparing state
        if (comparing.includes(i)) {
            element.style.background = 'linear-gradient(to bottom, #ffd700, #ffbf00)';
            element.style.transform = 'scale(1.1)';
        }
        
        // Swapping state
        if (swapping.includes(i)) {
            element.style.background = 'linear-gradient(to bottom, #ff4444, #cc0000)';
            element.style.transform = 'scale(1.2)';
        }
        
        // Sequential sorted state
        if (sortedIndices.includes(i)) {
            element.style.background = 'linear-gradient(to bottom, #66bb6a, #388e3c)';
            element.style.transform = 'scale(1.05)';
        }
    }
}

// Sorting algorithms with animation
function bubbleSort() {
    array = getArrayFromDOM();
    let { i, j } = currentStep;
    
    sortingInterval = setInterval(() => {
        if (i >= array.length) {
            stopSort();
            return;
        }
        
        if (j >= array.length - i - 1) {
            j = 0;
            i++;
            return;
        }
        
        if (array[j] > array[j + 1]) {
            [array[j], array[j + 1]] = [array[j + 1], array[j]];
            updateArrayView(array, [j, j + 1]);
        }
        j++;
        currentStep = {i, j};
    }, baseSpeed / speedMultiplier);
}

// Insertion Sort
function insertionSort() {
    array = getArrayFromDOM();
    let {i, j} = currentStep;
    
    sortingInterval = setInterval(() => {
        if (i >= array.length) {
            stopSort();
            return;
        }
        
        if (j >= 0 && array[j] > array[j + 1]) {
            [array[j], array[j + 1]] = [array[j + 1], array[j]];
            updateArrayView(array, [j, j + 1]);
            j--;
        } else {
            i++;
            j = i - 1;
        }
        currentStep = {i, j};
    }, baseSpeed / speedMultiplier);
}

// Selection Sort
function selectionSort() {
    array = getArrayFromDOM();
    let {i, j} = currentStep;
    let min_idx = i;
    
    sortingInterval = setInterval(() => {
        if (i >= array.length) {
            stopSort();
            return;
        }
        
        if (j >= array.length) {
            [array[i], array[min_idx]] = [array[min_idx], array[i]];
            updateArrayView(array, [], [i, min_idx]);
            i++;
            j = i + 1;
            min_idx = i;
            currentStep = {i, j};
            return;
        }
        
        updateArrayView(array, [j, min_idx]);
        if (array[j] < array[min_idx]) {
            min_idx = j;
        }
        j++;
        currentStep = {i, j};
    }, baseSpeed / speedMultiplier);
}

// Merge sort
function mergeSort() {
    array = getArrayFromDOM();
    let temp = [...array];
    let currSize = 1;
    let leftStart = 0;

    sortingInterval = setInterval(() => {
        if (currSize >= array.length) {
            stopSort();
            return;
        }

        if (leftStart >= array.length - 1) {
            leftStart = 0;
            currSize *= 2;
            return;
        }

        const mid = Math.min(leftStart + currSize - 1, array.length - 1);
        const rightEnd = Math.min(leftStart + 2 * currSize - 1, array.length - 1);

        merge(temp, leftStart, mid, rightEnd);
        leftStart += 2 * currSize;
    }, baseSpeed / speedMultiplier);
}

function merge(arr, left, mid, right) {
    let n1 = mid - left + 1;
    let n2 = right - mid;
    let L = new Array(n1), R = new Array(n2);

    for (let i = 0; i < n1; i++) L[i] = arr[left + i];
    for (let j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    let i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i++];
        } else {
            arr[k] = R[j++];
        }
        array[k] = arr[k];
        updateArrayView(array, [k]); // Highlight current merge step
        k++;
    }

    while (i < n1) {
        arr[k] = L[i++];
        array[k] = arr[k];
        updateArrayView(array, [k]); // Highlight remaining elements in L
        k++;
    }

    while (j < n2) {
        arr[k] = R[j++];
        array[k] = arr[k];
        updateArrayView(array, [k]); // Highlight remaining elements in R
        k++;
    }
}

function quickSort() {
    array = getArrayFromDOM();
    let { i, j } = currentStep;
    let stack = [[0, array.length - 1]];
    let partitionState = 'start'; // Track the phase of the partition

    sortingInterval = setInterval(() => {
        if (stack.length === 0) {
            stopSort();
            if (isSorted(array)) updateArrayView(array, [], [], true);
            return;
        }

        let [low, high] = stack[stack.length - 1]; // Peek at the top of the stack

        if (low >= high) {
            stack.pop(); // Remove fully processed partition
            return;
        }

        switch (partitionState) {
            case 'start':
                i = low - 1;
                j = low;
                partitionState = 'partition'; // Transition to partition phase
                updateArrayView(array); // Reset styles
                break;

            case 'partition':
                if (j < high) {
                    updateArrayView(array, [j, high]); // Highlight comparison
                    if (array[j] <= array[high]) {
                        i++;
                        [array[i], array[j]] = [array[j], array[i]]; // Swap smaller element
                        updateArrayView(array, [j, high], [i]); // Highlight swap
                    }
                    j++;
                } else {
                    // Complete partitioning, place pivot in correct position
                    i++;
                    [array[i], array[high]] = [array[high], array[i]];
                    updateArrayView(array, [], [i, high]); // Highlight pivot swap

                    // Add sub-partitions to stack
                    stack.pop(); // Remove current partition
                    if (i - 1 > low) stack.push([low, i - 1]); // Left sub-partition
                    if (i + 1 < high) stack.push([i + 1, high]); // Right sub-partition

                    partitionState = 'start'; // Reset for next partition
                }
                break;
        }

        currentStep = { i, j };
    }, baseSpeed / speedMultiplier);
}

// Start sorting function
function startSort(algorithm, resuming = false) {
    if (isSorting && !isPaused && !resuming) return;
    
    if (!resuming) {
        array = getArrayFromDOM();
        currentStep = { i: 0, j: 0 };
    }
    
    isSorting = true;
    isPaused = false;
    currentAlgorithm = algorithm;
    
    // Show pause/stop controls when sorting starts
    document.querySelector('.pause-stop').style.display = 'flex';
    
    switch(algorithm) {
        case 'bubble':
            bubbleSort(currentStep);
            break;
        case 'selection':
            selectionSort(currentStep);
            break;
        case 'insertion':
            insertionSort(currentStep);
            break;
        case 'merge':
            mergeSort(currentStep);
            break;
        case 'quick':
            quickSort(currentStep);
            break;
    }
}

// Stop sorting function
function pauseSort() {
    isPaused = !isPaused;
    const pauseButton = document.getElementById('pause');
    const pauseIcon = pauseButton.querySelector('i');
    
    if (isPaused) {
        clearInterval(sortingInterval);
        pauseIcon.classList.remove('fa-pause');
        pauseIcon.classList.add('fa-play');
    } else {
        pauseIcon.classList.remove('fa-play');
        pauseIcon.classList.add('fa-pause');
        startSort(currentAlgorithm, true);
    }
}

// Update stopSort function
function stopSort() {
    clearInterval(sortingInterval);
    isSorting = false;
    isPaused = false;
    currentStep = { i: 0, j: 0 };
    
    // Reset pause button icon
    const pauseButton = document.getElementById('pause');
    const pauseIcon = pauseButton.querySelector('i');
    pauseIcon.classList.remove('fa-play');
    pauseIcon.classList.add('fa-pause');
    
    // Hide controls when sorting stops
    document.querySelector('.pause-stop').style.display = 'none';
    
    if (isSorted(array)) {
        let index = array.length - 1;
        const sortingAnimation = setInterval(() => {
            if (index < 0) {
                clearInterval(sortingAnimation);
                return;
            }
            sortedIndices.push(index);
            updateArrayView(array);
            index--;
        }, baseSpeed / speedMultiplier);
    } else {
        sortedIndices = [];
        updateArrayView(array);
    }
}


// Function to display validation message inside the validation-box
function showValidationMessage(message) {
    const validationBox = document.querySelector('.validation-box');
    const validationMessage = validationBox.querySelector('p');
    const exclamationIcon = validationBox.querySelector('img');

    if (message) {
        // Update the message content and show the validation box
        validationMessage.textContent = message;
        validationBox.style.display = 'flex';
        exclamationIcon.style.display = 'block';

        // Hide the box after 5 seconds
        setTimeout(function() {
            validationBox.style.display = 'none';
            validationMessage.textContent = '';
            exclamationIcon.style.display = 'none';
        }, 5000); // Hide after 5 seconds
    } else {
        // Hide the validation box and clear the message content
        validationBox.style.display = 'none';
        validationMessage.textContent = '';
        exclamationIcon.style.display = 'none';
    }
}

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

// Timer for validation message
document.addEventListener('DOMContentLoaded', function() {
    const validationBox = document.querySelector('.validation-box');
    const errMessage = validationBox.dataset.errMessage; // Access the error message from the data attribute

    // Only show the validation box if there is an error message
    if (errMessage) {
        showValidationMessage(errMessage);
    }
});

// Prevent form submission (array creation) if sorting is in progress
document.querySelector('form').addEventListener('submit', function(e) {
    if (isSorting && !isPaused) {
        // Show validation message
        showValidationMessage("You are currently sorting. Please pause before submitting.");
        e.preventDefault(); // Prevent form submission
    }
});

document.querySelector('[name="generate"]').addEventListener('click', function(e) {
    if (isSorting && !isPaused) {
        showValidationMessage("You are currently sorting. Please pause before creating a new array.");
        e.preventDefault(); // Prevent array creation
    }
});
