'''
Abstract class -> from abc <- (ab)stract-(c)lass
abc is a library

import ABC <- A parent class.
A child class of 'ABC' will be abstact class.

abstractmethod <- A decorator. Using in a method
it will be an abstract method.
'''
from abc import ABC, abstractmethod

# Example
class Vehicle(ABC):     #   Abstract Base Class
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def end(self):
        pass

# obj
# obj = Vehicle() # Can't instantiate abstract class

'''Abstract class should be inherit from another class'''
class Car(Vehicle):
    def start(self):
        print("Car is starting")
    def jump(self):
        print("Car just jumped!")
    def end(self):
        print("Car has stopped")


# obj
c = Car()
c.start()
c.jump()
c.end()