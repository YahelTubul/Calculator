import pytest
from tokenize import split_tokenize
from parser import infix_to_prefix
import evaluator

"""this a basic function that help me to check the test in this file"""


def basic_calc(exp: str) -> float:
    tokens = split_tokenize(exp)
    prefix_tok = infix_to_prefix(tokens)
    result = evaluator.evaluator(prefix_tok)
    return result


#####syntax errors#####

def syntax_1():
    with pytest.raises(Exception):
        basic_calc("2*^3")

def syntax_2():
    with pytest.raises(Exception):
        basic_calc("7++5")

def syntax_3():
    with pytest.raises(Exception):
        basic_calc("2+9)")

def syntax_4():
    with pytest.raises(Exception):
        basic_calc("^7")

def syntax_5():
    with pytest.raises(Exception):
        basic_calc("~~3")


#####strings errors#####
