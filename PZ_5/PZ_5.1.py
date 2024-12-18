# Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные.

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


result = sum_numbers(60)
print("Сумма чисел от 1 до 60:", result)
