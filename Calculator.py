


def infix_to_prefix(tokens: list) -> list:
    # check if the characthers are valid, before I reverse the list
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
                # can not have consistent of prefix operators, except the minus
                if i > 0 and tokens[i - 1].type == Tokenize.OPERATOR:
                    prev_op_pos = operator_dict[tokens[i - 1].value]['position']
                    if prev_op_pos == 'left' and tokens[i - 1].value != '-' and operator != '-':
                        raise ValueError(f"syntax error: cannot have consecutive unary prefix operators")

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

        # check if the token type is an operator and filter them by the precedence and position
        elif rev_token.type == Tokenize.OPERATOR:
            operator = rev_token.value
            if operator not in operator_dict:
                raise ValueError(f"Invalid operator: {operator}")

            # get where the position needed be
            op_pos = operator_dict[operator]['position']

            # unary prefix, '~' operator
            if op_pos == 'left':
                if expect_opr:
                    raise ValueError(f"syntax error: '{operator}' must appear before an operand")
                # In reversed list, after processing prefix operator we still expect operand (number)
                expect_opr = False

            # unary postfix , '!' operator
            elif op_pos == 'right':
                if expect_opr:
                    raise ValueError(f"syntax error: '{operator}' must appear after an operand")
                expect_opr = False

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
                if get_precedence(top_op) >= get_precedence(operator):
                    pref_result.append(temp_stack.pop())
                else:
                    break

            temp_stack.append(rev_token)

        else:
            raise ValueError(f"Unexpected token: {rev_token.value}")

    # validate there is no more paren in the stack
    while temp_stack:
        top = temp_stack.pop()
        if top.type in (Tokenize.LPAREN, Tokenize.RPAREN):
            raise ValueError("Mismatched parentheses")
        pref_result.append(top)

    return list(reversed(pref_result))


# unit test for the function infix_to_prefix (credit: QA Lesson)
def test():
    tokens = Token.split_tokenize("~3")
    prefix_tokens = infix_to_prefix(tokens)
    values = []
    for token in prefix_tokens:
        values.append(token.value)
    print(values)


test()
