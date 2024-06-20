class person:

    def __init__(self , fname , lname) -> None:
        self.Fname = fname 
        self.Lname = lname 

    def Get_Full_name(self) -> str:
        return f"\nFname = {self.Fname} \nLname = {self.Lname}"
    
# using this method to inhert from person to the student 
class Student(person):

# here we use the student construcotr and pass it's paramter to the super class using super function built in function 
# and if we need to add more data to the init we can pass it to the student init method 
    def __init__(self, fname, lname , Degree) -> None:
        super().__init__(fname, lname)
        self.degree = Degree
        
# print object with all data directly using this function format without any call or with call doens't matter 
    def __str__(self) -> str:
        return f"Name:{super().Get_Full_name()} \nGrade:\n{self.degree}"

#***************************************************** main ******************************************

studen1 = Student("Eslam" , "Hussein" , 90)

print(studen1.__str__())