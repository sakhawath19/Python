# https://www.geeksforgeeks.org/inheritance-in-python/
# https://www.geeksforgeeks.org/types-of-inheritance-python/
# single inheritance(Mother inherited Grandfather)
# multiple inheritance(Child inherited Father and Mother)
# multilevel inheritance(Child inherited Mother and Mother inherited Grandfather, so Child inherited Grandfather too)
# hierarchical inheritance(Child and Adopted_child both are inheriting Mother class)
# hybrid inheritance 

# Base class 
class Grandfather:
    def __init__(self):
        self.grandfather_name = "Khalil Biswas"

    def grandmother(self):
        self.grandmother_name = "Momotaz Mohol"
        return self.grandmother_name

    def __str__(self):
        return "Grandfather"

# If Grandfather is a base class then Mother is an intermediate class
# here child is derived class from Mother and and Father 
class Mother(Grandfather): 
    def __init__(self, mother_name):
        self.mother_name = mother_name
        Grandfather.__init__(self)

    def mother_job(self): 
        print("Housewife") 

class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def father_job(self):
        print("Bank officer")

# Child inherited two base class named Mother and Father. This is known as multiple inheritance
# Mother inherited Grandfather, so Child inherited Grandfather too. This is known as multilevel inheritance
class Child(Mother, Father):
    def __init__(self, child_name, mother_name, father_name):
        self.child_name = child_name
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name) 

        self.__age = 25 # This is declared as private member
        self._height = 168 # This is declared as protected member # Class instance hass access of it

    def get_age(self):
        print("Age:", self.__age) # Private member is accessable inside the class 

    def __str__(self): 
        return "Child"


# Child and Adopted_child both are inheriting Mother class
# This is known as hierarchical inheritance
class Adopted_child(Mother, Father):
    def __init__(self, adopted_child_name, legal_mother, legal_father):
        self.adopted_child_name = adopted_child_name   
        Mother.__init__(self, legal_mother)
        Father.__init__(self, legal_father)
    
    def biological_parent(self):
        self.father = "unknown"
        self.mother = "unknown"
        print(f"Biological parent: {self.father}, {self.mother}")

# This is an example of hybrid inheritance
# Mother is inheriting Grandfather and Uncle is inheriting Grandfather and Mother too
# Example need to add 
        
if __name__ == "__main__":
    c = Child("Sakhawath", "Sultana", "Serazul")

    print(c.mother_job())
    print(c.grandfather_name)
    print(c.grandmother())
    print(c._height)
    c.get_age()
    print("__str__ is helping to print:", c)
    # print(c.__age) # This is not accessable outside class because this is a private member

    ac = Adopted_child("unknown", "Sultana", "Serazul")
    ac.biological_parent()


    




