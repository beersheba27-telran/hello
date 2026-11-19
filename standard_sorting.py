from bisect import  bisect_left, bisect_right
strings: list[str] =[ "lmn", "y", "aaaaa", "bb", "ddd"]
strings.sort(key=len)
print(strings)
print(strings[bisect_left(strings, 3, key=len):bisect_right(strings, 3, key=len)])

