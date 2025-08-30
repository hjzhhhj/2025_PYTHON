class InsufficientBalanceError(Exception):
    pass

class WrongAccountNumberError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("잔액이 부족합니다.") # 잔액 부족 예외 발생!
        self.balance -= amount

    def transfer(self, target_account, amount):
        if self.account_number == target_account.account_number:
            raise WrongAccountNumberError("잘못된 계좌 번호입니다.") # 잘못된 계좌 번호 예외 발생!
        self.withdraw(amount)
        target_account.deposit(amount)

account1 = BankAccount("123-456-789", 1000)
account2 = BankAccount("987-654-321", 500)

try:
    account1.transfer(account2, 200) 
except InsufficientBalanceError as e:
    print(e)
except WrongAccountNumberError as e:
    print(e)
except ValueError as e:
    print(e)

print(f"계좌 1의 잔액 : {account1.balance}")
print(f"계좌 2의 잔액 : {account2.balance}")

try:
    account1.transfer(account2, 1500) # 잔액 부족 예외 발생
except InsufficientBalanceError as e:
    print(e)
except WrongAccountNumberError as e:
    print(e)
except ValueError as e:
    print(e)

try:
    account1.transfer(account1, 100) # 잘못된 계좌 번호 예외 발생
except InsufficientBalanceError as e:
    print(e)
except WrongAccountNumberError as e:
    print(e)
except ValueError as e:
    print(e)