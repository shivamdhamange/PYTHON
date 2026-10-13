patient = {'id':101,'name':'shivam','brother':'harshit'}
p1 = patient.popitem()
# return last key value and delete it
print('pop iten',p1)
print('after removing',patient)


# updat`e`
patient = {'id':101,'name':'shivam','brother':'harshit'}
patient.update({'course':'http'})

print(patient)



# add student anme and id to dct

student = {}

sid = int(input('enter student is: '))
student['id']=sid


sname = input('enter student name: ')
student['name']=sname

print('patient details')

print(f"id : {student['id']} , name : {student['name']}")

print('enter key to update')
val = int(input('enter value'))
student.update({"id":val})
print(student)