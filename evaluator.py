from tokenize import Token, Tokenize, operator_dict, get_precedence
import math

NUM_OPERANDS = 2

"""This function handles defining the action of each of the operators"""


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


def unary_operator(operand: float, operator: str):


def classify_operator(operator: str, stack: list) -> list:
    op_info = operator_dict[operator]
    arity = op_info['arity']
    if len(stack) < arity:
        raise ValueError("There are not enough operands for this operator")
