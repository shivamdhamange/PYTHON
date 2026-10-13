#map function 

#one or more iteravbles are maped to the function   
#list and tuples are iterabeles


# map function returs one map object

# Example 1


res = lambda n : n*n
num = [1,2,3]

number = list(map(res,num))
print(number)


#    we can write it as 
#    number = list(map(lambda n : n*n ,num))


# Example 2


numbers1 = [1,2,3]
numbers2 = [4,5,6]

result = list(map(lambda x ,y : x+y,numbers1,numbers2))

print(result)