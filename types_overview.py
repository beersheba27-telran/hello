import random


s1:set[int] = set()
l1:list[int] =[ random.randint(1,10) for _ in range(10)]
print (f" l1 is {l1}")
s1 = {random.randint(1,10) for _ in range(10)}
print (f" s1 is {s1}")
s2: set[int] = {random.randint(1,10000000000) for _ in range(10)}
print (f" s2 is {s2}")
