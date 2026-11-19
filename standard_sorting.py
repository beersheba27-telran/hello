from bisect import  insort
from random import randint
"""
Example of insort use case "keeping a list sorted"
Note: insort has time complexity O[N]
"""
sorted_numbers: list[int] = []
for _ in range(10):
    insort(sorted_numbers, randint(1, 10))

print(sorted_numbers)