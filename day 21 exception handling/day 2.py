#7/10/26
# try except and finally and else

# raise




try:
    n1 = int(input("enter first no"))
    n2 = int(input("enter second no"))
    print(n1/n2)
except ZeroDivisionError as e:
    print("division by zero not posibble")
except ValueError as e:
    print("you entered alphabet")
    
else:
    print("elsee block exceute when error doesnt come")
finally:
    print("finnally block exceute every time")



############################################################################
'''
index error
'''

fruits = ["apple",'banana','cherrry']

try:
    print(fruits[0])
    print(fruits[3])
except IndexError as e:
    print(f"Error : {e}")


#########################################################
'''
key error
'''

student = {"name": "john","age":20}

try:
    print(student["name"])
    print(student["age1"])
except KeyError as e:
    print(f"Error : {e}")



##############################################################################

'''
Exception mother class
'''
try:
    result = 10/int(input("eneter a number: "))
    print(result)
except Exception as e:
    print(f"An unexpeted error occured : {e}")


##############################################################################
try:
    age = int(input("enter yourr age : "))
    if age <18:
        raise ValueError('age should be greater than 17')
    print(f"age : {age}")
except ValueError as e:
    print(e)

###########################################################################

try:
    bill = int(input("enter bill amount"))

    if bill < 0:
        raise ValueError("bill amount should be greater than 0")

except ValueError as e:
    print(e)

else:
    print(f"Bill amount : {bill}")


#######################################################################################
class NegativeNumberError(Exception):
    pass


try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    print(f"You entered: {num}")
    
except NegativeNumberError as nne:
    print("Error:", nne)

except ValueError:
    print("Please enter a valid number!")