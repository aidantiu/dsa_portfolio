from app import app
from flask import render_template, request
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
        base_node_spacing = 50# Reduces as tree grows
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

# Create a BinaryTree instance with root node "root"
tree = BinaryTree(0)

@app.route('/binary-tree', methods=['GET', 'POST'])
def binary_tree():
    """
    Handle GET and POST requests for the binary tree page.
    Allows adding children, searching for nodes, and deleting nodes.
    """
    message = ""
    parent_value = None  # Initializes a variable which will hold the value of the parent node

    if request.method == 'POST':

        # Retrieve action and form inputs
        action = request.form.get('action')
        selected_node = request.form.get('selected_node')

        # Perform the requested action
        if action == 'add_left':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:

                # Check if the parent node exists before trying to add a child
                parent_node = tree.find_node(tree.root, selected_node)
                if parent_node:
                    if parent_node.left:
                        message = f"Left child of node '{selected_node}' already exists!"
                    else:
                        tree.add_left_child(selected_node, None)  # Pass None to use incremental value
                        message = f"Added left child to node {selected_node}."
                else:
                    message = f"Parent node '{selected_node}' not found!"

        elif action == 'add_right':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:

                # Check if the parent node exists before trying to add a child
                parent_node = tree.find_node(tree.root, selected_node)
                if parent_node:
                    if parent_node.right:
                        message = f"Right child of node '{selected_node}' already exists!"
                    else:
                        tree.add_right_child(selected_node, None)  # Pass None to use incremental value
                        message = f"Added right child to node '{selected_node}'."
                else:
                    message = f"Parent node '{selected_node}' not found!"

        elif action == 'delete':
            if not selected_node or not selected_node.strip():
                message = "Please select a node."
            else:
                # Check if the node exists before trying to delete it
                node = tree.find_node(tree.root, selected_node)
                if node:
                    # Check if the node is the root node
                    if str(tree.root.value) == selected_node:
                        tree.clear_tree()
                        message = "The tree has been cleared!"
                    else:
                        # Find the parent node to delete the child
                        parent_node = tree.find_parent(tree.root, selected_node)
                        if parent_node.left and str(parent_node.left.value) == selected_node:
                            parent_node.left = None
                        elif parent_node.right and str(parent_node.right.value) == selected_node:
                            parent_node.right = None
                        message = f"Node '{selected_node}' has been deleted."
                else:
                    message = f"Node '{selected_node}' not found"  # Node not found

        # Clear the tree
        elif action == 'clear':
            tree.clear_tree()  # Clear the entire tree
            message = "The tree has been cleared!"

        # Traverse the tree to find a node
        elif action == 'search':
            if not selected_node or not selected_node.strip():
                message = "Please select a node to search."
            else:

                node = tree.find_node(tree.root, selected_node)
                if node:
                    message = f"Node '{selected_node}' found in the tree."
                else:
                    message = f"Node '{selected_node}' not found in the tree."
                
            

        # Update the tree structure after any modification
        tree_structure = tree.get_tree_structure()

    # Render the HTML template with updated data
    return render_template('binary_tree.html',tree_structure=tree_structure, message=message)