# Дана строка. Подсчитать количество содержащихся в ней цифр.

while True:
    try:
        stroka = input('Введите любую строку с любым набором символов: ')
        break
    except ValueError:
        print('Что-то пошло не так')

kolvo_chisel = 0
for i in stroka:
    if i.isdigit():
        kolvo_chisel += 1
print(f'в вашей строке {kolvo_chisel} чисел')