# Methods in OOP
# Methods and Fuctions are likely same things.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")

s1 = Student("Shirtling", 23)
s1.display()