'''Classs Atrributes'''

class Student:
    companyName = 'LTIM'    # class Atributes
    mobileNumber = 2147623518  # class Atributes
    
    
s1 = Student()
s2 = Student()

print('S1 details')
print(s1.companyName,s1.mobileNumber)

print('S2 details')
print(s2.companyName,s2.mobileNumber)


'''OR'''

print(Student.companyName,Student.mobileNumber)


'''instance attributes -- specific to an object and defined either inthe __init__ method
each object can have its own unjique value for the attributes'''


class Company:
    def __init__(self):
        print('constructor created')
        
s1 = Student()   # it will call constructor automatically




'''how to add instance attributes'''
class Custumer:
    def __init__(self):
        name = ""
        mobileNumber = 0
        
c1 = Custumer()
c1.name = "shivam"
c1.mobileNumber = 628746163416


print(c1.name)
print(c1.mobileNumber)


#how to do manually

class Custumer:
    shopCode = 111# class attribute
        
c1 = Custumer()
c1.name = "shivam"  # instance atrribute
c1.mobileNumber = 628746163416

print(c1.shopCode)
print(c1.name)
print(c1.mobileNumber)


'''methods'''

class Custumer:
    def __init__(self,name,mobile):
        self.name = name
        self.mobile = mobile
        
    def display(self):    # Method
        print(f'Name : {self.name}')
        print(f'Mobile : {self.mobile}')
        
        
name = input('Enter Name')
mobile = int(input('enter mobile number'))
c2 = Custumer(name, mobile)
c2.display()





class Phone:
    device_type = 'smartphone'
    
    
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
       
    def show_details(self):
        print("Phone details")
        print(f"device type : {self.device_type}")
        print(f"brand type: {self.brand}")
        print(f"model : {self.model}")
        print(f"price : {self.price}")
        
    def updateprice(self,price):
        self.price = price
        
p1 = Phone('iphone','18 pro',26371)
p1.show_details()


up = int(input("enter price to be updated"))
p1.updateprice(up)

p1.show_details()