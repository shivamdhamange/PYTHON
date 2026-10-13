# create a empty dictionary

student = {}
print(type(student))

# create a dictionary to  store name , age and city

student = {'name': 'shivam','age': 20,'city':'nagpur'}
print(student)


# user input
n = input('enter name')
a = int(input('enter age'))
c = input('enter city')
student1 = {'name': n,'age': a,'city':c}
print(student1)


# add data to dictionary
#using key and value
student1['roll no']=56
print(student1)


# using constructor
stud = dict(name=n,age=a,city=c)
print(stud)


#accessing from dictionary using key and square brackets
print('student details : ')
print(f"name : {stud['name']}")
print(f"age : {stud['age']}")
print(f"city : {stud['city']}")

#print(f"age : {stud['age1']}")  key error
'''
# if key not present then it will through key error
# so we have get method  it will give none
'''

# accessing using get method
print('student details')
print(stud.get('name'))
print(stud.get('age'))
print(stud.get('city'))

# create a dictionary named products to store product_id product name 
# price and stock accept from user and store it in dictionary then display using brackets and get method

products = {'product_id':101,'product_name':'pen'}
print(products)


name = input('enter name of stock')
price = int(input('enter price'))
stock = {'name':name,'price':price}

print(stock)
print(stock.get('name'))