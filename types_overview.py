def subtract(op1: int, op2: int)->float:
    # parameters are either positional or named
    return op1 - op2

 # positional arguments
print(subtract(20, 10)) # 10
# named arguments
print(subtract(op1=20, op2=10)) # 10

def div(op1: int, op2: int,/)->float:
    # parameters are only the positioanal ones
    return op1 / op2

print(div(20, 10))

def mult(*, op1:int, op2: int)->float:
    # only key parameters
    return op1 * op2

print(mult(op2=10, op1=20))
