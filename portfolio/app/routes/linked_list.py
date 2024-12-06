""" 
This module contains the routes for the linkedlist blueprint.
"""


from app import app
from flask import render_template, request, redirect, url_for

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

@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist_home():
    search_result = None  # Initialize search result
    search_query = ""  # Initialize search query
    show_search_result = False  # Track if the search result should be displayed

    if request.method == 'POST':
        action = request.form.get('action')  # Get the action from the button
        data = request.form.get('data', '')  # Get the user input (default to empty if not provided)

        if action == "add_at_beginning" and data:
            linkedlist.insert_at_beginning(data)
        elif action == "add_at_end" and data:
            linkedlist.insert_at_end(data)
        elif action == "remove_beginning":
            linkedlist.remove_beginning()
        elif action == "remove_end":
            linkedlist.remove_at_end()
        elif action == "search" and data:
                       # Redirect to include search query in the URL
            return redirect(url_for('linkedlist_home', search_query=data))

        # Redirect to avoid duplicate form submissions
        return redirect(url_for('linkedlist_home'))

    # Handle GET request
    search_query = request.args.get('search_query', "")  # Get search query from the query string
    if search_query:  # If there is a search query, perform the search
        search_result = linkedlist.search(search_query)
        show_search_result = True

    # Prepare output as a string
    linked_list_str = " -> ".join(linkedlist.to_list()) if linkedlist.to_list() else "The list is empty."

    # Render the linked list template with current data
    return render_template(
        'linked-list.html',
        linked_list=linkedlist.to_list(),
        linked_list_str=linked_list_str,
        search_result=search_result,
        search_query=search_query,
        show_search_result=show_search_result
    )