# 23/9/26


"""while True:
    print("1 . Check Balance")
    print("2 . Withdraw Cash")
    print("3 . Deposit Cash")
    print("4 . Transfer Money")
    print("5 . Change Pin")
    print("6 . Exit")
    
    print('-------------------------------------')
    
    choice = int(input('what you want to do ? (1,2,3,4,5,6) : '))

    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            break"""


class Custumer:
    def __init__(self,custId,name):
        self.custId=custId
        self.name = name
        self.accounts = []

    def add_account(self,account):
        self.accounts.append(account)
        
class Accounts:
    def __init__(self,accNo,balance=0):
        self.accNo = accNo
        self.balance = balance

c = Custumer(123,'shivam')
a = Accounts(5217351728,50000)
c.add_account(a)

print('custumer id',c.custId)
print('custumert name',c.name)

print('account no',c.accounts[0].accNo)
print('balance',c.accounts[0].balance)



class Student:
    def __init__(self,rNO,name):
        self.rNo = rNO
        self.name = name
        self.address = []
        
    def add_address(self,address):
        self.address.append(address)
        
class Address:
    def __init__(self,locality,city,state):
        self.locality = locality
        self.city = city
        self.state = state
        
s = Student(19,'shivam')
ad = Address('chhoni','nagpur','maharastra')
s.add_address(ad)

print('student roll no',s.rNo)
print('Student name',s.name)

print('locality',s.address[0].locality)
print('city',s.address[0].city)
print('state',s.address[0].state6g)