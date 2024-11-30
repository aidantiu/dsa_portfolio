"""
This is the main file that runs the Flask application.
"""

# Run the app
from app import app

if __name__ == '__main__':
    app.run(debug=True)