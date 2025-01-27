from app import app
from flask import session, render_template, request, redirect, url_for
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
                    session['err_message'] = "You went below the min value (5)!"
                elif array_size > 100:
                    session['err_message'] = "You went past the max value (100)!"
            else:
                session['err_message'] = "Please enter an array size."
        except ValueError:
            session['err_message'] = "Please enter a valid integer for the array size."

        # If there's no error, generate the array
        if 'err_message' not in session:
            speed_str = request.form.get('speed', '1')
            try:
                speed = float(speed_str)
            except ValueError:
                speed = 1.0

            array = [random.randint(1, 100) for _ in range(array_size)]
            session['array'] = array  # Store the generated array in session
            session['speed'] = speed  # Store speed in session
            return redirect(url_for('sorting'))  # Redirect to the same route

        return redirect(url_for('sorting'))  # Redirect to clear POST request

    # Handle GET request: Retrieve session data
    array = session.pop('array', [])
    speed = session.pop('speed', 1)
    err_message = session.pop('err_message', None)

    # Pass instruction_steps to the template
    instruction_steps = get_instruction_steps()
    return render_template('sorting.html', 
                         array=array, 
                         array_size=array_size, 
                         speed=speed,
                         instruction_steps=instruction_steps,
                         err_message=err_message)

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