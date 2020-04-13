""" This script is written to understand lambda function """
""" Filter, map and reduce function used to understand lambda function """
""" Filter, map and reduce is highly used for lambda function """

import functools

'''
At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console
'''
li = [1, 2, 3, 4, 5, 6, 7]
print("The sum of the tolatl list:",\
    functools.reduce((lambda a, b: a if a > b else b), li))

# map will return value [True, False, True]
a = [1, 2, 3, 4, 5, 6, 7]
maped = map (lambda x: x % 2 == 0, a)  
print(maped) # it will return object
print(list(maped))

# Filtering
# Filter will return parameter [1, 3, 5, 7]
li = [1, 2, 3, 4, 5, 6, 7]

filtered_list= list(filter(lambda x: (x % 2 != 0), li))

print(filtered_list)

# substituting the argument 2 for x
print((lambda x: x)(2))

# lambda function with one argument
x = lambda a: a + 10
print(x(5))

# lambda function with two arguments
y = lambda a, b: a * b
print(y(2, 3))

# lambda function with three arguments
z = lambda a, b, c: a + b + c
print(z(2, 3, 4))






