topic = '''
Example codes to learn 5 types of
inheritance.
Single, Multiple, Multi-level, Hierarchical,
Hybrid.
Extra feature: Diamond problem, MRO, and super() 
for problems and interviews.
'''

# Single Inheritance
# Natural example: A puppy is an animal
# Emplyee inherits from Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hi, I'm {self.name}"

class Employee(Person):
    '''
    Employee sub-class derived from Peron class.
    '''
    def __init__(self, name, age, emp_id):
        super().__init__(name, age) # to call parent constructor
        self.emp_id = emp_id
    def work(self):
        return f"{self.name} (id {self.emp_id}) is working."

e = Employee("Asad", 26, 207)
print(e.greet())
print(e.work())


# Multiple Inheritance
# Natural example: Platypus is a mammal(gives milk) and lays eggs.
# mixins like JSONSerializable + Timestamped + Model
class JSONSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
class TimestampMixin:
    def set_timestamp(self, ts):
        self.ts = ts

class Model:
    def save(self):
        return f"Saved {self.__class__.__name__}"
    
class User(Model, JSONSerializableMixin, TimestampMixin):
    def __init__(self, username):
        self.username = username

u = User("noscube")
u.set_timestamp("2025-11-29")
print(u.to_json()) # return the dictionary of u object
print(u.save()) # Saved User


# Multi-level Inheritance
# Parent -> Child -> Grandchild
# Plant -> tree -> apple_tree
# Vehicle -> Car -> electric_car

class Vehicle:
    def drive(self): return "Driving..."

class Car(Vehicle):
    '''Child of Vehicle Class'''
    def open_trunk(self): return "Trunk Opened."

class ElectricCar(Car):
    '''Child of Car Class'''
    def charge(self): return "Charging"


ec = ElectricCar()
print(f"{ec.drive()}\n{ec.open_trunk()}\n{ec.charge()}")



# Hierarchical Inheritance
# One parent, many children
# Natural example: Animal -> Dog, Cat, Bull, Bird, Frog
# Notification -> EmailNotification, SMSNotification, PushNotification

class Notification:
    def send(self): raise NotImplementedError

class EmailNotification(Notification):
    def send(self): return 'Email Sent'

class SMSNotification(Notification):
    def send(self): return 'SMS Sent'

print(f"\n{EmailNotification().send()}\n{SMSNotification().send()}")
