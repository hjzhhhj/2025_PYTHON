class InsufficientBalanceError(Exception):
    pass

class WrongAccountNumberError(Exception):
    pass

class Bank:
    def __init__(self):
        self.accounts = {}  

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
        else:
            self.accounts[account_number] = amount
        print(f"계좌 {account_number}에 {amount}원 입금되었습니다. 잔액: {self.accounts[account_number]}원")

    def withdrawal(self, account_number, amount):
        if account_number not in self.accounts:
            raise WrongAccountNumberError("잘못된 계좌 번호입니다.")
        if self.accounts[account_number] < amount:
            raise InsufficientBalanceError("잔액이 부족합니다.")
        self.accounts[account_number] -= amount
        print(f"계좌 {account_number}에서 {amount}원 출금되었습니다. 잔액: {self.accounts[account_number]}원")

bank = Bank()   

try:
    bank.deposit("123-456-789", 1000)  
    bank.withdrawal("123-456-789", 500)  
    bank.withdrawal("123-456-789", 600)  
    bank.withdrawal("987-654-321", 100)
    bank.deposit("987-654-321", 100)
    
except InsufficientBalanceError as e:
    print(e)
except WrongAccountNumberError as e:
    print(e)
except Exception as e:
    print(e)

print(bank.accounts)