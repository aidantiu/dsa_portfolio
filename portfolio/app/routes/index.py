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
    {
        "image_path": "images/infix-to-postfix.png", 
        "title": "Infix To Postfix Converter", 
        "description": "Transform the way you understand expression conversion with the Infix to Postfix Converter! This interactive tool lets you input complex infix expressions and instantly see them converted to postfix notation. It’s designed to make learning operator precedence, stack operations, and expression parsing straightforward and intuitive. Whether you’re a student diving into algorithms or a developer brushing up on concepts, this converter provides a hands-on, engaging way to master the topic. Try it now and see the magic of postfix unfold!",
        "route" : "infix-to-postfix"
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
