#multilevel inheritance A--> B --> C

# only attribute
class Person:
    name = 'shivam'

class Employee(Person):
    salary = 50000

class PartTimeEmployee(Employee):
    working_hours = 8


p = PartTimeEmployee()
print(f"Name : {p.name}")
print(f"salary : {p.salary}")
print(f"working hours : {p.working_hours}")


# with methods
class Person:
    def get_name(self,name):
        self.name = name
        return self.name
class Employee(Person):
    def get_salary(self,salary):
        self.salary = salary
        return self.salary
class PartTimeEmployee(Employee):
    def get_wh(self,wh):
        self.wh = wh
        return self.wh

p = PartTimeEmployee()
print(f"Name : {p.get_name('shivam')}")
print(f"salary : {p.get_salary(25671)}")
print(f"working hours : {p.get_wh(8)}")