text: str =" Hello world"
a: int = 10
text += str(10)
#string interpolation: inserting any expression into a string
def add(op1:int, op2:int)->int:
    return op1 + op2
text_f:str = f"Result of add(10, 20) is {{{add(10, 20)}}}"
print(text_f)