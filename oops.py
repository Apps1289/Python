#> OOPS concept
#> deals with classes and objects

class Student: #>defining classs
    name="Abhi" #> for every student's, name will Abhi only
    #> if we mention class then every student belongs to same class
s1=Student()#>creating object
print(s1)
#>output: <__main__.Student object at 0x0000027272EF96D0>
print(s1.name) #> accessing the name of the Student defined in the class

#> if we want to give different name of the student class, we need init function;
class Person:
     name="Rahul"
     def __init__(self,fname):  #> here self argument is the most which calls the object
        self.name = fname
        # print("We are inside init function")
# s2=Person()
s2=Person("Rajesh")
print(s2.name)
# just creating an object of a class, it access the __init__ function


        