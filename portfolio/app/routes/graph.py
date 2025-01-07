import networkx as nx
from app import app
from flask import render_template, request

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
        "EDSA", "Baclaran"
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
        
        # Attach line information to each station in the path
        path_with_lines = []
        for station in path:
            line = G.nodes[station]['line']
            path_with_lines.append((station, line))
        
        return path_with_lines, distance
    except nx.NetworkXNoPath:
        return None, None
    except ValueError as e:
        print(f"Error: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None

def get_line_changes(path_with_lines):
    # Identify line changes along the path
    changes = []
    current_line = path_with_lines[0][1]
    
    for i, (station, line) in enumerate(path_with_lines):
        if line != current_line:
            changes.append(f"Change from {current_line} to {line} at {station}")
            current_line = line
    
    return changes


# Create the graph representing the Manila rail system
G = create_manila_rail_graph()

@app.route('/graph', methods=['GET', 'POST'])
def graph():
    # Specify start and end stations for the route
    start = request.form.get('start', '').strip()  # Get start input from the form
    end = request.form.get('end', '').strip()  # Get end input from the form
    line_changes_output = []  # Initializes the output for line changes (as a list)

    if request.method == "POST":
        # Find the shortest path and its details
        path_with_lines, distance = find_shortest_path(G, start, end)
    
        if path_with_lines and distance:
            from_to = f"Shortest path from {start} to {end}:"
            shortest_path = f"Path: {' → '.join((station for station, _ in path_with_lines))}"
            no_stations = f"Number of stations: {distance}"
            
            # Print line changes along the route
            line_changes = get_line_changes(path_with_lines)
            line_changes_output = line_changes  # Ensure this is a list
        else:
            shortest_path = f"No path found between {start} and {end}"

    elif request.method == "GET":
        # Reset all variables for GET request
        start = ""
        end = ""
        from_to = ""
        shortest_path = ""
        no_stations = ""
        line_changes_output = []
    
    # Render a template with the output variables 
    return render_template(
        'graph.html',
        from_to=from_to,
        shortest_path=shortest_path,
        no_stations=no_stations,
        line_changes_output=line_changes_output,  # Pass as list
        start=start,
        end=end
    )
