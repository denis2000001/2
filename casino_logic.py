import random
import time
class Automat_Roulette:
    def __init__(self,balans, game):
        self.balans = balans
        self.game = game
    def start(self):
        while True:
            answer = input("Готовы начать? (Да или Нет):  ")
            if answer.lower() == "да" or answer.lower() == "yes":
                bid = int(input("Введите вашу ставку: "))
                if bid > self.balans:
                    print("Недостаточно средств!")
                    break
                nums = [0, 1, 2, 3, 4, 5, 6, 7]
                self.balans -= bid
                print("Генерация первого числа...")
                time.sleep(2)
                print("Генерация второго числа...")
                time.sleep(2)
                print("Генерация третьего числа...")
                time.sleep(2)
                choice = random.choices(nums, k=3)
                print(choice)
                if choice == ['1', '1', '1']:
                    print('+250$')
                    self.balans += 250
                elif choice == ['2', '2', '2']:
                    print('+500$')
                    self.balans += 500
                elif choice == ['3', '3', '3']:
                    print('+750$')
                    self.balans += 750
                elif choice == ['4', '4', '4']:
                    print('+1000$')
                    self.balans += 1000
                elif choice == ['5', '5', '5']:
                    print('+1500$')
                    self.balans += 1500
                elif choice == ['6', '6', '6']:
                    print('+2000$')
                    self.balans += 2000
                elif choice == ['7', '7', '7']:
                    print('+5000$')
                    self.balans += 5000
                elif choice == ['0', '0', '0']:
                    print('+0$')
                else:
                    print('Вы проиграли!')
                print(f"Ваш баланс: {self.balans}")
            else:
                    print("Спасибо за игру!")
                    break