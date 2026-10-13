import bankday2  # bank is user defined module whare it contains bal variable and three function

# deposited
amount = int(input("enter amount to be deposited: "))
result = bankday2.deposit(amount)
print(result)

#withdraw
amount1 = int(input("enter amount to be withdraw: "))
result1 = bankday2.withdraw(amount1)
print(result1)



#####          ---------------same using class --------------------------------------


# creating object
s = bankday2.Saving()

amount = int(input("enter amount to be deposited: "))
print(s.depositl(amount))

amount1 = int(input("enter amount to be withdraw: "))
print(s.withdrawl(amount1))




'''we can call deposit withdraw seperately'''
'''
from bankday2 import Saving'''


'''impoorting modules as alias'''

'''from bankday2 import Saving as s'''

