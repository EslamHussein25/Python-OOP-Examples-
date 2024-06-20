
class car:
    # pass key word we can use it if we have class or construcotr or method to make it embty and pass from interprter 
    pass 



class Dog:
#***************************************************** properties ******************************************************************#
    # Class attribute
         # this to decalare the properties in the class in python 
    _age : int 
    _address : str
    _name : str
    _state : bool 
# how to define propertes in the class 

#1- using prtopertes part it self like above declare properteis with it's datatypes and use it in the class using self pointer 

#2- using construcotr any parameter we declared insidd the construcotr we can use it as propertes in  the class 

#***************************************************** Construcotr ******************************************************************#

#this is default constructor this first type of constructor in python and doesn't need any paramter else self pointer is forced paramter to 
#access the propertes insed the class 

    def __init__(selfy):
        # we can't access any  propertes else using self pointer 
        #self pointer like this in c++ but can't be use else passed as paramter to construcotr or method 
        #also we can call it any thing not care but the imprtant is the first parameter in the class construcotr or method 
        selfy._name = "Eslam"

# 2- paramterized construcotr 

#python doens't support any other types of construcotr like copy or move just default and parameterizd 
# we can't define 2 constrcutors here because python doesn't support that 
# must be send first paramter self then other parmeters you need 
#and we can pass any number of argment after self pointer here in this constructor 
    '''def __init__(self ,name , age , address ):
        self._name = name
        self._age = age
        self._address = address'''
    

#***************************************************** main program ******************************************************************#

# Instantiate the Dog class
#my_dog = Dog("Rex", 5 , "Cairo" , True)
my_Dog2 = Dog()
print("Name 2 is: " , my_Dog2._name)  # Output: Rex


# to delete the object you can use del keyword 
del my_Dog2
#print("Name is: " , my_dog._name)  # Output: Rex
#print("Ags is: " , my_dog._age)   # Output: 5
