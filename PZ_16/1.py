# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки. 
# Добавьте методы для вычисления процентных начислений и снятия денег.
class Bank:
    def __init__(self, money, percent):
        self.money = money
        self.percent = percent
    def show_balance(self):
        print(f"На счёте: {self.money} рублей")
    def calculate_percent(self):
        insert = self.money * self.percent / 100
        self.money += insert
        print(f"Начислено процентов: {insert} рублей")
        print(f"Новый баланс: {self.money} рублей")
    def withdraw(self, amount):
        if amount < 0 or amount > self.money:
            print("Сумма не может быть отрицательной или недостаточно средств")
        else:
            self.money -= amount
            print(f"Вы сняли {amount} рублей")
            print(f"Остаточный баланс: {self.money} рублей")
bank = Bank(10000, 10)
bank.show_balance()
bank.calculate_percent()
bank.withdraw(5700)
bank.show_balance()
bank.withdraw(10000)