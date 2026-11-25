from typing import Callable, Sequence
def __merge[T, K](part1: list[T], part2: list[T], key: Callable[[T], T|K]|None)->list[T]:
    i1 = i2 = 0
    len1 = len(part1)
    len2 = len(part2)
    result: list[T] = []
    while i1 < len1 and i2 < len2:
        if key(part1[i1]) <= key(part2[i2]): # type: ignore
            result.append(part1[i1])
            i1 += 1
        else:
            result.append(part2[i2])
            i2 += 1
    result.extend(part1[i1:])  
    result.extend(part2[i2:])  
    return result

def __get_sorted_part[T,K](items: Sequence[T], i: int, key: Callable[[T], T|K]|None)->list[T]:
    result: list[T] = [items[i]]
    lim: int = len(items) - 1
    while i < lim and key(items[i]) <= key(items[i + 1]): # type: ignore
        i += 1
        result.append(items[i])
    return result
def __get_sorted_parts[T, K](items: Sequence[T],key: Callable[[T], T|K]|None)->list[list[T]]:
     i = 0
     size = len(items)
     result: list[list[T]] = []
     while i < size:
        part = __get_sorted_part(items, i, key)
        result.append(part)
        i += len(part)
     return result    
def __merge_parts[T, K](sorted_parts: list[list[T]], key: Callable[[T], T|K]|None)->list[T]:
    len_parts = len(sorted_parts)
    while  len_parts > 1:
       sorted_parts = __merge_in_pairs(sorted_parts, key)
       len_parts = len(sorted_parts)
    return sorted_parts[0] if len_parts else [] #sorted_part has only one list that will be the sorted

def __merge_in_pairs[T,K](sorted_parts:list[list[T]],
                           key: Callable[[T], T|K]|None) -> list[list[T]]:
    result:list[list[T]] = []
    len_parts = len(sorted_parts)
    last_ind = len_parts - 1
    lim = last_ind if len_parts % 2 else len_parts
    result = [__merge(sorted_parts[i], sorted_parts[i + 1], key)\
               for i in range(0, lim, 2)]
    # for odd len_parts the last sorted part should be appended
    if lim == last_ind: result.append(sorted_parts[last_ind])  
    return result 
def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
      (no additional sorting is required)
    2. Merge of all parts from the created above list  
     
    """
    if key is None: key = lambda a: a
    sorted_parts = __get_sorted_parts(items, key)
    result: list[T] = __merge_parts(sorted_parts, key) 
    return result   
    
    

         