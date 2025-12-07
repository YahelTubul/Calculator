from enum import Enum

class Levels(Enum):
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6

class Assembler:
    level : int = Levels.LEVEL_6
    def assembler(number:int)->int:
        solve : int = 1
        i : int = 1
        for i in range(number+1) :
            solve *= i
        return solve
class Negative:
    level : int = Levels.LEVEL_6
    def negative(number:int)->int:
        return -number
class Average:
    level : int = Levels.LEVEL_5
    def average(num_1:int, num_2:int)->int:
        return (num_1 + num_2) / 2

class Minimum:
    level : int = Levels.LEVEL_5
    def minimum(num_1:int, num_2:int)->int:
        if num_1 > num_2 :
            return num_2
        else:
            return num_1

class Maximum:
    level : int = Levels.LEVEL_5
    def maximum(num_1:int, num_2:int)->int:
        if num_1 > num_2 :
            return num_1
        else:
            return num_2

class Module:
    level : int = Levels.LEVEL_4
    def module(num_1:int, num_2:int)->int:
        return num_1 % num_2

class Pow:
    level : int = Levels.LEVEL_3
    def power(num_1:int, num_2:int)->int:
        return num_1 ** num_2

class division:
    level : int = Levels.LEVEL_2
    def division(num_1:int, num_2:int)->int:
        return num_1 // num_2

class  Multiplication:
    level : int = Levels.LEVEL_2
    def multiplication(num_1:int, num_2:int)->int:
        return num_1 * num_2

class Subtraction:
    level : int = Levels.LEVEL_1
    def subtraction(num_1:int, num_2:int)->int:
        return num_1 - num_2

class Addition:
    level : int = Levels.LEVEL_1
    def addition(num_1:int, num_2:int)->int:
        return num_1 + num_2




