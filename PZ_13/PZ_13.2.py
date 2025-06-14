# 2. В двумерном списке найти максимальный положительный элемент, кратный 4.


import random
matrix = [[random.randint(-100, 100) for i in range(4)] for i in range(4)]

print("Матрица: ")
for row in matrix:
    print(row)

max_element = 0

for row in matrix:
    for num in row:
        if num > 0 and num % 4 == 0:
            if num > max_element:
                max_element = num

if max_element > 0:
    print(f"\nМаксимальный положительный элемент, кратный 4: {max_element}")
else:
    print("\nВ матрице нет положительных элементов, кратных 4.")