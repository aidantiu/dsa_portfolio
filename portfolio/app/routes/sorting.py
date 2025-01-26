from app import app
from flask import render_template, request
import random


@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    array = []
    array_size = 10  # Default array size 
    speed = 1  # Default speed multiplier
    err_message  = None
    array_size = None
    
    if request.method == 'POST':
        # Get array size from form
        array_size_str = request.form.get('arraySize', '')
        try:
            if array_size_str:  # Check if the input is not empty
                array_size = int(array_size_str)
                if array_size < 5:
                    err_message = "You went below the min value (5)!"
                    array_size = None  # Reset array_size if invalid
                elif array_size > 100:
                    err_message = "You went past the max value (100)!"
                    array_size = None  # Reset array_size if invalid
            else:
                err_message = "Please enter an array size."
                array_size = None  # Reset array_size if invalid
        except ValueError:
            err_message = "Please enter a valid integer for the array size."
            array_size = None  # Reset array_size if invalid

        # Get speed from form
        speed_str = request.form.get('speed', '1')
        try:
            speed = float(speed_str)
        except ValueError:
            speed = 1.0

        # Generate array only if array_size is valid
        if array_size and err_message is None:
            array = [random.randint(1, 100) for _ in range(array_size)]


    # Pass instruction_steps to the template
    instruction_steps = get_instruction_steps()
    return render_template('sorting.html', 
                         array=array, 
                         array_size=array_size, 
                         speed=speed,
                         instruction_steps=instruction_steps)

def get_instruction_steps():
    return [
        "Enter a number between 5 and 100 to generate an array of that size.",
        "Click 'Create Array' button to generate a random array.",
        "Choose a sorting algorithm from the dropdown menu.",
        "Adjust animation speed using the speed control (0.25x - 2.00x).",
        "Use pause/play button to control the visualization.",
        "Use stop button to reset the visualization.",
        "Watch the sorting process in action with color-coded animations: Blue for default array elements; Yellow for elements being compared; Red for elements being swapped; and Green for elements in their final sorted position.",
    ]

    return render_template('sorting.html', array=array, array_size=array_size, speed=speed, err_message=err_message)
