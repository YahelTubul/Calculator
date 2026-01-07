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

def giberish_string():
    with pytest.raises(Exception):
        basic_calc("abcdefg..")


def empty_string():
    with pytest.raises(Exception):
        basic_calc("")


def space_string():
    with pytest.raises(Exception):
        basic_calc("      ")


def tab_string():
    with pytest.raises(Exception):
        basic_calc("\t \t")


#####basic expressions#####


def add_test():
    assert basic_calc("2+9") == 11

def sub_test():
    assert basic_calc("5-3") == 2

def mul_test():
    assert basic_calc("5*6") == 30

def div_test():
    assert basic_calc("63/7") == 9

def pow_test():
    assert basic_calc("2^4") == 16

def mod_test():
    assert basic_calc("5 % 3") == 2

def max_test():
    assert basic_calc("16 $ 20") == 20

def min_test():
    assert basic_calc("7&6") == 6

def avg_test():
    assert basic_calc("20@10") == 15

def factor_test():
    assert basic_calc("4!") == 24

def tilda_test():
    assert basic_calc("~17") == -17

def minus_test():
    assert basic_calc("-3+7") == 4

def unary_test():
    assert basic_calc("--5 + 3") == 8

def minus_and_pow_test():
    assert basic_calc("-2^3") == -8

def two_unary_test():
    assert basic_calc("~-3!") == 6


#####complex expressions#####

def comp_1():
    assert basic_calc("(2 + 3) * 4 - 5 / 5") == 19


def comp_2():
    assert basic_calc("2 ^ 3 + 4 * 5 - 6 / 2") == 25


def comp_3():
    assert basic_calc("((10 + 5) * 2) / 3") == 10


def comp_4():
    assert basic_calc("5! - 100 + 20 / 4") == 25


def comp_5():
    assert basic_calc("~(3 + 4) * 2 + 10") == -4


def comp_6():
    assert basic_calc("2 ^ (3 + 1) - 4 * 2") == 8


def comp_7():
    assert basic_calc("(5 $ 8) & (10 $ 3)") == 8


def comp_8():
    assert basic_calc("3! + 2! * 4 - 1") == 13


def comp_9():
    assert basic_calc("10 % 3 + 15 / 3 * 2") == 11


def comp_10():
    assert basic_calc("(4 @ 6) * (8 @ 12)") == 50


def comp_11():
    assert basic_calc("2 + 3 * 4 - 5 / 5 + 1") == 14


def comp_12():
    assert basic_calc("~-2 ^ 3 + 4 * 5") == 28


def comp_13():
    assert basic_calc("(10 - 5) * (3 + 2) / 5") == 5


def comp_14():
    assert basic_calc("4! / 6 + 2 ^ 3 - 1") == 11


def comp_15():
    assert basic_calc("(2 $ 3) + (4 & 5) * 2") == 11


def comp_16():
    assert basic_calc("~(5 - 10) + 3! - 2") == 9


def comp_17():
    assert basic_calc("2 ^ 3 ^ 2 / 8 + 1") == 65


def comp_18():
    assert basic_calc("(3 @ 7) * 2 - 1 + 5 % 3") == 11


def comp_19():
    assert basic_calc("10 / 2 + 3 * 4 - 5 $ 2") == 12


def comp_20():
    assert basic_calc("~5 + (2 + 3) * 4") == 15

    