# Set - mutable unordered collection with unique items


# creating a empty sets

num = set()
print(type(num))
print(num)


# creating a set
stud = {111,'amit','ssd','amit'}
print(stud)   # doesn't follow the order    # {111, 'ssd', 'amit'} output
# one amit is removed


# creating a set using set constructor
student = set([111,'amit','ssd','amit'])
print(student)


# union |
stud1 = {'shivam','ssd',23}
stud2 = {'donalod',23}
stud = stud1 | stud2
print(stud)

#intersection &
print(stud1 & stud2)

# difference (-) stud1 but not in stud2  and remove comman
print(stud1-stud2) # {'ssd', 'shivam'}

print(stud2-stud1)


#subset  and superset

course1 = {'java','php','pyhton','oracle','html'}
course2 = {'php','html'}

# subset
result = course1 <= course2   
print(result) # false

result1 = course2 <= course1 
print(result1) # true

# superset
result3 = course1 >= course2   
print(result3) # true

result4 = course2 >= course1 
print(result4) # false