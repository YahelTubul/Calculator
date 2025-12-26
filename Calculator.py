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


def get_precedence(opr_tok: list) -> int:
    return operator_dict[opr_tok]['precedence']


def infix_to_prefix(tokens: list) -> list:
    reverse_tokens: list = []
    # reverse the tokenes and swap the parens
    for token in reversed(tokens):
        if token.type == Tokenize.LPAREN:
            reverse_tokens.append(Token(Tokenize.RPAREN, ')'))
        elif token.type == Tokenize.RPAREN:
            reverse_tokens.append(Token(Tokenize.LPAREN, '('))
        else:
            reverse_tokens.append(token)
    pref_result: list = []
    temp_stack: list = []
    expect_opr = True


    for rev_token in reverse_tokens:
        # check if the token is number type
        if rev_token.type == Tokenize.NUMBER:
            pref_result.append(rev_token)
            expect_opr = True
        elif rev_token.type == Tokenize.LPAREN:
            temp_stack.append(rev_token)
            expect_opr = True
        elif rev_token.type == Tokenize.RPAREN:
            left_paren = False
            while temp_stack:
                token = temp_stack.pop()
                if token.type == Tokenize.LPAREN:
                    left_paren = True
                    break
                pref_result.append(token)
            if not left_paren:
                raise ValueError("missmatch left parenthesis")
            expect_opr = True
        #check if the token type is an operator and filter them by the precedence and position
        elif rev_token.type == Tokenize.OPERATOR:
            operator = rev_token.value
            if operator not in operator_dict:
                raise ValueError(f"Invalid operator: {operator}")
            #check operator unary
            if operator == '~':
                if not expect_operand:
                    raise ValueError("Syntax error: '~' must appear before an operand")

            if operator_dict[operator]['position'] != 'middle':
                raise ValueError(f"unary operator not handled yet: {operator}")
            while temp_stack and temp_stack[-1].type == Tokenize.OPERATOR:
                top_operator = temp_stack[-1].value
                if get_precedence(top_operator) >= get_precedence(operator):
                    pref_result.append(temp_stack.pop())
                else:
                    break

            temp_stack.append(rev_token)

        else:
            raise ValueError(f"unexpected token: {rev_token.value}")

    # validate there is no more paren in the stack
    while temp_stack:
        token = temp_stack.pop()
        if token.type in (Tokenize.LPAREN, Tokenize.RPAREN):
            raise ValueError("missmatch parenthesis")
        pref_result.append(token)

    return list(reversed(pref_result))




