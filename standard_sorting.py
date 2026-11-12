text: list[str] = ["Vasya", "aaaaaaa", "bbbb","BBB" ]
print(sorted(text))# ['BBB', 'Vasya', 'aaaaaaa', 'bbbb']
print(sorted(text,key=len)) #['BBB', 'bbbb', 'Vasya', 'aaaaaaa']
print(sorted(text,key=lambda s: s.upper()))
numbers: list[int] = [20, -3, -10, 30]
print(sorted(numbers)) # [-10, -3, 20, 30]
print(sorted(numbers, key=abs))# [-3, -10, 20, 30]
pairs: list[tuple[int, int]] = [(1,100), (-1, 1000), (1, -100), (-1, -10)]
print(sorted(pairs))#[(-1, -10), (-1, 1000), (1, -100), (1, 100)]


