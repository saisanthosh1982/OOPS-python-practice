# Encapsulation

class BadBankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

# account = BadBankAccount(123,0)
# account.balance = -10

# print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return f'Updated account balance {self._balance}'
    
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Initial balance must be non-negative")
        self._balance = amount
    
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposits must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawals must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

account = BankAccount()
print(account.balance)
account.deposit(5)
print(account.balance)
account.withdraw(3)
print(account.balance)
account.withdraw(15)