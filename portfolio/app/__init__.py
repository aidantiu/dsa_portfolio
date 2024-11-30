"""
This file is for the initialization of the Flask App.
"""

# app/__init__.py
from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Import the routes from the routes folder
from app.routes import *
