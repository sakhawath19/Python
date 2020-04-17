import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

# creating group of optional argument which are mutually exclusive. So you can not use both at the same time
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-p", "--play", action="store_true")
group2.add_argument("-n", "-noplay", action="store_true")

parser.add_argument("x", type=int, help="the base") # positional argument, you have to provide value
parser.add_argument("y", type=int, help="the exponent") # positional argument, you have to provide value

# action count, explained more in next example
parser.add_argument("-a", "--count_verbose", action="count", default=0) # optional argument, it will count verbosity

# choises of the argument could be added
parser.add_argument("-c", "--choice", type=int,
                    choices=[1, 2, 3], help="increase output verbosity")

args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equal {answer}")
else:
    print(f"{args.x}^{args.x} == {answer}")

# Run the code
# python .\argparse_test.py --help 
# It will give
# usage: argparse_test.py [-h] [-v | -q] x y
# we can either use -v or -q

'''
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("b", type=int, help="the base")

parser.add_argument("x", type=int, help="the exponent")

# count action will take consideration of number of verbosity
# It works similar to action_true
# It does not accept any value
# “count”, to count the number of occurrences of a specific optional arguments

parser.add_argument("-v", "--verbosity", action="count", default=0)

args = parser.parse_args()

answer = args.b**args.x

if args.verbosity >= 2:
    print(f"Running {__file__}")

if args.verbosity >= 1:
    print(f"{args.b}^{args.x}"),
    print(answer)

# Run the program
# $ python argparse_test.py 2 3 -vv # counts verbosity 2
# $ python argparse_test.py 2 3 -vvv # counts verbosity 3
# $ python argparse_test.py 2 3 -v 1
'''
'''
import argparse 

parser = argparse.ArgumentParser()

# Positional argument
parser.add_argument("int_val", type=int, help="insert an integer")

# Optional argument with choises
# choises of the argument could be added
parser.add_argument("-v", "--verbose", type=int,
                    choices=[1, 2, 3], help="increase output verbosity")

args = parser.parse_args()

if args.verbose==1:
    print(f"Sorry! I will not print square of the value: {args.int_val}")
elif args.verbose==2: 
    print(f"Square of the value {args.int_val} is {args.int_val**2}") 
else:
    print(f"Square of the value {args.int_val} is {args.int_val**2}") 

'''

'''
import argparse 

parser = argparse.ArgumentParser()

# optional argument --verbose is defined as -v
# the state of the argument is stored true. If you add any value, it will show an error
# need to call optional argument -v to make its action true

parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

args = parser.parse_args()

if args.verbose:
    print("verbose turned on")

# $ python argparse_test.py --help # observe how help message is showing optional arguments
# $ python argparse_test.py -v 1 # it will show error. It does not requrire any value. It is used as a flag
# $ python argparse_test.py -v # it whill show verbosity turned on
'''


'''
import argparse 

parser = argparse.ArgumentParser()

# --verbosity is a optional argument
# if you specify value on it, it will display verbosity turned on
# if you do not specify value on it, it will not display anything
parser.add_argument("--verbosity", help="increase output verbosity")

args = parser.parse_args()

if args.verbosity:
    print("verbosity turned on")

# Run the code
# $ python argparse_test.py --help # it will show that verbosity is an optional argument
# $ python argparse_test.py --verbosity 1 # it will print verbosity turned on
# $ python argparse_test.py # it will do nothing, and will not ask for verbosity value
'''


'''
# All the code below this line used positional arguments
import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("int_val", help="Give an integer value", type=int) # type of argument is defined explicitly

arg = parser.parse_args()

print(f"Square of the integer, {arg.int_val} is {arg.int_val**2}")
'''

'''
# Parsing multiple arguments
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("msg1", help="Write first message") # Argument is taken as a string

parser.add_argument("msg2", help="Write second message")

args = parser.parse_args()

print(f"first argument {args.msg1}. Second argument {args.msg2}.")

# Run the code
# $ python argparse_test.py say hello
'''

'''
import argparse

parser = argparse.ArgumentParser() # created an object of argument parser # msg is a positional argument

parser.add_argument("msg", help="echo the string you use here") # msg will receive value from command line

args = parser.parse_args() # args will track all the given argument

print(args.msg)

# Run the code 
# $ python argparse_test.py hi # output will be hi
'''


'''
import argparse 

parser = argparse.ArgumentParser(description="Testing")
parser.parse_args()
# Run this code 
# $ python argparse_test --help
# See what happens
'''