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
        while current_node:  # Traverse the list
            if current_node.data == data:  # Data found
                return True
            current_node = current_node.next
        return False  # Data not found

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

# Create a LinkedList instance
linkedlist = LinkedList()
app.secret_key = 'temporary-key'

# Route for handling linked list operations via the web interface
@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist_home():
    search_result = None
    delete_data = request.form.get('data', '').strip()
    search_query = ""
    validation_message = session.get('validation_message', None)
    validation_type = session.get('validation_type', None)
    data = request.form.get('data', '').strip()

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
        if action == 'add_at_beginning' and not data:
            validation_message = "Please input data in the input field."
            validation_type = "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'add_at_end' and not data:
            validation_message = "Please input data in the input field."
            validation_type = "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'add_at_beginning' and data:
            linkedlist.insert_at_beginning(data)
            validation_message = f"'{data}' added at the beginning."
            validation_type = "success"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'add_at_end' and data:
            linkedlist.insert_at_end(data)
            validation_message = f"'{data}' added at the end."
            validation_type = "success"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        # Handle search, deletion, or empty list conditions
        elif linkedlist.head is None:
            if action == 'search':
                validation_message = "The list is empty. You cannot search items."
                validation_type = "error"
                session['validation_message'] = validation_message
                session['validation_type'] = validation_type
            elif action in ['remove_beginning', 'remove_end', 'remove_at']:
                validation_message = "The list is empty. You cannot delete items."
                validation_type = "error"
                session['validation_message'] = validation_message
                session['validation_type'] = validation_type
            else:
                validation_message = "The list is empty."
                validation_type = "error"
                session['validation_message'] = validation_message
                session['validation_type'] = validation_type

        # Search for a specific value in the linked list
        elif action == 'search':
            search_result = linkedlist.search(data)
            validation_message = f"Please enter a value to search." if not data else f"'{data}' {'is found' if search_result else 'is not found'}."
            validation_type = "success" if search_result else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        # Remove the first element from the list
        elif action == 'remove_beginning':
            removed_data = linkedlist.remove_beginning()
            validation_message = f"'{removed_data}' removed from the beginning." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        # Remove the last element from the list
        elif action == 'remove_end':
            removed_data = linkedlist.remove_at_end()
            validation_message = f"'{removed_data}' removed from the end." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        # Remove a specific element by value
        elif action == 'remove_at':
            if not delete_data:
                validation_message = "Please enter a value to delete."
                validation_type = "error"
            else:
                removed_data = linkedlist.remove_at(delete_data)
                validation_message = f"'{removed_data}' has been removed." if removed_data else f"'{delete_data}' not found for removal."
                validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        # Update the linked list data in cookies and redirect
        linked_list_data = linkedlist.to_list()
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', json.dumps(linked_list_data))
        return resp

    # Clear linked list data when 'clear' query parameter is set
    if request.args.get('clear') == 'true':
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', '', expires=0)
        return resp
    
    # Remove validation messages from session after rendering
    if validation_message:
        session.pop('validation_message', None)
        session.pop('validation_type', None)

    # Prepare the linked list for display
    linked_list_str = " -> ".join(linkedlist.to_list()) if linkedlist.to_list() else "The list is empty."

    # Render the linked list template with context data
    return render_template(
        'linked-list.html',
        linked_list_str=linked_list_str,
        validation_message=validation_message,
        validation_type=validation_type,
        search_query=request.form.get('data', '').strip(),
        empty_list=linkedlist.head is None
    )
