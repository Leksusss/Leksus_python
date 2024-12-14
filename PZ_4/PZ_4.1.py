# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...
# •A (числа A перемножаются N раз).

while True:
    try:
        A = int(input('Введите вещественное число A: '))
        break
    except ValueError:
        print('Некорректно введено число А. Повторите попытку.')
while True:
    try:
        N = int(input('Введите целое число N, больше 0: '))
        if N <= 0:
            print('N должно быть больше 0.')
        else:
            break
    except ValueError:
        print('Некорректно введено число N. Повторите попытку.')
result = A
for i in range(1, N):
    result = result * A
print(A, ' в степени ', N, ' равно ', result)