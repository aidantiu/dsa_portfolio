from app import app
from flask import render_template, request, session, redirect, url_for
import random

@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    # Check if this is a redirected GET request
    is_redirected_get = session.get('is_redirected_get', False)
    
    array = []
    array_size = 10  # Default array size
    speed = 1  # Default speed multiplier
    show_confirmation = False
    
    if request.method == 'POST':
        # Get action from form if exists
        action = request.form.get('action')
        
        # If action is to continue or refresh, handle it
        if action in ['continue', 'refresh']:
            session['sorting_in_progress'] = False
            return redirect(url_for('sorting'))
        
        # Handle form submission
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

        # Generate or get array
        array_str = request.form.get('array', '')
        if array_str:
            try:
                array = list(map(int, array_str.split(',')))
            except ValueError:
                array = [random.randint(1, 100) for _ in range(array_size)]
        else:
            array = [random.randint(1, 100) for _ in range(array_size)]
        
        # Set sorting in progress
        session['sorting_in_progress'] = True
        
        # Redirect to prevent form resubmission
        resp = redirect(url_for('sorting'))
        session['is_redirected_get'] = True
        session['array'] = array
        session['array_size'] = array_size
        session['speed'] = speed
        
        return resp

    # Determine if confirmation should be shown
    show_confirmation = (
        session.get('sorting_in_progress', False) and 
        is_redirected_get
    )

    # Handle GET request logic
    if not is_redirected_get:
        # Clear the array on normal GET request
        array = []
        session.pop('sorting_in_progress', None)
    else:
        array = session.get('array', [])
        array_size = session.get('array_size', 10)
        speed = session.get('speed', 1.0)
        session['is_redirected_get'] = False

    # Render the main sorting template
    return render_template('sorting.html', 
                           array=array, 
                           array_size=array_size, 
                           speed=speed, 
                           sorting_in_progress=session.get('sorting_in_progress', False),
                           show_confirmation=show_confirmation)