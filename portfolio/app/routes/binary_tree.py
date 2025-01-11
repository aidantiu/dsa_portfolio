from app import app
from flask import render_template, request, session, redirect, url_for
from collections import deque

# Define a Node class to represent each node in the binary tree
class Node(object):
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None    # Pointer to the left child
        self.right = None   # Pointer to the right child

# Define a BinaryTree class to manage the tree structure and operations
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)  # Initialize the tree with a root node
        self.next_value = 1     # Initialize counter for incremental nodes
        self.visited_nodes = []
        self.target_found = False
        self.current_animation = None

    def get_tree_structure(self):
        if not self.root:
            return {"nodes": [], "edges": [], "width": 0, "height": 0}

        # Calculate max possible nodes per level
        def max_nodes_at_level(level):
            return 2 ** level

        # Get tree height
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        tree_height = get_height(self.root)
        
        # Calculate dimensions with exponential spacing
        # Adjust base spacing based on tree size
        base_node_spacing = 50 # Reduces as tree grows
        level_height = 70 # Reduces vertical spacing too

        nodes = []
        edges = []
        
        # Adjusted width calculation
        max_bottom_nodes = max_nodes_at_level(tree_height - 1)
        canvas_width = max(800, max_bottom_nodes * base_node_spacing)
        canvas_height = tree_height * level_height + 50

        def traverse(node, x, y, level, left_bound, right_bound):
            if node:
                nodes.append({
                    "id": str(node.value),
                    "x": x,
                    "y": y
                })

                # Reduced spacing calculation
                level_factor = max(2, 1 / (level + 1))  # Reduces spacing at deeper levels
                spacing = (right_bound - left_bound) / (2 ** (level + 3)) * level_factor
                
                if node.left:
                    left_x = x - spacing * (2 ** level)  # Reduced exponential growth
                    left_y = y + level_height
                    edges.append({
                        "from": {"x": x, "y": y},
                        "to": {"x": left_x, "y": left_y}
                    })
                    traverse(node.left, left_x, left_y, level + 1, left_bound, x)
                
                if node.right:
                    right_x = x + spacing * (2 ** level)  # Reduced exponential growth
                    right_y = y + level_height
                    edges.append({
                        "from": {"x": x, "y": y},
                        "to": {"x": right_x, "y": right_y}
                    })
                    traverse(node.right, right_x, right_y, level + 1, x, right_bound)
        
        # Start traversal from root
        traverse(self.root, canvas_width/2, 50, 0, 0, canvas_width)

        return {
            "nodes": nodes,
            "edges": edges,
            "width": canvas_width,
            "height": canvas_height
        }

    def add_left_child(self, parent_value, child_value=None):
        """
        Add a left child to the node with the specified parent value.
        If no child_value is provided, use the next incremental value.
        """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            if not parent_node.left:  # Only add if left child does not exist
                # Use incremental value if no specific value provided
                if child_value is None or child_value.strip() == "":
                    child_value = self.next_value
                    self.next_value += 1  # Increment counter
                parent_node.left = Node(child_value)

    def add_right_child(self, parent_value, child_value=None):
        """
        Add a right child to the node with the specified parent value.
        If no child_value is provided, use the next incremental value.
        """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            if not parent_node.right:  # Only add if right child does not exist
                # Use incremental value if no specific value provided
                if child_value is None or child_value.strip() == "":
                    child_value = self.next_value
                    self.next_value += 1  # Increment counter
                parent_node.right = Node(child_value)

    def find_node(self, start, value):
        """
        Find a node with the specified value in the tree.
        """
        if start:
            if str(start.value) == str(value):  # Node found (compare as strings)
                return start
            # Search in the left and right subtrees
            left = self.find_node(start.left, value)
            if left:
                return left
            right = self.find_node(start.right, value)
            if right:
                return right
        return None  # Node not found
    
    def find_node_with_traversal(self, value: str, traversal_type: str) -> list[str]:
        """
        Find a node with the specified value using the specified traversal method.
        Returns the path of the search.
        """

        path = []
        found = False
        target_value = str(value)

        # Perform pre-order traversal
        def pre_order_search(node):
            nonlocal found 

            # Stop traversal if node is None or target is found
            if not node or found:
                return

            # Visit the current node
            path.append(str(node.value))
            if str(node.value) == target_value:
                found = True
                return
            
            # Visit left and right subtrees
            pre_order_search(node.left)
            pre_order_search(node.right)

        # Perform in-order traversal
        def in_order_search(node):
            nonlocal found

            # Stop traversal if node is None or target is found
            if not node or found:
                return 
    
             # Visit left subtree
            in_order_search(node.left)
            if found: 
                return
          
            # Visit the current node
            path.append(str(node.value))
            if str(node.value) == target_value:
                found = True
                return
            
            # Visit right subtree
            in_order_search(node.right)

        # Perform post-order traversal
        def post_order_search(node):
            nonlocal found

            # Stop traversal if node is None or target is found
            if not node or found:
                return
            
            # Visit left and right subtrees
            post_order_search(node.left)
            post_order_search(node.right)

            # Visit the current node
            if not found:
                path.append(str(node.value))
                if str(node.value) == target_value:
                    found = True

        # Perform the specified traversal method
        if traversal_type == 'pre_order':
            pre_order_search(self.root)
        elif traversal_type == 'in_order':
            in_order_search(self.root)
        elif traversal_type == 'post_order':
            post_order_search(self.root)

        return path

    def clear_tree(self):
        """
        Clears the entire tree by resetting the root to None.
        """
        self.root.left = None
        self.root.right = None
        self.next_value = 1  # Reset the incremental value for future nodes

    def find_parent(self, start, target):
        """
        Find the parent node of a node with the specified target value.
        Returns None if target is root or not found.
        """
        if start is None:
            return None
            
        # Check if either child is the target
        if (start.left and str(start.left.value) == str(target)) or \
           (start.right and str(start.right.value) == str(target)):
            return start
            
        # Recursively search left and right subtrees
        left_result = self.find_parent(start.left, target)
        if left_result:
            return left_result
            
        right_result = self.find_parent(start.right, target)
        if right_result:
            return right_result
            
        return None

# Create a BinaryTree instance with root node "0"
tree = BinaryTree(0)

# Add secret key for session management
app.secret_key = 'temporary-key'  

@app.route('/binary-tree', methods=['GET', 'POST'])
def binary_tree():
    """
    Handle GET and POST requests for the binary tree page.
    Allows adding children, searching for nodes, and deleting nodes.
    """
    message = ""
    path = []  # Initialize path for search results
    found = False  # Initialize search result flag
    
    # Track if the current request is a redirected GET request using session
    is_redirected_get = session.get('is_redirected_get', False)

    if request.method == 'POST':
        # Retrieve action and form inputs
        action = request.form.get('action')
        selected_node = request.form.get('selected_node')

        # Handle all POST actions
        if action == 'add_left':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:
                parent_node = tree.find_node(tree.root, selected_node)
                if parent_node:
                    if parent_node.left:
                        message = f"Left child of node '{selected_node}' already exists!"
                    else:
                        tree.add_left_child(selected_node, None)
                        message = f"Added left child to node {selected_node}."
                else:
                    message = f"Parent node '{selected_node}' not found!"

        elif action == 'add_right':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:
                parent_node = tree.find_node(tree.root, selected_node)
                if parent_node:
                    if parent_node.right:
                        message = f"Right child of node '{selected_node}' already exists!"
                    else:
                        tree.add_right_child(selected_node, None)
                        message = f"Added right child to node '{selected_node}'."
                else:
                    message = f"Parent node '{selected_node}' not found!"

        elif action == 'delete':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:
                node = tree.find_node(tree.root, selected_node)
                if node:
                    if str(tree.root.value) == selected_node:
                        tree.clear_tree()
                        message = "The tree has been cleared!"
                    else:
                        parent_node = tree.find_parent(tree.root, selected_node)
                        if parent_node.left and str(parent_node.left.value) == selected_node:
                            parent_node.left = None
                        elif parent_node.right and str(parent_node.right.value) == selected_node:
                            parent_node.right = None
                        message = f"Node '{selected_node}' has been deleted."
                else:
                    message = f"Node '{selected_node}' not found"

        elif action == 'search':
            search_value = request.form.get('search_value')
            traversal_type = request.form.get('traversal_type')
            path = tree.find_node_with_traversal(search_value, traversal_type)
            found = search_value in path
            message = f"Node '{search_value}' {'found' if found else 'not found'}"

        elif action == 'clear':
            tree.clear_tree()
            message = "The tree has been cleared!"

        # Store message and search results in session for redirect
        session['message'] = message
        session['search_path'] = path
        session['search_found'] = found
        session['is_redirected_get'] = True
        return redirect(url_for('binary_tree'))

    # Handle GET request logic
    if not is_redirected_get:
        # Clear the tree on fresh page load (not after POST redirect)
        tree.clear_tree()
        message = None
        path = []
        found = False
    else:
        # Retrieve saved message and search results from session
        message = session.get('message')
        path = session.get('search_path', [])
        found = session.get('search_found', False)

    # Clean up session data after processing
    session['is_redirected_get'] = False
    session.pop('message', None)
    session.pop('search_path', None)
    session.pop('search_found', None)

    # Get current tree structure and render template
    tree_structure = tree.get_tree_structure()
    return render_template('binary_tree.html',
                         tree_structure=tree_structure,
                         message=message,
                         search_path=path,
                         search_found=found,
                         instruction_steps=get_instruction_steps(),)

# List to store the How To Use data
def get_instruction_steps():
    return [
        "Click on a node to select it.",
    ]
    # Will add more steps for the binary tree page