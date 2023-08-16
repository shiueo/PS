import sys


def infix_to_postfix(expression):
    operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []

    for char in expression:
        if char.isalpha():
            output.append(char)
        elif char in '+-*/':
            while (operator_stack and operator_stack[-1] != '(' and
                   operator_precedence.get(char, 0) <= operator_precedence.get(operator_stack[-1], 0)):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output.append(operator_stack.pop())

    return ''.join(output)


print(infix_to_postfix(sys.stdin.readline().strip()))
