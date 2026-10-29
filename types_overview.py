a:int = 10 #int
b:float = 10.7 #float
c:str = "Hello" #str
# c= 9 typing error of VSC but not Python
d:bool = True #bool
l:list[int] = [1, 2, 3] #list
print(type(c))
def add(op1:float, op2:int) -> int:
    result:int = int(op1 + op2)
    return result

l.append(10 // 2)
