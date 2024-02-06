


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, value):
        if value < 0:
            print("You cannot deposit a negative value!")
        else:
            self.balance += value
    def withdrawal(self, value):
        if self.balance - value < 0:
            print("You are not allowed to overdraw your account!")
        else:
            self.balance -= value

a1 = Account("temik", 42)
a1.deposit(7)
print(a1.balance)