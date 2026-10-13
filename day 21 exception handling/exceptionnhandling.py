#Exception handling

'''error coming when you run the program is called Exception
'''
##########################################################################################
"""

EXAMPLE 1
ZERO DIVISION ERROR

"""



# exception
'''''''''n1 = 10
n2 = 0

result = n1/n2
print(result)'''''''''

'''when i run thge above program run timem eroor (exception) will come at line no 3

because n2 is zero so division byu zero error will come'''


'''ZeroDivisionError: division by zero'''


'''So exception handling mechanism will handle the error and program will successfully run till the end '''


'''in try block you will write the code where run time error will occur

'''


# handling the zero division error
try:
    n1 = 10
    n2 = 0
    result = n1/n2  #error will come if n2 will be zero
    print(f"Result : {result}")
except ZeroDivisionError as e:
    print(f"error : {e}")

print("Bye")



try:
    n1 = int(input("enter first no."))
    n2 = int(input("enter second no."))
    result = n1/n2  #error will come if n2 will be zero
    print(f"Result : {result}")
except ZeroDivisionError:
    print(f"Error : Cannot divide by zero")

print("Bye")


"""
so if we open a file if that file is not present then also error will come
"""

###############################################################################################
"""

EXAMPLE 2
INVALID INPUT ERROR

"""

try:
    age = int(input("enter your age : "))
    print(f"You are {age} years old")
except ValueError as e:
    print(f"Error : {e}")
    print("Invalid input")
    print("try again")

print("Bye")