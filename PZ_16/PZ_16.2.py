# Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
# класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
# связанные с социальным положением (например, "семейное положение",
# "количество детей" и т.д.).


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Human):
    def __init__(self, name, age, family_status=0, children=0):
        Human.__init__(self, name, age, 'Мужской')
        self.family_status = family_status
        self.children = children
    def info(self):
        print(f"Мужчина: {self.name}, {self.age} лет, {self.family_status}, детей: {self.children}")

class Woman(Human):
    def __init__(self, name, age, family_status=0, children=0):
        Human.__init__(self, name, age, 'Женский')
        self.family_status = family_status
        self.children = children
    def info(self):
        print(f"Женщина: {self.name}, {self.age} лет, {self.family_status}, детей: {self.children}")

man1 = Man("Иван", 48, "разведён", 4)
man1.info()

woman1 = Woman("Анастасия", 35, "замужем", 2)
woman1.info()