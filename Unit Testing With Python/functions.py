from typing import Union


def divide(dividend:Union[int,float],divisor:Union[int,float]):
    if divisor == 0:
        raise ValueError("You can't divide with zero !!")
    return dividend / divisor

def multiply(*args: Union[int,float]):
    if len(args) == 0:
        raise ValueError("We need at least one value for multiplication !!!")

    total = 1
    for arg in args:
        total *= arg

    return total