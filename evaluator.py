from tokenize import Token, Tokenize, operator_dict, get_precedence
import math

NUM_OPERANDS = 2

"""This function calc the factorial that getting from the unary_operator function"""
def factorial(num : int) -> float:
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

"""This function handles defining the action of each of the binary operators"""

def binary_operator(op_1: float, op_2: float, operator: str):
    if operator == '+':
        return op_1 + op_2
    elif operator == '-':
        return op_1 - op_2
    elif operator == '*':
        return op_1 * op_2
    elif operator == '/':
        if op_2 == 0:
            raise ValueError('Cannot divide by zero')
        return op_1 / op_2
    elif operator == '^':
        return pow(op_1, op_2)
    elif operator == '%':
        if op_2 == 0:
            raise ValueError('Cannot modulo by zero')
        return op_1 % op_2
    elif operator == '$':
        return max(op_1, op_2)
    elif operator == '&':
        return min(op_1, op_2)
    elif operator == '@':
        return (op_1 + op_2) / NUM_OPERANDS
    else:
        raise ValueError('Invalid operator')

"""This function handles defining the action of each of the binary operator"""


def unary_operator(operand: float, operator: str):
    if operator == '~':
        return -operand
    elif operator == '!':
        return factorial(int(operand))
    else:
        raise ValueError('Invalid operator')


def classify_operator(operator: str, stack: list):
    op_info = operator_dict[operator]
    arity = op_info['arity']
    #check if there is enough operand in the expression
    if len(stack) < arity:
        raise ValueError("There are not enough operands for this operator")
    if arity == 1:
        operand = stack.pop()
        return unary_operator(operand, operator)
    elif arity == 2:
        operand_1 = stack.pop()
        operand_2 = stack.pop()
        return binary_operator(operand_1, operand_2, operator)
    else:
        raise ValueError("Too much arity for the operator")

def evaluator(tokens_lst: list):
    stack = []
    for token in reversed(tokens_lst):
        #when the token type is number we directly append it to the stack
        if token.type == Tokenize.NUMBER:
            stack.append(float(token.value))
        #when the token type is operator, need to classify which operator it is , and append the result to the stack
        elif token.type == Tokenize.OPERATOR:
            operator = token.value
            result = classify_operator(operator, stack)
            stack.append(result)
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    #return the last element in the stack
    return stack.pop()





