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
    {
        "image_path": "images/aidan.jpg",
        "name": "Aidan Tiu",
        "student_number": "2023-0001",
        "role": "Project Manager",
        "about": "I am an aspiring DevOps engineer passionate about streamlining workflows and improving system efficiency. Outside of programming, I enjoy playing basketball and cooking. A fun fact about me is that I have a lot of birthmarks!",
        "school": "XYZ University",
        "degree": "Bachelor of Science in Computer Science",
        "skills": ["Leadership", "Project Management", "Agile Development", "DevOps", "Python", "Docker", "Kubernetes", "CI/CD", "Git", "Jira", "Confluence"],  # Aidan's detailed skills
        "socials": {
            "facebook": "https://facebook.com/aidantiu",
            "instagram": "https://instagram.com/aidantiu",
            "github": "https://github.com/aidantiu",
            "linkedin": "https://linkedin.com/in/aidantiu"
        },
        "projects": [
            {"title": "Project Alpha", "description": "A comprehensive tool for task management.", "image_path": "../static/images/aidan.jpg"},
            {"title": "Project Beta", "description": "A mobile app for fitness tracking.", "image_path": "../static/images/aidan.jpg"}
        ]
    },
    {
        "image_path": "images/renz.png",
        "name": "Renz Tyrone Arcilla",
        "student_number": "2023-0002",
        "role": "Back-end Developer",
        "about": "Renz specializes in designing scalable APIs and optimizing server-side operations.",
        "school": "ABC Institute of Technology",
        "degree": "Bachelor of Science in Software Engineering",
        "skills": ["API Design", "Server-Side Optimization", "Database Management", "Node.js", "Express", "RESTful APIs"],  # Renz's skills
        "socials": {
            "facebook": "https://facebook.com/renzarcilla",
            "instagram": "https://instagram.com/renzarcilla",
            "github": "https://github.com/renzarcilla",
            "linkedin": "https://linkedin.com/in/renzarcilla"
        },
        "projects": [
            {"title": "E-Commerce Platform", "description": "A robust platform for online shopping.", "image_path": "images/ecommerce_platform.jpg"},
            {"title": "Inventory Management System", "description": "A tool for managing warehouse inventories.", "image_path": "images/inventory_management.jpg"}
        ]
    },
    {
        "image_path": "images/earl.jpg",
        "name": "Earl Clyde Banez",
        "student_number": "2023-0003",
        "role": "UI/UX Designer",
        "about": "Earl creates intuitive and visually compelling user interfaces to elevate the user experience.",
        "school": "National Design Institute",
        "degree": "Bachelor of Arts in Interaction Design",
        "skills": ["UI/UX Design", "Wireframing", "Prototyping", "Adobe XD", "Figma", "Sketch", "User Research"],  # Earl's skills
        "socials": {
            "facebook": "https://facebook.com/earlclydebanez",
            "instagram": "https://instagram.com/earlclyde",
            "github": "https://github.com/earlclyde",
            "linkedin": "https://linkedin.com/in/earlclyde"
        },
        "projects": [
            {"title": "User Dashboard Redesign", "description": "Improved UI for an enterprise dashboard application.", "image_path": "images/user_dashboard_redesign.jpg"},
            {"title": "Mobile Design System", "description": "Created a design system for mobile applications.", "image_path": "images/mobile_design_system.jpg"}
        ]
    },
    {
        "image_path": "images/denn.jpg",
        "name": "Denn Adrian Capus",
        "student_number": "2023-0004",
        "role": "Front-end Developer",
        "about": "Denn is passionate about creating responsive and accessible web interfaces.",
        "school": "Global Tech University",
        "degree": "Bachelor of Science in Web Development",
        "skills": ["HTML", "CSS", "JavaScript", "React", "Responsive Design", "Web Accessibility"],  # Denn's skills
        "socials": {
            "facebook": "https://facebook.com/denncapus",
            "instagram": "https://instagram.com/denncapus",
            "github": "https://github.com/denncapus",
            "linkedin": "https://linkedin.com/in/denncapus"
        },
        "projects": [
            {"title": "Responsive Portfolio", "description": "Built a portfolio showcasing personal projects.", "image_path": "images/responsive_portfolio.jpg"},
            {"title": "Interactive Quiz App", "description": "Developed a quiz app with real-time scoring.", "image_path": "images/interactive_quiz_app.jpg"}
        ]
    },
    {
        "image_path": "images/roman.jpg",
        "name": "Roman Joseph Gallardo",
        "student_number": "2023-0005",
        "role": "Front-end Developer",
        "about": "Roman focuses on building visually appealing and high-performing web applications.",
        "school": "TechWorld Academy",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["HTML", "CSS", "JavaScript", "Vue.js", "Webpack", "Performance Optimization"],  # Roman's skills
        "socials": {
            "facebook": "https://facebook.com/romanjoseph",
            "instagram": "https://instagram.com/romanjoseph",
            "github": "https://github.com/romanjoseph",
            "linkedin": "https://linkedin.com/in/romanjoseph"
        },
        "projects": [
            {"title": "Weather App", "description": "A weather forecasting web app with live data.", "image_path": "images/weather_app.jpg"},
            {"title": "Portfolio Website", "description": "A modern and responsive personal portfolio website.", "image_path": "images/portfolio_website.jpg"}
        ]
    },
    {
        "image_path": "images/railey.jpg",
        "name": "Railey Guinto",
        "student_number": "2023-0006",
        "role": "UI/UX Designer",
        "about": "Railey delivers seamless user experiences by combining aesthetics and functionality.",
        "school": "Creative Arts Academy",
        "degree": "Bachelor of Arts in Graphic Design",
        "skills": ["UX Research", "Wireframing", "UI Design", "Figma", "Prototyping", "Adobe Illustrator", "Photoshop"],  # Railey's skills
        "socials": {
            "facebook": "https://facebook.com/raileyginto",
            "instagram": "https://instagram.com/raileyginto",
            "github": "https://github.com/raileyginto",
            "linkedin": "https://linkedin.com/in/raileyginto"
        },
        "projects": [
            {"title": "E-Learning Platform", "description": "Designed an intuitive platform for online learning.", "image_path": "images/e_learning_platform.jpg"},
            {"title": "Food Delivery App", "description": "Created UI mockups for a food delivery application.", "image_path": "images/food_delivery_app.jpg"}
        ]
    },
    {
        "image_path": "images/arvie.jpg",
        "name": "Arvie Lastra",
        "student_number": "2023-0007",
        "role": "Back-end Developer",
        "about": "Arvie ensures the smooth operation of server-side systems and database management.",
        "school": "TechSphere University",
        "degree": "Bachelor of Science in Information Technology",
        "skills": ["Database Management", "API Development", "Node.js", "Express", "MongoDB", "Authentication"],  # Arvie's skills
        "socials": {
            "facebook": "https://facebook.com/arvielastra",
            "instagram": "https://instagram.com/arvielastra",
            "github": "https://github.com/arvielastra",
            "linkedin": "https://linkedin.com/in/arvielastra"
        },
        "projects": [
            {"title": "Payment Gateway Integration", "description": "Developed a secure payment gateway system.", "image_path": "images/payment_gateway_integration.jpg"},
            {"title": "API for Mobile App", "description": "Built APIs for a mobile app to handle user data.", "image_path": "images/api_for_mobile_app.jpg"}
        ]
    }
]

# List of works
works = [
    {
        "image_path": "images/linked-list.png", 
        "title": "Linked List Simulator", 
        "description": "The Linked List Simulator makes learning data structures a breeze! It's an interactive, hands-on tool where you can see linked lists in action. Add, remove, and move through nodes in real-time, with everything laid out visually so it's easy to follow.",
        "route": "linked-list"
    },
    {
        "image_path": "images/infix-to-postfix.png", 
        "title": "Infix To Postfix Converter", 
        "description": "Transform the way you understand expression conversion with the Infix to Postfix Converter! This interactive tool lets you input complex infix expressions and instantly see them converted to postfix notation. It's designed to make learning operator precedence, stack operations, and expression parsing straightforward and intuitive.",
        "route": "infix-to-postfix"
    },
    {
        "image_path": "images/queue.png",  # Make sure to add this image to your static/images folder
        "title": "Queue Operations Simulator",
        "description": "Experience queue data structures in action with our Queue Operations Simulator! This interactive tool demonstrates both simple queues and double-ended queues (deques). Add and remove elements from either end, visualize the queue structure, and understand FIFO operations through a user-friendly interface.",
        "route": "queue"
    }
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

# Profile route
@app.route('/profile/<profile_name>')
def profile(profile_name):
    # Match the profile by its name
    profile = next((p for p in profiles if profile_name == p["name"].lower().replace(" ", "-")), None)
    if not profile:
        return "Profile not found", 404

    # Render the profile page with detailed profile data
    return render_template('profile.html', profile=profile)