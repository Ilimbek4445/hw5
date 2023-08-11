# Задача 1
# Вам нужно создать программу для рисования различных геометрических фигур. У вас должен быть базовый класс Shape (Фигура), а также несколько подклассов, представляющих различные фигуры, такие как Circle (Круг) и Rectangle (Прямоугольник).
# Класс Shape должен иметь метод draw(), который будет выводить на экран "Рисуем фигуру". Классы Circle и Rectangle должны наследовать этот метод и дополнительно реализовать свою функциональность. 
# Подсказка: Делайте точно так же как и на уроке
# class Shape:
#     def draw(self):
#         return "Рисуем фигуру"
# class Circle(Shape):
#     def draw(self):
#         return "Рисуем круг"

# class Rectangle(Shape):
#     def draw(self):
#         return "Рисуем прямоугольник"
    
# def drowing(t):
#     return t.draw()

# shape = Shape()
# circle = Circle()
# rectangle = Rectangle()
# print(drowing(shape))
# print(drowing(circle))
# print(drowing(rectangle ))
# Задача 2

# Создайте класс Counter (Счетчик), который будет представлять счетчик, способный увеличиваться на заданное значение и возвращать текущее значение.
# Класс Counter должен иметь следующие методы:
# __init__(self): Конструктор для инициализации счетчика, начальное значение - 0.
# increment(self, value): Увеличивает счетчик на указанное значение.
# get_value(self): Возвращает текущее значение счетчика.
# class Counter:
#     def __init__(self ):
#         self.amount = 0

#     def increment(self , num):
#         self.amount += num
 
#     def get_value(self): 
#         return self.amount
    
# counter = Counter()
# counter.increment(5)
# print(counter.get_value())


