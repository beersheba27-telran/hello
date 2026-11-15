from typing import Callable, Sequence

def __move_max_to_end(objects: list[object], size: int,
                       key: Callable[[object], object]|None)->int:
    nSwaps = 0
    if not key:
        key = lambda obj: obj
    for i in range(size):
        if key(objects[i]) > key(objects[i + 1]): # type: ignore
           nSwaps += 1
           objects[i], objects[i + 1] = objects[i + 1], objects[i]
    return nSwaps
def bubble_sorted(items: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
      in accorgance with key function-converter like standard Python sorting 
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
          default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers 
                 bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=                
    """
    result = list(items)
    unsorted = True
    size = len(items)
    while unsorted:
        size -= 1
        unsorted = bool(__move_max_to_end(result, size, key))
    return result    

def even_asc_odd_desc(numbers: list[int])->list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    return sorted(numbers, key = lambda num: (1, -num) if num % 2 else (0, num))
def  merge(part1: Sequence[object], part2: Sequence[object], key: Callable[[object], object]|None = None)->list[object]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
              default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """ 
    result: list[object] = []
    i1 = i2 = 0
    len1 = len(part1)
    len2 = len(part2)
    if not key:
        key = lambda obj: obj
    while i1 < len1 and i2 < len2:
        if key(part1[i1]) > key(part2[i2]): # type: ignore
            result.append(part2[i2])
            i2 += 1
        else:
            result.append(part1[i1])
            i1 += 1
    lenRes = len(result)        
    result[lenRes:lenRes] = part1[i1:] 
    result[lenRes:lenRes] = part2[i2:]
    return result     
        
   