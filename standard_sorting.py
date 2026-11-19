from bisect import  bisect_left, bisect_right
from random import randint

numbers: list[int] = [randint(1, 1000) for _ in range(5000)]
numbers.sort()
print(f"bisect_left(numbers, -20) is {bisect_left(numbers, -20)}") # -20 doesn't exist, 0 will be returned
print(f"bisect_right(numbers, -20) is {bisect_right(numbers, -20)}") # -20 doesn't exist, 0 will be returned
print(f"bisect_left(numbers, 20) is {bisect_left(numbers, 20)}") # index of first occurrence of 20
print(f"bisect_right(numbers, 20) is {bisect_right(numbers, 20)}") # index of last occurrence 20 plus 1
print(bisect_left([1, 2,3 ,4],2))
print(bisect_right([1, 2,3 ,4],2))
print(numbers.count(20)) 
print(bisect_right(numbers, 20) -bisect_left(numbers, 20) )
# printing numbers in the closed range [30-40]
left = bisect_left(numbers, 30)
right = bisect_right(numbers, 40)
print(numbers[left:right])


