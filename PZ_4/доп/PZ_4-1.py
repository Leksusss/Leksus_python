# Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных
# чисел.

summa = 0
negative = 0
for i in range(4):
    while True:
        try:
            num = int(input("Введите число: "))
            summa = summa + num
            if num < 0:
                negative = negative + 1
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

print("Сумма чисел:", summa)
print("Количество отрицательных чисел:", negative)

