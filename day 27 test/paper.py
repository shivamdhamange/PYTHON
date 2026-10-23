print("QUestion no 1")
print("--------------------------------")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


s1 = Student("Rahul", 85)
s2 = Student("Priya", 92)

s1.display()
s2.display()



print("QUestion no 2")
print("--------------------------------")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


r = Rectangle(8, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())



print("Question no 3")
print("--------------------------------")

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def show(self):
        print("Final Count:", self.count)


c = Counter()

c.increment()
c.increment()
c.increment()
c.decrement()

c.show()

print("QUestion no 4")
print("--------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)


s = Student("Shivam", 20, 101)
s.display()


print("QUestion no 5")
print("--------------------------------")

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.deposit(1000)
account.withdraw(400)
account.withdraw(800)

print("Final Balance:", account.get_balance())