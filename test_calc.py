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

def string_1():
    with pytest.raises(Exception):
        basic_calc("abcdefg..")


def string_2():
    with pytest.raises(Exception):
        basic_calc("")


def string_3():
    with pytest.raises(Exception):
        basic_calc("      ")


def string_4():
    with pytest.raises(Exception):
        basic_calc("\t \t")


#####basic expressions#####


def exp_1():
    assert basic_calc("2+9") == 11

def exp_2():
    assert basic_calc("5-3") == 2

def exp_3():
    assert basic_calc("5*6") == 30

def exp_4():
    assert basic_calc("63/7") == 9

def exp_5():
    assert basic_calc("2^4") == 16

def exp_6():
    assert basic_calc("5 % 3") == 2

def exp_7():
    assert basic_calc("16 $ 20") == 20

def exp_8():
    assert basic_calc("7&6") == 6

def exp_9():
    assert basic_calc("20^10") == 15

def exp_10():
    assert basic_calc("4!") == 24

def exp_11():
    assert basic_calc("~17") == -17

def exp_12():
    assert basic_calc("-3+7") == 4

def exp_13():
    assert basic_calc("--5 + 3") == 8

def exp_14():
    assert basic_calc("-2^3") == -8

def exp_15():
    assert basic_calc("~-3!") == 6


