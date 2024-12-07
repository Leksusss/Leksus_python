# дано двузначное число. Вывести число, полученное
# при перестановкe цифр исходного числа.

try:
    num_str = input("Введите двузначное число: ")
    num = int(num_str)
    if 10 <= num <= 99:
        one = num // 10  # это будут единицы
        ten = num % 10  # это будут десятки
        reversed_num = ten * 10 + one
        print("Вы получили число: " + str(reversed_num))
    else:
        print("Введено некорректное число")
except ValueError:
    print("Вы ввели не число!!")