print("QUestion no 1")
print("--------------------------------")

square = lambda x: x * x

print(square(5))
print(square(12))



print("QUestion no 2")
print("--------------------------------")

add = lambda a, b: a + b

max_of_two = lambda a, b: a if a > b else b

print(add(15, 27))
print(max_of_two(15, 27))


print("QUestion no 3")
print("--------------------------------")

nums = [1, 2, 3, 4, 5, 6]

new_nums = list(map(lambda x: x * 3, nums))

print("Original list:", nums)
print("New list:", new_nums)


print("QUestion no 4")
print("--------------------------------")

nums = [10, 15, 22, 33, 40, 51, 64]

# (a) Even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))

# (b) Numbers greater than 30
greater_nums = list(filter(lambda x: x > 30, nums))

print("Even numbers:", even_nums)
print("Numbers greater than 30:", greater_nums)



print("QUestion no 5")
print("--------------------------------")


students = [
    ("Ravi", 78),
    ("Anita", 92),
    ("Suresh", 65),
    ("Meena", 85)
]

# (a) Sort by marks in ascending order
ascending = sorted(students, key=lambda x: x[1])

# (b) Sort by marks in descending order
descending = sorted(students, key=lambda x: x[1], reverse=True)

# (c) Sort alphabetically by name
alphabetical = sorted(students, key=lambda x: x[0])

print("Ascending order:", ascending)
print("Descending order:", descending)
print("Alphabetical order:", alphabetical)