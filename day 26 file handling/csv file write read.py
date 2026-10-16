#it convert python data to csv rows

# program to create a csv file and write the data into it

import csv

# create or open the csv file in write mode
'''
with open('student.csv','w',newline='') as file:   # you can give the path for it also where you want to create the csv file
    w = csv.writer(file)
    w.writerow(['Name','Age','Salary'])
    w.writerows([["shivam",24,35000],["mohini",22,30000],["Falguni",21,36000]])
    for i in range(3):
        n = input("enter name")
        a = int(input("enter age"))
        s = float(input("salary"))
        w.writerows([[n,a,s]])

print("file created successfully")

'''


# read a csv file

with open('student.csv','r',newline="") as file:
    read = csv.reader(file)

    for r in read:
        print(r)

        
    print('Student Details :')
    for r in read:
        print(f"Name : {r[0]} Age : {r[1]} Salary : {r[2]}")
