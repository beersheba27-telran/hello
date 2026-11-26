def get_persons_salary(persons: list[tuple[str,int]])->dict[int,list[tuple[str,int]]]:
    result:dict[int,list[tuple[str,int]]] ={}
    for p in persons:
        result.setdefault(p[1], []).append(p)
    return result
persons = [("Vasya", 10000), ("Kolya", 5000), ("Fedya", 10000)]
print(get_persons_salary(persons))
def get_persons_by_salary (persons: list[tuple[str,int]], salary:int)->list[tuple[str,int]]:
    persons_age = get_persons_salary(persons)
    return persons_age.get(salary, [])

print(get_persons_by_salary(persons, 20000))# empty list
print(get_persons_by_salary(persons, 10000))# [("Vasya", 10000), ("Fedya", 10000)]