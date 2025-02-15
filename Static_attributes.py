# Static attributes

class BankAccount:
    user_count = 0

    def __init__(self,owner, balance = 0):
        self.owner = owner
        self._balance = balance
        BankAccount.user_count += 1

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__log_transcation(self.owner,'deposited', amount)
        else:
            print("deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.__log_transcation(self.owner,'withdrawed', amount)
        else:
            print("Insufficient funds or withdrawal amount must be positive")

    def __log_transcation(self,owner,transation_type,amount):
        print(f"{self.owner} {transation_type} ${amount}. Updated balance: {self._balance}")

    def display_balance(self):
        print(f"{self.owner}'s current balance: {self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        if 0 <= rate <= 8:
            return f'given interest reate is valid'
        else:
            return f'give another interest rate that is valid'
    
    @staticmethod
    def calculate_interest_year(balance, rate):
        if BankAccount.is_valid_interest_rate(rate):
            interest = balance * (rate / 100)
            return f'interest rate for one year is {round(interest,2)}'
        else:
            print("Invalid interest rate. Interest rate must be between 0 and 8")
            return 0


user1 = BankAccount('daniel',500)
user2 = BankAccount('emanuel',0)

user1.deposit(30)
user1.withdraw(50)

user1.display_balance()

print(BankAccount.is_valid_interest_rate(5))

print(BankAccount.calculate_interest_year(5000, 7))