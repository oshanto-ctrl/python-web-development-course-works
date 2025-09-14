class Human:
    def __init__(self, name, age):
        # attributes
        self.name = name
        self.age = age
    # methods
    def say_hello(self):
        print(f"Hello, my name is {self.name}, and I'm {self.age} years old.")

# Objs
obj_1 = Human("Alice", 22)
print(obj_1.name)
obj_1.say_hello()

obj_2 = Human('Omango', 26)
print(obj_2.name)
obj_2.say_hello()

# Constructor: What is constructor?
"""
__init__() method is the constructor.
When we create a new object of a class, 
this special function initialize attributes of the object.
"""

class Area:
    
    family_count = 0 # Class variable family_count
    # Initializing attributes
    def __init__(self, building_name):
        self.building_name = building_name
        self.count = 0
        self.family = []

    def add_family(self, family):
        self.family.append(family)
        Area.family_count += 1
        self.count += 1
        print( f"{self.family} has been added to {self.building_name}")

    def count_building_family(self):
        print(f"{self.building_name} has {self.count} families")
    
    def count_area_family(self):
        print(f"Total {Area.family_count} families are living in this area.")

# Building instances
b1 = Area("Building_1")
b1.add_family("Smiths")
b1.add_family("Alices")
b1.count_building_family()

# dict of families in b1
print(b1.__dict__)
print(Area.count_area_family)

print("\n------------------------\n")
b2 = Area("Building_2")
b2.add_family("Russes")
b2.add_family("Mikaells")
b2.add_family("Duroovs")
b2.count_building_family()

# dict of families in b1
print(b2.__dict__)

# Total family in this area
print(Area.count_area_family) # Some Issue Here Hex address prints.
b1.count_area_family()

