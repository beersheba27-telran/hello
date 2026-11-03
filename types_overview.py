import random


l1: list[int] = [1, 2, 3]
min = 100
max = 200
def addRandomNumber(l2: list[int], min1: int, max1: int):
    l2.append(random.randint(min1, max1))
    print(min is min1) #True
    min1 = 1000
    max1 = 5000
    print (min is min1) # False

addRandomNumber(l1, min, max)
print(l1, min, max)
