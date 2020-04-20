from math import pi

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2

if __name__ == "__main__":
    a = Square(4)
    b = Circle(7)
    print(b)
    print(b.fact())
    print(a.fact())
    print(b.area())

    """Here, we can see that the methods such as __str__(), 
    which have not been overridden in the child classes, 
    are used from the parent class.

    Due to polymorphism, the Python interpreter automatically recognizes 
    hat the fact() method for object a(Square class) is overridden. 
    So, it uses the one defined in the child class.
    """

    num1 = 1
    num2 = 2
    print(num1+num2)

    str1 = "Python"
    str2 = "Programming"
    print(str1+" "+str2)

    """Here, we can see that a single operator + has been used to carry out different operations for distinct data types. 
    This is one of the most simple occurrences of polymorphism in Python.
    """