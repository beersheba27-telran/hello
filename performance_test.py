from random import randint
from timeit import timeit
from functions import bubble_sort, my_sorted
numbers:list[int] = [randint(1, 100000) for _ in range(100000)]
# numbers.sort()
# numbers[0], numbers[-1] = numbers[0], numbers[-1]
print(f"running rime of my_sort for list containing {len(numbers)} numbers", \
      timeit(lambda : my_sorted(numbers),number=1))
print(f"running rime of my_sort for list containing {len(numbers)} numbers", \
      timeit(lambda : sorted(numbers),number=1))
print(f"running rime of bubble_sort for list containing {len(numbers)} numbers", \
      timeit(lambda : bubble_sort(numbers,0,len(numbers)),number=1))
