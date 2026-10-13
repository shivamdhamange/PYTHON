# passing tuple to function

def calculate(m):
    print(type(m))
    sum = 0
    for i in m:
        sum+=i
    print("total marks",sum)
    
    
m1 = int(input("enter no1 "))
m2 = int(input("enter no2 "))
m3 = int(input("enter no3 "))
marks = (m1,m2,m3)
calculate(marks)

# variable length argumnets

def calculate(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum+=i
    print("total marks",sum)
    
    
m1 = int(input("enter no1 "))
m2 = int(input("enter no2 "))
m3 = int(input("enter no3 "))

calculate(m1,m2,m3)


# function returning a tuple

def calculate1(r):
    area = 3.14 * r * r
    circ = 2 * 3.14 * r
    ci = (area,circ)
    return ci

radius = int(input("enter radius"))
result = calculate1(radius)
print(f"area of circle : {result[0]}")
print(f"circumference of circle : {result[1]:.2f}")


''''method of tuple'''
age=(18,20,18,23,24,55)
l=len(age)
print(f"length :{l}")
for i in range(l):
   print(age[i])
num=int(input("enter age"))
c=age.count(num)
print(f"count of age {num} in tuple :{c}")
ind=age.index(num)
print(f"index of {num} is : {ind}")