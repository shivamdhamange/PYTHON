#accept password calc len, how many digits , how many special character, if valid password
password=input("enter password")
d=0
s=0
l=len(password)
special ="!@#$%"
print(f"lenght : {l}")
for p in password :
    if p.isdigit():
        d += 1
    if p in special:
        s += 1
print(f"digits : {d}")
print(f"special character : {s}")

if (l > 8 and d > 0 and s > 0) :
    print("password is valid")
else:
    print("password is not valid")
    
#accept no. of products
noprod = int(input("enter no. of products"))
total=0
gtotal=0
for i in range(1,noprod+1):
    print("---------------------------------")
    print(f"enter details for product :{i}")
    #accept productname, price and quantiy
    prodname=input("enter product name")
    price=float(input("enter product price"))
    quantity=int(input("enter product quantity"))
    total = price * quantity
    gtotal += total
    print(f"total amount : {total}")
    print("--------------------------------")
print(f"grant total amount :{gtotal}")