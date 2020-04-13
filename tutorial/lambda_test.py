
def greet(greetings, name):
    return f"{greetings} {name}" 

print(greet("Hello", "Sakha"))

# Filtering
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






