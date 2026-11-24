from bisect import bisect_left
from math import sqrt
from typing import Callable, Sequence, cast
def __move_max_to_end[T, K](items: list[T], start: int, size: int,\
                             key: Callable[[T], T|K])->int:
    nSwaps = 0
    if key is None: key = lambda x: x
    for i in range(start, size):
        if key(items[i]) > key(items[i + 1]): # pyright: ignore[reportOperatorIssue]
            items[i], items[i + 1] = items[i + 1], items[i]
            nSwaps += 1
    return nSwaps 
def bubble_sort[T,K](items: list[T], start: int, size: int,\
                       key: Callable[[T], T|K]|None=None)-> None:
    unsorted = True

    while unsorted:
        size -= 1
        if key is None: key = lambda a: a
        unsorted = bool(__move_max_to_end(items, start, size, key))  
def __merge_in_place[T, K](items: list[T], start1: int, start2: int, size: int,\
                            key: Callable[[T], T|K])->None:
    temp: list[T] = []
    i1 = start1; i2 = start2
    lim = start1 + size
    while i1 < start2 and i2 < lim:
        if key(items[i1]) < key(items[i2]): # pyright: ignore[reportOperatorIssue]
            temp.append(items[i1])
            i1 += 1
        else:
            temp.append(items[i2])
            i2 += 1
    temp.extend(items[i1:start2]) 
    temp.extend(items[i2:lim]) 
    items[start1:size] = temp
         
def __sort_and_merge[T,K](items: list[T], start_sorted: int,\
                           start_unsorted: int, size: int,key: Callable[[T], T|K])-> None:
    bubble_sort(items, start_unsorted, size, key)
    __merge_in_place(items,start_sorted, start_unsorted, size, key)






def get_all_range(numbers: Sequence[int], allowed: range|None = None)->list[int]:
    """
    numbers - sorted list of numbers in ascending order
   allowed - range of numbers (may be empty)
    returns list of numbers that greater or equal minimal value of range and less than maximal value 
    for empty range the function returns the empty list
    for missed second argument the function returns the same "numbers"
    """
    result:list[int] = cast(list[int], numbers)
    if allowed is not None:
        result = []
        if len(allowed) != 0:
            min = allowed[0]
            max = allowed[-1]
            if min > max: min, max = max, min
            start = bisect_left(numbers, min)
            stop = bisect_left(numbers, max)
            result = list(numbers[start:stop])
    return result    

def get_all_not_in_range(numbers: Sequence[int], disallowed: range)->list[int] :
    """
    numbers - sorted list of numbers in ascending order 
    disallowed - range of numbers (may be empty)
     returns list of numbers from "numbers" that are not in a given range
    """
    return [num for num in numbers if num not in disallowed]
def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    "items" is divided on the parts, each of which contains sqrt(len(items)) items
    Each part should be sorted separately by bubble sorting algorithm that you have already implemented
    After that all parts should be merged.
    No limitations for extra space
    Note: To use "sqrt" function from the module "math". This function returns float type
        so you should apply function "int" and the last part may contain more items
    """ 
    size = len(items)
    items_list: list[T] = []
    if size:
        items_list = list(items)
        len_part_norm = len(items) // int(sqrt(size))
        remainder: int = size % len_part_norm
        lim_norm = size - remainder - len_part_norm
        if key is None:
            key = lambda a: a
        bubble_sort(items_list, 0, len_part_norm, key)
        size_current = len_part_norm
        for i in range(len_part_norm, lim_norm, len_part_norm):
            size_current += len_part_norm
            __sort_and_merge(items_list, 0, i,size_current, key)
        __sort_and_merge(items_list, 0, lim_norm, size, key )  
        return items_list

         