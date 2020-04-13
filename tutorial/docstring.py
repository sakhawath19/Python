""" After creating function if you just type three double quote and hit enters """
""" Automatic docstring will be generated to write proper comments """

def greetings(greet, name):
    """[summary]
    
    Arguments:
        greet {[type]} -- [description]
        name {[type]} -- [description]
    """
    print(f"{greet} {name}")

greetings("Hello", "Sakha")