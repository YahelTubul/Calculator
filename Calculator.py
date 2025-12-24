from enum import Enum


# create enum for definition the types of token

class Tokenize(Enum):
    NUMBER = 1
    OPERATOR = 2
    LPAREN = 3
    RPAREN = 4


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    #pass each char in the exprssion
    def split_tokenize(expression : str) -> list:
        tokens : list = []
        long_num : str = ""
        for char in expression:
            if (char.isdigit() or (char == '.' and '.' not in long_num)):
                long_num += char
            else:
                if long_num:
                    tokens.append(Token(Tokenize.NUMBER, long_num))
                    long_num = ""




