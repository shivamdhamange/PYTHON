# accept age and print eligible or not
age = int(input("enter the age :"))
if(age>=18):
    print("eligible")
else:
    print("not eligible")
    
# using elif 

n1  = int(input("enter n1 :"))
n2  = int(input("enter n2 :"))
n3  = int(input("enter n3 :"))

if(n1>n2 and n1>n3):
    print("n1 is greater")
elif(n2>n3):
    print("n2 is greater")
else:
    print("n3 is greater")
    
'''
if(n1>n2):
    if(n1>n3):
        print("n1 is greater")
    else:
        print("n3 is grater")
else:
    if(n2>n3):
        print("n2 is greater")
'''

#accept three subject marks and print percentage and grade
m1 = int(input("enter marks of maths : "))
m2 = int(input("enter marks of science : "))
m3 = int(input("enter marks of sst : "))

percentage = ((m1+m2+m3) / 300) * 100
print(percentage)

if(percentage>90):
    print("grade A")
elif(percentage>80):
    print("grade B")
else:
    print("fail")
'''
## important  
# here we have used .2f 
print(f"percentage  : {percentage : .2f}")

per = 12.5663782673
print(format(per,".2f"))

print("%.2f" % per)
'''


# acceprt no and print positive negative or zero
num = int(input("enter the no : "))
if(num > 0):
    print(num , "is positive")
elif(num<0):
    print(num , "is negative")
else:
    print(num , "is zero")
    
    
# accept user name and check if equal to admin print login successfull

user = input("enter user name : ")
password = input("enter password : ")
if(user == "admin"):
    if(password == "admin123"):
        print("login successfull")
    else:
        print("invalid password")
else:
    print("invalid username")
    
# delivery charges over bill amount
# bill amount > 1000 free
# bill amount >500 50
# bill amoiunt > 100 100

bill_Amount = int(input("enter bill amount: "))
delivery_charge = 0

if(bill_Amount>1000):
    delivery_charge = 0
elif(bill_Amount>500):
    delivery_charge = 50
else:
    delivery_charge = 100

print("delivery charge : ",delivery_charge)
