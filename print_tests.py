from typing import Callable

from functions import get_all_range, get_all_not_in_range, my_sorted
from unittest_print import print_results, print_test
from random import randint
numbers: list[int] = [-10, -3, 1, 20, 25, 30, 40, 41]
unsorted_numbers: list[int] = [randint(1, 100000) for _ in range(1023)]
sorted_numbers_by_str: list[int]=my_sorted(unsorted_numbers, key=lambda a: str(a))
sorted_numbers: list[int]=my_sorted(unsorted_numbers)
test_numbers = [20, -10, 1, 30, -11, 1,-50]
test_numbers_sorted = my_sorted(test_numbers)
print(test_numbers_sorted)
def is_sorted[T,K](lst: list[T], key:Callable[[T], T|K]|None=None)-> bool:
    lim = len(lst) - 1
    i = 0
    if key is None:
        key = lambda a: a
    while i < lim and key(lst[i]) <= key(lst[i + 1]): # type: ignore
        i += 1
    return i >= lim    




print_test(f"get_all_range takes numbers={numbers}, allowed=range(1, 41)",\
           [1, 20, 25, 30], get_all_range(numbers, range(1, 41)))
print_test(f"get_all_range takes numbers={numbers}, allowed=range(41, 25, -1)",\
           [30, 40], get_all_range(numbers, range(41, 25, -1)))
print_test(f"get_all_not_in_range takes numbers={numbers}, disallowed: range(1, 41, 2)",\
           [-10, -3, 20, 30, 40, 41], get_all_not_in_range(numbers,range(1, 41, 2)))
print_test(f"get_all_not_in_range takes numbers={numbers}, disallowed: range(1, 41, 2)",\
           [-10, -3, 20, 30, 40, 41], get_all_not_in_range(numbers,range(1, 41, 2)))

print_test("sorting list with 1023 random numbers by key converter to strings", True,  is_sorted(sorted_numbers_by_str, key=lambda a: str(a)))
print_test("sorting list with 1023 random numbers ", True,  is_sorted(sorted_numbers))

print_results()
