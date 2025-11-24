


class Bank():
    def __init__(self, balance:int):
        self.balance = balance
        print(f"Current Balance {balance}")


    def withdraw(self, amount:int):
        self.balance = self.balance - amount
        print(f"Your balance is: {self.balance}")


    def check_balance(self):
        print(f"Your balance is: {self.balance}")





