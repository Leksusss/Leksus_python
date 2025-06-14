# Приложение ТОВАРНЫЙ ЗАПАС для автоматизированного учета товарных
# запасов на складе. БД должна содержать таблицу Товары со следующей структурой
# записи: Код товара, Торговая марка, Тип, Цена, Количество на складе, Минимальный
# запас.

#Программа должна обеспечивать функционал по вводу данных в БД (10 позиций), их
#поиску(SELECT), удалению(DELETE) и редактированию(UPDATE). При организации поиска, удаления и
#редактирования использовать WHERE, предусмотреть по три SQL-запроса для каждой
#операции


import sqlite3 as sq

with sq.connect('warehouse.db') as con:
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS products')
    cur.execute("""CREATE TABLE IF NOT EXISTS products (
                product_code INTEGER PRIMARY KEY AUTOINCREMENT,
                brand TEXT NOT NULL,
                product_type TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                quantity INTEGER NOT NULL,
                min_stock INTEGER NOT NULL)""")

    products = [
        ('Samsung', 'Смартфон', 45000, 25, 5),
        ('Apple', 'Ноутбук', 120000, 15, 3),
        ('Xiaomi', 'Наушники', 3500, 50, 10),
        ('Bosch', 'Дрель', 8000, 30, 8),
        ('Nike', 'Кроссовки', 7000, 40, 15),
        ('Adidas', 'Футболка', 2500, 60, 20),
        ('LG', 'Холодильник', 65000, 10, 2),
        ('Sony', 'Телевизор', 90000, 12, 3),
        ('Philips', 'Бритва', 3000, 45, 12),
        ('Lenovo', 'Планшет', 28000, 18, 4)]
    cur.executemany("INSERT INTO products (brand, product_type, price, quantity, min_stock) VALUES (?, ?, ?, ?, ?)",
        products)

    cur.execute("SELECT * FROM products WHERE brand = ?", ('Samsung',))
    print(cur.fetchall())
    cur.execute("SELECT * FROM products WHERE quantity < min_stock")
    print(cur.fetchall())
    cur.execute("SELECT * FROM products WHERE price < ?", (50000,))
    print(cur.fetchall())

    cur.execute("DELETE FROM products WHERE brand = ?", ('Nike',))
    cur.execute("DELETE FROM products WHERE quantity = 0")
    cur.execute("DELETE FROM products WHERE product_type = ? AND price < ?", ('Наушники', 4000))

    cur.execute("UPDATE products SET price = ? WHERE brand = ?", (95000, 'Sony'))
    cur.execute("UPDATE products SET quantity = quantity + 10 WHERE product_type = ?", ('Футболка',))
    cur.execute("UPDATE products SET min_stock = ? WHERE brand = ? AND product_type = ?", (5, 'Xiaomi', 'Наушники'))

    con.commit()