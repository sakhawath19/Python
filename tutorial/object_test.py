
# CollectPrint is accessing two different class method 
# PrintVal and PrintKVal class accessing attributes of CollectionPrint class 


class PrintVal:
    def __init__(self, endl):
        self.endl = endl

    def print_d8(self, data):
        print(f"data_0: {data[0]}, data_1: {data[1]} {self.endl}")

class PrintKVal:
    def __init__(self, knm):
        self.knm = knm

    def print_d8(self, data):
        print(f"{self.knm}: data_0: {data[0]}, data_1: {data[1]}")

class CollectPrint:
    def __init__(self, endl):
        self.endl = endl
        self.knm = "[K]"

    print_8 = PrintVal.print_d8
    print_8k = PrintKVal.print_d8

if __name__=="__main__":
    c = CollectPrint("}")

    c.print_8([1, 2])
    c.print_8k([4, 5])
    




'''
# Understanding of object 
class D:
    pass 

class C:
    def do(self):
        print("do run", self)

def doo(obj):
    print("doo run", obj)

    obj.do()

if __name__=="__main__":
    c = C()
    d = D()

    doo(c)

    #doo(d)

    #c.do()

'''

'''
# C is a callable class
class C:
    def __call__(self):
        print("adf")

c = C()
c()

# implicit passing of self
c.__call__()
'''

'''
def func():
    print("adf")

func()

# implicit call method
func.__call__()
'''

'''
class C:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

if __name__ == "__main__":
    obj = C("Polash", [1, 2])

    print(obj.arg1)
    
    obj.arg2.append(3)
    print(obj.arg2)

    k = []
    print(k.__class__)
'''
'''
# Join need iterable string 
print(' '.join(['hello', 'world']))
'''