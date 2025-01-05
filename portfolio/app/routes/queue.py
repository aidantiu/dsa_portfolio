from app import app
import json
from flask import render_template, request, redirect, url_for, session, make_response
from .linked_list import LinkedList  # Import the LinkedList class


# Create a LinkedList instance
linkedlist_stack = LinkedList()
app.secret_key = 'temporary-key'

@app.route('/queue', methods=['GET', 'POST'])
def queue_home():
    # Check if this is a redirected GET request
    is_redirected_get = session.get('is_redirected_get', False)
    queue_type = session.get('queue_type', 'queue')  # Default to normal queue
    data = request.form.get('data', '').strip()  # Get data input from the form
    validation_string = session.get('validation_string', None)
    instruction_steps = get_instruction_steps() 
    
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'toggle_queue':  # Toggle between normal queue and double-ended queue
            linkedlist_stack.clear()  # Reset the linked list
            if queue_type == 'queue':
                queue_type = 'double-ended-queue'
                validation_string = "Switched to Double Ended Queue."
            else:
                queue_type = 'queue'
                validation_string = "Switched to Queue."

            session['queue_type'] = queue_type  # Update session variable
            session['validation_string'] = validation_string
            session.modified = True  # Force session persistence

        if queue_type == 'queue':  # Basic Queue Logic
            if action == 'add_at_end':  # Add at the end
                if not data:
                    validation_string = "Please input data in the input field."
                else:
                    linkedlist_stack.insert_at_end(data)
                    validation_string = f"'{data}' added to the queue."

            elif action == 'pop_at_start':  # Pop from the front
                removed_data = linkedlist_stack.remove_beginning()
                if removed_data:
                    validation_string = f"'{removed_data}' removed from the queue."
                else:
                    validation_string = "The queue is empty."

            elif action == 'delete_at_node':  # Delete a specific node
                if not data:
                    validation_string = "Please input node data to delete."
                else:
                    removed_data = linkedlist_stack.remove_at(data)
                    if removed_data:
                        validation_string = f"'{removed_data}' deleted from the queue."
                    else:
                        validation_string = "Node not found."

        elif queue_type == 'double-ended-queue':  # Double-Ended Queue Logic
            if action == 'add_at_end':  # Add at the end
                if not data:
                    validation_string = "Please input data in the input field."
                else:
                    linkedlist_stack.insert_at_end(data)
                    validation_string = f"'{data}' added to the double-ended queue."

            elif action == 'add_at_start':  # Add at the start
                if not data:
                    validation_string = "Please input data in the input field."
                else:
                    linkedlist_stack.insert_at_beginning(data)
                    validation_string = f"'{data}' added to the start of the double-ended queue."

            elif action == 'pop_at_start':  # Pop from the front
                removed_data = linkedlist_stack.remove_beginning()
                if removed_data:
                    validation_string = f"'{removed_data}' removed from the double-ended queue."
                else:
                    validation_string = "The double-ended queue is empty."

            elif action == 'pop_at_end':  # Pop from the end
                removed_data = linkedlist_stack.remove_at_end()
                if removed_data:
                    validation_string = f"'{removed_data}' removed from the end of the double-ended queue."
                else:
                    validation_string = "The double-ended queue is empty."

            elif action == 'delete_at_node':  # Delete a specific node
                if not data:
                    validation_string = "Please input node data to delete."
                else:
                    removed_data = linkedlist_stack.remove_at(data)
                    if removed_data:
                        validation_string = f"'{removed_data}' deleted from the double-ended queue."
                    else:
                        validation_string = "Node not found."

        # Set the validation string and save to session
        session['validation_string'] = validation_string
        linked_list_data = linkedlist_stack.to_list()  # Get linked list as a string
        resp = make_response(redirect(url_for('queue_home')))
        resp.set_cookie('linked_list_data', json.dumps(linked_list_data))

        # Set the redirected GET flag to True for the next request
        session['is_redirected_get'] = True

        return resp

    # Handle GET request logic
    if not is_redirected_get:
        linkedlist_stack.clear()  # Clear the linked list on normal GET request
        validation_string = None  # Don't show any validation string on initial GET

    # Set the redirected GET flag to False after handling the request
    session['is_redirected_get'] = False

    return render_template(
        'queue.html',
        queue_type=queue_type,
        validation_string=validation_string,  # Only show validation if set
        linked_list_items=linkedlist_stack.to_list(),
        instruction_steps=instruction_steps,
        title='Queue Operations'
    )

# List to store the How To Use data
def get_instruction_steps():
    return [
        "Begin by entering your desired value in the input field.",

        "Select the operation you would like to perform on the queue using the dropdown menu. You can switch between \n"
        "a Simple Queue and a Double-Ended Queue by clicking the specific toggle queue button.",

        "For Simple Queue, use the \"Add at Rear\" button to insert values at the back, maintaining the First-In-First-Out (FIFO) principle; \n"
        "for Double-Ended Queue, click the \"Add Operations\" dropdown to choose between adding at front or rear.",

        "Remove elements using \"Pop at Front\" in Simple Queue to delete the first element; in Double-Ended Queue, \n"
        "use the \"Delete Operations\" dropdown to remove from either end.",

        "Watch the visual feedback as purple highlights indicate active operations, and arrows show the flow direction.",

        "Monitor the success/error messages at the top of the screen that confirm your actions and provide helpful feedback about queue status.",

        "Observe how elements are displayed as rounded rectangles with connecting arrows, showing the relationship between items in both queue types.",

        "Note that when the queue is empty, a message \"Queue is empty\" appears, and operations are performed based on the selected queue type \n"
        "Simple Queue maintains strict FIFO, while Double-Ended Queue allows flexible operations at both ends."
    ]