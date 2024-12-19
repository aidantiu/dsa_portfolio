from app import app
from flask import render_template, request, make_response, redirect, url_for
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


# Helper function to validate the input expression
def is_valid_expression(expression):
    stack = []
    valid_chars = set("0123456789+-*/^()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") # Set of valid characters in the input expression
    last_char = ""
    
    for char in expression.replace(" ", ""): # Ensures that the input expression has no spaces
        if char not in valid_chars:
            return False  # Invalid character found
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False  # Unmatched closing parenthesis
            stack.pop()
        elif is_operator(char):
            if not last_char or is_operator(last_char) or last_char == "(":
                return False  # Invalid operator placement
        elif char.isalnum():  # Check if alphanumeric (digits or letters)
            if last_char and last_char.isalnum():
                return False  # Consecutive operands found
        last_char = char

    # Ensure no unmatched opening parentheses and last character is valid
    return not stack and (last_char.isalnum() or last_char == ")")


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
    if request.method == 'POST':
        input_expr = request.form['input']
        if not is_valid_expression(input_expr):  # Validate input expression
            response = make_response(redirect(url_for('Infix_to_Postfix')))
            response.set_cookie('input_expr', input_expr)
            response.set_cookie('output', 'Invalid Expression! Try again...')
            return response

        output = infix_to_postfix(input_expr)
        response = make_response(redirect(url_for('Infix_to_Postfix')))
        response.set_cookie('input_expr', input_expr)
        response.set_cookie('output', " ".join(output))
        return response
    
    input_expr = request.cookies.get('input_expr', '')
    output = request.cookies.get('output', '')
    response = make_response(render_template('infix_to_postfix.html', 
                                             title="Infix To Postfix",
                                             input=input_expr,
                                             output=output))
    response.set_cookie('input_expr', '', expires=0)
    response.set_cookie('output', '', expires=0)
    return response