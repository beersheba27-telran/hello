from sortedcontainers import SortedKeyList
persons: SortedKeyList =\
 SortedKeyList([("Vasya", 10), ("Kolya", 60),("Abram", 60)], lambda p: p[1]);
print(persons)
print([person for person in persons])
print(persons.bisect_left(("", 60)))#1
print(persons.bisect_right(("", 60)))#3
print(persons.bisect_key_left(60))#1
print(persons.bisect_key_right( 60))#3




