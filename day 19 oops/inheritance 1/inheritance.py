# 22/9/26
'''
class Saving:
    def __init__(self,accno,bal):
        self.accno = accno
        self.bal = bal
    def deposit(self,amount):
        self.bal = self.bal+amount
        print('amount deposited successfully')
    def show_balance(self):
        return f"balance : {self.bal}"
    
a = int(input("enter acc number"))
b = int(input('enter balance'))
s = Saving(a,b)

amt = int(input("enter amount to deposit"))
s.deposit(amt)
print(s.show_balance())
'''

# inheritance

# only attribute
class Person:
    name = 'shivam'
    address = 'nagpur'
        
class Employee(Person):
    empid = 123
    salary = 12000
    
e1 = Employee()
print(e1.name)
print(e1.address)
print(e1.empid)
print(e1.salary)


# methods
class Person:
    def getpersondata(self,name,address):
        self.name = name
        self.address = address
    def displaypersondata(self):
        print(self.name)
        print(self.address)
        
class Employee(Person):
    def getemployeedata(self,empid,salary):
        self.empid = empid
        self.salary = salary
    def displayemployeedata(self):
        print(self.empid)
        print(self.salary)
        
e1 = Employee()
e1.getpersondata('shivam','chandrapur')
e1.getemployeedata(123,342425)

e1.getemployeedata()
e1.getpersondata()