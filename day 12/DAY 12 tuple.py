# tuple -- immutable , orderedd collection of data , store differnt data types

# it cannot be modified or edited after it is created

# denoted by ()

#empty tuple
empty_tuple = ()

num7 = (1,"hello",2,3,True)
print(type(num7))

print(num7[0])

for i in num7:
    print(i)
    
"""important   single element tuple"""


num1 = (11)
print(type(num1)) # give type as integer 

# if we want a single in tuple we have to use ,
num2 = (11,)
print(type(num2))


"""implicit way to declare tuple"""
# without using ()
num3 = 1,2,34,True
print(type(num3))
for i in num3:
    print(i)
   
   
    
"""indexing in tuple"""

'''  1,2,3,5,7   tuple
 0, 1, 2,  3, 4    positive indexing
-5,-4,-3,-2,-1      negative indexing     
'''


num=(1,2,3,4,5)
print(num)
print(num[1:4])
print(num[:3])
print(num[3:])
print(num[::2])
print(num[::-2])  
print(num[::-1])   # used for reversing