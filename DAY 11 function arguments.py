# arguments in function

# positional
# keyword

def add(n1,n2):
    return n1+n2

num1 = int(input("enter first"))
num2 = int(input("enter second"))
print(add(n2=num2,n1=num1))


# default

def sub(n1,n2=3):
    return n1-n2


num1 = int(input("enter first"))

print(sub(num1))

# contact details using defalut keyword
def contact(fullname,phonenumber,city="nagpur"):
    print("---contact details----")
    print(f"Full name : {fullname}")
    print(f"phone number : {phonenumber}")
    print(f"City : {city}")
    
    
fn = input("enter full name")
pn = input("enter phone number")

ch = input("do you want to enter city yes/no").lower()
if ch == "yes":
    city = input("enter city")
    contact(fn,pn,city)
else:
    contact(fn , pn)
    
    
# variable length arguments

'''accept arbitrary no of arguments

two types

 *args into a tuple
 ** kwargs  into a dictionary'''