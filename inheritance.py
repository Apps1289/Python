#> it the property in which child class inherit the properties of parent class

class car: # parent class
    @staticmethod
    def start():
        print("Car is started!")

    @staticmethod
    def stop():
        print("Car has stopped!")

class Hyundai(car): # child class which is inheriting the parent class property i.e. car
    def __init__(self,name):
        self.name = name


car1= Hyundai("xyz")
car2 = Hyundai("abc")
print(car1.name)
print(car1.start())  # here rather we are in class hyundai but we are able to access the method of parent class, this is inheritance
print(car1.stop())