"""
This file is for the index route of the Flask App.
"""

# Imports
from app import app
from flask import render_template

# Routes
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Aidan'}
    return render_template('index.html', title='Home', user=user)