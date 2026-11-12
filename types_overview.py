from typing import Callable


def add(op1: int, op2: int)->float:
    return op1 + op2
def div(op1: int, op2: int)->float:
    return op1 / op2

number: int

def compute(op1: int, op2: int, fun: Callable[[int, int], float] )->float:
    result: float = fun(op1, op2)
    return result

print(compute(2,2,add)) #4
print(compute(2,2,div)) #1