from sortedcontainers import SortedList
numbers: SortedList[int] = SortedList([10, 5, -100, 20]);
print(numbers)
print([num for num in numbers])
print(numbers.bisect_left(3))# 1
print(numbers.bisect_right(3))# 1
numbers.add(3)
print(numbers.bisect_left(3))# 1
print(numbers.bisect_right(3))# 2

