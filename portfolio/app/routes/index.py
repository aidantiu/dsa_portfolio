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
    # Project Manager
    {
        "image_path": "images/aidan.jpg",
        "name": "Aidan Tiu",
        "student_number": "20**-06***-MN-*",
        "role": "Project Manager",
        "about": "I am an aspiring DevOps engineer passionate about streamlining workflows and improving system efficiency. Outside of programming, I enjoy playing basketball and cooking. A fun fact about me is that I have a lot of birthmarks!",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["Python", "Cloud Computing", "AWS", "Full Stack Development", "Linux", "Web Scraping", "DevOps"],
        "socials": {
            "facebook": "https://www.facebook.com/haha.hauwieks",
            "instagram": "https://www.instagram.com/y.mnwri/",
            "github": "https://github.com/aidantiu",
            "linkedin": "https://www.linkedin.com/in/aidan-tiu-58650520b/"
        },
        "projects": [
            {
                "title": "PUPGS Alumni Engagement Portal System",
                "description": "The PUPGS Alumni Engagement Portal System is an online platform designed to connect and engage alumni of the Polytechnic University of the Philippines Graduate School. It offers features such as alumni profiles, event updates, and networking opportunities to foster continuous interaction and collaboration within the PUPGS community.",
                "image_path": "../static/images/aidan_PUPGS Alumni Portal.jpg",
                "link": "https://github.com/aidantiu/pup_alumni_portal"
            },
            {
                "title": "PUPSIS Grades and Contact Grabber",
                "description": "The PUPSIS Grades and Contact Grabber is a tool designed to automate the extraction of grades and contact information from the PUP Student Information System (PUPSIS). It simplifies the process of retrieving academic data and contact details for administrative and academic purposes.",
                "image_path": "../static/images/aidan_PUPSIS Grades and Contact Grabber.jpg",
                "link": "https://github.com/aidantiu/PUPSIS-Grades-and-Contact-Grabber"
            },
            {
                "title": "TechnoQuatro",
                "description": "The BSCPE 2-4 (TechnoQuatro) website serves as an online platform for the students of the Bachelor of Science in Computer Engineering (BSCPE)2-4. It provides important information, updates, and resources related to their academic programs and activities, fostering communication and collaboration within the TechnoQuatro community.",
                "image_path": "../static/images/aidan_TechnoQuatro.jpg",
                "link": "https://github.com/aidantiu/tecnoquatro"
            },
            {
                "title": "Cattlery",
                "description": "Catllery is a delightful online gallery dedicated to celebrating the charm and personalities of my cats. It features a collection of curated images, each showcasing their playful and endearing moments, offering visitors a heartwarming and interactive experience with the cats through a visually appealing layout.",
                "image_path": "../static/images/aidan_Cattlery.jpg",
                "link": "https://github.com/aidantiu/catllery"
            }
        ]
    },
    # UI/UX Designers
    {
        "image_path": "images/earl.jpg",
        "name": "Earl Clyde M. Bañez",
        "student_number": "20**-01***-MN-*",
        "role": "UI/UX Designer",
        "about": "UI/UX Designer with expertise in creating intuitive digital experiences",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["HTML", "CSS", "Python", "UI/UX Design", "Content Creation", "Adobe Photoshop", "Adobe InDesign", "Adobe Audition", "Adobe Premiere", "Image Editing"],
        "socials": {
            "facebook": "https://www.facebook.com/EarlClydeqt/",
            "instagram": "https://www.instagram.com/earl_cly/",
            "github": "https://github.com/EarlClydeeee",
            "linkedin": "https://www.linkedin.com/in/earl-clyde-ba%C3%B1ez-40a494254/"
        },
        "projects": [
            {
                "title": "Under Construction",
                "description": "Project coming soon",
                "image_path": "../static/images/temporary_underconstruction.jpg",
                "link": "#"
            }
        ]
    },
    {
        "image_path": "images/railey.jpg",
        "name": "Railey C. Guinto",
        "student_number": "20**-01***-MN-*",
        "role": "UI/UX Designer",
        "about": "An aspiring UI/UX designer passionate about creating intuitive and visually engaging digital experiences. With a keen eye for detail and a creative mindset, I enjoy exploring design trends and enhancing user interactions. Outside the design realm, I love expressing creativity through cooking and immerse myself in gaming as a way to unwind and draw inspiration.",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["Python", "UI/UX", "Image Editing", "Video Editing", "Content Creation", "Microsoft Excel", "Microsoft Powerpoint", "Canva", "Adobe Photoshop"],
        "socials": {
            "facebook": "https://www.facebook.com/Raiii.Guinto/",
            "instagram": "https://www.instagram.com/raiiiraiiiraiii/",
            "github": "https://github.com/raiiiraiiiraiii",
            "linkedin": "https://www.linkedin.com/in/railey-guinto/"
        },
        "projects": [
            {
                "title": "TV Functions Simulator",
                "description": '"TV Functions Simulator" is an interactive project that replicates basic TV controls, enabling users to turn on or off two TVs, switch channels, and adjust their volume seamlessly.',
                "image_path": "../static/images/Railey_TV_function_Simulator.png",
                "link": "https://github.com/raiiiraiiiraiii/tv_class_and_testdrivers_in_oop_way"
            },
            {
                "title": "TropangGiga's UI/UX Design",
                "description": "The group UI/UX design project portfolio is a comprehensive showcase of creativity and collaboration. It features a dynamic homepage, detailed member profiles, and a curated collection of the group's standout projects.",
                "image_path": "../static/images/Railey_TropangGiga_UI-UX_design.png",
                "link": "https://www.figma.com/proto/duP29FiSaxYUteIsRw2BDk/PORTFOLIO-DSA?node-id=23-3&t=4fI2uMplWSCZJhra-1"
            }
        ]
    },
    # Front-end Developers
    {
        "image_path": "images/roman.jpg",
        "name": "Roman Joseph Gallardo",
        "student_number": "20**-01***-MN-*",
        "role": "Front-end Developer",
        "about": "I'm an aspiring front-end developer with experience in building responsive web applications using HTML, CSS, JavaScript, and Flask. I also have an interest in graphic editing and audio production, including cover art design and mashups. I'm constantly learning and looking for ways to combine creativity with technology.",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["HTML", "CSS", "JavaScript", "Python", "UI/UX", "Content Creation", "Image Editing", "Audio Mixing", "Mashups", "FL Studio"],
        "socials": {
            "facebook": "https://www.facebook.com/romanjosephgallardo/",
            "instagram": "https://www.instagram.com/romanramonroman/",
            "github": "https://github.com/romanjosephgallardo",
            "linkedin": "https://www.linkedin.com/in/roman-joseph-gallardo/"
        },
        "projects": [
            {
                "title": "Under Construction",
                "description": "Project coming soon",
                "image_path": "../static/images/temporary_underconstruction.jpg",
                "link": "#"
            }
        ]
    },
    {
        "image_path": "images/denn.jpg",
        "name": "Denn Adrian J. Capus",
        "student_number": "2023-04328-MN-0",
        "role": "Front-End Developer",
        "about": "I'm Denn Adrian I'm a passionate programmer with a strong interest in logic and web design. I love creating websites with cool, innovative features and I'm always looking for ways to improve. My strong personality and motivation drive me to push my limits and explore new possibilities. In the future, I hope to combine my tech skills and creativity to inspire others as a tech YouTuber or vlogger. I'm excited to see where this journey takes me.",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["Python", "CSS", "HTML"],
        "socials": {
            "facebook": "https://www.facebook.com/denn.adrian.capus/",
            "instagram": "https://www.instagram.com/kiyetchap/",
            "github": "https://github.com/qwakkhead",
            "linkedin": "https://www.linkedin.com/in/denn-adrian-capus-4b8787342/?fbclid=IwY2xjawHY9O9leHRuA2FlbQIxMAABHcpcPNj8clyzbJU1vyNxx1RpzpMCCs2FOAuKLFgWix3cRZRzAZI1IyYe4A_aem_jd-usJfUncUVgoYEp9QWEg"
        },
        "projects": [
            {
                "title": "Under Construction",
                "description": "Project coming soon",
                "image_path": "../static/images/temporary_underconstruction.jpg",
                "link": "#"
            }
        ]
    },
    # Back-end Developers
    {
        "image_path": "images/arvie.jpg",
        "name": "Arvie Lastra",
        "student_number": "20**-04***-MN-*",
        "role": "Back End Developer",
        "about": "I'm an aspiring data engineer with a passion for data pipelines, cleaning, and uncovering impactful insights from big data. Beyond my love for data, I enjoy cooking, playing volleyball, and immersing myself in anime, manga, manhwa, and manhua. My curious nature fuels my constant pursuit of learning, growth, and new perspectives in both work and life.",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["Python", "Flask", "AWS", "Back End Development", "SQL", "Pandas", "C# (basics)"],
        "socials": {
            "facebook": "https://www.facebook.com/arvie.gavica",
            "instagram": "https://www.instagram.com/arvielastra/",
            "github": "https://github.com/Arvienism",
            "linkedin": "https://www.linkedin.com/in/arvie-lastra-748a072b9/"
        },
        "projects": [
            {
                "title": "Under Construction",
                "description": "Project coming soon",
                "image_path": "../static/images/temporary_underconstruction.jpg",
                "link": "#"
            }
        ]
    },
    {
        "image_path": "images/renz.png",
        "name": "Renz Tyrone Arcilla",
        "student_number": "2023-0002",
        "role": "Back-end Developer",
        "about": "Renz is a proficient Back-end Developer with a focus on building scalable APIs and optimizing server-side performance. He has extensive experience in database management, API design, and using technologies like Node.js and Express. Renz is passionate about creating efficient and reliable back-end systems that support seamless user experiences, and he is also deeply interested in exploring data science to enhance his technical expertise.",
        "school": "Polytechnic University of the Philippines - Manila",
        "degree": "Bachelor of Science in Computer Engineering",
        "skills": ["Python", "Flask", "Scikit-Learn", "Tableau", "AWS", "PostgreSQL", "Node.js", "Express", "RESTful APIs", "Server-Side Optimization", "Database Management", "Data Preprocessing", "Statistical Analysis"],
        "socials": {
            "facebook": "https://www.facebook.com/renztyrone.arcilla.3",
            "instagram": "https://www.instagram.com/wash.n.rinse/",
            "github": "https://github.com/RenzArcilla",
            "linkedin": "https://www.linkedin.com/in/renz-tyrone-arcilla-35098a323"
        },
        "projects": [
            {
                "title": "Under Construction",
                "description": "Project coming soon",
                "image_path": "../static/images/temporary_underconstruction.jpg",
                "link": "#"
            }
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
        "image_path": "images/queue.png",  
        "title": "Queue Operations Simulator",
        "description": "Experience queue data structures in action with our Queue Operations Simulator! This interactive tool demonstrates both simple queues and double-ended queues (deques). Add and remove elements from either end, visualize the queue structure, and understand FIFO operations through a user-friendly interface.",
        "route": "queue"
    },
    {
        "image_path": "images/binary-tree.png",
        "title": "Binary Tree Operations Simulator",
        "description": "Explore the fundamental concepts of binary trees with our interactive Binary Tree Operations Simulator! This tool allows you to create, modify, and traverse binary trees in real-time. Add nodes, delete elements, and visualize different traversal methods (pre-order, in-order, post-order) through an intuitive interface.",
        "route": "binary-tree"
    },
   {
        "image_path": "images/raillsystem.png",
        "title": "Manila Rail Shortest Path Finder",
        "description": "Navigate the Manila rail system with ease using the Manila Rail Shortest Path Finder! This interactive tool helps you find the shortest path between stations on the Manila rail network. Input your starting and destination stations, and instantly see the optimal route, complete with travel times and transfer points. Perfect for commuters and travelers looking to save time and navigate the city efficiently.",
        "route": "graph"
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