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

    def get_tree_structure(self):
        """
        Returns a string representation of the tree structure
        showing parent-child relationships
        """
        return self._get_structure(self.root, "", 0)

    def _get_structure(self, node, structure, level):
        """
        Helper method to recursively build tree structure string
        with proper indentation for visualization
        """
        if node:
            # Add current node with proper indentation
            structure += "  " * level + str(node.value) + "\n"
            # Recursively add left and right subtrees
            structure = self._get_structure(node.left, structure, level + 1)
            structure = self._get_structure(node.right, structure, level + 1)
        return structure
    
    def level_order_print(self):
        """
        Perform a level-order traversal (Breadth-First Search).
        Returns the tree structure as a string in level-by-level, left-to-right order.
        """
        if not self.root:
            return ""
        
        result = ""
        queue = deque([self.root])  # Start with the root node in the queue

        while queue:
            node = queue.popleft()  # Dequeue the front node
            result += str(node.value) + " "  # Add the node's value to the result string

            # Enqueue the left and right children if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result.strip()  # Return the string without trailing space

    def preorder_print(self, start, traversal):
        """
        Perform a preorder traversal (Root -> Left -> Right).
        Used for search operations only.
        """
        if start:
            traversal += str(start.value)  # Visit the root node
            traversal = self.preorder_print(start.left, traversal)  # Traverse left subtree
            traversal = self.preorder_print(start.right, traversal)  # Traverse right subtree
        return traversal
    
    def inorder_print(self, start, traversal):
        """
        Perform an inorder traversal (Left -> Root -> Right).
        Used for search operations only.
        """
        if start:
            traversal = self.inorder_print(start.left, traversal)  # Traverse left subtree
            traversal += str(start.value) + "-"  # Visit the root node
            traversal = self.inorder_print(start.right, traversal)  # Traverse right subtree
        return traversal
    
    def postorder_print(self, start, traversal):
        """
        Perform a postorder traversal (Left -> Right -> Root).
        Used for search operations only.
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
    
    def clear_tree(self):
        """
        Clears the entire tree by resetting the root to None.
        """
        self.root.left = None
        self.root.right = None
        self.next_value = 1  # Reset the incremental value for future nodes

# Create a BinaryTree instance with root node "root"
tree = BinaryTree(0)

@app.route('/binary-tree', methods=['GET', 'POST'])
def binary_tree():
    """
    Handle GET and POST requests for the binary tree page.
    Allows adding children, searching for nodes, and deleting nodes.
    """
    message = ""
    # Get the current tree structure for display instead of traversal
    tree_structure = tree.get_tree_structure()
    parent_value = None  # Initializes a variable which will hold the value of the parent node

    if request.method == 'POST':
        # Retrieve action and form inputs
        action = request.form.get('action')
       # input_field = request.form.get('input_field', 0)  # Provide empty string as default
        input_field = str(0)

        # Perform the requested action
        if action == 'add_left':
            if not input_field or not input_field.strip():
                message = "Please select a parent node."
            else:
                # Check if the parent node exists before trying to add a child
                parent_node = tree.find_node(tree.root, input_field)
                if parent_node:
                    if parent_node.left:
                        message = f"Left child of '{input_field}' already exists!"
                    else:
                        tree.add_left_child(input_field, None)  # Pass None to use incremental value
                        message = f"Added left child to '{input_field}'."
                else:
                    message = f"Parent node '{input_field}' not found!"

        elif action == 'add_right':
            if not input_field or not input_field.strip():
                message = "Please select a parent node."
            else:
                # Check if the parent node exists before trying to add a child
                parent_node = tree.find_node(tree.root, input_field)
                if parent_node:
                    if parent_node.right:
                        message = f"Right child of '{input_field}' already exists!"
                    else:
                        tree.add_right_child(input_field, None)  # Pass None to use incremental value
                        message = f"Added right child to '{input_field}'."
                else:
                    message = f"Parent node '{input_field}' not found!"

        # Search operations
        elif action == 'preorder_search':
            if not input_field or not input_field.strip():
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.preorder_print(tree.root, "")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in preorder."

        elif action == 'inorder_search':
            if not input_field or not input_field.strip():
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.inorder_print(tree.root, "")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in inorder."

        elif action == 'postorder_search':
            if not input_field or not input_field.strip():
                message = "Enter a value in the Input Field to search."
            else:
                traversal = tree.postorder_print(tree.root, "")
                message = f"Node {input_field} {'found' if input_field in traversal else 'not found'} in postorder."

        elif action == 'delete':
            if not input_field or not input_field.strip():
                message = "Enter a value in the Input Field to delete."
            elif input_field == "0":
                message = "Invalid operation! We can't remove the root node!"
            else:
                deleted = tree.delete_node(input_field)
                message = f"Node {input_field} deleted." if deleted else f"Node {input_field} not found!"
        
        # Clear the tree
        elif action == 'clear':
            tree.clear_tree()  # Clear the entire tree
            message = "The tree has been cleared!"
                

        # Update the tree structure after any modification
        tree_structure = tree.level_order_print()

    # Render the HTML template with updated data
    return render_template('binary_tree.html', tree_structure=tree_structure, message=message)