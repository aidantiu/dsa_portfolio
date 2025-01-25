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

    return render_template('sorting.html', array=array, array_size=array_size, speed=speed)
