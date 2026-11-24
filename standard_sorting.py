from sortedcontainers import SortedKeyList
numbers: SortedKeyList[int] = SortedKeyList([10, 5, -100, 20], str);
print(numbers)
print([num for num in numbers])
print(numbers.bisect_left(3))# 3
print(numbers.bisect_right(3))# 3
numbers.add(3)
print(numbers.bisect_left(3))# 3
print(numbers.bisect_right(3))# 4

