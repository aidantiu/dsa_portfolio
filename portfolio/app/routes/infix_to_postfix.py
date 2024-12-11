from app import app
from flask import render_template, request, redirect, url_for
from .linked_list import LinkedList


# Helper function to determine if a character is an operator
def is_operator(char):
    return char in "+-*/^" # Returns True or False


# Helper function to define operator precedence
def precedence(operator):
    if operator in "+-":
        return 1
    if operator in "*/":
        return 2
    if operator == "^":
        return 3
    return 0


# Infix to Postfix conversion
def infix_to_postfix(expression):
    operator_stack = LinkedList()  # Stack to hold operators
    output = LinkedList()  # Linked list (treated as stack) to hold the postfix expression
    expression = expression.replace(" ", "")  # Removes spaces before transforming to postfix
    
    for element in expression:  
        if element.isalnum():  # Checks if element is an operand
            output.insert_at_end(element) # Pushed to output stack 
        elif element == '(':  
            operator_stack.insert_at_beginning(element) # Pushed to operator stack 
        elif element == ')':  
            # If the top of the operator_stack is an openning bracket
            while operator_stack.head and operator_stack.head.data != '(': 
                # Pops elemnent from the operator_stack and pushed to the output stack
                output.insert_at_end(operator_stack.remove_beginning()) 
            operator_stack.remove_beginning()  # Pops the '(' from the stack
        elif is_operator(element):  
            # While an operator at the top of the operators stack has greater/equal precedence than element
            while (operator_stack.head and precedence(operator_stack.head.data) >= precedence(element)): 
                # Pop operator from the operator_stack into the output stack 
                output.insert_at_end(operator_stack.remove_beginning()) 
            operator_stack.insert_at_beginning(element) # Pushes element in the outputr stack

    # Pop remaining operators from the operator stack to the output stack 
    while operator_stack.head:
        output.insert_at_end(operator_stack.remove_beginning())
    
    return output.to_list()  # Returns a list for readability





@app.route('/infix-to-postfix', methods=['GET', 'POST'])
def Infix_to_Postfix():
    output = ""  # Initialize output
    
    if request.method == 'POST':
        # Handle form submission (POST)
        input_expression = request.form['input']  # Match the form field name
        output = infix_to_postfix(input_expression)  # Process the input
        
        # Redirect to the same page with the output (GET request)
        return redirect(url_for('Infix_to_Postfix', output=" ".join(output)))
    
    # Handle GET request: check for 'output' parameter
    if 'output' in request.args:    
        output = request.args['output']
    
    return render_template('infix_to_postfix.html', title="Infix To Postfix", output=output)