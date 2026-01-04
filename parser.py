from tokenize import Token, Tokenize, operator_dict, get_precedence

"""Check if current prefix operator can follow previous prefix operator"""


def follow_prefix_op(curr_op: str, prev_op: str) -> bool:
    curr_pos = operator_dict[curr_op]['position']
    prev_pos = operator_dict[prev_op]['position']

    if curr_pos != 'left' or prev_pos != 'left':
        return True

    if operator_dict[curr_op]['arity'] == 2 or operator_dict[prev_op]['arity'] == 2:
        return True

    # return false when there is two unary prefix operators in a row
    return False


"""valid that operators appear in valid positions according to the dictinary"""


def validate_appearance(tokens: list) -> None:
    for i in range(len(tokens)):
        if tokens[i].type == Tokenize.OPERATOR:
            operator = tokens[i].value
            op_pos = operator_dict[operator]['position']
            # check unary prefix operators
            if op_pos == 'left':
                # unary operator can not come after number or right paren or postfix operator
                if i > 0:
                    prev = tokens[i - 1]
                    if prev.type == Tokenize.NUMBER:
                        raise ValueError(
                            f"syntax error: unary prefix operator '{operator}' cannot appear after operand")
                    if prev.type == Tokenize.RPAREN:
                        raise ValueError(f"syntax error: unary prefix operator '{operator}' cannot appear after ')'")
                    if prev.type == Tokenize.OPERATOR and operator_dict[prev.value]['position'] == 'right':
                        raise ValueError(
                            f"syntax error: unary prefix operator '{operator}' cannot appear after postfix operator")
                # can not have consecutive unary prefix operators
                if i > 0 and tokens[i - 1].type == Tokenize.OPERATOR:
                    if not follow_prefix_op(operator, tokens[i - 1].value):
                        raise ValueError(f"syntax error: cannot have consecutive unary prefix operators")

            # check unary postfix operators
            elif op_pos == 'right':
                # postfix operator must come after number or right paren or another postfix operator
                if i == 0:
                    raise ValueError(f"syntax error: postfix operator '{operator}' must appear after an operand")
                prev = tokens[i - 1]
                if prev.type not in [Tokenize.NUMBER, Tokenize.RPAREN]:
                    if prev.type != Tokenize.OPERATOR or operator_dict[prev.value]['position'] != 'right':
                        raise ValueError(f"syntax error: postfix operator '{operator}' must appear after an operand")


""" return the list of token reverse but with swap parens"""


def reverse_tokens(tokens: list) -> list:
    reverse_tokens: list = []
    for token in reversed(tokens):
        if token.type == Tokenize.LPAREN:
            reverse_tokens.append(Token(Tokenize.RPAREN, ')'))
        elif token.type == Tokenize.RPAREN:
            reverse_tokens.append(Token(Tokenize.LPAREN, '('))
        else:
            reverse_tokens.append(token)
    return reverse_tokens


def parser(reverse_tokens: list) -> list:
    pref_result: list = []
    temp_stack: list = []
    # when this variable is true it expect get operand. if false it expect get operator
    expect_opr = True

    for rev_token in reverse_tokens:
        # check if the token is number type
        if rev_token.type == Tokenize.NUMBER:
            pref_result.append(rev_token)
            expect_opr = False

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

            expect_opr = False

        # check if the token type is an operator and filter them by the position
        elif rev_token.type == Tokenize.OPERATOR:
            operator = rev_token.value
            if operator not in operator_dict:
                raise ValueError(f"Invalid operator: {operator}")

            # get where the position needed be
            op_pos = operator_dict[operator]['position']

            if operator == '-':
                if expect_opr:
                    raise ValueError(f"syntax error: binary operator '{operator}' missing left operand")
                expect_opr = True

            # unary prefix
            elif op_pos == 'left':
                if expect_opr:
                    raise ValueError(f"syntax error: '{operator}' must appear before an operand")
                expect_opr = False

            # unary postfix
            elif op_pos == 'right':
                if not expect_opr:
                    raise ValueError(f"syntax error: '{operator}' must appear after an operand")
                expect_opr = True

            # binary operator is in the middle
            elif op_pos == 'middle':
                if expect_opr:
                    raise ValueError(f"syntax error: binary operator '{operator}' missing left operand")
                expect_opr = True

            else:
                raise ValueError("invalid operator position")

            # pop from the stack by precedence
            while temp_stack and temp_stack[-1].type == Tokenize.OPERATOR:
                top_op = temp_stack[-1].value
                need_pop = False
                top_pre = get_precedence(top_op)
                curr_pre = get_precedence(operator)

                if top_pre > curr_pre:
                    need_pop = True

                elif top_pre == curr_pre:
                    top_pos = operator_dict[top_op]['position']
                    curr_pos = operator_dict[operator]['position']

                    if top_pos == 'right' and curr_pos == 'left':
                        need_pop = False
                    else:
                        need_pop = True

                if need_pop:
                    pref_result.append(temp_stack.pop())
                else:
                    break

            temp_stack.append(rev_token)
        else:
            raise ValueError(f"Unexpected token: {rev_token.value}")

    # validate there is no more paren in the stack
    while temp_stack:
        top_stack = temp_stack.pop()
        if top_stack.type in (Tokenize.LPAREN, Tokenize.RPAREN):
            raise ValueError("mismatched parentheses")
        pref_result.append(top_stack)

    return pref_result


"""convert the expression from infix presentation to prefix presentation"""


def infix_to_prefix(tokens: list) -> list:
    # check if the characters are valid, before I reverse the list
    validate_appearance(tokens)

    # reverse the tokens and swap the parens
    reverse_lst = reverse_tokens(tokens)

    # process reversed tokens
    pref_result = parser(reverse_lst)
    return list(reversed(pref_result))
