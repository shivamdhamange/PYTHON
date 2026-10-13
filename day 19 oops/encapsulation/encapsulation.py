# public protected and private


# private arttribute example
class Account:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no   # public attribute
        self.__balance = balance # private attribute
        
    # private method
    def __showbalance(self):
        print(f"show balance is : {self.__balance}")
        
a =Account(111,1000)
print(a.acc_no)
print(a._Account__balance)   # accesssing private attribute using name mangling
a._Account__showbalance()



# protected attribute example

class Account:
    def __init__(self,act_no,balance):
        self.act_no = act_no   # public attribute
        self._balance = balance # protected attribute
        
class Saving(Account):
    def showbalance(self):   # public method
        print(f"show balance is : {self._balance}")
        
s =Saving(111,1000)
print(s.act_no)
s.showbalance()