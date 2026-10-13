# polymorphism    --- many forms
'''


shape class   #base class
draw()



circle class   and rectangle class   #child class
draw()               draw()



'''


# polymorphic way to call a method from class after creating object

# run time polymorphism
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print('draw method of circle')


class Rectangle(Shape):
    def draw(self):
        print('draw method of rectangle')


def call_draw(shape):
    shape.draw()
    
obj = input("enter circle or rectangle : ")

if obj == "circle":
    c = Circle()

elif obj == "rectangle":
    c = Rectangle()
    
call_draw(c)



# polymorphism without inheritance



class Circle():
    def draw(self):
        print('draw method of circle')


class Rectangle():
    def draw(self):
        print('draw method of rectangle')

def call_draw(s):
    s.draw()
    
obj = input("enter circle or rectangle : ")

if obj == "circle":
    c = Circle()

elif obj == "rectangle":
    c = Rectangle()
    
call_draw(c)



# you can call directly
c.draw()

#create a base class account having method deposit, create child class saving and 
# #current and override the deposit method, create a method call_deposit to achieve 
# #polymorphism


class Account:
    bal = 1000
    def deposited(self,amount):
        print("deposit method of account class")
        
class Saving(Account):
    # overriding the base class deposit method
    def deposited(self,amount):
        self.interest = 500
        self.bal = self.bal+self.interest+amount
        print(f"amount deposit , bal is {self.bal}")

class Current(Account):
    # overriding the base class deposit method
    def deposited(self,amount):
        self.bal = self.bal+amount
        print(f"amount deposit without interest, bal is {self.bal}")
        
        
def call_deposit(s):
    s.deposited(200)


s1 = Saving()
call_deposit(s1)


c1 = Current()
call_deposit(c1)