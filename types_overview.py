numbers = [1, 2, 3,4]
d1 = {k + 1: v / 2 for k, v in enumerate(numbers)}
for k in d1: # printing keys
    print(k)
for item in d1.items(): # printing tuples (key, value)
    print(item) 
for value in d1.values(): # printing values
    print(value) 


