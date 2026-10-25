# JSON  - java script object notation   store and exchange data

# key value pair
'''{
      "name": "shivam"
      "age" : 34
}'''
#json module

'''load and loads

dump and dumps'''

'''
json.dump(obj.file)  ---write python object to file as json
json.dumps(obj) ---- covert pytjon object to json string 
json.load(file) ---- read json  frorm file   ---  python object
json.loads(string) --- parse jsonstring --- python object


'''
'''
1 . serialization

convert to json String'''


import json
# creating a dictionary object to store payment details
payment = {'id':1,'cust_name':'amit','amount':120.34}

# coverting python dictionary object to json string
jp = json.dumps(payment,indent=4)

# print
print("json payment details")
print(jp)




'''json.dump()  -- object ---- file
'''


import json

# creating a dictionary object to store payment details

payment = {'id':1,'cust_name':'amit','amount':120.34}


with open('payment.json','w') as file:
    json.dump(payment,file)

# print
print("json file created")


'''
2 . deserialization

json to object'''


import json
with open('payment.json','r') as file:
	result = json.load(file)
# load is used to convert json file into pyhton dictionary
print(result)




'''json string to python dictionary object'''
import json

# declaring a json string using '''

json_string = '''
{
    "rno" : 102,
    "name" : "Bob",
    "totalmarks" : 472
}'''

#converting json string to python dictionary object

data = json.loads(json_string)
print(type(data))

print("Student Details")
print(f"roll no . : {data['rno']}")
print(f"name . : {data['name']}")
print(f"total marks . : {data['totalmarks']}")
