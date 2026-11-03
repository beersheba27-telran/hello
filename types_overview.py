l1:list[int] = list(range(100000))
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
print(strNumberPresentation(1))  
print(strNumberPresentation(2))
print(strNumberPresentation(20))

