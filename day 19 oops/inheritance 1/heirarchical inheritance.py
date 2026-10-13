class Account:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal
    def show_balance(self):
        return f"balance is : {self.bal}"
    
class Savings(Account):
    interest = 500
    def deposit(self,amount):
        self.bal = self.bal + amount + self.interest
        return f"amount deposited in saving account , bal is : {self.bal}"

class Current(Account):
    def deposit(self,amount):
        self.bal = self.bal + amount
        return f"amount deposited in current account , bal is : {self.bal}"



s = Savings(123,1000)
print(s.deposit(100))
print(s.show_balance())


c = Current(254,5000)
print(c.deposit(100))
print(c.show_balance())

