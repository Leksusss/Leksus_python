# Дан номер года (положительное целое число). Определить количество дней в этом
# году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366 дней.
# Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 — являются).

while True:
    try:
        num_year = int(input("Введите год: "))
        if num_year <= 0:
            raise ValueError("Год не может быть отрицательным!!!")

        days = 365
        if num_year % 4 == 0:
            days = 366
            if num_year % 100 == 0:
                days = 365
                if num_year % 400:
                    days = 366

        print('В ' + str(num_year) + ' году ' + str(days) + ' дней')
        break

    except ValueError:
        print('Год не может быть отрицательным!!! Введите корректный год!')