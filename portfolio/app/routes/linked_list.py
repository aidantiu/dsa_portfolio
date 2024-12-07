""" 
This module contains the routes for the linkedlist blueprint.
"""


from app import app
from flask import render_template, request, redirect, url_for, session

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data): # Insert a new node with the given data at the beginning of the list
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data): # Insert a new node with the given data at the end of the list
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data): # Search for a node with the given data in the list
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self): # Print all the nodes' data in the list
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_beginning(self): # Remove the node at the beginning of the list and return its data
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_data

    def remove_at_end(self): # Remove the node at the end of the list and return its data
        if self.head is None:
            return None
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        self.tail = current
        return removed_data

    def remove_at(self, data): # Remove the node with the given data from the list and return its data
        if self.head is None:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_data
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            return None
        removed_data = current.next.data
        current.next = current.next.next
        if current.next is None:
            self.tail = current
        return removed_data

    def to_list(self): # Convert the linked list to a Python list and return it
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

linkedlist = LinkedList()
app.secret_key = 'temporary-secret-key' # Required for persistent data during sessions

@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist_home():
    search_result = None
    delete_data = request.form.get('index', '').strip()
    search_query = ""
    show_search_result = False
    index_data = request.form.get('index', '').strip()
    validation_message = session.get('validation_message', None)  # Get validation message from session
    data = request.form.get('data', '').strip()

    if request.method == 'POST':
        action = request.form.get('action')    

        # Handle adding actions first
        # When the input field is missing:
        if action == 'add_at_beginning' and not data:
            validation_message = "Please input a data in the input field."
            session['validation_message'] = validation_message
        elif action == 'add_at_end' and not data:
            validation_message = "Please input a data in the input field."
            session['validation_message'] = validation_message
        # When the input field is not missing:
        elif action == 'add_at_beginning' and data:
            linkedlist.insert_at_beginning(data)
            validation_message = f"'{data}' added at the beginning."
            session['validation_message'] = validation_message
        elif action == 'add_at_end' and data:
            linkedlist.insert_at_end(data)
            validation_message = f"'{data}' added at the end."
            session['validation_message'] = validation_message

        # Handle empty list validation for search and delete actions
        elif linkedlist.head is None:
            if action == 'search':
                validation_message = "The list is empty. You cannot search items."
                session['validation_message'] = validation_message
            elif action in ['remove_beginning', 'remove_end', 'remove_at']:
                validation_message = "The list is empty. You cannot delete items."
                session['validation_message'] = validation_message
            else:
                validation_message = "The list is empty."
                session['validation_message'] = validation_message

        # Handle search actions
        elif action == 'search':
            search_result = linkedlist.search(data)
            validation_message = f"Please enter a value to search." if not data else f"'{data}' {'is found' if search_result else 'is not found'}."
            session['validation_message'] = validation_message

        # Handle delete actions
        elif action == 'remove_beginning':
            removed_data = linkedlist.remove_beginning()
            validation_message = f"'{removed_data}' removed from the beginning." if removed_data else "The list is empty."
            session['validation_message'] = validation_message
        elif action == 'remove_end':
            removed_data = linkedlist.remove_at_end()
            validation_message = f"'{removed_data}' removed from the end." if removed_data else "The list is empty."
            session['validation_message'] = validation_message
        elif action == 'remove_at' and delete_data:
            removed_data = linkedlist.remove_at(delete_data)
            validation_message = f"'{removed_data}' has been removed." if removed_data else f"'{delete_data}' not found for removal."
            session['validation_message'] = validation_message

        # Redirect to avoid duplicate form submissions
        return redirect(url_for('linkedlist_home'))
  
    # After the GET request is handled, clear the validation message from the session
    if validation_message:
        session.pop('validation_message', None)

    # Prepare output as a string
    linked_list_str = " -> ".join(linkedlist.to_list()) if linkedlist.to_list() else "The list is empty."

    # Render the linked list template with current data
    return render_template(
        'linked-list.html',
        linked_list_str=linked_list_str,
        validation_message=validation_message,
        search_query=request.form.get('data', '').strip(),
        empty_list=linkedlist.head is None
    ) 