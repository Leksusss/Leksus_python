# 2. Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.



f = open('text18-19.txt', 'r', encoding='utf-8')
text = f.read()
f.close()

print("Содержимое файла: ")
print(text)

letter_count = 0
for i in text:
    if i.isalpha():
        letter_count += 1
print("\nКоличество букв в тексте: ", letter_count)

new_file = open('new18-19.txt', 'w', encoding='utf-8')
lower_text = text.lower()
new_file.write(lower_text)
new_file.close()

print("\nСодержимое нового файла 'new18-19.txt':")
new_file = open('new18-19.txt', 'r', encoding='utf-8')
print(new_file.read())
new_file.close()