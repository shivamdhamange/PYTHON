#Deserialization

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
