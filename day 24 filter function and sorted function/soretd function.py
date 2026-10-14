#the sorted function in python is used to sort an iterable and return a new iterable


#sorted(iterable ,key=None,reverse=True)


num = [11,23,1,3,10,9,7]

print(f"before sorting : {num}")

num.sort()

print(f"after sorting : {num}")


#it changes the original list

#but sorted creates a new list

# in ascending
num1 = [11,23,1,3,5,24,10,9,7]

print(f"before sorting : {num1}")

new = sorted(num1)

print(f"after sorting : {new}")


# in decending
num1 = [11,23,1,3,5,24,10,9,7]

print(f"before sorting : {num1}")

new = sorted(num1,reverse=True)

print(f"after sorting : {new}")



# sorting strings

words = ['shivam','harshit','sanjay']

sorted_words = sorted(words,reverse=True)
print(sorted_words)

# on length 
words = ['shivam','harshit','sanjay','ssd']

sorted_words = sorted(words, key = lambda x : len(x))
print(sorted_words)


# on length 
words = ['shivam','harshit','sanjay','ssd']

sorted_words = sorted(words, key = lambda x : len(x),reverse=True)
print(sorted_words)


# sort a dicitionary by specific key

people = [{"name":"shivam","age":23},{"name":"ssd","age":25},{"name":"bob","age":30}]
sorted_people = sorted(people , key = lambda x: x["age"])
print(sorted_people)
