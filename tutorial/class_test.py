"""Possible to define method outside the class. But it is not recommended
"""

class Player:
    class_type = "info"

    def __init__(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def set_sport(self, sport):
        self.sport = sport

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, sport: {self.sport}")

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

if __name__=="__main__":
    p = Player("Shakib")
    p.set_age(33)
    p.set_sport("cricket")
    p.print_info()
    print(p.class_type)


    b = Bag()
    b.addtwice(3)
    print(b.data)

