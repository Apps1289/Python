# class and instance attributes

class student:
    college_name="LPU"  #> if we want same value of every object, here all students belong to the same college
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def info(self): #> functions of class are called methods
        print("The name of a student is",self.name,self.marks) #> self parameter is mandatary and it is enough to access the value from constructor

    def get_marks(self):
        return self.marks  #> here either we can return or print the value

s1 = student("samit",95)
print(s1.info())
print(s1.get_marks())

# program to  print the name of students with marks of 3 subjects in constructor and create a method to
# print the avearge of marks

class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in range(len(self.marks)):
            sum = sum + self.marks[value]
        
        avg = sum/len(self.marks)
        print("Avg marks is:",avg)

s1 = students("Abhi",[75,85,90])
print(s1.get_avg())
