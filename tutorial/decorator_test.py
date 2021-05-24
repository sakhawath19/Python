'''
# Function take funtions as arguments
def say_hello(name): 
    print(name)
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

greet_bob(say_hello)
greet_bob(be_awesome)



# Define a function inside another function 
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

# Function returning another function 
def parent_1(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent_1(1)

print(first)
print(first())
'''

'''
# Decorators are callable objects which are used to modify functions or classses 
# my_decorator took say_whee function as an argument and changed its behavior by 
# wrapper function 

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# my_decorator is actually returning a function named wrapper
# Actually we are calling wrpper function 
# In other ward we say decorate the say_whee function

my_decorator(say_whee)()

# call_say_whee is holding the wrapper function here
# it is also called function aliasing
# this line is not needed to decorate the function when we use @my_decorator before defining the say_whee
# look at the next example to understnad the whole idea 
call_say_whee = my_decorator(say_whee)

call_say_whee()

# When we want to call say_whee function, we want the functionality of my_decorator function
'''

'''
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        # val will hold the return value, val is not needed otherwise
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper

@f1
def f(a, b=3):
    print(a, b)

@f1
def add(x, y):
    return x + y

print(add(7, 2))
f(3,4)
'''

import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Execution time: ", time.time() - before, "seconds")

    return wrapper

@timer 
def fun():
    time.sleep(2)

fun()


# https://www.youtube.com/watch?v=r7Dtus7N4pI&ab_channel=KiteKite
