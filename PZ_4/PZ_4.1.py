# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...
# •A (числа A перемножаются N раз).

try:
    A = int(input('Введите целое число A: '))
    N = int(input('Введите целое число N, больше 0: '))
    if N <= 0:
        print('N должно быть больше 0.')
    else:
        result = A
        for i in range(1, N):
            result = result * A
        print(A, ' в степени ', N, ' равно ', result)
except ValueError:
    print('Что-то пошло не так. Введите корректное число.')