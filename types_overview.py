from typing import Callable

div:Callable[[int, int], float]  = lambda a, b : a / b 


def compute(op1: int, op2: int, fun: Callable[[int, int], float] )->float:
    result: float = fun(op1, op2)
    return result

print(compute(2,2,lambda op1, op2: op1 + op2)) #4
print(compute(2,2,div)) #1