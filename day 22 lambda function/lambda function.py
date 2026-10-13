# lambda function a small anomynous function defined using lambda keyword

# lambda x,y : x+y

# argument comma separerated input parametres
# expression where result is returned


#example 1

add = lambda x,y : x+y
print(add(2,5))

# example 2

sub = lambda a,b : a-b
print(sub(5,2))

#example 3

n1 = int(input("enter no 1 : "))
n2 = int(input("enter no 2 : "))
mul = lambda c,d : c*d
print(mul(n1,n2))

# example 4
#square of a number

n3 = int(input("enter no: "))
sq = lambda n3 : n3**2
print(f"square of a no. : {sq(n3)}")

#example 5
#concatinate 2 strings
fullName = lambda fn,ln : fn + " " + ln
print(fullName("Shivam","Dhamange"))

#example 6
# even no check
even = lambda number : number%2 == 0
print(even(5))
print(even(2))


'''conditional expression'''
# greater of two no

result = lambda x,y : x if x>y else y
print(result(5,4))


# calculate length of string
l = lambda x : len(x)
print(l("shivam"))


# positive or negative
r = lambda x: "positive" if x>0 else "negative"
print(r(12))