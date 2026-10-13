students = []

while True:
    print("-------------------------------------")
    print('1 - add a student')
    print('2 - display')
    print('3 - search for a student')
    print('4 - delete student record')
    print('5 - exit')
    print("-------------------------------------")
    
    choice = int(input('enter your choice : '))
    
    print("-------------------------------------")
    
    if choice == 1:
        n = input('enter student name : ')
        r = int(input('enter student roll no : '))
        c = input('enter cource enrolled : ')
        stud = [n,r,c]
        students.append(stud)
        print('\nStudent added successfully')
        
    elif choice == 2:
        if len(students)==0:
            print('No Studemt data present')
        else:
            print('Student details are : ')
            for stu in students:
                print(f"Name : {stu[0]} , Roll No. : {stu[1]} , Course : {stu[2]}")
    
    elif choice == 3:
        search_roll = int(input('enter roll no to search : '))
        found = False
        for i in students:
            if i[1] == search_roll:
                found = True
                print('\nFound Student')
                print(f"Name : {i[0]} , Roll No. : {i[1]} , Course : {i[2]}")
        if found == False:
            print('\nStudent with roll no not found')
            
    elif choice == 4:
        n = int(input('enter student roll no to remove : '))
        foun = False
        for i in students:
            if i[1] == n:
                foun = True
                students.remove(i)
                print('\nStudent removed successfully')
        if foun == False:
            print('\nStudent with name not present')
            
    elif choice == 5:
        print("program exitted")
        break
    
    else:
        print('Invalid choice')