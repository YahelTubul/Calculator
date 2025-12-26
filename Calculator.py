from enum import Enum


# create enum for definition the types of token

class Tokenize(Enum):
    NUMBER = 1
    OPERATOR = 2
    LPAREN = 3
    RPAREN = 4


operators: list = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!']

operator_dict = {
    '+': {'precedence': 1, 'position': 'middle', 'arity': 2},  # add
    '-': {'precedence': 1, 'position': 'middle', 'arity': 2},  # sub

    '*': {'precedence': 2, 'position': 'middle', 'arity': 2},  # multiply
    '/': {'precedence': 2, 'position': 'middle', 'arity': 2},  # divide

    '^': {'precedence': 3, 'position': 'middle', 'arity': 2},  # power

    '%': {'precedence': 4, 'position': 'middle', 'arity': 2},  # modulo

    '$': {'precedence': 5, 'position': 'middle', 'arity': 2},  # max number
    '&': {'precedence': 5, 'position': 'middle', 'arity': 2},  # minimum number
    '@': {'precedence': 5, 'position': 'middle', 'arity': 2},  # average

    '~': {'precedence': 6, 'position': 'left', 'arity': 1},  # negative
    '!': {'precedence': 6, 'position': 'right', 'arity': 1},  # factorial
}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    # pass each char in the exprssion and defines each character in the expression to the type of the token.
    def split_tokenize(expression: str) -> list:
        tokens: list = []
        long_num: str = ""
        token_type: Tokenize = None
        for char in expression:
            # check for negative numbers. by comare if the prev token its not a number type
            if char == '-' and (token_type in [None, Tokenize.OPERATOR, Tokenize.LPAREN]):
                long_num += char
            # check if the char is number or float number and for number with two numbers and more
            elif (char.isdigit() or (char == '.' and '.' not in long_num)):
                long_num += char
            else:
                # add the number to the tokens list
                if long_num:
                    tokens.append(Token(Tokenize.NUMBER, long_num))
                    long_num = ""
                    token_type = Tokenize.NUMBER
                # check if char is a valid operator,and add it to list
                if (char in operators):
                    tokens.append(Token(Tokenize.OPERATOR, char))
                    token_type = Tokenize.OPERATOR
                # check if char is left paren
                elif (char == '('):
                    tokens.append(Token(Tokenize.LPAREN, char))
                    token_type = Tokenize.LPAREN
                # check if char is right paren
                elif (char == ')'):
                    tokens.append(Token(Tokenize.RPAREN, char))
                    token_type = Tokenize.RPAREN
                else:
                    raise ValueError("Invalid token")
        # add if there is the last char to the list
        if long_num:
            tokens.append(Token(Tokenize.NUMBER, long_num))
        return tokens

def infix_to_prefix(tokens: list) -> list:
    # TODO: implement the rest of the function
    prefix_result: list = []
    temp_stack: list = []
    for token in tokens:
