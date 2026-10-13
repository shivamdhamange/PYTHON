# match -> switch case
"""
match expression:
    case pattern1:
        #code
    case pattern2:
        #code
    case_:
        #code
        
"""


# accept daynumber and  print day name

"""dayno = int(input("enter day no(1-7)"))
match dayno:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("invalid input")"""
        
        
"""monthno = int(input("enter day no(1-12)"))
match monthno:
    case 1:
        print("january")
    case 2:
        print("feb")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("jun")
    case 7:
        print("july")
    case 8:
        print("aug")
    case 9:
        print("sep")
    case 10:
        print("oct")
    case 11:
        print("nov")
    case 12:
        print("dec")
    case _:
        print("invalid input")"""
   
   
"""# progran to check vowel or not     
ch = input("enter charcter")

match ch:
    case 'a' |'e'|'i'|'o'|'u' :
        print("vowel")
    case _:
        print("not vowel")"""
        

"""# take two input and one operator and give result

n1 = int(input("no 1"))
n2 = int(input("no 2"))

op = input("enter operator")

match op:
    case '+':
        print(n1+n2)
    case '-':
        print(n1-n2)
    case '*':
        print(n1*n2)
    case '/':
        print(n1/n2)
    case _:
        print("not a valid operator")"""
        
        
#grade evaluator with guard conditions(if)
"""
# accep score and print grade using grade evaluator

score = int(input("enter score"))

match score:
    case s if s>=90 and s<100:
        print("grade a")
    case s if s>=80:
        print("grade b")
    case s if s>=70:
        print("grade c")
    case s if s>=60:
        print("grade d")
    case s if s>0:
        print("fail")
    case _:
        print("invalid score")
        
"""

"""# program to accept age and print old young and child

age = int(input("enter age"))

match age:
    case s if s>=60:
        print("old")
    case s if s>=18 and s<60:
        print("young")
    case _:
        print("child")"""
        
"""#program to accept sales_amount and print wheather eligible to get discount or not

sales_amount = int(input("eneter sales amount"))
if sales_amount >= 10000:
    print("Eligible for discount")
else:
    print("Not eligible for discount")
"""

