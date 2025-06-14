# 13. В строках исходного текстового файла (dates1.txt) все даты представить в виде
# подстроки. Поместить в новый текстовый файл все даты февраля в формате
# ДД/ММ/ГГГГ.


import re

with open('dates1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

date_poisk = r'\d{2}\.\d{2}\.\d{4}'
all_dates = re.findall(date_poisk, text)
feb_dates = []
for date in all_dates:
    day, month, year = date.split('.')
    if month == '02':
        new_date = f"{day}/{month}/{year}"
        feb_dates.append(new_date)

with open('feb_dates.txt', 'w', encoding='utf-8') as new_file:
    for date in feb_dates:
        new_file.write(date + '\n')

print(f"Всего дат: {len(all_dates)}")
print(f"Даты февраля: {len(feb_dates)}")