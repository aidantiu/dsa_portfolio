""" 
This module contains the routes for the linkedlist blueprint.
"""

# Imports
from app import app
from flask import render_template

# Routing
@app.route('/linked-list')
def linkedlist():
    return render_template('linked-list.html', title='Linked List')
