from app import app
from flask import render_template, request, redirect, url_for
from .linked_list import LinkedList


# Helper function to determine if a character is an operator
def is_operator(char):
    return char in "+-*/^"  # Returns True or False


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
    
    i = 0
    while i < len(expression):
        if expression[i].isdigit():  # Checks if element is a digit
            num = expression[i]
            while i + 1 < len(expression) and expression[i + 1].isdigit():
                i += 1
                num += expression[i]
            output.insert_at_end(num)  # Push the full number to the output stack
        elif expression[i].isalpha():  # Checks if element is an operand
            output.insert_at_end(expression[i])  # Push to output stack
        elif expression[i] == '(':
            operator_stack.insert_at_beginning(expression[i])  # Push to operator stack
        elif expression[i] == ')':
            # If the top of the operator_stack is an opening bracket
            while operator_stack.head and operator_stack.head.data != '(':
                # Pop element from the operator_stack and push to the output stack
                output.insert_at_end(operator_stack.remove_beginning())
            operator_stack.remove_beginning()  # Pop the '(' from the stack
        elif is_operator(expression[i]):
            # While an operator at the top of the operators stack has greater/equal precedence than element
            while (operator_stack.head and precedence(operator_stack.head.data) >= precedence(expression[i])):
                # Pop operator from the operator_stack into the output stack
                output.insert_at_end(operator_stack.remove_beginning())
            operator_stack.insert_at_beginning(expression[i])  # Push element in the operator stack
        i += 1

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