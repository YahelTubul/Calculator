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

def test_syntax_1():
    with pytest.raises(Exception):
        basic_calc("2*^3")


def test_syntax_2():
    with pytest.raises(Exception):
        basic_calc("7++5")


def test_syntax_3():
    with pytest.raises(Exception):
        basic_calc("2+9)")


def test_syntax_4():
    with pytest.raises(Exception):
        basic_calc("^7")


def test_syntax_5():
    with pytest.raises(Exception):
        basic_calc("~~3")


#####strings errors#####

def test_giberish_string():
    with pytest.raises(Exception):
        basic_calc("abcdefg..")


def test_empty_string():
    with pytest.raises(Exception):
        basic_calc("")


def test_space_string():
    with pytest.raises(Exception):
        basic_calc("      ")


def test_tab_string():
    with pytest.raises(Exception):
        basic_calc("\t \t")


#####basic expressions#####


def test_add():
    assert basic_calc("2+9") == 11

def test_sub():
    assert basic_calc("5-3") == 2

def test_mul():
    assert basic_calc("5*6") == 30

def test_div():
    assert basic_calc("63/7") == 9

def test_pow():
    assert basic_calc("2^4") == 16

def test_mod():
    assert basic_calc("5 % 3") == 2

def test_max():
    assert basic_calc("16 $ 20") == 20

def test_min():
    assert basic_calc("7&6") == 6

def test_avg():
    assert basic_calc("20@10") == 15

def test_factor():
    assert basic_calc("4!") == 24

def test_tilda():
    assert basic_calc("~17") == -17

def test_minus():
    assert basic_calc("-3+7") == 4

def test_unary():
    assert basic_calc("--5 + 3") == 8

def test_minus_and_pow():
    assert basic_calc("-2^3") == -8

def test_two_unary():
    assert basic_calc("~-3!") == 6


#####complex expressions#####

def test_comp_1():
    assert basic_calc("(2 + 3) * 4 - 5 / 5") == 19


def test_comp_2():
    assert basic_calc("2 ^ 3 + 4 * 5 - 6 / 2") == 25


def test_comp_3():
    assert basic_calc("((10 + 5) * 2) / 3") == 10


def test_comp_4():
    assert basic_calc("5! - 100 + 20 / 4") == 25


def test_comp_5():
    assert basic_calc("~(3 + 4) * 2 + 10") == -4


def test_comp_6():
    assert basic_calc("2 ^ (3 + 1) - 4 * 2") == 8


def test_comp_7():
    assert basic_calc("(5 $ 8) & (10 $ 3)") == 8


def test_comp_8():
    assert basic_calc("3! + 2! * 4 - 1") == 13


def test_comp_9():
    assert basic_calc("10 % 3 + 15 / 3 * 2") == 11


def test_comp_10():
    assert basic_calc("(4 @ 6) * (8 @ 12)") == 50


def test_comp_11():
    assert basic_calc("2 + 3 * 4 - 5 / 5 + 1") == 14


def test_comp_12():
    assert basic_calc("~-2 ^ 3 + 4 * 5") == 28


def test_comp_13():
    assert basic_calc("(10 - 5) * (3 + 2) / 5") == 5


def test_comp_14():
    assert basic_calc("4! / 6 + 2 ^ 3 - 1") == 11


def test_comp_15():
    assert basic_calc("(2 $ 3) + (4 & 5) * 2") == 11


def test_comp_16():
    assert basic_calc("~(5 - 10) + 3! - 2") == 9


def test_comp_17():
    assert basic_calc("2 ^ 3 ^ 2 / 8 + 1") == 9


def test_comp_18():
    assert basic_calc("(3 @ 7) * 2 - 1 + 5 % 3") == 11


def test_comp_19():
    assert basic_calc("10 / 2 + 3 * 4 - 5 $ 2") == 12


def test_comp_20():
    assert basic_calc("~5 + (2 + 3) * 4") == 15

