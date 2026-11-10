def binary_search(numbers: list[int], num: int)->int:
    """
    numbers - a sorted list
    num - being searched number
    returns index of "num" at which "num" resides in "numbers" or -1 if "num" doesn't exist
    """
    left: int = 0
    right: int = len(numbers) - 1
    middle: int = (left + right) // 2
    while left <= right and numbers[middle] != num:
        if num < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1
        middle =  (left + right) // 2
    return middle if left <= right else -1       