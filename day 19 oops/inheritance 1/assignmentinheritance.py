#single inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)
        
        
class Employee(Person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary
        
    def display(self):
        super().display()
        print(self.salary)
        
e = Employee('shivam',23,3526532)
e.display()



class Vehicle:
    def fuel_type(self):
        print("uses petrol/diesel")
        
class Car(Vehicle):
    def num_wheels(self):
        print("4 wheels")
        
c = Car()
c.num_wheels()
c.fuel_type()



# hierarchical inheritance

class Shape():
    def info():
        print("This is a Shape")
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        print(area)

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        area = self.l * self.b
        print(area)
        
        
r = Rectangle(3,4)
c = Circle(5)

c.area()
r.area()




class Bank:
    def bank_info(self):
        print('Welcome to the bank')
        
class SavingsAccount(Bank):
    def typeof(self):
        print("savings Acoount")
        print("intresrt rate = 5%")

class CurrentAccount(Bank):
    def typeof(self):
        print('current account')
        print("interest rate 0 %")


s = SavingsAccount()
c = CurrentAccount()

s.typeof()
c.typeof()


# multilevel inheritance
class Animal:
    def eat(self):
        print('eat')
    
class Mammal(Animal):
    def walk(self):
        print('walk')
    
class Dog(Mammal):
    def bark(self):
        print('bark')
        
d = Dog()

d.bark()
d.walk()
d.eat()




class Student:
    def student_details(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")


class UnderGraduate(Student):
    def course_details(self, course):
        self.course = course
        print(f"Course: {self.course}")


class FinalYearStudent(UnderGraduate):
    def project_details(self, project_title):
        self.project_title = project_title
        print(f"Project Title: {self.project_title}")


s1 = FinalYearStudent()
s1.student_details("Anita Verma", 21)
s1.course_details("B.Sc Computer Science")
s1.project_details("AI Based Attendance System")


# multiple inheritance

class Father:
    def skills(self):
        print("Father's Skills: Gardening, Cooking")


class Mother:
    def skills(self):
        print("Mother's Skills: Painting, Dancing")


class Child(Father, Mother):
    def own_skills(self):
        print("Child's Own Skill: Coding")

    def all_skills(self):
        Father.skills(self)
        Mother.skills(self)
        self.own_skills()


c1 = Child()
c1.all_skills()




class Camera:
    def click_photo(self):
        print("Clicking photo...")


class MusicPlayer:
    def play_music(self):
        print("Playing music...")


class SmartPhone(Camera, MusicPlayer):
    def make_call(self):
        print("Making a call...")


phone = SmartPhone()
phone.click_photo()
phone.play_music()
phone.make_call()
