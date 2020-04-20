# Example of public, protected and private access modifier
# Example of name mangling

# Access modifier also ensure encapsulation 
# This puts restrictions on accessing variables and methods directly 
# and can prevent the accidental modification of data.

class Super: 
      
    # public data member 
    var1 = "Public data member"
  
    # protected data member with one pre underline
    _var2 = "Protected data member"
       
     # private data member with two pre underline
    __var3 = "Private data member"
      
    # constructor 
    def __init__(self, var1, var2, var3):   
          self.var1 = var1 
          self._var2 = var2 
          self.__var3 = var3 
      
    # public member function    
    def displayPublicMembers(self): 
   
        # accessing public data members 
        print("Public Data Member: ", self.var1) 
         
    # protected member function    
    def _displayProtectedMembers(self): 
   
        # accessing protected data members 
        print("Protected Data Member: ", self._var2) 
       
    # private member function    
    def __displayPrivateMembers(self): 
   
        # accessing private data members 
        print("Private Data Member: ", self.__var3) 
  
    # public member function 
    def accessPrivateMembers(self):              
        # accessing private memeber function 
        self.__displayPrivateMembers() 
   
# derived class 
class Sub(Super): 
   
    # constructor  
    def __init__(self, var1, var2, var3):  
        Super.__init__(self, var1, var2, var3) 
            
    # public member function  
    def accessProtectedMemebers(self): 
        # accessing protected member functions of super class  
        self._displayProtectedMembers()

if __name__ == "__main__":
    # creating objects of the derived class      
    obj = Sub("Geeks", 4, "Geeks !")  
    
    # calling public member functions of the class 
    obj.displayPublicMembers() 
    obj.accessProtectedMemebers() 
    obj.accessPrivateMembers() 

    # Name mangling
    # Python performs name mangling on private attributes. 
    # Every member with a double underscore will be changed to _<className><memberName>
    s = Super("Geeks", 4, "Geeks !")  
    print(s._Super__var3)

    # this will show all members of object s 
    # here you will see _Super__var3
    print(dir(s)) 
    
    # Object can access protected member in python. 
    # in C++ or java protected member can be accessed within the class or by subclass only
    print("Object is accessing protected member:", obj._var2)

    # object can not access private member, so it will generate Attribute error
    # print(obj.__var3)

