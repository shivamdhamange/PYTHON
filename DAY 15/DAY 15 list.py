# list is mutable , ordered collection of items , store different data types
#created using [] brackets

# creating empty list
empty_list = []
print(empty_list,type(empty_list))

# creating using different data types and print it
student = [123,'shivxd','shivxd@gmail.com',4326178127]
print(student)
print(f'roll number : {student[0]}')
print(f'name : {student[1]}')
print(f'email : {student[2]}')
print(f'phone number : {student[3]}')

print('--------------------------------------------')
# similary accept rno,name,email, and mobile from user and store it in a list and then display the student details
rno = int(input("enter roll no"))
name = input("enter name of student")
email = input("enter email of sudent")
mobile = int(input("enter mobile no"))

student = [rno,name,email,mobile]
print("Student details------------")
print(f'roll number : {student[0]}')
print(f'name : {student[1]}')
print(f'email : {student[2]}')
print(f'phone number : {student[3]}')

print('--------------------------------------------')
# accept employee details and print them
employee_id = int(input("enter employee id"))
name = input("enter name of employee")
email = input("enter email of employee")
mobile = int(input("enter mobile no of employee"))

employee = [employee_id,name,email,mobile]

print("Employee details-----------")
print(f'roll number : {employee[0]}')
print(f'name : {employee[1]}')
print(f'email : {employee[2]}')
print(f'phone number : {employee[3]}')

for e in employee:
    print(e)
    