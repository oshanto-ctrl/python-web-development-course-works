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
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return f"Hi, I'm {self.name}"

# class Employee(Person):
#     '''
#     Employee sub-class derived from Peron class.
#     '''
#     def __init__(self, name, age, emp_id):
#         super().__init__(name, age) # to call parent constructor
#         self.emp_id = emp_id
#     def work(self):
#         return f"{self.name} (id {self.emp_id}) is working."

# e = Employee("Asad", 26, 207)
# print(e.greet())
# print(e.work())


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


# Hybrid Inheritance
# Combination of two or more type (Often Multi-level + multiple)
# Manager inherits Employee (single) but also includes 
# TeamLeadMixin and BudgetOwnerMixin (multiple)

# class Employee:
#     def base_info(self): return 'Base Employee'

# class TeamLeadMixin:
#     def lead(self): return 'Leading Teams'

# class BudgetOwnerMixin:
#     def allocate(self): return 'Allocating Budget'


# # Hybrid for manager class: Manager has single + Mixins
# class Manager(Employee, TeamLeadMixin, BudgetOwnerMixin):
#     pass

# m = Manager()
# print(m.base_info()) # Base Employee
# print(m.lead()) # Leading Teams
# print(m.allocate()) # Allocating Budgets


''' Practice Problem Inheritance'''
'''
Shape Area Calculator
A program needs to calculate the area of different shapes. Each shape has a name, and different shapes have different ways to calculate their area.
•	Circle: Area = π × radius²
•	Rectangle: Area = width × height
•	Triangle: Area = 0.5 × base × height
Write a program that allows the user to create different shapes and calculate their areas.
Example Input:
circle = Circle (5)  
rectangle = Rectangle (4, 6)  
triangle = Triangle (3, 8)  

print(circle.area())  
print(rectangle.area())  
print(triangle.area())  
Example Output:
78.54  
24  
12  
'''
# Shape area calculator
import math

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        """Area method will be overridden by child classes"""
        raise NotImplementedError("Base Shape.Area Method Not Implemented.")

# Circle
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle") # Parent class has the 'Name' at __init__
        self.radius = radius # Passed as an argument
    def area(self):
        return math.pi * (self.radius ** 2) # pi * r^2

# Rectangle
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__("Rectangle")
        self.height = height
        self.width = width
    def area(self):
        return (self.height * self.width)

# Tri-angle
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
    
# obj
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

print(
    f"Circle area = {c.area()}\nRectangle area = {r.area()}\nTriangle area = {t.area()}"
)



'''
Employee Management System
A company maintains records of its employees. Each employee has a name, employee ID, and salary. The company has two types of employees:
•	Full-Time Employees are paid a fixed monthly salary.
•	Contract Employees are paid per project they complete.
Write a program to calculate the total salary paid to each employee.
Example Input:
e1 = FullTimeEmployee("Alice", 101, 5000)  
e2 = ContractEmployee("Bob", 102, 2000, 3)  # Paid per project, completed 3 projects  

print(e1.calculate_salary())  
print(e2.calculate_salary())  

'''
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def calculate_salary(self):
        """
        This method will be overriden by child methods.
        Different salary for different roles.    
        """
        raise NotImplementedError("Salary method isn't implemented at Base class.")

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary):
        # Fetch employee name, id from base class
        super().__init__(name, emp_id)
        self.base_salary = base_salary
    def calculate_salary(self):
        return self.base_salary
    def __str__(self) -> str:
        return f"FullTimeEmployee(name={self.name}, id={self.emp_id}, salary={self.base_salary})"

class ContractEmployee(Employee):
    def __init__(self, name, emp_id, base_project_fees, projects_done):
        super().__init__(name, emp_id)
        self.base_project_fees = base_project_fees
        self.projects_done = projects_done
    def calculate_salary(self):
        if self.base_project_fees < 0:
            raise ValueError("Project fees must be positive")
        if self.projects_done < 0:
            raise ValueError(f"{self.name}[{self.emp_id}] projects can't be negative.")
        return self.base_project_fees * self.projects_done
    def __str__(self) -> str:
        salary = self.calculate_salary()
        return f"ContractualEmployee(name={self.name}, id={self.emp_id}, salary={salary})"

# obj
e1 = FullTimeEmployee("Alice", 101, 5000)
e2 = ContractEmployee("Bob", 102, 2500, 3) # Paid per project, completed 3
# print(e1.calculate_salary())
# print(e2.calculate_salary())
print(e1)
print(e2)

'''
Online Shopping System:
An online store sells products, and customers can add items to their cart. Each product has a name, price, and stock quantity. When a customer places an order, the system should:
1.	Calculate the total cost.
2.	Reduce the stock of purchased items.
Write a program that allows customers to add items to their cart and place an order.
Example Input:
p1 = Product("Laptop", 1000, 5)  
p2 = Product("Phone", 500, 10)  

customer = Customer("John")  
customer.add_to_cart(p1, 2)  
customer.add_to_cart(p2, 1)  

print(customer.checkout())  
print(p1.stock)  
print(p2.stock)  
Example Output:
Total cost: $2500  
3  
9  
'''
class Product:
    """Product(Name, Price/unit, Quantity)"""
    def __init__(self, product_name, product_price, product_quantity):
        # Check Product price, and quantity value is not negative
        if product_price < 0:
            raise ValueError("Product price cannot be negative.")
        if product_quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
    def __str__(self):
        return f"Prodcut name(name = {self.product_name}, price = ${self.product_price}, quantity = {self.product_quantity})"

class Customer(Product):
    """
    Cusomer: has name, can add product to cart, 
    can checkout with product.

    """
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = {}  #   {product: quantity}
    
    # add to cart method
    def add_to_cart(self, product: Product, quantity):
        """Add product to customer's cart"""
        if quantity <= 0:
            raise ValueError("Selected product quantity must be positive number.")
        if product in self.cart:
            self.cart[product] += quantity
        else:
            self.cart[product] = quantity

    # checkout method
    def checkout(self):
        """Process the order and return total cost"""
        if not self.cart:
            return "Your cart is empty."
        
        # Check stock availabilty of product
        for product, quantity in self.cart.items():
            if product.product_quantity < quantity:
                raise ValueError(
                    f"Insufficient stock for {product.product_name}"
                    f"Available: {product.product_stock}, Requested: {quantity}"
                )
        # total cost and update stock
        total_cost = 0.0
        for product, quantity in self.cart.items():
            total_cost += product.product_price * quantity
            product.product_quantity -= quantity
        
        # Clear the cart after checkout
        self.cart.clear()

        return f"Total cost: ${total_cost:.2f}"
    
    def __str__(self):
        cart_items = ", ".join(
            f"{product.product_name} x {quantity}"
            for product, quantity in self.cart.items()
        )
        return f"Customer(name={self.customer_name}, cart=[{cart_items}])"
# obj
p1 = Product("Laptop", 75000, 5)
p2 = Product("Phone", 25000, 7)

customer = Customer("Jabir")
customer.add_to_cart(p1, 1) # Product object, Quantity
customer.add_to_cart(p2, 3) # Product object, Quantity

print(customer.checkout()) # Total cost 75000 + (3*25000 = 75000) = 150000
print(f"Reaminging Stock of product 1: {p1.product_quantity}")
print(f"Remaining stock of product 2 {p2.product_quantity}")

