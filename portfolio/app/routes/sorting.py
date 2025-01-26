from app import app
from flask import render_template, request
import random


@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    array = []
    array_size = 10  # Default array size 
    speed = 1  # Default speed multiplier
    
    if request.method == 'POST':
        # Get array size from form
        array_size_str = request.form.get('arraySize', '10')
        try:
            array_size = int(array_size_str)
        except ValueError:
            array_size = 10

        # Get speed from form
        speed_str = request.form.get('speed', '1')
        try:
            speed = float(speed_str)
        except ValueError:
            speed = 1.0

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