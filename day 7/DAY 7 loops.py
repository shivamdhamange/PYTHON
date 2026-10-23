# loops
# used to iterate over a sequence
# list tuple string and range
# range function is used to generate a sequence of numbers

# range(start, stop, step)

# start default is 0
# step default is 1

# using for loop print "shhvam" 5 times

for i in range(5):
    print("shivam")
  
# print from 1 to 5  
for i in range(1,6):
    print(i)
    
# print odd no from 1 t 10 
for i in range(1,11):
    if(i % 2 != 0):
        print(i)
        
#print even no from 50 to 70
for i in range(50,70):
    if(i % 2 == 0):
        print(i)
   
  
'''reverse no printing'''   
# print 5 to 1
for i in range(5,0,-1):
    print(f'i : {i}')
    
    
# print even no fro m 10 to 0
for i in range(10,0,-2):
    print(f'i : {i}')
    
# accept the no and give the factorial

a = int(input('enter no'))
fact = 1
for i in range(1,a+1):
    fact = fact * i
    
print(f"factorial : {fact}")

# accept 5 subject marks using for loop and print total and percentage
total = 0
for i in range(5):
    marks = int(input("enetr marks"))
    total = total + marks

per = total/5
print(f"total = {total}")
print(f"percentage = {per}")

# write a program to accept no and print the table of the no

num = int(input("enter the no"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    

# to tal for first 5 natural no
sum = 0
for i in range(1,6):
    sum = sum + i
    
print(f"Sum : {sum}")

# print prime no from 1 to 100

for i in range(1,101):
    prime = True
    if(i<2):
        prime = False
    for j in range(2,i):
        if(i % j == 0):
            prime = False
            break
    if prime:
        print(f"{i} is prime no")
    else:
        print(f"{i} is not prime")
        
        
# interest calculate
principal = 1000
rate = 0.05
years = 4

print("Initial principal : ",principal)
for year in range(1,years+1):
    interest = principal * year
    principal += interest
    print(f"{year} principal :",principal)
