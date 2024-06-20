class Vehicles:
    def __init__(self) -> None:
        pass

    def move_Method(self):
        print("\nmove!")

# car is move so we will do any changes here so this class will pass directly 
class Car(Vehicles):
    pass 

class Plane(Vehicles):
    # here we override move method to chnage it's code for this class 
    def move_Method(self):
        print("\nFly!")

class Boat(Vehicles):
    def move_Method(self):
        print("\nSail!")

#************************************* main *****************************

car1 = Car()
plane1 = Plane()
boat1 = Boat()

car1.move_Method()
plane1.move_Method()
boat1.move_Method()
