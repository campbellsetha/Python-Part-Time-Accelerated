class User:

    def __init__(self):
        self.name = "John Hammond"
        self.email = "sparednoexpense@jurassicpark.com"
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.account.balance)
        return self
    

class BankAccount:

    def __init__(self, int_rate, balance):

        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = amount + self.balance
        print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance =  self.balance - amount
        print(self.balance)
        return self





