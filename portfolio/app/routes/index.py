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
        "skills": ["Leadership", "Project Management", "Agile Development", "Full Stack Development", "Web Scraping", "DevOps", "Cloud Computing", "AWS", "Python", "Docker", "Kubernetes", "CI/CD", "Git", "Jira", "Confluence", "Linux"],  # Aidan's detailed skills
        "socials": {
            "facebook": "https://www.facebook.com/haha.hauwieks",
            "instagram": "https://www.instagram.com/y.mnwri/",
            "github": "https://github.com/aidantiu",
            "linkedin": "https://www.linkedin.com/in/aidan-tiu-58650520b/"
        },
        "projects": [
            {"title": "PUPGS Alumni Engagement Portal System", "description": "The PUPGS Alumni Engagement Portal System is an online platform designed to connect and engage alumni of the Polytechnic University of the Philippines Graduate School. It offers features such as alumni profiles, event updates, and networking opportunities to foster continuous interaction and collaboration within the PUPGS community.", "image_path": "../static/images/aidan_PUPGS Alumni Portal.jpg"},
            {"title": "PUPSIS Grades and Contact Grabber", "description": "The PUPSIS Grades and Contact Grabber is a tool designed to automate the extraction of grades and contact information from the PUP Student Information System (PUPSIS). It simplifies the process of retrieving academic data and contact details for administrative and academic purposes.", "image_path": "../static/images/aidan_PUPSIS Grades and Contact Grabber.jpg"},
            {"title": "TechnoQuatro", "description": "The BSCPE 2-4 (TechnoQuatro) website serves as an online platform for the students of the Bachelor of Science in Computer Engineering (BSCPE)2-4 . It provides important information, updates, and resources related to their academic programs and activities, fostering communication and collaboration within the TechnoQuatro community.", "image_path": "../static/images/aidan_TechnoQuatro.jpg"},
            {"title": "Cattlery", "description": "Catllery is a delightful online gallery dedicated to celebrating the charm and personalities of my cats. It features a collection of curated images, each showcasing their playful and endearing moments, offering visitors a heartwarming and interactive experience with the cats through a visually appealing layout.", "image_path": "../static/images/aidan_Cattlery.jpg"}


        ]
    },
    {
        "image_path": "images/renz.png",
        "name": "Renz Tyrone Arcilla",
        "student_number": "2023-0002",
        "role": "Back-end Developer",
        "about": "Renz is a proficient Back-end Developer with a focus on building scalable APIs and optimizing server-side performance. He has extensive experience in database management, API design, and using technologies like Node.js and Express. Renz is passionate about creating efficient and reliable back-end systems that support seamless user experiences, and he is also deeply interested in exploring data science to enhance his technical expertise.",
        "school": "ABC Institute of Technology",
        "degree": "Bachelor of Science in Software Engineering",
        "skills": ["Python", "Flask", "Scikit-Learn", "Tableau", "AWS", "PostgreSQL", "Node.js", "Express", "RESTful APIs", "Server-Side Optimization", "Database Management", "Data Preprocessing", "Statistical Analysis"],  
        "socials": {
            "facebook": "https://www.facebook.com/renztyrone.arcilla.3",
            "instagram": "https://www.instagram.com/wash.n.rinse/",
            "github": "https://github.com/RenzArcilla",
            "linkedin": "https://www.linkedin.com/in/renz-tyrone-arcilla-35098a323"
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
        "about": "Earl is a passionate UI/UX Designer with a keen eye for detail. He specializes in creating intuitive and visually compelling user interfaces that enhance the overall user experience. With expertise in wireframing, prototyping, and user research, Earl ensures that every design is both functional and aesthetically pleasing.",
        "school": "National Design Institute",
        "degree": "Bachelor of Arts in Interaction Design",
        "skills": ["HTML", "CSS", "Python", "UI/UX Design", "Content Creation", "Adobe Photoshop", "Adobe InDesign", "Adobe Audition", "Adobe Premeire", "Image Editing", "Wireframing", "Prototyping", "Adobe XD", "Figma", "Sketch", "User Research"],  # Earl's skills
        "socials": {
            "facebook": "https://www.facebook.com/EarlClydeqt/",
            "instagram": "https://www.instagram.com/earl_cly/",
            "github": "https://github.com/EarlClydeeee",
            "linkedin": "https://www.linkedin.com/in/"
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
        "about": "Denn is a dedicated Front-end Developer with a passion for building responsive and accessible web interfaces. He specializes in creating seamless user experiences using HTML, CSS, JavaScript, and React. Denn is committed to ensuring that web applications are not only functional but also inclusive and user-friendly.",
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
        "about": "I’m an aspiring front-end developer with experience in building responsive web applications using HTML, CSS, JavaScript, and Flask. I also have an interest in graphic editing and audio production, including cover art design and mashups. I’m constantly learning and looking for ways to combine creativity with technology.",
        "school": "TechWorld Academy",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "Vue.js", "UI/UX", "Content Creation", "Image Editing",  "Webpack", "Audio Mixing", "Mashups", "FL Studio" "Performance Optimization"],  # Roman's skills
        "socials": {
            "facebook": "https://www.facebook.com/romanjosephgallardo/",
            "instagram": "https://www.instagram.com/romanramonroman/",
            "github": "https://github.com/romanjosephgallardo",
            "linkedin": "https://www.linkedin.com/in/roman-joseph-gallardo/"
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
        "about": "Railey is a skilled UI/UX Designer known for creating seamless user experiences that balance both aesthetics and functionality. With expertise in UX research, wireframing, and UI design, she crafts intuitive interfaces using tools like Figma, Adobe Illustrator, and Photoshop. Railey is dedicated to designing digital experiences that are both visually appealing and user-centric.",
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
        "about": "Arvie is a skilled Back-end Developer focused on ensuring the smooth operation of server-side systems and managing databases. He specializes in API development and integrating technologies like Node.js, Express, and MongoDB. Arvie is committed to building secure, scalable back-end solutions that enhance system efficiency and user experience.",
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