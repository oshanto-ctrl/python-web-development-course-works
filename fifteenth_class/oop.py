class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, and I'm {self.age} years old.")

# Objs
obj_1 = Human("Alice", 22)
print(obj_1.name)
obj_1.say_hello()

# Constructor: What is constructor?
"""
__init__() method is the constructor.
When we create a new object of a class, 
this special function initialize attributes of the object.
"""