from app import app
import json
from flask import render_template, request, redirect, url_for, session, make_response

# Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the list

# LinkedList class to manage linked list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Points to the first node of the linked list
        self.tail = None  # Points to the last node of the linked list

    # Inserts a new node at the beginning of the linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:  # If the list is not empty
            new_node.next = self.head
            self.head = new_node
        else:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        return True

    # Inserts a new node at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:  # If the list is not empty
            self.tail.next = new_node
            self.tail = new_node
        else:  # If the list is empty
            self.tail = new_node
            self.head = new_node
        return True
    
    # Searches for a node with the specified data
    def search(self, data):
        current_node = self.head
        index = 0  # Track the position of the node
        while current_node:
            if current_node.data == data:
                return index  # Return the position of the found node
            current_node = current_node.next
            index += 1
        return -1  # Return -1 if data is not found


    # Removes the first node from the linked list
    def remove_beginning(self):
        if self.head is None:  # If the list is empty
            return None
        removed_data = self.head.data  # Data of the node to remove
        self.head = self.head.next  # Update head to the next node
        if self.head is None:  # If the list becomes empty
            self.tail = None
        return removed_data

    # Removes the last node from the linked list
    def remove_at_end(self):
        if self.head is None:  # If the list is empty
            return None
        if self.head.next is None:  # If the list has only one node
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current = self.head
        while current.next.next:  # Traverse to the second-to-last node
            current = current.next
        removed_data = current.next.data  # Data of the node to remove
        current.next = None
        self.tail = current  # Update the tail to the second-to-last node
        return removed_data

    # Removes a node with the specified data
    def remove_at(self, data):
        if self.head is None:  # If the list is empty
            return None
        if self.head.data == data:  # If the data is in the head node
            removed_data = self.head.data
            self.head = self.head.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
            return removed_data
        current = self.head
        while current.next and current.next.data != data:  # Traverse the list
            current = current.next
        if current.next is None:  # Data not found
            return None
        removed_data = current.next.data  # Data of the node to remove
        current.next = current.next.next
        if current.next is None:  # If the removed node was the tail
            self.tail = current
        return removed_data

    # Converts the linked list to a Python list
    def to_list(self):
        result = []
        current = self.head
        while current:  # Traverse the list
            result.append(current.data)
            current = current.next
        return result
    
    # Converts the linked list to a string (for display purposes)
    def to_string(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements) if elements else 'Empty'
    
    # Empties the list
    def clear(self):
        self.head = None
        self.tail = None

# Create a LinkedList instance
linkedlist = LinkedList()
app.secret_key = 'temporary-key'

## Route for handling linked list operations via the web interface
@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist_home():
    search_result = None
    delete_data = request.form.get('data', '').strip()
    search_query = ""
    validation_message = session.get('validation_message', None)
    validation_type = session.get('validation_type', None)
    data = request.form.get('data', '').strip()
    highlighted_item = None  # New variable to track the item to highlight
    instruction_steps = get_instruction_steps()  # Get the instruction steps for the How To Use section

    # Retrieve linked list data from cookies
    linked_list_data = request.cookies.get('linked_list_data')
    
    # Initialize the linked list for a new session
    if request.method == 'GET' and not linked_list_data:
        linkedlist.head = None
        linkedlist.tail = None

    # Populate linked list with data from cookies
    if linked_list_data:
        linked_list_data = json.loads(linked_list_data)
        linkedlist.head = None
        linkedlist.tail = None
        for item in linked_list_data:
            linkedlist.insert_at_end(item)

    # Handle POST requests for different linked list operations
    if request.method == 'POST':
        action = request.form.get('action')

        # Add data at the beginning of the list
        if action in ['add_at_beginning', 'add_at_end']:
            if not data:
                validation_message = "Please input data in the input field."
                validation_type = "error"
            else:
                if action == 'add_at_beginning':
                    linkedlist.insert_at_beginning(data)
                    validation_message = f"'{data}' added at the beginning."
                else:
                    linkedlist.insert_at_end(data)
                    validation_message = f"'{data}' added at the end."
                validation_type = "success"

        # Handle search
        elif action == 'search':
            if not data:  # Check if no input is provided
                validation_message = "Please input data in the input field."
                validation_type = "error"
            else:
                search_index = linkedlist.search(data)
                search_result = search_index != -1  # Check if the item is found
                validation_message = (
                    f"'{data}' is found." if search_result else f"'{data}' is not found."
                )
                validation_type = "success" if search_result else "error"
                if search_result:
                    highlighted_item = data  # Highlight the found item

        # Remove the first element from the list
        elif action == 'remove_beginning':
            removed_data = linkedlist.remove_beginning()
            validation_message = f"'{removed_data}' removed from the beginning." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"

        # Remove the last element from the list
        elif action == 'remove_end':
            removed_data = linkedlist.remove_at_end()
            validation_message = f"'{removed_data}' removed from the end." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"

        # Remove a specific element by value
        elif action == 'remove_at':
            if not delete_data:
                validation_message = "Please enter a value to delete."
                validation_type = "error"
            else:
                removed_data = linkedlist.remove_at(delete_data)
                validation_message = f"'{removed_data}' has been removed." if removed_data else f"'{delete_data}' not found for removal."
                validation_type = "success" if removed_data else "error"

        # Update the linked list data in cookies and redirect
        linked_list_data = linkedlist.to_list()
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', json.dumps(linked_list_data))
        resp.set_cookie('highlighted_item', highlighted_item or "", max_age=3600)  # Store highlighted item for 1 hour
        session['validation_message'] = validation_message
        session['validation_type'] = validation_type
        return resp

    # Clear linked list data when 'clear' query parameter is set
    if request.args.get('clear') == 'true':
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', '', expires=0)
        resp.set_cookie('highlighted_item', '', expires=0)
        return resp
    
    # Remove validation messages from session after rendering
    if validation_message:
        session.pop('validation_message', None)
        session.pop('validation_type', None)

    # Prepare the linked list for display as separate items
    linked_list_items = linkedlist.to_list() if linkedlist.to_list() else None
    
    # Get the highlighted item from cookies
    highlighted_item = request.cookies.get('highlighted_item', None)

    # Render the linked list template with context data
    return render_template(
        'linked-list.html',
        linked_list_items=linked_list_items,
        validation_message=validation_message,
        validation_type=validation_type,
        empty_list=linkedlist.head is None,
        highlighted_item=highlighted_item,
        instruction_steps=instruction_steps,  # Add instruction steps for the How To Use section
        title='Linked List'
    )
# Dictionary to store the How To Use data
def get_instruction_steps():
    return [
        "Enter your desired data in the input field.",
        "Click the \"Add\" button and select either \"Add at Beginning\" to insert the value at the start or \"Add at End\" to append it to the list.",
        "To remove elements, click the \"Delete\" button and choose \"Delete at Beginning\" to remove the first node or \"Delete at End\" to remove the last node.",
        " For deleting a specific value, type the value you want to remove in the input field, then click \"Delete\" and select \"Delete a Node\".",
        "Use the \"Search\" button to find a specific value in the list, which will highlight the matching node if found",
        "Watch for success/error messages at the top of the box that will confirm your actions.",
        "Follow the linked list connections through the arrow (→) indicators, with an \"X\" marking the end of the list.",
    ]