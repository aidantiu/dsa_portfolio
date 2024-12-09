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


    # List of profiles
    profiles = [
        {"image_path": "images/aidan.jpg", "name": "Aidan Tiu", "role": "Project Manager"},
        {"image_path": "images/renz.png", "name": "Renz Tyrone Arcilla", "role": "Back-end Developer"},
        {"image_path": "images/earl.jpg", "name": "Earl Clyde Banez", "role": "UI/UX Designer"},
        {"image_path": "images/denn.jpg", "name": "Denn Adrian Capus", "role": "Front-end Developer"},
        {"image_path": "images/roman.jpg", "name": "Roman Joseph Gallardo", "role": "Front-end Developer"},
        {"image_path": "images/railey.jpg", "name": "Railey Guinto", "role": "UI/UX Designer"},
        {"image_path": "images/arvie.jpg", "name": "Arvie Lastra", "role": "Back-end Developer"},
    ]
    
    return render_template('index.html', title='Home', profiles=profiles)