names=[]
while True:
    print('1 - add a student')
    print('2 - display')
    print('3 - remove an student')
    print('4 - exit')
    
    
    choice = int(input("enter choice"))
    if choice == 1:
        name = input("enter a name to add")
        r = int(input('roll no of student'))
        c = input('cource enrolled')
        
        stud =[name,r,c]
        names.append(stud)
        print('student added successfully')
        
    elif choice == 2:
        print('Students that are added:\n')
        print(names)
        
    elif choice == 3:
        n = input('enter student name to remove')
        for i in names:
            if i[0] == n:
                names.remove(i)
                print('removed successfully')
            else:
                print('student with name not present')
        
    elif choice == 4:
        print('Program exitted')
        break
    
    