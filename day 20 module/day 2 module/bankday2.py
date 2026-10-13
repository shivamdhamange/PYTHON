# creating a userdegfeined module named bank.py having variabvle bal and 3 function



def deposit(amount):
    bal = 1000
    bal = bal + amount
    return f"amount deposited , bal is {bal}"

def withdraw(amount):
    bal = 1000
    bal = bal - amount
    return f"amount withdraw , bal is {bal}"

def show_balance():
    bal = 1000
    return f"current balance is {bal}"

# save this file as bank.py
# and import it in main file where you have to use it




# using class

class Saving:
    bal = 1000
    def depositl(self,amount):
        self.bal = self.bal + amount
        return f"amount deposited , bal is {self.bal}"

    def withdrawl(self,amount):
        self.bal = self.bal - amount
        return f"amount withdraw , bal is {self.bal}"

    def show_balance(self):
        return f"current balance is {self.bal}"