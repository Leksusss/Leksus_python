# 1.Проверить есть ли в последовательности целых N чисел число K


try:
    numbers = input("Введите целые числа через пробел: ")
    N = list(map(int, numbers.split()))

    K = int(input("Введите число для поиска: "))

    matches = list(map(lambda x: x == K, N))
    found_Tr = True in matches

    if found_Tr:
        print(f"Число {K} присутствует в списке {N}")
    else:
        print(f"Число {K} отсутствует в списке {N}")


except ValueError:
    print("Ошибка! Вводите то, о чем вас просят")