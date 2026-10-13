#method overriding
# child changes the implementation of the inherited method from parent class



#example one
class Account:
    def deposit(self):
        print("deposit method of account class")
        
class Saving(Account):
    # overriding the base class deposit method
    def deposit(self):
        print("deposit method of saving class")

s = Saving()
s.deposit()


#example two
class Animal:
    def display(self):
        print("This is an animal")

class Dog(Animal):
    def display(self):
        print("This is a dog")

obj = Dog()
obj.display()


#exaple 3
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

s1 = Saving()
s1.deposited(200)




#example 4     (heirarchical inheritance)
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
s1 = Saving()
s1.deposited(200)


c1 = Current()
c1.deposited(200)




# example 5  method overriding and use of method overriding

class Person:
    def __init__(self,name):
        self.name = name

    def display(self):
        return f"name : {self.name}"
    
class Student(Person):
    def __init__(self, name,rno):
        super().__init__(name)
        self.rno = rno
        
    def display(self):
        print(super().display())
        return f"rno : {self.rno}"
    
class parttime_student(Student):
    def __init__(self, name,rno,cource):
        super().__init__(name,rno)
        self.cource = cource
    
    def display(self):
        print(super().display())
        return f"rno : {self.cource}"


s = Student("shivam",19)
print(s.display())

p = parttime_student("harshit",3,"java")
print(p.display())


