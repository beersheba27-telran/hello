from typing import Callable
from unittest_print import print_test, print_results

def remove_predicate[T](items: list[T], /, *, pred: Callable[[T], bool] )->None:
    """
    space complexity O[1]
    removing in-place items matching a given preedicate
    complexity O[N] even if no item matching a given pred exists
    """
    for item in items:
        if pred(item):
            items.remove(item)

lst = [i for i in range(10)]  
res = lst.copy()
remove_predicate(res, pred=lambda num: num % 2 == 0)  
print_test(f"removing even numbers from {lst}", [i for i  in range(1, 10, 2)], res)  
print_results()     

