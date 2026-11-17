l1: list[list[int]] = [[]]
l2 = l1
print(l1 is l2) # True
print (l1:=l1 * 2) # [[],[]] 
print(l1 is l2) # False
l3 = l1
print(l3 is l1) #True
l1 = l1 + [[3]]
print(l3 is l1) #False as "+" returns new list
l4 = l1
print(l4 is l1) #True as l4 and l1 refer to the same list
l1 += [[5]] #underline extend
print(l1) # [[], [], [3], [5]]
print(l4 is l1) #True as l4 and l1 refer to the same list
lst1: list[int] = [2]
lst2: list[int] = [2]
l5: list[list[int]] = [lst1, lst2]
print(l5)# [[2], [2]]
lst1.append(3)
print(l5) #[[2,3], [2]]
l5[0].append(4)
print(lst1) #[2,3,4]
l6:list[list[int]] = [[]]
l7 = l6 * 2
print(l7[0] is l7[1]) #True
l7[0].append(1)
print(l7) # [[1], [1]]




