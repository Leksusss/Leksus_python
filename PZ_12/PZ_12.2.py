# 2.Составить список, в который будут включены только согласные буквы и привести
# их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
# 'Каир'].


cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
glasn = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

def filter_glasn(char):
    return char.lower() not in glasn

newlist = list(
      map(lambda slovo: ''.join([str(letter).upper() for letter in slovo if filter_glasn(letter)]), cities))

print(newlist)
