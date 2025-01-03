""" Polymorphism """
# Type of polymorphism:
# 1. Duck Typing

""" 
Duck Typing 
https://www.analyticsvidhya.com/blog/2024/07/duck-typing-in-python/#h-what-is-duck-typing
"""

class Duck:
    def sound(self):
        print("Quack Quack")

class Cat:
    def sound(self):
        print("Meow Meow")

def animal_sound(voice):
    voice.sound()

d = Duck()
c = Cat()

animal_sound(d)
animal_sound(c)

# 2. Operator overloading
# Example of operator overloading
"""
a = 10
b = 20
c = a + b
print(f"{a} + {b} = {c}\ntype = {type(c)}")

a = "10"
b = "20"
c = a + b
print(f"{a} + {b} = {c}\ntype = {type(c)}")
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
            # This magic method overloads the '+' operator for Point objects
            
            # Parameters:
            # - self: The current Point instance (automatically passed)
            # - other: Another Point instance that's being added
            
            # Example:
            # p1 = Point(1, 2)
            # p2 = Point(3, 4)
            # p3 = p1 + p2  # Under the hood, this calls p1.__add__(p2)
            
            # Returns:
            # - A new Point instance with summed coordinates 
      
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

# Object of Point class
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2 # for '+' operator, __add__ method will be called
print(p3.x, p3.y)

