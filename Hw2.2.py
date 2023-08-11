# Создайте класс SlotMachine, в котором в конструкторе принимает один атрибут name, и также у него есть два динамических атрибутов user_balance(пользовательский баланс по умолчанию равен 100) и game_balance(игровой баланс, по умолчанию равен 0). 

# И также у него есть 6 методов
# 1 метод info, выводит информацию об игроке(имя, пользовательский баланс, игровой баланс)

# 2 метод top_up_balance, который отнимает пользовательский баланс и пополняет игровой баланс. И также пополнить баланс можно до 100$. Если пользователь хочет пополнить больше денег, то выведите “Вы можете пополнить до 100$”, и также при пополнении денег создайте 
# 3 третий метод balance_up и пусть пополнение идет через этот метод.

# 4 метод game в котором автомат загадывает случайное число(от 1 до 10, при помощи модуля random) и пользователь должен его угадать и также у пользователя есть 5 попыток угадать число. Если пользователь не угадал число, то с его баланса отнимается 10$ и выводит сообщение “Вы проиграли”. Если пользователь выиграл, то его игровой баланс пополняется на 50$

# 5 метод conslusion_money для вывода игровых денег на пользовательский, и также вы можете вывести от 50$, если пользователь попытается вывести до 50$, то выведите сообщение “Вывести можно от 50$”.x

# Создайте главный 6 метод main, который отвечает за команды игрового автомата. У игрового автомата есть 4 команды(метода).
# 1 - Вызывает метод info и выводит информацию об игроке
# 2 - Пополняет игровой баланс вызывая метод top_up_balance
# 3 - Вызывает метод - game
# 4 - Вызывает метод - conslusion_money 
import random
# Создайте объект класса и вызовите метод main
class SlotMachine:
    def __init__(self, name, ) -> None:
        self.name = name 
        self.user_balance = 100
        self.game_balance = 0
    
    def info(self):
        print(f"Имя игрока {self.name}")
        print(f"Баланс Игрока: {self.user_balance}")
        print(f"Гейм баланс игрока: {self.user_balance}")
    
    def top_up_balance(self,amount):
        if amount >= 100:
            self.user_balance -=amount
            self.game_balance += amount
        else:
            print("Вы можете пополнить до 100$")

    def balance_up(self, amount):
        self.balance_up(amount)

    def game(self,amount):
        a = random.randint(1,10)
        b = 5
         
        while b > 0:
            try:
                user = input("Введите число от 1 до 10:")
                if user == a:
                    print("Вы выиграли ")
                    self.game_balance += 50
                    return
                else: 
                    b -= 1
                    print("Вы не угадали.Осталось {b} попыток ")
            except:
                print("Введите число!")

        print("Вы проиграли!")
        self.game_balance -= 10



    def conslusion_money(self,amount):  
        if amount >= 50: 
            self.game_balance -= amount
            self.user_balance += amount
        else:
            print("Можно выводить до 50 ")

# Создайте класс SlotMachine, в котором в конструкторе принимает один атрибут name 
# и также у него есть два динамических атрибутов user_balance(пользовательский баланс по умолчанию равен 100)
#  и game_balance(игровой баланс, по умолчанию равен 0). 

import random

class  SlotMachine:
    def __init__(self, name) -> None:
        self.name = name 
        self.user_balance = 100
        self.game_balance = 0  

    def info(self):
        print(f'Имя: {self.name}') 
        print(f'пользовательский баланс: {self.user_balance}com')
        print(f'игровой баланс: {self.user_balance}com')

    def top_up_balance(self,amount):
        
        if amount >= 100: 
            self.user_balance -= amount
            self.game_balance += amount
        else:
            print("котуну кыс")


    def balance_up(self, amount):
        self.balance_up(amount)


    def game(self):

        a = random.randint(1,10)
        b = 5 

        while b > 0:
            try:
                user = input('Введите число от 1 до 10')
                if user == a:
                    print('Вы выйграли ')
                    self.game_balance += 50
                    return
                else:
                    b -= 1 
                    print(f"вы не угадали. Осталось {b} попыток")
            except:
                print("Введите число !")

        print("Вы проиграли")
        self.game_balance -= 10 


    def conslusion_money(self,amount):  
        if amount >= 50: 
            self.game_balance -= amount
            self.user_balance += amount
        else:
            print("Можно выводить до 50 ")



    def main(self):
        while True:
            print("Команды игрового автомата:")
            print("1 - Вывести информацию об игроке")
            print("2 - Пополнить игровой баланс")
            print("3 - Запустить игровой автомат")
            print("4 - Вывести игровые деньги на пользовательский баланс")
            print("0 - Выйти из игры")

            command = input("Введите номер команды: ")

            if command == '1':
                self.info()
            elif command == '2':
                try:
                    amount = int(input("Введите сумму для пополнения: "))
                    self.top_up_balance(amount)
                except ValueError:
                    print("Введите число!")
            elif command == '3':
                self.game()
            elif command == '4':
                try:
                    amount = int(input("Введите сумму для вывода: "))
                    self.conclusion_money(amount)
                except ValueError:
                    print("Введите число!")
            elif command == '0':
                break
            else:
                print("Некорректная команда. Повторите ввод.")

if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    slot_machine = SlotMachine(player_name)
    slot_machine.main()