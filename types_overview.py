a = 50000
b = a
d = 100000
print(b is a)# TRue
def double(c: int) :
    res: int = c * 2
    print(a is c) #True
    return res
a = double(a)
print(b is a) #False
print (a == d) #True
print (a is d) #False
