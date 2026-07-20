#MINI PROJECT STUDENT MANAGEMENT(OOP BASICS)
print("Hello Apoorva")
class Student:
    pass

print("Class Created")

class Student:

    def __init__(self):
        print("Constructor Running")

print("Before Object")

s1 = Student()

print("After Object")


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student Object Created Successfully!")

    def study(self):
        print(self.name, "is studying Python.")
        print("Age:", self.age)

print("Before Object")

s1 = Student("Apoorva", 24)

print("Before Method")

s1.study()

print("Program Finished")

   
