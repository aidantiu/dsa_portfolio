from app import app 
from flask import render_template, request, make_response, redirect, url_for, session
from .linked_list import LinkedList
import json
import base64
import zlib

def is_operator(char):
    return char in "+-*/^−∗"

def precedence(operator):
    if operator in "+-−":
        return 1
    if operator in "*/∗":
        return 2
    if operator == "^":
        return 3
    return 0

def normalize_operator(operator):
    operator_map = {
        '−': '-',
        '∗': '*',
    }
    return operator_map.get(operator, operator)

def is_valid_expression(expression):
    expression = expression.replace('−', '-').replace('∗', '*')
    
    stack = []
    valid_chars = set("0123456789+-*/^()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    last_char = ""
    
    expression = expression.replace(" ", "")
    
    for i, char in enumerate(expression):
        if char not in valid_chars:
            return False
            
        if char == "(":
            stack.append(char)
                
        elif char == ")":
            if not stack:
                return False
            stack.pop()
            
        elif is_operator(char):
            if i == 0 and char != '-':
                return False
            if i > 0 and is_operator(expression[i-1]) and char != '-':
                return False
                
        elif char.isalnum():
            if last_char and last_char.isalnum():
                continue
                
        last_char = char
    
    if stack or (last_char and not (last_char.isalnum() or last_char == ")")):
        return False
        
    return True

def infix_to_postfix(expression):
    expression = expression.replace('−', '-').replace('∗', '*')
    
    operator_stack = LinkedList()
    postfix = LinkedList()
    steps = []
    current_postfix = []
    
    def add_step(action, scanning, stack_contents, postfix_contents):
        step = {
            "action": action,
            "scanning": scanning,
            "stack": stack_contents,
            "postfix": postfix_contents
        }
        steps.append(step)
    
    i = 0
    while i < len(expression):
        current_char = expression[i]
        scanning = expression[:i+1]
        
        if current_char.isalnum():
            operand = current_char
            while i + 1 < len(expression) and expression[i + 1].isalnum():
                i += 1
                operand += expression[i]
                scanning = expression[:i+1]
            
            postfix.insert_at_end(operand)
            current_postfix.append(operand)
            add_step(
                f"Add operand '{operand}'",
                scanning,
                operator_stack.to_list(),
                current_postfix.copy()
            )
            
        elif current_char == '(':
            operator_stack.insert_at_beginning(current_char)
            add_step(
                "Push '(' to stack",
                scanning,
                operator_stack.to_list(),
                current_postfix.copy()
            )
            
        elif current_char == ')':
            while operator_stack.head and operator_stack.head.data != '(':
                op = operator_stack.remove_beginning()
                postfix.insert_at_end(op)
                current_postfix.append(op)
                add_step(
                    f"Pop and append '{op}'",
                    scanning,
                    operator_stack.to_list(),
                    current_postfix.copy()
                )
                
            if operator_stack.head and operator_stack.head.data == '(':
                operator_stack.remove_beginning()
                add_step(
                    "Remove '('",
                    scanning,
                    operator_stack.to_list(),
                    current_postfix.copy()
                )
                
        elif is_operator(current_char):
            normalized_op = normalize_operator(current_char)
            add_step(
                f"Process operator '{normalized_op}'",
                scanning,
                operator_stack.to_list(),
                current_postfix.copy()
            )
            
            while (operator_stack.head and 
                   operator_stack.head.data != '(' and 
                   precedence(normalize_operator(operator_stack.head.data)) >= precedence(normalized_op)):
                op = normalize_operator(operator_stack.remove_beginning())
                postfix.insert_at_end(op)
                current_postfix.append(op)
                add_step(
                    f"Pop higher precedence '{op}'",
                    scanning,
                    operator_stack.to_list(),
                    current_postfix.copy()
                )
                
            operator_stack.insert_at_beginning(normalized_op)
            add_step(
                f"Push '{normalized_op}' to stack",
                scanning,
                operator_stack.to_list(),
                current_postfix.copy()
            )
        
        i += 1
    
    while operator_stack.head:
        operator = operator_stack.remove_beginning()
        if operator != '(':
            normalized_op = normalize_operator(operator)
            postfix.insert_at_end(normalized_op)
            current_postfix.append(normalized_op)
            add_step(
                f"Pop remaining '{normalized_op}'",
                expression,
                operator_stack.to_list(),
                current_postfix.copy()
            )
    
    add_step(
        "Conversion complete",
        expression,
        operator_stack.to_list(),
        current_postfix.copy()
    )
    
    return postfix.to_list(), steps

def compress_data(data):
    """Compress data to fit within cookie size limits"""
    json_str = json.dumps(data)
    compressed = zlib.compress(json_str.encode('utf-8'))
    return base64.b64encode(compressed).decode('utf-8')

def decompress_data(compressed_data):
    """Decompress data from cookie"""
    if not compressed_data:
        return []
    try:
        compressed_bytes = base64.b64decode(compressed_data.encode('utf-8'))
        decompressed = zlib.decompress(compressed_bytes)
        return json.loads(decompressed.decode('utf-8'))
    except:
        return []

@app.route('/infix-to-postfix', methods=['GET', 'POST'])
def Infix_to_Postfix():
    if request.method == 'POST':
        input_expr = request.form['input']
        if not is_valid_expression(input_expr):
            response = make_response(redirect(url_for('Infix_to_Postfix')))
            response.set_cookie('input_expr', input_expr)
            response.set_cookie('output', 'Invalid Expression! Try again...')
            response.set_cookie('steps_data', '')
            return response

        output, steps = infix_to_postfix(input_expr)
        
        # Compress steps data to fit in cookie
        compressed_steps = compress_data(steps)
        
        response = make_response(redirect(url_for('Infix_to_Postfix')))
        response.set_cookie('input_expr', input_expr)
        response.set_cookie('output', " ".join(output))
        response.set_cookie('steps_data', compressed_steps)
        return response
    
    input_expr = request.cookies.get('input_expr', '')
    output = request.cookies.get('output', '')
    compressed_steps = request.cookies.get('steps_data', '')
    steps = decompress_data(compressed_steps)
    instruction_steps = get_instruction_steps()
    
    response = make_response(render_template('infix_to_postfix.html', 
                                           title="Infix To Postfix",
                                           input=input_expr,
                                           output=output,
                                           steps=steps,
                                           instruction_steps=instruction_steps))
    
    # Clear cookies after rendering
    response.set_cookie('input_expr', '', expires=0)
    response.set_cookie('output', '', expires=0)
    response.set_cookie('steps_data', '', expires=0)
    return response

# Dictionary to store the How To Use data
def get_instruction_steps():
    return [
        "Enter your mathematical expression in the input field using standard infix notation (e.g., \"3 + 4 * 2\").",
        "Click the \"Convert\" button to convert your infix expression to postfix notation.",
        "View your converted postfix expression in the output box.",
        "Use the toggle button with the eye symbol to show/hide the step-by-step conversion process on the right side.",
        "View the detailed conversion steps in the table, showing each operation and stack changes.",
        "Clear the input and output at any time using the \"Reset\" button.",
        "For valid expressions, use: Numbers (0-9), Operators (+, -, *, /, ^) and Parentheses ( ). Spaces between numbers and operators are optional.",
        "Watch for error messages if your input expression is invalid."
    ]