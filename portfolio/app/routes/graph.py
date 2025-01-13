import networkx as nx
from app import app
# Added imports for handling form resubmission and session management
from flask import render_template, request, redirect, url_for, session

# Global variables for station lists remain unchanged
MRT3_STATIONS = sorted([
    "North Avenue", "Quezon Avenue", "GMA Kamuning", "Cubao", 
    "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni", 
    "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"
])

LRT2_STATIONS = sorted([
    "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", 
    "Betty Go-Belmonte", "Araneta Center-Cubao", "Anonas", "Katipunan", 
    "Santolan", "Marikina-Pasig", "Antipolo"
])

LRT1_STATIONS = sorted([
    "Roosevelt", "Balintawak", "Yamaha Monumento", "5th Avenue", 
    "R. Papa", "Abad Santos", "Blumentritt", "Tayuman", "Bambang", 
    "Doroteo Jose", "Carriedo", "Central Terminal", "United Nations", 
    "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", 
    "EDSA", "Baclaran", "Redemptorist", "MIA", "Asia World", 
    "Ninoy Aquino", "Dr. Santos"
])

def create_manila_rail_graph():
    # Initialize an undirected graph
    G = nx.Graph()
    
    # Define station lists for each rail line
    mrt3_stations = [
        "North Avenue", "Quezon Avenue", "GMA Kamuning", "Cubao", 
        "Santolan-Annapolis", "Ortigas", "Shaw Boulevard", "Boni", 
        "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"
    ]
    
    lrt2_stations = [
        "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore", 
        "Betty Go-Belmonte", "Araneta Center-Cubao", "Anonas", "Katipunan", 
        "Santolan", "Marikina-Pasig", "Antipolo"
    ]
    
    lrt1_stations = [
        "Roosevelt", "Balintawak", "Yamaha Monumento", "5th Avenue", 
        "R. Papa", "Abad Santos", "Blumentritt", "Tayuman", "Bambang", 
        "Doroteo Jose", "Carriedo", "Central Terminal", "United Nations", 
        "Pedro Gil", "Quirino", "Vito Cruz", "Gil Puyat", "Libertad", 
        "EDSA", "Baclaran", "Redemptorist", "MIA", "Asia World", 
        "Ninoy Aquino", "Dr. Santos"
    ]
    
    # Add stations as nodes with line attributes
    for station in mrt3_stations:
        G.add_node(station, line="MRT3")
    for station in lrt2_stations:
        G.add_node(station, line="LRT2")
    for station in lrt1_stations:
        G.add_node(station, line="LRT1")
    
    # Helper function to add edges between consecutive stations in a line
    def add_line_edges(stations):
        for i in range(len(stations) - 1):
            G.add_edge(stations[i], stations[i + 1], weight=1)
    
    # Add edges for each line
    add_line_edges(mrt3_stations)
    add_line_edges(lrt2_stations)
    add_line_edges(lrt1_stations)
    
    # Add interchange connections between lines
    interchanges = [
        ("Araneta Center-Cubao", "Cubao", 1),  # MRT3-LRT2 interchange
        ("Doroteo Jose", "Recto", 1),          # LRT1-LRT2 interchange
        ("EDSA", "Taft Avenue", 1)             # LRT1-MRT3 interchange
    ]
    for station1, station2, weight in interchanges:
        G.add_edge(station1, station2, weight=weight)
    
    return G

def find_shortest_path(G, start, end):
    try:
        if start not in G or end not in G:
            raise ValueError(f"One or both stations {start} and {end} are not in the graph.")
        
        path = nx.shortest_path(G, start, end, weight='weight')
        distance = nx.shortest_path_length(G, start, end, weight='weight')
        
        # Calculate travel time based on line
        total_time = 0
        current_line = None
        
        for i in range(len(path)):
            station = path[i]
            line = G.nodes[station]['line']
            
            # Add transfer time if changing lines
            if current_line and line != current_line:
                total_time += 5  # 5 minutes transfer time
            
            # Calculate time to next station if not last station
            if i < len(path) - 1:
                if line == "MRT3":
                    total_time += 6
                elif line == "LRT1":
                    total_time += 7
                elif line == "LRT2":
                    total_time += 6
            
            current_line = line
            
        path_with_lines = " → ".join([f"{station} ({G.nodes[station]['line']})" for station in path])
        
        return path_with_lines, distance, total_time
    except nx.NetworkXNoPath:
        return None, None, None
    except ValueError as e:
        print(f"Error: {e}")
        return None, None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None, None

def get_line_changes_with_times(path_with_lines_str):
    path_parts = path_with_lines_str.split(" → ")
    changes = []
    current_line = None
    
    for i, part in enumerate(path_parts):
        # Split on the last occurrence of " (" to handle station names with parentheses
        station = part[:part.rindex(" (")]
        line = part[part.rindex("(") + 1:].rstrip(")")
        
        if current_line and line != current_line:
            changes.append({
                'text': f"Change from {current_line} to {line} at {station}",
                'time': "5 mins transfer time",
                'station': station
            })
        
        current_line = line
    
    return changes

def convert_path_to_list(path_with_lines_str):
    return path_with_lines_str.split(" → ")

def get_instruction_steps():
    return [
        "Select your starting station from the dropdown menu.",
        "Select your destination station from the dropdown menu.",
        "Click on the 'Find Path' button to calculate the shortest path.",
        "View the shortest path, number of stations, and estimated travel time.",
        "Check the journey details for any line changes and transfer times."
    ]

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    if request.method == "POST":
        start = request.form.get('start', '').strip()
        end = request.form.get('end', '').strip()
        
        if start == '' and end == '':
            session['validation'] = "Please choose start and end stations."
        elif start == '':
            session['validation'] = "Invalid! Starting station was missing."
        elif end == '':
            session['validation'] = "Invalid! Destination (end station) was missing."
        elif start == end:
            session['validation'] = "Invalid! Start and end destination must be two different stations."
        else:
            path_with_lines, distance, total_time = find_shortest_path(G, start, end)
            if path_with_lines and distance:
                session['from_to'] = f"Shortest path from {start} to {end}:"
                session['shortest_path'] = path_with_lines
                session['no_stations'] = f"Number of stations: {distance}"
                session['total_time'] = f"Estimated total travel time: {total_time} mins"
                session['line_changes'] = get_line_changes_with_times(path_with_lines)
                session['path_list'] = convert_path_to_list(path_with_lines)
                session['validation'] = ""
            else:
                session['shortest_path'] = f"No path found between {start} and {end}"
                session['from_to'] = ""
                session['no_stations'] = ""
                session['total_time'] = ""
                session['line_changes'] = []
                session['path_list'] = []
                session['validation'] = ""
        
        session['form_submitted'] = True
        return redirect(url_for('graph', start=start, end=end))
        
    # Rest of the code remains unchanged
    elif request.method == "GET":
        if not session.get('form_submitted', False):
            session.pop('from_to', None)
            session.pop('shortest_path', None)
            session.pop('no_stations', None)
            session.pop('line_changes', None)
            session.pop('path_list', None)
            start = ""
            end = ""
        else:
            session.pop('form_submitted', None)
            start = request.args.get('start', '')
            end = request.args.get('end', '')

    from_to = session.pop('from_to', "")
    shortest_path = session.pop('shortest_path', "")
    no_stations = session.pop('no_stations', "")
    line_changes_output = session.pop('line_changes', [])
    path_list = session.pop('path_list', [])
    validation = session.get('validation', "")
    total_time = session.pop('total_time', "")  # Add this line to get total_time
    session.pop('validation', None)
    
    return render_template(
        'graph.html',
        from_to=from_to,
        shortest_path=shortest_path,
        no_stations=no_stations,
        line_changes_output=line_changes_output,
        start=start,
        end=end,
        mrt3_stations=MRT3_STATIONS,
        lrt2_stations=LRT2_STATIONS,
        lrt1_stations=LRT1_STATIONS,
        path_list=path_list,
        validation=validation,
        total_time=total_time,  # Add this line to pass total_time to template
        instruction_steps=get_instruction_steps(),
    )

# Create the graph representing the Manila rail system
G = create_manila_rail_graph()

# Add secret key for session management
app.secret_key = 'your_secret_key_here'