# Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов


import random
matrix = [[random.randint(-15, 15) for i in range(4)] for i in range(4)]

print("Матрица: ")
for row in matrix:
    print(row)

print("Средние арифметические для строк с нечетными номерами: ")

number_rows = [matrix[0], matrix[2]]
sred_arifm = list(map(lambda row: sum(row)/len(row), number_rows))

print(f"Строка 1: {matrix[0]} - Среднее арифметическое: {sred_arifm[0]}")
print(f"Строка 3: {matrix[2]} - Среднее арифметическое: {sred_arifm[1]}")