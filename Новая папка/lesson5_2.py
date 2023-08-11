name = "Ilim"

def info(name):
    print(f"My name is {name}")

class User:
    name = "Ilim"

    def info(name):
        print(f"My name is {name}")

class Parent1:
    def text1(self):
        print("Это  родительский класс Parent1")

class Parent2(Parent1):
    def text(self):
        print("Это дочерний  класс Parent1")

parent = Parent2()
parent.text()
parent.text()