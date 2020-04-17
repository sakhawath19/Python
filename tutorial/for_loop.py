squares = []

# normal for loop
for x in range(10):
    squares.append(x**2)

# use of lambda function
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# concise and clean
squares = [x**2 for x in range(10)] # mapped
print(squares)

squares = [x**2 for x in range(10) if x > 5] # filtered 
print(squares)

# comparing and combining multiple list 
a = [1, 2, 3]
b = [2, 4, 6]

comb = [(x, y) for x in a for y in b if x!=y] # created list of tuples
print(comb)
print(comb[1])

# flatteing the list
vec = [[1,2,3], [4,5,6], [7,8,9]]

vec = [num for elem in vec for num in elem] # OAWW
print(vec)








