'''-------------------------------------------------------------------------------------'''

'''String Manipulation'''

# concatination : Join two string
# Repetation : repeat string

# 1 Concatination

fn = input("enter first name")
ln = input("enter second name")

fullname = fn + " " + ln
print(fullname)


# 2 Repetation

'''example 1'''
name = "shivam "
print(name * 3)

'''example 2'''
print("-" * 50)
print("Customer Details")
print("-" * 50)


'''-------------------------------------------------------------------------------------'''

'''String indexing and slicing'''

'''indexing'''

# left indexing start with 0
# right indexing start with -1

lang = "Python"
l = len(lang)
print(l)
for s in range(l):
    print(lang[s])


'''slicing'''
# string[start:end:step]

str = "shivam"
print(str[0:2])
print(str[2:4])
print(str[:4:2])
print(str[::2])  #hole string with keeping 2 gap\

print(str[::-1])


# example of revcrese of a string using a loop

s = "falguni"
reverse = ""
for i in s:
    reverse = i + reverse
print(f"Original String : {s}")
print(f"Reverse String : {reverse}")


#count the character e

t = "helloeollh"
count = 0
for i in t:
    if i == 'e':
        count = count + 1

print(count)

#print no of vowels in above string

c = 0
for i in t:
    if i in "aeiou":
        c = c + 1

print(c)