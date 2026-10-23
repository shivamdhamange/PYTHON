# function 

# def function_name():
#    code
#    return

# create the function display to print("hello from itp")

def display():
    print("hello from itp")
    
print("calling the display function")
display()

print("calling the display function again")
display()


# function to square the number

def square(num):
    s = num * num
    return s

num = int(input("enter the no. to square it"))
result = square(num)

print(f"square of the no is : {result}")

# function to print factorial of the number

def factorial(n):
    fact = 1
    while n>0:
        fact = fact * n
        n-=1
    return fact

n = int(input("enter the no to do factorial"))
res = factorial(n)

print(f"factorial of no is : {res}")


# create a function calculate with 3 pareamter to accept 2 no and 1 operator

def calculate(n1,n2,op):
    if op == "+":
        print(f"result : {n1+n2}")
    elif op == "-":
        print(f"result : {n1-n2}")
    elif op == "*":
        print(f"result : {n1*n2}")
    elif op == "/":
        print(f"result : {n1/n2}")
    else:
        print("Invalid Operator")

num1 = int(input("enter no. 1 : "))
num2 = int(input("enter no. 2 : "))
operator = input("enter operator(+,-,*,/)")
calculate(num1,num2,operator)


# function to check username and password

u = input("enter username")
p = input("enter password")

def check(u,p):
    if u == "admin" and p == "admin":
        print("login successfull")
    else:
        print("Invalid username or password")
    
check(u,p)


# 3 subject marks and calculate total percentage and grade 



def calculate1(m1,m2,m3):
    total = m1+m2+m3
    print(f"total : {total}")
    percen = total/3
    print(f"percentage : {percen}")
    if(percen>=90):
        print('Grade A')
    elif percen>=80:
        print('Grade B')
    elif percen>=70:
        print('Grade C')
    elif percen>=40:
        print('Grade D')
    else:
        print("fail")
        
        
m1 = int(input("enter the marks of 1st subject"))
m2 = int(input("enter the marks of 2nd subject"))
m3 = int(input("enter the marks of 3rd subject"))

calculate1(m1,m2,m3)


# function to caluculate bill amount based on unit consumed

unit = int(input("enter the units consumed"))

def bill(unit):
    rate = 0
    if unit>300:
        rate = 15
    elif unit>101 and unit<300:
        rate = 12
    elif unit<101:
        rate = 8
    
    calculate_bill = unit*rate
    return calculate_bill

billl=bill(unit)
print(f"Total bill : {billl}")