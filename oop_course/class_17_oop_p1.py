"""
OOP Contents

1. Classes and Objects
2. Attributes and Methods
3. Constructor
4. Inheritance
5. Polymorphism
6. Encapsulation
7. Abstraction
8. Composition and Aggregation
9. Static and Class Methods
10. Dunder Methods
11. Class Attributes vs Instance Attributes
12. Meta
13. Decorator
14. Context Manager

"""
# A student clss
class Student:
    """ A class student that stores student details."""
    # Initialization method
    def __init__(self, name, id):
        """ Init method returns none. We should no return anything from constructors. """
        print("This is a constructor")
        self.name = name
        self.id = id
    
    def student_info(self):
        """ A method that prints student information."""
        return self.name, self.id

    # Attributes
    # name = ''

name = "Tom"
id = 101
# Create an object/instance of the class
student1 = Student(name, id)
stud1name, stud1id = student1.student_info() # invoking the method of class.
print(f"Student id: {stud1id}, Name: {stud1name}")

# student1.name = "Tom" # Accessing the attribute of the class
# print(student1.name)    



class Rectangle:
    """ A class that calculates the area, perimeter of a rectangle."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)

    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Create an object of Rectangle class
rectangle = Rectangle(10, 15)
# Area
print(f"Area of rectangle: {rectangle.area()}")
# Perimeter
print(f"Perimeter of rectangle: {rectangle.perimeter()}")





