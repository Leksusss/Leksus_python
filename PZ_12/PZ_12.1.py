# 1.Проверить есть ли в последовательности целых N чисел число K


try:
    numbers_input = input("Введите целые числа через пробел: ")
    numbers = list(map(int, numbers_input.split()))

    K = int(input("Введите число для поиска: "))

    matches = list(map(lambda x: x == K, numbers))
    found_Tr = True in matches

    if found_Tr:
        print(f"Число {K} присутствует в списке {numbers}")
    else:
        print(f"Число {K} отсутствует в списке {numbers}")


except ValueError:
    print("Ошибка! Вводите то, о чем вас просят")