import networkx as nx
from app import app
# Added imports for handling form resubmission and session management
from flask import render_template, request, redirect, url_for, session

# Global variables for station lists
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
        # Check if the start and end stations exist in the graph
        if start not in G or end not in G:
            raise ValueError(f"One or both stations {start} and {end} are not in the graph.")
        
        # Compute the shortest path and its length
        path = nx.shortest_path(G, start, end, weight='weight')
        distance = nx.shortest_path_length(G, start, end, weight='weight')
        
        # Build the path with line information as a formatted string
        path_with_lines = " → ".join([f"{station} ({G.nodes[station]['line']})" for station in path])
        
        return path_with_lines, distance
    except nx.NetworkXNoPath:
        return None, None
    except ValueError as e:
        print(f"Error: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None

def get_line_changes(path_with_lines_str):
    # Split the formatted path into stations with their line information
    path_parts = path_with_lines_str.split(" → ")
    
    changes = []
    current_line = None
    
    for part in path_parts:
        station, line = part.rsplit(" (", 1)  # Split on the last '(' to get the station and line
        line = line.rstrip(")")  # Remove the closing ')'
        
        if current_line and line != current_line:
            changes.append(f"Change from {current_line} to {line} at {station}")
        
        current_line = line  # Update the current line
    
    return changes

def convert_path_to_list(path_with_lines_str):
    # Split the formatted path into stations with their line information
    path_parts = path_with_lines_str.split(" → ")
    
    # Extract station names along with their respective lines as strings
    path_list = []
    for part in path_parts:
        station, line = part.rsplit(" (", 1)  # Split on the last '(' to get the station and line
        line = line.rstrip(")")  # Remove the closing ')'
        path_list.append(f"{station} ({line})")  # Format as a string "Station (Line)"
    
    return path_list

# Create the graph representing the Manila rail system
G = create_manila_rail_graph()

# Add secret key for session management
app.secret_key = 'your_secret_key_here'

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    # For POST request: process form submission
    if request.method == "POST":
        # Get start and end inputs from the form
        start = request.form.get('start', '').strip()
        end = request.form.get('end', '').strip()
        
        # Store results in session to prevent form resubmission issues
        if start and end:
            path_with_lines, distance = find_shortest_path(G, start, end)
            
            if path_with_lines and distance:
                # Store all path information in session
                # line_changes is now stored as a direct list for simpler template rendering
                session['from_to'] = f"Shortest path from {start} to {end}:"
                session['shortest_path'] = path_with_lines
                session['no_stations'] = f"Number of stations: {distance}"
                session['line_changes'] = get_line_changes(path_with_lines)  # Stores list directly
                session['path_list'] = convert_path_to_list(path_with_lines)
            else:
                session['shortest_path'] = f"No path found between {start} and {end}"
                session['from_to'] = ""
                session['no_stations'] = ""
                session['line_changes'] = []
                session['path_list'] = []
            
            # Set a flag to indicate that the request is a result of a POST (form submission)
            session['form_submitted'] = True

            # Redirect to prevent form resubmission on refresh
            return redirect(url_for('graph', start=start, end=end))
        
    elif request.method == "GET":
        # Check if this is a fresh GET request (not redirected after POST)
        if not session.get('form_submitted', False):
            # Clear session data to reset outputs
            session.pop('from_to', None)
            session.pop('shortest_path', None)
            session.pop('no_stations', None)
            session.pop('line_changes', None)
            session.pop('path_list', None)

            # Set start and end inputs to empty
            start = ""
            end = ""
        else:
            # Clear the flag after handling the redirected request
            session.pop('form_submitted', None)

            # Use values from the redirected GET request
            start = request.args.get('start', '')
            end = request.args.get('end', '')

    # Retrieve and clear session data
    from_to = session.pop('from_to', "")
    shortest_path = session.pop('shortest_path', "")
    no_stations = session.pop('no_stations', "")
    line_changes_output = session.pop('line_changes', [])
    path_list = session.pop('path_list', [])  # Retrieve the path list from session
    
    # Render template with empty inputs and any stored results
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
        path_list = path_list
    )