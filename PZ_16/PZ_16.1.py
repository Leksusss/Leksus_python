# 13. Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
# память". Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".


class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram
    def print_information(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram} ГБ")

pc1 = Computer("Lenovo", "Intel Core i7", 16)
pc1.print_information()
pc2 = Computer("Apple", "M1 Pro", 32)
pc2.print_information()