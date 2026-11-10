import binary_search
numbers: list[int] = [10, 20, 30, 40, 50]
print(f"in list {numbers} index of 10 is expected 0,\
 actual {binary_search.binary_search(numbers, 10)}")
print(f"in list {numbers} index of 50 is expected 4,\
 actual {binary_search.binary_search(numbers, 50)}")
print(f"in list {numbers} index of 30 is expected 2,\
 actual {binary_search.binary_search(numbers, 30)}")
print(f"in list {numbers} index of 35 is expected -1,\
 actual {binary_search.binary_search(numbers, 35)}")
