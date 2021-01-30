class Account:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return (f"The account balance is: {self.balance} \nThe account holder is: {self.name}")

    def deposit(self, amount):
        self.balance += amount
        print(f"you deposited {amount} and your balance is now: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough funds"
        else:
            self.balance -= amount
            return f"You withdrew {amount}, your balance is now {self.balance}"