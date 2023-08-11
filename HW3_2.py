# Задача: 1
# Создайте класс "Транспортное средство" (Vehicle) с атрибутами "brand" (марка) и "model" (модель). У класса должен быть метод "info()", который выводит информацию о транспортном средстве (марка и модель).
# Затем создайте подкласс "Автомобиль" (Car), который наследует от класса "Транспортное средство". В классе "Автомобиль" определите дополнительный атрибут "year" (год выпуска), а также переопределите метод "info()" для вывода дополнительной информации о годе выпуска автомобиля.

# class Vehicle():
#     def __init__(self , brand , model):
#         self.brand = brand
#         self.model = model
    
#     def info(self):
#         return f"Ваша машина {self.brand} {self.model}"
# rev = Vehicle("MERSEDES","BANAN")
# rev.info()

# class Car(Vehicle):
#     def __init__(self, brand, model,year ):
#         super().__init__(brand, model)
#         self.year = year
    
#     def info(self):
#         return f"Ваша машина {self.brand} {self.model} {self.year} Года"

# ver = Car("MERSEDES","BANAN",2015)
# ver.info()
# print(ver.info())


# Задача: 2
# Создайте три класса: "Родитель" (Parent), "Мама" (Mother) и "Папа" (Father).
# Класс "Родитель" должен содержать атрибуты "first_name" (имя) и "last_name" (фамилия), а также метод "get_full_name()", который возвращает полное имя родителя (имя и фамилию).
# Классы "Мама" и "Папа" должны наследоваться от класса "Родитель". Каждый из этих классов должен иметь свой дополнительный атрибут: "child_count" (количество детей у родителя). Определите метод "get_child_count()" в каждом из классов "Мама" и "Папа", чтобы возвращать количество детей у соответствующего родителя.

class Parent():
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_name(self):
        return f"{self.first_name} {self.last_name}"

class Mother(Parent):
    def __init__(self, first_name, last_name,child_count):
        super().__init__(first_name, last_name)
        self.child_count = child_count

    def get_child_count(self):
        return f"У мамы {self.child_count} детей"

qwe =Mother("Имя","Фамилия",97)
print(qwe.get_name())
print(qwe.get_child_count())

class Father(Parent):
    def __init__(self, first_name, last_name,child_count):
        super().__init__(first_name, last_name)
        self.child_count = child_count

    def get_child_count(self):
        return f"У папы {self.child_count } детей"

ewq = Father("Имя","Фамилия",98)
print(ewq.get_name())
print(ewq.get_child_count())






