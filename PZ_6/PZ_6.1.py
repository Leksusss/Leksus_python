# Дан список A размера N. Вывести вначале его элементы с четными номерами (в
# порядке возрастания номеров), а затем — элементы с нечетными номерами (также в
# порядке возрастания номеров): A2, A4, А6, . . ., A1, A3, A5, ... . Условный оператор не
# использовать.


while True:
    try:
        N = int(input('Введите размер списка: '))
        break
    except ValueError:
        print('Что-то пошло не так. Введите корректное число')

print('Числа в списке должны начинаться с четного и по возрастанию чередоваться с нечётными')
A = []
for i in range(N):
    while True:
        try:
            chislo = int(input(f'Введите число в список с индексом {i}: '))
            A.append(chislo)
            break
        except ValueError:
            print('Что-то пошло не так. Введите корректное число')
chetn = A[::2]
nechetn = A[1::2]
print('Созданный вами список c чётными числами по возрастанию: ', chetn)
print('Созданный вами список c нечётными числами по возрастанию: ', nechetn)
print(chetn + nechetn)