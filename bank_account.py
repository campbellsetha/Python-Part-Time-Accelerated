
class BankAccount:

    all_accounts = []

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

    def display_account_info(self):
        print("Balance:",self.balance, "Interest Rate:",self.int_rate)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            yield_int = self.balance * self.int_rate
            print("Yield Interest:",yield_int)
        else:
            print("Insufficient Funds")
        return self

    @classmethod
    def display_all_info(cls):
        for account in cls.all_accounts:
            print(account.display_account_info)
        return cls

account_1 = BankAccount(0.0325, 600)
account_2 = BankAccount(0.02, 1750)

account_1.deposit(1000).deposit(750).deposit(2500).withdraw(600).yield_interest().display_account_info()
account_2.deposit(5000).deposit(150).withdraw(2000).withdraw(600).withdraw(400).withdraw(900).yield_interest().display_account_info()

