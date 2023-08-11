# class Toy:
#     def play(self):
#         pass

# class Ball(Toy):
#     def play(self):
#         return "Мячь прыгает"

# class Car(Toy):
#     def play(self):
#         return "Машина едет"

# class Doll(Toy):
#     def play(self):
#         return "Кукла одевается"
      

# def playing(Toy):
#     return Toy.play()

# ball = Ball()
# car = Car()
# doll = Doll()

# # print(ball.play())

# print(playing(car))
# print(playing(doll))
# print(playing(ball))

# class Animals:
#     def sound(self):
#         pass

# class Dog(Animals):
#     def sound(self):
#         return "Гав гав "
    
# class Cat(Animals):
#     def sound(self):
#         return "мяу мяу"
    
# def sounds(ilim):
#     return ilim.sound()

# dog = Dog()
# cat = Cat()

# print(sounds(dog))
# print(sounds(cat))

class Person:
    def __init__(self ,name , age):
        self.name = name 
        self._age = age
        self.__password = "1234"

    def info(self):
        return f"Имя {self.name} Возраст: {self._age} лет"
    
    def __private(self):
        return {self.__password}

person = Person("Ilim",19)

print(person.name)
print(person._age)
print(person.info())
print(person.__private())