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
# s2=Person() # >>just creating an object of a class, it access the __init__ function
s2=Person("Rajesh")
print(s2.name)

#day_2 of OPPS
class students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s3=students("Arjun",85)
print(f"{s3.name} has scored {s3.marks}")

s4=students("Prakash",90)
print(s4.name,s4.marks)



        