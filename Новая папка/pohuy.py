# Задача: Создайте класс "Таймер" (Timer), который будет представлять простой таймер обратного отсчета. Класс должен иметь следующие методы:

# 1. Метод `__init__`: Этот метод должен инициализировать таймер с начальным значением времени (в секундах), которое передается аргументом при создании объекта.

# 2. Метод `get_time`: Этот метод должен возвращать текущее значение времени таймера в секундах.

# 3. Метод `start`: Этот метод должен запустить таймер, уменьшая значение времени на 1 каждую секунду, пока таймер не достигнет значения 0.

# 4. Метод `reset`: Этот метод должен сбрасывать значение таймера в начальное значение, указанное при создании объекта.
import time

class Timer:
    def __init__(self ,sek):
        self.sek = sek
        self.kes = sek
        
    
    def get_time(self):
        return f"Таймер установлен на {self.sek} секунд"
    
    def start(self):
        while self.sek >0:
            print(self.sek)
            time.sleep(1)
            self.sek -= 1
            
            # self.sek -=1
            # time.sleep(1)
        print("Таймер завершен!")

    def reset(self):
        # self.sek = self.sek
        if self.sek == 0 :
            print("Do you wanna reset Timer y. or n. ")
        a = input("Введите  y or n: ")      
        if a == "y":
            return timer.get_time(), timer.start() ,  timer.reset()
        else:
            print("dffdfd")
        

timer = Timer(3)

print(timer.get_time())  

timer.start()


timer.reset()
