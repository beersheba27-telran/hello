from typing import Callable, Sequence
from bisect import insort
def my_sorted[T, K](items: Sequence[T],/,*, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    based on creating sorted list using bisect package
     Note: O[N^2]
    """
    result: list[T] = []
    for item in items:
        insort(result, item, key=key) # type: ignore
    return result   
    
    

         