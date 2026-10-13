# what is abstract class and abstract method
#define common interface for a group of related classes

# from abc import ABC , abstractmethod    # here abc is module   # ABC is class


from abc import ABC,abstractmethod

class Account(ABC):
    # creating A ABSTRACT METHOD
    @abstractmethod
    def deposit(self):
        pass
    
class Saving(Account):  
    def deposit(self):
        print("Hello from saving class")
        
s = Saving()
s.deposit()





from abc import ABC,abstractmethod

class Account(ABC):
    bal = 1000
    # creating A ABSTRACT METHOD
    @abstractmethod
    def deposit(self):
        pass
    
class Saving(Account):  
    def deposit(self,amount):
        interest = 500
        self.bal = self.bal + amount + interest
        print(f"bal for saving class is {self.bal}")
        
class Current(Account):  
    def deposit(self,amount):
        self.bal = self.bal + amount
        print(f"bal for current class is {self.bal}")
             
        
        
s = Saving()
s.deposit(200)


c = Current()
c.deposit(300)


