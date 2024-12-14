# Ввести 4 числа. Найти и вывести на экран количество четных чисел.

chetn = 0
for i in range(4):
    while True:
        try:
            num4 = int(input('Введите число: '))
            if num4 % 2 == 0:
                chetn = chetn + 1
            break
        except ValueError:
            print('Что-то пошло не так. Введите корректное число.')
print('Количество четных чисел: ', chetn)