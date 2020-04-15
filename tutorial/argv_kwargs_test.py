def fun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

argv = ("value", "is", 1)

fun(*argv)


def fun2(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


fun2(first="geeks", second="for", third="geeks")



def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "ks") 
myFun(*args) 
  
param = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Ges"} 
myFun(**param) 

# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))


# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# concatenate.py
def concatenate2(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs:
        result += arg
    return result

print(concatenate2(a="Real", b="Python", c="Is", d="Great", e="!"))

la = [1, 2, 3]
print(la)

print(*la)

l1 = [1, 2]
l2 = [3, 4]

print([l1, l2])
l3 = [*l1, *l2]
print(l3)

# order of the arguments
def my_function(a, b, *args, **kwargs):
    pass

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

# string to list
a = [*"RealPython"]
print(a)
