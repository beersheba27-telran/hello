l1:list[int] = list(range(100000))
num1, num2, *_ = l1 #works with performance issue as creating unneded list
num3, num4 = l1[3], l1[4] #works with no performance issue
t1: tuple[int,...] = tuple(l1)
t2: tuple[str, int] = "1", 2

def strNumberPresentation(num: int) -> tuple[str, int]:
    strPr: str = ""
   
    if num == 1:
        strPr = "one"
    elif num == 2:
        strPr = "two"
    else:
        strPr = str(num)
    return strPr, num  

strNum, numberNum = strNumberPresentation(10) #unpacking
