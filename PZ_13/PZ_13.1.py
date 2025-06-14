# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов


import random
matrix = [[random.randint(-15, 15) for i in range(4)] for i in range(4)]

print("Матрица: ")
for row in matrix:
    print(row)

print("Средние арифметические для строк с нечетными номерами: ")

row_number = 1
for row in matrix:
    if row_number % 2 != 0:
        sred_arifm = sum(row) / len(row)
        print(f"Строка {row_number}: {row} - Среднее арифметическое: {sred_arifm}")
    row_number += 1