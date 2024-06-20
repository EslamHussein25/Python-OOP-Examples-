class Human:

    def __init__(self):
        self.name = "None"
    

#*********************************** Methods in class *******************
#even methods need at least one argumnent is self this forced passed paramter, so in get and set name we need self to access anme 
#properts in class also in print hello we need it even we didn't need any propetes in the class 

#then we can use it like any normal method like any language 

# just here we have this internal method to helps us to print all object data we need without any claa just 
#when print in main function the object data we call the object and this function will run automticlly and print the data we need to show 

    def __str__(selfy) -> str:
        return f"name={selfy.name}"
    
    def Set_Name(selfy , n) -> str:
        selfy.name = n
    
    def Get_Name(self) -> None:
        return self.name 

    def print_Hello(self) -> None:
        print("Hello")

    def print_Hello_User(self) -> None:
        print("Hello" , self.name)
#************************** main ***********************
h = Human()
h.Set_Name("Eslam")
print(h)
'''
print(h.Get_Name())
h.print_Hello()
h.Set_Name("Eslam")
h.print_Hello_User()'''