class Bank:

    def __init__(self, balance: list):
        self.balances = balance 
        self.length = len(self.balances)

    def validateAc(self, accountNo: int):
        return 0 < accountNo <= self.length 

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self.validateAc(account1) and self.validateAc(account2)):
            return False 
        if self.balances[account1 - 1] < money:
            return False 

        self.balances[account1 - 1] -= money 
        self.balances[account2 - 1] += money 
        return True


    def deposit(self, account: int, money: int) -> bool:
        if not self.validateAc(account):
            return False 
        self.balances[account - 1] += money 
        return True 


    def withdraw(self, account: int, money: int) -> bool:
        if not self.validateAc(account):
            return False 

        if self.balances[account - 1] < money:
            return False 

        self.balances[account - 1] -= money 
        return True 


