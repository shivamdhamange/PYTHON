#while loop
i = 1
while i<=5 :
    print(i)
    i+=1
    
#factorial

while True:
    
    num = int(input("enter no"))
    fact = 1
    while num>0:
        fact = fact * num
        num -= 1
    print("factorial",fact)

    print("do you want to continue(yes/no)")
    ans = input().lower()
    
    if(ans == "no"):
        break
    