from jinja2.nodes import Break
from patsy.user_util import balanced


class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self,num):
        if (self.balance - num) < 0:
            print("Sorry not enough in the bank to take that amount")
            print("Only this Account balance:", self.balance)
        else:
            self.balance = self.balance - num
            print("Account balance:",self.balance)

    def Deposit(self,num):
        self.balance = self.balance + num
        print("Account balance:", self.balance)

    def __str__(self):
        print(f"Account owner:{self.owner}")
        print(f"Account balance:{self.balance}")

Account1 = Account(owner="Ben",balance=1000)

Account1.__str__()
#Account owner:Ben
#Account balance:1000

Account1.withdraw(100)
900

Account1.withdraw(100)
800

Account1.withdraw(350)
450

print(Account1.balance)
450

Account1.withdraw(500)
#Sorry not enough in the bank to take that amount
#Only this Account balance: 450

Account1.Deposit(400)
850

Account1.withdraw(850)
#Account balance: 0
