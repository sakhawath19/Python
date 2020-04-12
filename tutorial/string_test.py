import math

table = {'Sjoerd': 4127, 
        'Jack': 4098, 
        'Dcab': 7678}

for name, phone in table.items():
    print(f"{name:10}==>{phone:10d}")

# Formatted string
print(f"The value of pi is approximately {math.pi:.3f}.")
print("......................................")

# Formatted String Literals or f-string
year = 1971
event = "liberation"

print(f"We won the {event} war in {year}")
print("......................................")

# To define string single quote, double qutoe or double quote three times can be used
message1 = 'Apostrophe can be used for string'
print(message1)
print("......................................")

message2 = 'I\'m: to print single quote back slash required. But with the double quotation marks this problem can be solved'
print(message2)
print("......................................")

message3 = "I'm using double quotation marks. Now we do not need back slash"
print(message3)
print("......................................")

message4 = 'To print quotation marks such as "double quote", we need to use apostrophe'
print(message4)
print("......................................")

movie_quote = """One of the favourite line from the Godfather is: \
"I'm going to make an offer and he can't refuse" \
Do you know who said this?"""
print("......................................")

print(movie_quote)