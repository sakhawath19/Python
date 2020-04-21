import sys
import fibo # created a python script with some function

# To set python path
# sys.path.append('/ufs/guido/lib/python')

"""dir() lists all types of names: variables, modules, functions, etc.
"""
# >>> dir(fibo)
# ['__name__', 'fib', 'fib2']

# >>> dir(sys)  
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
# >>> dir()
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

"""dir() does not list the names of built-in functions and variables. 
If you want a list of those, they are defined in the standard module builtins:
"""     
# >>> import builtins
# >>> dir(builtins)

import glob 
print(glob.glob('*.py'))

