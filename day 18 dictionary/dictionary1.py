# dictionary to store cureent user id name and role

currentUser = {'id':123,'name':'shivam','role':'admin'}
print(currentUser)

print('User details using [] brackets')
print(f"User Id : {currentUser['id']}")
print(f"Name : {currentUser['name']}")
print(f"Role : {currentUser['role']}")

print('user details using get method')
print(f"User Id : {currentUser.get('id')}")
print(f"Name : {currentUser.get('name')}")
print(f"Role : {currentUser.get('role')}")

# make a dictionary and add a set in it and then convert it to list and print it

d = {'name': 'shivam','age':20,'rn':{1,2}}

# set
s = d['rn']

#list
l = list(s)

print(l[0])
print(l[1])


'''Methods'''

my_dict = {'name':'shivam','age':20,'role':'admin'}

print('keys',my_dict.keys())
print('values',my_dict.values())
print('items',my_dict.items())

# get method get(key,'default')
print('get method',my_dict.get('name','None'))

# pop method delete the key
print('pop',my_dict.pop('name'))

print(my_dict)