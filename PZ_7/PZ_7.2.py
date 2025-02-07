# Дана строка-предложение на русском языке. Вывести самое длинное слово в
# предложении. Если таких слов несколько, то вывести первое из них. Словом считать
# набор символов, не содержащий пробелов, знаков препинания и ограниченный
# пробелами, знаками препинания или началом/концом строки.


while True:
    stroka = input('Введите свою строку, состоящую только из слов: ')
    if len(stroka) == 0:
        print('Вы ничего не ввели. Повторите попытку')
        continue

    bez_probel = stroka.split()
    proverka = True
    for slovo in bez_probel:
        if not slovo.isalpha():
            proverka = False
            print('Вы ввели не только слова. Повторите попытку')
            break

        if proverka:
            longest_word = ""
            for slovo in bez_probel:
                if len(slovo) > len(longest_word):
                    longest_word = slovo
    break
print("Введена корректная строка:", stroka)
# noinspection PyUnboundLocalVariable
print("Самое длинное слово в нём:", longest_word)