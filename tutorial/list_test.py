

# List can be declared in both ways
example = list()
example = []

example = [2 ,3, 5, 7, 11, 13]
print(example)

# List is mutable. Value can be added
example.append(17)
print(example)

# List indexing
print("Value of index zero:", example[0])

print("Index 2 to 5 printed:", example[2:5])

print(example[-1])

# List can take any type of object
example2 = [122, True, "Alpha", 3.23, [3, False]]
print(example2)

# List can contain any complex objects like functions classes and modules
import math
def foo():
    pass
comp_list = [int, len, foo, math]
print(comp_list)

numbers = [2, 3, 4]
letters = ['a', 'b', 'c']

print(numbers+letters)

# List can be nested
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x)
print(x[2])

print(x[1][1][0]) # Accessing sublist

# List must be concatenated by another list
# a list must be concatenated with an object that is iterable
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a += ['grault', 'garply']
print(a)

a += [20] # a += 20 or a += 'cor' would not work 
print(a)

# Useful funtion 
a = ['a', 'b']
a.append(123)
print(a)

a.extend([345]) # extend expects iterable object so argument with values would not work
print(a)

a.insert(3, 3.14159) # reamaining list elements are pushed back
print(a[3])

a.remove(345) # if element is present it will be removed otherwise will throw error

a.pop # it removes the last item # index also can be defined 

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[2:3] = []
del a[0] 
print(a) # After deleting element list will be automatically shrinked

