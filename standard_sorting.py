numbers: list[int] = [100, 150, -10, -3, 110]
numbers_sorted = sorted(numbers) 
print(numbers)#[100, 150, -10, -3, 110]
print(numbers_sorted) # [-10, -3, 100, 110]
numbers.sort()
print(numbers) #  [-10, -3, 100, 110]