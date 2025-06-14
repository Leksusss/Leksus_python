# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:


num = ['-50 8 15 -42 30 17 200 -10']
t3 = open('inf_1.txt', 'w')
t3.writelines(num)
t3.close()


t4 = open('inf_2.txt', 'w', encoding="utf-8")
t4.write('Исходные данные: ')
t4.write('\n')
t4.writelines(num)
t4.close()


t3 = open('data_1.txt')
k = t3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
t3.close()


count = len(k)
sum_numbers = sum(k)
n = k[-1]
multiplied = []
for x in k[:-1]:
    multiplied.append(x * n)


t4 = open('inf_2.txt', 'a', encoding="utf-8")
t4.write(f'Количество элементов: {count}\n')
t4.write(f'Сумма элементов: {sum_numbers}\n')
t4.write(f'Элементы до n-1 умножены на элемент n: {multiplied})
t4.close()