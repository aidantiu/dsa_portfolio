from app import app
from flask import session, render_template, request, redirect, url_for
import random

@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
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

    return render_template('sorting.html', array=array, speed=speed, err_message=err_message)