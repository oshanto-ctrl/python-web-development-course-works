"""
Inheritance: Part 2:
Method Overriding
"""
# Method overriding in inheritance (also:Polymorphism) refers to
# the ability of a subclass to provide a specific
# implementation of a method that is already defined in the superclass.

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, length, width, height):
        super().__init__(length, width) # Calling parent's __init__ method
        self.height = height
    
    def area(self):
        return 0.5 * self.length * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)

# Create an object of Rectangle class
rectangle = Rectangle(5, 4)
circle = Circle(5)
triangle = Triangle(5, 0, 4)
print(f"Rectangle area {rectangle.area()},\t Circle area {circle.area()}")
print(f"Traianlge area {triangle.area()}")


# Superclass: If we want to access something from base class to derived class
# we use super() method.
# Accessing Parent Clss
# It ensures hat you're accessing the next class in the method resolution order. (MRO)
# This helps in maintaining a consistent an predicatable behavior of the code.

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # Calling parent's __init__ method
        self.age = age

    def greet(self):
        greeting = super().greet() # Calling parent's greet method
        return f"{greeting} and I'm {self.age} years old."

# Object 
child = Child("JIGSAW", 25)
print(child.greet())


# Task 1: Using super() without inheritance
# In Python, super() can be used in composition/delegation pattern
# https://realpython.com/inheritance-composition-python/
class Delegator:
    def __init__(self):
        self.name = "Delegator"
    
    def work(self):
        return "Delegator is working"

class Worker:
    def __init__(self):
        self._delegator = Delegator()  # Composition instead of inheritance
        
    def work(self):
        # Delegating work without inheritance
        return self._delegator.work()

# Task 2: Multiple inheritance example with super()
# Real-world example: Smart Device with both Phone and Computer capabilities

class Phone:
    def __init__(self, number):
        self.number = number
    
    def make_call(self):
        return f"Calling from {self.number}"

class Computer:
    def __init__(self, processor):
        self.processor = processor
    
    def run_program(self):
        return f"Running program on {self.processor}"

class Smartphone(Phone, Computer):
    def __init__(self, number, processor, model):
        Phone.__init__(self, number)
        Computer.__init__(self, processor)
        self.model = model
    
    def get_specs(self):
        return f"Smartphone {self.model} with number {self.number} and processor {self.processor}"

# Testing the examples
worker = Worker()
print(worker.work())

iphone = Smartphone("123-456-7890", "A15 Bionic", "iPhone 13")
print(iphone.make_call())
print(iphone.run_program())
print(iphone.get_specs())



