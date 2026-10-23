#variable type can be changed during execution by assigning a new value of a different type
num = 20
print(type(num))
num = 20.6
print(type(num))
num = "hello"
print(type(num))

# declare multiple variable in python in single line
a,b,c = 1, 2 ,3

#format string function
print(f"num1 : {a}, num2 : {b} , num3 : {c}")

# change the type of a variable
n1 = "34"
n2 = "12"

result = int(n1) + int(n2)
print(f"result : {result}")

# coverting input to boolean 
# eg for yes/no questions

is_student = input("are you a student ? (yes/no): ").lower() == "yes"
print("Student status : " , is_student)


# bool input

is_active = bool(input("enter true or false : "))
print(is_active)

# multiple input using , 
x,y = input("enter two no (sepearted by comma): ").split(",")
print(f"value of x : {x} , value of y : {y}")

# program to accept len and bredth in same line and print area

l,b = input("enter length and bredth(separated by ,)").split(",")
area = int(l) * int(b) 
print(f"area : {area}")


#program to accept five subject marks in same ;line and print total and percent
a,s,d,f,g =input("enter five subject marks sepaprated by , ").split(",")
total = int(a)+int(s)+int(d)+int(f)+int(g)
percent = total/5
print(total)
print(percent)


