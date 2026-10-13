'''add()'''

course = set()
#add 3 enteries in set
for i in range(3):
    c = input('enter what to be added')
    course.add(c)
    print('course added to set')
    
print('Courses Present : ')
print(course)

'''remove()''' # it will throw an error if the element is not present

corse1 = {'java','php','html'}
ct = input('enter course name to remove')
course.remove(ct)
print(corse1)



'''Discard()'''  # it will not throw an error if element is not present

t = {'java','hello','html'}
i = input('enter course name to remove')
t.discard(i)
print(t)


student = set()
while True:
    print('1 - Add Student name')
    print('2 - remove Student name using remove()')
    print('3 - remove Student name using discard()')
    print('4 - display')
    print('5 - exit')
    
    choice = int(input('enter your choice'))
    
    if choice == 1:
        i = input('enter student name to add')
        student.add(i)
        print('student added')
    elif choice == 2:
        t = input('enter student name to remove')
        student.remove(t)
    elif choice == 3:
        t = input('enter student name to remove')
        student.discard(t)
        print('student removed')
    elif choice == 4:
        print(student)
    else:
        print('program exitted')
        break