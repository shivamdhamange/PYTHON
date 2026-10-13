'''syntax
filter(function,iterable)'''


#filter object returns
#filter even no from numbers
numbers = [1,2,3,4,5,6]

result = list(filter(lambda x : x%2==0,numbers))

print(result)