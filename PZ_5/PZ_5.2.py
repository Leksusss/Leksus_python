# Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
# значение A переходит в B, значение B — в C, значение C — в A (A, B, C —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# помощью этой функции выполнить правый циклический сдвиг для двух данных
# наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

def ShiftRight3(A, B, C):
    saved = C
    C = B
    B = A
    A = saved
    return A, B, C


while True:
    try:
        A1 = int(input('Введите целое число A1: '))
        B1 = int(input('Введите целое число B1: '))
        C1 = int(input('Введите целое число C1: '))
        break
    except ValueError:
        print('Что-то пошло не так.')

A1, B1, C1 = ShiftRight3(A1, B1, C1)
print("Первый набор после сдвига:", A1, B1, C1)

while True:
    try:
        A2 = int(input('Введите целое число A2: '))
        B2 = int(input('Введите целое число B2: '))
        C2 = int(input('Введите целое число C2: '))
        break
    except ValueError:
        print('Что-то пошло не так.')

A2, B2, C2 = ShiftRight3(A2, B2, C2)
print("Второй набор после сдвига:", A2, B2, C2)