from bisect import  insort
from random import randint
"""
Example of insort introduction
Note: insort has time complexity O[N]


"""
sorted_numbers: list[int] = []
numbers: list[int] = [randint(1, 10) for _ in range(10)]
print(numbers)
for num in numbers:
    insort(sorted_numbers, num)
print(sorted_numbers)    