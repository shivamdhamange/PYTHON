# 9/10/2026   revision

# accept bill deatails

#  Example 1
# value error
try:
    cust_name = input("enter your name : ")
    amount = float(input("enter bill amount : "))
except ValueError as e: # this block will excecute if exceptio noccurs
    print(f"Error : {e}")
    amount = float(input("enter bill amount : "))
except Exception as e:
    print(f"Error : {e}")
else:  # this will exceute if there is no exception
    print("--------details------------")
    print(f"Custumer name : {cust_name}")
    print(f"bill amount : {amount}")
finally: # execute every time
    print("-----Thank you for purchasing -------")





#  Example 2
# string conversion error
try:
    cust_name = input("enter your name : ")
    amount = float(input("enter bill amount : "))
    discount = "20"   # str
    amount = amount - discount
except ValueError as e: # this block will excecute if exceptio noccurs
    print(f"Error : {e}")
    #amount = float(input("enter bill amount : "))
except Exception as e:
    print(f"Error : {e}")
    amount = amount - float(discount)
else:  # this will exceute if there is no exception
    pass
finally: # execute every time
    print("--------details------------")
    print(f"Custumer name : {cust_name}")
    print(f"bill amount : {amount}")
    print("-----Thank you for purchasing -------")


'''---------------------RAISE ----------------------------------------'''
#  Example 3 RAISE
# string conversion error
try:
    cust_name = input("enter your name : ")
    amount = float(input("enter bill amount : "))
    if amount<0:
        raise Exception("amount cannot be less than zero")
    discount = "20"   # str
    amount = amount - discount
except ValueError as e: # this block will excecute if exceptio noccurs
    print(f"Error : {e}")
    #amount = float(input("enter bill amount : "))
except Exception as e:
    print(f"Error : {e}")
    amount = float(input("enter bill amount : "))
    amount = amount - float(discount)
else:  # this will exceute if there is no exception
    pass
finally: # execute every time
    print("--------details------------")
    print(f"Custumer name : {cust_name}")
    print(f"bill amount : {amount}")
    print("-----Thank you for purchasing -------")
