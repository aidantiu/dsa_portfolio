from app import app
import json
from flask import render_template, request, redirect, url_for, session, make_response

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_data

    def remove_at_end(self):
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

    def remove_at(self, data):
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

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

linkedlist = LinkedList()
app.secret_key = 'temporary-secret-key'

@app.route('/linked-list', methods=['GET', 'POST'])
def linkedlist_home():
    search_result = None
    delete_data = request.form.get('index', '').strip()
    search_query = ""
    validation_message = session.get('validation_message', None)
    validation_type = session.get('validation_type', None)
    data = request.form.get('data', '').strip()

    linked_list_data = request.cookies.get('linked_list_data')
    
    if request.method == 'GET' and not linked_list_data:
        linkedlist.head = None
        linkedlist.tail = None

    if linked_list_data:
        linked_list_data = json.loads(linked_list_data)
        linkedlist.head = None
        linkedlist.tail = None
        for item in linked_list_data:
            linkedlist.insert_at_end(item)

    if request.method == 'POST':
        action = request.form.get('action')

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
            if not linkedlist.search(data):
                linkedlist.insert_at_beginning(data)
                validation_message = f"'{data}' added at the beginning."
                validation_type = "success"
            else:
                validation_message = f"'{data}' already exists."
                validation_type = "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'add_at_end' and data:
            if not linkedlist.search(data):
                linkedlist.insert_at_end(data)
                validation_message = f"'{data}' added at the end."
                validation_type = "success"
            else:
                validation_message = f"'{data}' already exists."
                validation_type = "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
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
        elif action == 'search':
            search_result = linkedlist.search(data)
            validation_message = f"Please enter a value to search." if not data else f"'{data}' {'is found' if search_result else 'is not found'}."
            validation_type = "success" if search_result else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'remove_beginning':
            removed_data = linkedlist.remove_beginning()
            validation_message = f"'{removed_data}' removed from the beginning." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'remove_end':
            removed_data = linkedlist.remove_at_end()
            validation_message = f"'{removed_data}' removed from the end." if removed_data else "The list is empty."
            validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type
        elif action == 'remove_at' and delete_data:
            removed_data = linkedlist.remove_at(delete_data)
            validation_message = f"'{removed_data}' has been removed." if removed_data else f"'{delete_data}' not found for removal."
            validation_type = "success" if removed_data else "error"
            session['validation_message'] = validation_message
            session['validation_type'] = validation_type

        linked_list_data = linkedlist.to_list()
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', json.dumps(linked_list_data))
        return resp

    if request.args.get('clear') == 'true':
        resp = make_response(redirect(url_for('linkedlist_home')))
        resp.set_cookie('linked_list_data', '', expires=0)
        return resp
    
    if validation_message:
        session.pop('validation_message', None)
        session.pop('validation_type', None)

    linked_list_str = " -> ".join(linkedlist.to_list()) if linkedlist.to_list() else "The list is empty."

    return render_template(
        'linked-list.html',
        linked_list_str=linked_list_str,
        validation_message=validation_message,
        validation_type=validation_type,
        search_query=request.form.get('data', '').strip(),
        empty_list=linkedlist.head is None
    )