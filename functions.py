from typing import Callable, Sequence
from sortedcontainers import SortedKeyList
def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    based on SortedKeyList
     Note: O[N * LogN]
    """
    if key is None: key = lambda a: a
    return list(SortedKeyList(items, key))
    
    

         