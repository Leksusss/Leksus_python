# Дано число R и список размера N. Найти два соседних элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
# их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной).


while True:
    try:
        R = int(input("Введите число R: "))
        break
    except ValueError:
        print("Что-то пошло не так. Введите корректное число")
while True:
    try:
        N = int(input("Введите размер списка, более 2: "))
        if N < 2:
            print("Размер списка должен быть не менее 2.")
        else:
            break
    except ValueError:
        print('Что-то пошло не так. Введите корректное число.')

A = []
for i in range(N):
    while True:
        try:
            chislo = int(input(f'Введите число в список с индексом {i}: '))
            A.append(chislo)
            break
        except ValueError:
            print("Что-то пошло не так. Введите корректное число")

maxx = 10 ** 18
resultat = []

for i in range(N - 1):
    summ_index = A[i] + A[i + 1]
    minus = summ_index - R
    if minus < 0:
        minus = minus * -1

    if minus < maxx:
        maxx = minus
        resultat = [A[i], A[i + 1]]

resultat.sort()
print(f"Два соседних элемента, сумма которых наиболее близка к {R}: {resultat}")