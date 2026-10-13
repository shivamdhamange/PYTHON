# oops is a programming pattern based on the concepts of objects
# there are attributes and methods

class Student:
    name = 'shivam'
    age = 24
    
s1 = Student()
print(s1.name)
print(s1.age)

print('student setails')
print(f'Name : {s1.name}')
print(f'age : {s1.age}')



class Book:
    title = None
    author = None
    price = 0
    
b1 = Book()

print('enter book details')
b1.title = input('enter title')
b1.author = input('enter author')
b1.price = int(input('enter price'))

print('book details')
print(f'title : {b1.title}')
print(f'author : {b1.author}')
print(f'price : {b1.price}')


class Custumer:
    cust_id = 123
    cust_name = 'shivam'
    cust_email = 'shivam@gmail.com'
    cust_mobile = 23473726382
    
c1 = Custumer()

print('Custumer details')
print(f'cust_id : {c1.cust_id}')
print(f'cust_name : {c1.cust_name}')
print(f'cust_email : {c1.cust_email}')
print(f'cust_mobile : {c1.cust_mobile}')


class Patient:
    pat_id=1
    name = 'shivam'
    disease = 'heart attack'
    doctorName = 'danish'
    
p1 = Patient()


print('enter patient details')
p1.pat_id = int(input('enter title'))
p1.name = input('enter name')
p1.disease = input('enter disease')
p1.doctorName = input('enter doct name')

print('book details')
print(f'patient id : {p1.pat_id}')
print(f'name : {p1.name}')
print(f'disease : {p1.disease}')
print(f'doctNAme : {p1.doctorName}')