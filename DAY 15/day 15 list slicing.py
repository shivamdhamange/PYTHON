month = ['jan','feb','march','april','may','june','july']


#[start:end:step]

print(month[1:4])
print(month[:4])
print(month[3:])
print(month[0:6:2])
print(month[::2])
# reverse a list
print(month[::-1])


# methods in list

# append -- add data at the end of list  append(x)

num = [1,2,3,4,5,6]

num.append(7)
print(num)

# insert -- add element at specific position

num.insert(1,6)
print(num)

# remove -- remove specific value

num.remove(5)
print(num)

# pop -- remove value using index
num.pop(3)
print(num)

# sort -- sort in ascending

num.sort()
print(num)

num.sort(reverse=True)
print(num)


# reveresse

num.reverse()
print(num)

# len()
l=len(num)
print(l)


# extend()
name = ['shivam','harshit']
print('list of names')
print(name)

name2 = [23,67,78]
name.extend(name2)
print('name after extending')
print(name)