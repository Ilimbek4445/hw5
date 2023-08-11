# Создайте класс SlotMachine, в котором в конструкторе принимает один атрибут name, и также у него есть два динамических атрибутов user_balance(пользовательский баланс по умолчанию равен 100) и game_balance(игровой баланс, по умолчанию равен 0). 

# И также у него есть 6 методов
# 1 метод info, выводит информацию об игроке(имя, пользовательский баланс, игровой баланс)

# 2 метод top_up_balance, который отнимает пользовательский баланс и пополняет игровой баланс. И также пополнить баланс можно до 100$. Если пользователь хочет пополнить больше денег, то выведите “Вы можете пополнить до 100$”, и также при пополнении денег создайте 3 третий метод balance_up и пусть пополнение идет через этот метод.

# 4 метод game в котором автомат загадывает случайное число(от 1 до 10, при помощи модуля random) и пользователь должен его угадать и также у пользователя есть 5 попыток угадать число. Если пользователь не угадал число, то с его баланса отнимается 10$ и выводит сообщение “Вы проиграли”. Если пользователь выиграл, то его игровой баланс пополняется на 50$

# 5 метод conslusion_money для вывода игровых денег на пользовательский, и также вы можете вывести от 50$, если пользователь попытается вывести до 50$, то выведите сообщение “Вывести можно от 50$”.x

# Создайте главный 6 метод main, который отвечает за команды игрового автомата. У игрового автомата есть 4 команды(метода).
# 1 - Вызывает метод info и выводит информацию об игроке
# 2 - Пополняет игровой баланс вызывая метод top_up_balance
# 3 - Вызывает метод - game
# 4 - Вызывает метод - conslusion_money 

# Создайте объект класса и вызовите метод main


import random

class SlotMachine:
    def __init__(self, name):
        self.name = name
        self.user_balance = 100
        self.game_balance = 0

    def info(self):
        print(f"Player: {self.name}")
        print(f"Пользовательский баланс: ${self.user_balance}")
        print(f"Game Balance: ${self.game_balance}")

    def balance_up(self, amount):
        if amount > 100:
            print("Вы можете пополнить до 100$")
            return
        self.user_balance -= amount
        self.game_balance += amount

    def top_up_balance(self, amount):
        self.balance_up(amount)

    def game(self):
        number_to_guess = random.randint(1, 10)
        for _ in range(5):
            user_guess = int(input("Угадайте число от 1 до 10: "))
            if user_guess == number_to_guess:
                print("Поздравляем! Вы угадали число!")
                self.game_balance += 50
                return
            else:
                print("Вы не угадали!")
                self.user_balance -= 10

        print("Вы проиграли!")

    def conslusion_money(self):
        amount_to_withdraw = int(input("Введите сумму для вывода: "))
        if amount_to_withdraw < 50:
            print("Вывести можно от 50$")
            return
        self.game_balance -= amount_to_withdraw
        self.user_balance += amount_to_withdraw
        print(f"Вы успешно вывели {amount_to_withdraw}$")

    def main(self):
        while True:
            print("\nВыберите действие:")
            print("1 - Просмотр информации об игроке")
            print("2 - Пополнить игровой баланс")
            print("3 - Играть в игру")
            print("4 - Вывести деньги")
            print("0 - Выйти из игры")
            choice = int(input("Введите номер действия: "))

            if choice == 0:
                print("Спасибо за игру! До свидания.")
                break
            elif choice == 1:
                self.info()
            elif choice == 2:
                amount = int(input("Введите сумму для пополнения: "))
                self.top_up_balance(amount)
            elif choice == 3:
                self.game()
            elif choice == 4:
                self.conslusion_money()
            else:
                print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    name = input("Введите ваше имя: ")
    slot_machine = SlotMachine(name)
    slot_machine.main()
