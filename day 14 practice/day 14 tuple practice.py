print("question 1------------------------") 

revenue = (45000, 52000, 48000, 60000, 55000, 70000)
length = len(revenue)
lar = -1
smallest = 10000
total = 0
for i in revenue:
    total += i
    avg = total/length
    
    if i > lar:
        lar = i
    
    if smallest>i:
        smallest = i
        
print(lar)
print(smallest)
print(total)
print(avg)

print("question 2----------------")

ratings = (4, 5, 3, 5, 4, 2, 5, 3, 4, 5)
length = len(ratings)
print("length",length)
count = 0
largest = -1
smallest = 10000
sum1 = 0
for i in ratings:
    if i  == 5:
        count+=1
    if i>largest:
        largest = i
    if i<smallest:
        smallest = i
    sum1 += i

avg = sum1/length
print("5 star",count)
print("high",largest)
print("lowest",smallest)
print("average",avg)


print("question 3-------------------")

attendance = (92, 85, 76, 95, 88, 67, 91)
largest = -1
smallest = 10000
length = len(attendance)
sum1 = 0
for i in attendance:
    if i > largest:
        largest = i
    if i<smallest:
        smallest = i
    sum1 += i
    
avg = sum1/length
print(f"Highest attendance : {largest} \nLowest attendance : {smallest} \nAverage attendance : {avg} \nNumber of employees : {length}")


print("question 4----------------------")

products = (101, 105, 108, 112, 115, 120)

prod = int(input("enter product ID's"))

if prod in products:
    print("product found")
    print("Position: ",products.index(prod))
else:
    print("product not found")
    
    

print("question 5----------------------")


sales = (25000, 30000, 28000, 35000, 40000, 38000,
        45000, 42000, 50000, 48000, 55000, 60000)

print("First quater total :",sales[0]+sales[1]+sales[2])
print("second quater total :",sales[3]+sales[4]+sales[5])
print("third quater total :",sales[6]+sales[7]+sales[8])
print("fourth quater total :",sales[9]+sales[10]+sales[11])


print("question 6----------------------")

ages = (21, 35, 42, 28, 19, 55, 31, 47)


print("Youngest :",min(ages))
print("Oldest :",max(ages))
print("Average age :",sum(ages)/len(ages))
print("Total customers :",len(ages))


print("question 7----------------------")

sales = (25000, 45000, 38000, 52000, 60000)

s = int(input("enter the saales amount to search"))

if s in sales:
    print("sales amount found")
else:
    print("sales amount doesn't exist")
    
print("question 8----------------------")

ages = (25, 32, 28, -5, 41, 150, 35)

age = int(input("enter the age"))

if age in ages:
    print("age exists")
else:
    print("age not exists")
    
if age<0 :
    print("invalid age")
elif age>100:
    print("suspicious age")
else:
    print("valid age")
    
print("question 9----------------------")

transactions = (1200, 5000, 2500, 8000, 3500, 10000)

print("Total Transaction amount : ",sum(transactions))
print("Average Transaction amount : ",sum(transactions)/len(transactions))
print("highest Transaction amount : ",max(transactions))
print("lowest Transaction amount : ",min(transactions))
print("no of Transaction  : ",len(transactions))



print("question 10----------------------")
salary = (30000, 45000, 52000, 38000, 65000, 42000)

print("highest salary",max(salary))
print("lowest salary",min(salary))
print("average salary",sum(salary)/len(salary))
print("total salary",sum(salary))