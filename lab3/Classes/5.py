class Account:
    def __init__(self, owner, balance):
        self.owner = str(owner)
        self.balance = int(balance)
    def deposit(self):
        dep = int(input())
        self.balance += dep
    def withdraw(self):
        wit = int(input())
        if wit <= self.balance:
            self.balance -= wit
        else:
            print('Insufficient funds!')

owner = input()
balance = input()
my = Account(owner, balance)
my.deposit()
print(my.balance)
my.withdraw()
print(my.balance)
