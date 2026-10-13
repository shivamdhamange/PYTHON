# to edit the tuple we need  to unpack it and then edit and then convert it to tuple

def process(a,b):
    a1,a2= a #unpacking the tuple
    b1,b2 = b # unpacking the tuple
    a1 = 'abc1'
    a2 = 'abc2'
    b1 = 0.1
    b2 = 0.2
    return (a1,a2),(b1,b2)

a = ('abc','bbc')
b = (0.0,0.0)

a,b = process(a,b) # passing the tuple
for i in a :
    print(i)
for j in b:
    print(j)