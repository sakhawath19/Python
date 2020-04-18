# https://dbader.org/blog/meaning-of-underscores-in-python

# Single Leading Underscore _var #
"""
Naming convention indicating a name is meant for internal use. 
Generally not enforced by the Python interpreter (except in wildcard imports) 
and meant as a hint to the programmer only.
"""
"""
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

>>> t = Test()
>>> t.foo
11
>>> t._bar
23

the leading single underscore in _bar did not prevent us from “reaching into” 
the class and accessing the value of that variable.
"""
# However, leading underscores do impact how names get imported from modules.
"""
# This is my_module.py:

def external_func():
    return 23

def _internal_func():
    return 42

Now if you use a wildcard import to import all names from the module

>>> from my_module import *
>>> external_func()
23
>>> _internal_func()
NameError: "name '_internal_func' is not defined"

Python will not import names with a leading underscore
(unless the module defines an __all__ list that overrides this behavior):
"""

# Single Trailing Underscore var_ # 
"""
Used by convention to avoid naming conflicts with Python keywords.
When you want to have a variable which conflicts with keyword.
"""
"""
>>> def make_object(name, class):
SyntaxError: "invalid syntax"

>>> def make_object(name, class_):
...     pass
"""

# Double Leading Underscore __var # 
""" 
Triggers name mangling when used in a class context. Enforced by the Python interpreter.
the interpreter changes the name of the variable in a way that makes it harder to create collisions 
when the class is extended later.
"""
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23
t = Test()

print(dir(t))

"""
If you look closely you’ll see there’s an attribute called _Test__baz on this object.
This is the name mangling that the Python interpreter applies.
It does this to protect the variable from getting overridden in subclasses.

Let’s create another class that extends the Test class and attempts to override its existing attributes
added in the constructor:
"""

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

"""
>>> t2 = ExtendedTest()
>>> t2.foo
'overridden'
>>> t2._bar
'overridden'
>>> t2.__baz
AttributeError: "'ExtendedTest' object has no attribute '__baz'"
>>> dir(t2)
'_ExtendedTest__baz'
"""

# Double Leading and Trailing Underscore __var__ # 
"""
Indicates special methods defined by the Python language. Avoid this naming scheme for your own attributes.
However, names that have both leading and trailing double underscores are reserved for special use in the language. 
This rule covers things like __init__ for object constructors, or __call__ to make an object callable.

These dunder methods are often referred to as magic methods.
"""             


# Single Underscore _ #
"""
Sometimes used as a name for temporary or insignificant variables (“don’t care”). 
Also: The result of the last expression in a Python REPL.
"""
for _ in range(3):
    print('Hello, World.')

car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color)

"""
in python interpreter
>>> 20 + 3
>>> _
23
>>> print(_)
23

>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _.append(3)
>>> _
[1, 2, 3]
"""

