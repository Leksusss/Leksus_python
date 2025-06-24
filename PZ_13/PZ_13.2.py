# 2. В двумерном списке найти максимальный положительный элемент, кратный 4.


import random
matrix = [[random.randint(-10, 10) for i in range(4)] for i in range(4)]

print("Матрица: ")
for row in matrix:
    print(row)

all_elements = [num for row in matrix for num in row]
proverka = list(filter(lambda x: x > 0 and x % 4 == 0, all_elements))

if proverka:
    max_element = max(proverka)
    print(f"\nМаксимальный положительный элемент, кратный 4: {max_element}")
else:
    print("\nВ матрице нет положительных элементов, кратных 4.")