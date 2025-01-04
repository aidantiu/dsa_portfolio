from app import app
from flask import render_template, request

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

    def print_tree(self, traversal_type):
        """
        Print the tree in the specified traversal order.
        Currently supports "preorder" traversal.
        """
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        return False

    def preorder_print(self, start, traversal):
        """
        Perform a preorder traversal (Root -> Left -> Right).
        """
        if start:
            traversal += str(start.value) + "-"  # Visit the root node
            traversal = self.preorder_print(start.left, traversal)  # Traverse left subtree
            traversal = self.preorder_print(start.right, traversal)  # Traverse right subtree
        return traversal
    
    def inorder_print(self, start, traversal):
        """
        Perform a inorder traversal (Root -> Left -> Right).
        """
        if start:
            traversal = self.inorder_print(start.left, traversal)  # Traverse left subtree
            traversal += str(start.value) + "-"  # Visit the root node
            traversal = self.inorder_print(start.right, traversal)  # Traverse right subtree
        return traversal
    
    def postorder_print(self, start, traversal):
        """
        Perform a postorder traversal (Root -> Left -> Right).
        """
        if start:
            traversal = self.postorder_print(start.left, traversal)  # Traverse left subtree
            traversal = self.postorder_print(start.right, traversal)  # Traverse right subtree
            traversal += str(start.value) + "-"  # Visit the root node
        return traversal
    

    def find_node(self, start, value):
        """
        Find a node with the specified value in the tree.
        """
        if start:
            if start.value == value:  # Node found
                return start
            # Search in the left and right subtrees
            left = self.find_node(start.left, value)
            if left:
                return left
            right = self.find_node(start.right, value)
            if right:
                return right
        return None  # Node not found

    def find_parent(self, start, child):
        """
        Find the parent of the specified child node.
        """
        if start:
            # Check if the current node is the parent of the child
            if start.left == child or start.right == child:
                return start
            # Search in the left and right subtrees
            left = self.find_parent(start.left, child)
            if left:
                return left
            right = self.find_parent(start.right, child)
            if right:
                return right
        return None  # Parent not found

    def add_left_child(self, parent_value, child_value):
        """
        Add a left child to the node with the specified parent value.
        """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            if not parent_node.left:  # Only add if left child does not exist
                parent_node.left = Node(child_value)

    def add_right_child(self, parent_value, child_value):
        """
        Add a right child to the node with the specified parent value.
        """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            if not parent_node.right:  # Only add if right child does not exist
                parent_node.right = Node(child_value)

    def delete_node(self, value):
        """
        Delete a node with the specified value from the tree.
        Handles three cases:
        1. Node has no children (leaf node).
        2. Node has one child.
        3. Node has two children.
        """
        node_to_delete = self.find_node(self.root, value)
        if not node_to_delete:  # Node not found
            return False

        parent = self.find_parent(self.root, node_to_delete)

        # Case 1: Node has no children
        if not node_to_delete.left and not node_to_delete.right:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = None
                else:
                    parent.right = None
            else:  # Deleting the root node
                self.root = None

        # Case 2: Node has one child
        elif node_to_delete.left and not node_to_delete.right:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.left
                else:
                    parent.right = node_to_delete.left
            else:  # Deleting the root node
                self.root = node_to_delete.left

        elif node_to_delete.right and not node_to_delete.left:
            if parent:
                if parent.left == node_to_delete:
                    parent.left = node_to_delete.right
                else:
                    parent.right = node_to_delete.right
            else:  # Deleting the root node
                self.root = node_to_delete.right

        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest node in the right subtree)
            successor = node_to_delete.right
            while successor.left:
                successor = successor.left

            # Recursively delete the successor
            self.delete_node(successor.value)

            # Replace node_to_delete's value with successor's value
            node_to_delete.value = successor.value

        return True  # Node successfully deleted

# Create a BinaryTree instance with root node "root"
tree = BinaryTree("root")

@app.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree():
    """
    Handle GET and POST requests for the binary tree page.
    Allows adding children, searching for nodes, and deleting nodes.
    """
    message = ""
    traversal = tree.print_tree("preorder")  # Get the current preorder traversal
    parent_value = None #Initializes a variable which will hold the value of the parent node (front end will refer to this variable to store the node clicked by the user)

    if request.method == 'POST':
        # Retrieve action and form inputs
        action = request.form.get('action')
        input_field = request.form.get('input_field')

        # Perform the requested action
        if action == 'add_left':
            if parent_value.left:
                message = f"Left child of '{parent_value}' already exists!"
            else:
                if not input_field.strip():
                    message = "Please enter a value in the Input Field."
                else:
                    tree.add_left_child(parent_value, input_field)
                    message = f"'{input_field}' added as left child of '{parent_value}'."

        elif action == 'add_right': 
            if parent_value.right:
                message = f"Right child of '{parent_value}' already exists!"
            else:
                if not input_field.strip():
                    message = "Please enter a value in the Input Field."
                else:
                    tree.add_right_child(parent_value, input_field)
                    message = f"'{input_field}' added as right child of '{parent_value}'."

        elif action == 'preorder_search':
            if not input_field:
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.print_tree("preorder")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in preorder."

        elif action == 'inorder_search':
            if not input_field:
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.print_tree("inorder")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in inorder."

        elif action == 'postorder_search':
            if not input_field:
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.print_tree("postorder")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in postorder."

        elif action == 'delete':
            if not input_field.strip():
                message = "Enter a value in the Input Field to search."
            elif input_field == "root":
                message = "Invalid operation! We can't remove the root node!"
            else:
                deleted = tree.delete_node(input_field)
                message = f"Node {input_field} deleted." if deleted else f"Node {input_field} not found!"

        # (To be deleted, used by back-end for verification of functionalities)
        # Update the traversal after the action
        traversal = tree.print_tree("preorder")

       

    # Render the HTML template with updated data
    return render_template('binary_tree.html', traversal=traversal, message=message)
