# This module is created to test module 
# test is carried in module_test.py
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# if you wish to run fibo.py module you need this 
# it will parse the command line if it is executed as main file
# it can be executed as main file or can be imported
"""
This is often used either to provide a convenient user interface to a module, 
or for testing purposes (running the module as a script executes a test suite)
"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    fib(int(sys.argv[2]))
    print("Third argument", sys.argv[3])