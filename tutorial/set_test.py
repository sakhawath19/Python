
# in set order is not important
example = set()

example.add(42)
example.add(False)
example.add(3.182818)
example.add("Thorium")

# set do not allow duplicate element
example.add(42)

print(example)

example.remove(42)

example.discard(42) # it does not return error if element is not present

print(example)

example2 = set([34, 43, 56, "hi"])

print(example2)
print(len(example2))

example2.clear()

print(example2)

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(composites.intersection(odds)) 

print(2 in composites)
print(2 in evens)
print(9 not in evens)

print(dir(evens))