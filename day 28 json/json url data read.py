'''

EXAMPLE 1

'''

# reading api from a python program
import requests

# api url
url = "https://jsonplaceholder.typicode.com/users/6"

#send get request
response = requests.get(url)

# read json data
data = response.json()

# display data 

print(f"ID : {data['id']}")
print(f"Name : {data['name']}")
print(f"Email : {data['email']}")
print(f"City : {data['address']['city']}")



'''
EXAMPLE 2
'''
import requests
url1 = "https://fake-json-api.mock.beeceptor.com/users"

resp = requests.get(url1)

data1 = resp.json()

print(data1)
print(len(data1))

for i in range(10):
    # Display data
    print("---------------")
    print("ID:", data1[i]["id"])
    print("Name:", data1[i]["name"])
    print("company:", data1[i]["country"])
    print("---------------")

