# importing the module named fibo
# function fib is accessed 
import fibo 
print(fibo.fib(1000))

# module is imported with different name
import fibo as fi
print(fi.fib(1000))

# Not importing whole module but importing some function
from fibo import fib, fib2
print(fib(1000))

# Importing a function with different name
from fibo import fib as fun
print(fun(1000))

# import all names that module defines
from fibo import *
print(fib(100))

"""
Please look at the fibo file to understand how module can be executed as a main file
"""



