numbers: list[int] = [100, 150, -10, -3, 110]
sorted_part = sorted(numbers[1:4]) #[-10, -3, 150]
numbers[1:4] = sorted_part
print(numbers) #[100,  -10, -3, 150, 110]
numbers[3:3] = [80]
print(numbers)#[100,  -10, -3, 80, 150, 110]
numbers[3:4]=[90, 130]
print(numbers) #[100,  -10, -3, 90,130 150, 110]
