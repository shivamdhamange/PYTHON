names=[]
while True:
    print('1 - add a student')
    print('2 - display')
    print('3 - remove an student')
    print('4 - index  of an student')
    print('5 - exit')
    
    
    choice = int(input("enter choice"))
    if choice == 1:
        name = input("enter a name to add")
        names.append(name)
        print('student added successfully')
        
    elif choice == 2:
        print('Names that are added:\n')
        print(names)
        
    elif choice == 3:
        n = int(input('enter student name to remove'))
        names.remove(n)
        print('removed successfully')
    
    elif choice == 4:
        n = int(input('enter student name to find index'))
        ind = names.index(n)
        print('index is :',ind)
        
    elif choice == 5:
        print('Program exitted')
        break
    
    