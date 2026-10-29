a: int = 10
if a: #10 considered as True
    print (True)
l: list[int] = [0, 0, 0] 
print (bool(l))  
if 0: #0 considered as False
    print(True)
else:
    print(False) 
# "False"  => True
# "" => False
# " " =? True
# [] =? False
if " ": print("space is True") 
n: None = None
if n is None: print("a is None")
if n: 
    print ("n containing None is True")
else:
    print ("n containing None is False")
# a = None  since a is defined as int  


