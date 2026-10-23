# even odd

num = int(input("enter the no:"))

if(num % 2 == 0):
    print("even no")
else:
    print("odd no")
    
    
# positive negative zero

n = int(input("enter no :"))

if(n>0):
    print("positive")
elif(n<0):
    print("negative")
else:
    print("zero")
    
#largest of two no
n1 = int(input("enter no1 :"))
n2 = int(input("enter no2 :"))

if(n1>n2):
    print(" n1 is greater than n2")
elif(n2>n1):
    print("n2 greater than n1")
else:
    print("both are equal")

#Pass or Fail

n3 = int(input("eneter marks"))
if(n3>40):
    print("pass")
else:
    print("fail")
    
# day of the week

day = int(input("enter the day no"))
if day == 1 :
    print("monday")
elif day == 2 :
    print("tuesday")
elif day == 3:
    print("wed")
elif day == 4 :
    print("thru")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("invalid")
    
'''Simple Calculator (Basic)
Situation:
Take two numbers and an operator (+, -, *, /) and perform the calculation.
'''
a = int(input("eneter first"))
b = int(input("eneter seconfd"))

opr = input("eneter operator")

if(opr == "+"):
    print("result :",a+b)
elif(opr == "-"):
    print("result :", a-b)
elif(opr == "*"):
    print("result :",a*b)
elif(opr == "/"):
    print("result :",a/b)
else:
    print("invalid")
    
   # caharcetere check vowwl or not 
t = input("enter the caharacter : ")

if t in "aeiouAEIOU":
    print("vowel")
else:
    print("consonent")

'''1. Temperature Check
Situation:
Check the temperature and give advice:'''

temp = int(input("enter temp"))

if(temp<10):
    print("very cold")
elif(temp<20):
    print("cold")
elif(temp<30):
    print("pleasant")
else:
    print("hot")
    
'''
2. Discount on Shopping
Situation:
A shop gives discount based on bill amount:
'''

bill = int(input("eneter bill"))

if(bill<1000):
    discount = 0
elif(bill<5000):
    discount = bill * 0.05
else:
    discount = bill * 0.10
    
final = bill - discount

print(final)

'''3. Driving Eligibility
Situation:
Check if a person can drive:

Age < 18 → Cannot drive
Age 18–60 → Can drive
Age > 60 → Can drive but with caution'''

age = int(input("eneter age"))

if(age<18):
    print("cannot drive")
elif(age<60):
    print("can drive")
else:
    print("Can drive but with caution")
    
    
'''
4. Number Divisible by 3 and 5
Situation:
Check if a number is divisible by both 3 and 5, only by 3, only by 5, or by neither.
Solution:
'''

number = int(input("enter no "))

if number % 3 == 0 and number % 5 == 0:
    print("divisble by both")
elif number % 3 == 0:
    print("divisible by 3") 
elif number % 5 == 0:
    print("divisible by 5")
else:
    print("neither divisble")
    
    
'''
5. Simple Interest Rate
Situation:
Bank gives interest based on years:

Less than 1 year → 5%
1 to 3 years → 7%
More than 3 years → 10%'''

years = int(input("enter years"))

if(years<1):
    print("rate 5%")
elif(years<3):
    print("rate 7%")
else:
    print("rate 10%")
    
'''
6. Character Type Checker
Situation:
Check whether the entered character is:

Uppercase letter
Lowercase letter
Digit
Special character
'''

ch = input("enter character")

if (ch.islower()):
    print("lowercase")
elif(ch.isupper()):
    print("uppercase")
elif(ch.isdigit()):
    print("digit")
else:
    print("special character")
    
'''
4. Customer Segment (Data Analyst Style)
Situation:
Classify customers based on total spend:

Spend ≥ 50000 → Premium
Spend ≥ 20000 → Gold
Spend ≥ 5000 → Silver
Below 5000 → Bronze
'''

spend = int(input("eneter customer spend"))

if(spend>=50000):
    print("Presmium")
elif(spend>=20000):
    print("gold")
elif(spend>5000):
    print("silver")
else:
    print("bronze")
    
'''5. Leap Year Checker
Situation:
A year is a leap year if:

Divisible by 4, and
If divisible by 100, it must also be divisible by 400.
'''

years = int(input("eneter years"))

if(years % 400 == 0):
    print("leap year")
elif(years % 100 == 0):
    print("not leap")
elif(years % 4 == 0):
    print("leap year")
else:
    print("not leap")
    
