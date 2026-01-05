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

    'minus_unary': {'precedence': 2.5, 'position': 'left', 'arity': 1},  # minus unary
    '~': {'precedence': 6, 'position': 'left', 'arity': 1},  # negative
    '!': {'precedence': 6, 'position': 'right', 'arity': 1},  # factorial
}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


"""pass on each char in the long number if all char they digits"""


def check_digits(long_number):
    for char in long_number:
        if char.isdigit():
            return True
    return False


"""pass on the the long number a normalize the number to valid number of minus operator"""


def organize_minus(long_num: str) -> str:
    if not long_num.startswith('-'):
        return long_num
    count = 0
    for minus in long_num:
        if minus == '-':
            count += 1
        else:
            break
    number = long_num[count:]
    if count % 2 == 0:
        return number
    else:
        return '-' + number


"""pass each char in the expression and defines each character in the expression to the type of the token."""


def split_tokenize(expression: str) -> list:
    tokens: list = []
    long_num: str = ""
    token_type: Tokenize = None

    for char in expression:
        # check for negative numbers. by compare if the prev token it's not a number type
        if char == '-':
            if check_digits(long_num):
                organize_exp = organize_minus(long_num)
                tokens.append(Token(Tokenize.NUMBER, organize_exp))
                token_type = Tokenize.NUMBER
                long_num = ""
                tokens.append(Token(Tokenize.OPERATOR, '-'))
                token_type = Tokenize.OPERATOR
            elif token_type in [Tokenize.NUMBER, Tokenize.RPAREN]:
                tokens.append(Token(Tokenize.OPERATOR, '-'))
                token_type = Tokenize.OPERATOR
            elif token_type is None:
                tokens.append(Token(Tokenize.OPERATOR, 'minus_unary'))
                token_type = Tokenize.OPERATOR
            else:
                long_num = char
        # check if the char is number or float number and for number with two numbers and more
        elif char.isdigit() or (char == '.' and '.' not in long_num):
            long_num += char

        else:
            # add the number to the tokens list
            if long_num:
                if long_num == '-' * len(long_num):
                    for minus in long_num:
                        tokens.append(Token(Tokenize.OPERATOR, 'minus_unary'))
                    long_num = ""
                else:
                    organize_exp = organize_minus(long_num)
                    tokens.append(Token(Tokenize.NUMBER, organize_exp))
                    long_num = ""
                    token_type = Tokenize.NUMBER

            # check if char is a valid operator, and add it to list
            if char in operators:
                tokens.append(Token(Tokenize.OPERATOR, char))
                token_type = Tokenize.OPERATOR
            # check if char is left paren
            elif char == '(':
                tokens.append(Token(Tokenize.LPAREN, char))
                token_type = Tokenize.LPAREN
            # check if char is right paren
            elif char == ')':
                tokens.append(Token(Tokenize.RPAREN, char))
                token_type = Tokenize.RPAREN
            # ignore from spaces
            elif char == ' ':
                continue
            else:
                raise ValueError(f"Invalid token: '{char}'")

    # add if there is, the last char to the list
    if long_num:
        if long_num == '-' * len(long_num):
            for minus in long_num:
                tokens.append(Token(Tokenize.OPERATOR, 'minus_unary'))
        else:
            organize_exp = organize_minus(long_num)
            tokens.append(Token(Tokenize.NUMBER, organize_exp))

    return tokens


"""This function returns the precedence level of the operator"""


def get_precedence(operator: str) -> int:
    return operator_dict[operator]['precedence']
