'''
Inheritances have some drawbacks.
Chainging child class can sometime
effect parent class and vice-versa.
'''

# Engine, Car example
# class Engine:
#     def __init__(self):
#         print("Engine class constructor.")
#     def start(self):
#         print("Engine started.")

# class Car(Engine):
#     def __init__(self):
#         print("Car class constructor.")
#         super().__init__()
#     def drive(self):
#         print("Driving")

# # obj
# car = Car()
# print(car.drive())

# Car is not engine

class Engine:
    def __init__(self):
        print("Engine class constructor.")
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        print("Car class constructor.")
        self.engine = engine #  composition
    def drive(self):
        self.engine.start()
        print("Driving.")

# obj 
engine = Engine()
car = Car(engine)
car.drive()


