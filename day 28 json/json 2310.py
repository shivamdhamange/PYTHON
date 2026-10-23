#Deserialization
'''

loads

'''


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


'''

load

'''

#reading json file to python dictionary object
with open('payment.json','r') as file:
    result = json.load(file)

print(type(result))
print("payment Details")
print(f"Id . : {result['id']}")
print(f"name . : {result['cust_name']}")
print(f"amount . : {result['amount']}")