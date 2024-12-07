# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно
# из чисел A, B, C положительное»

while True:  # проверка для A
    try:
        A = int(input('Введите число для A: '))
        break
    except ValueError:
        print('Что-то пошло не так. Вы ввели некорректное число. Повторите попытку')

while True:  # проверка для B
    try:
        B = int(input('Введите число для B: '))
        break
    except ValueError:
        print('Что-то пошло не так. Вы ввели некорректное число. Повторите попытку')

while True:  # проверка для C
    try:
        C = int(input('Введите число для C: '))
        break
    except ValueError:
        print('Что-то пошло не так. Вы ввели некорректное число. Повторите попытку')

if A > 0 or B > 0 or C > 0:
    print('Здесь есть положительное число!')
else:
    print('Здесь нет положительных чисел')
