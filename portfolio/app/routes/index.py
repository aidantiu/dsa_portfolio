"""
This file is for the index route of the Flask App.
"""

# Imports
from app import app
from flask import render_template


# 
# Data for rendering
#

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

# List of works
works = [
    {
        "image_path": "images/linked-list.png", 
        "title": "Linked List Simulator", 
        "description": "The Linked List Simulator makes learning data structures a breeze! It’s an interactive, hands-on tool where you can see linked lists in action. Add, remove, and move through nodes in real-time, with everything laid out visually so it’s easy to follow. Whether you're new to linked lists or just need to brush up, this simulator makes it all simple, fun, and engaging. Start exploring and watch your understanding grow!",
        "route" : "linked-list"
    },
]

# Routes
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', profiles=profiles, works=works)


# Specific Project route
@app.route('/<project_route>')
def project(project_route):
    # Match the project by its route
    project = next((work for work in works if work["route"] == project_route), None)
    if not project:
        return "Project not found", 404

    # Dynamically render a template based on the project route
    try:
        return render_template(f'{project_route}.html', project=project)
    except Exception as e:
        return f"Template for {project_route} not found: {str(e)}", 404
