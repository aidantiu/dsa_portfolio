from app import app
from flask import render_template, request
import random


@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    array = []
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

    return render_template('sorting.html', array=array, array_size=array_size, speed=speed, err_message=err_message)
