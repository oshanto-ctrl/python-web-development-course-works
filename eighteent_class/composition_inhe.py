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

"""
E-commerce order system example
for composition.

An Order - 
has Products
has a Customer
has a Payment method
has a Shipping method
has an OrderStatus

👉 Order is NOT any of these things
👉 Order HAS all of these things

Order
 ├── Customer
 ├── List[Product]
 ├── PaymentMethod
 ├── ShippingMethod
 └── OrderStatus
"""

class Product:
    """Product class with id, name, price attributes"""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Customer:
    """Customer class with id, name, email attributes"""
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

class PaymentMethod:
    """
    PaymentMethod class not implemented.
    It's a parent class for other sub-classes.
    """
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    """
    CreditCardPayment class for paying with
    credit card with total amount of purchase.
    """
    def pay(self, amount):
        return f"Paid {amount} using credit card"

class BkashPayment(PaymentMethod):
    """
    BkashPayment class for paying with
    bkash wallet with total amount of purchase.
    
    """
    def pay(self, amount):
        return f"Paid {amount} using Bkash"

class ShippingMethod:
    """
    ShippingMethod with type of delivery and cost for shipping.
    """

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
    def ship(self):
        return f"Shipping via {self.name}"

class OrderStatus:
    """
    OrderStatus class for tracking order's position
    Pending/Complete
    """
    def __init__(self): 
        self.status = "Pending"
    def update(self, new_status):
        self.status = new_status

class Order:
    """
    Order class has order_id, customer, payment_method, shipping_method
    products list to purchase and order_status.
    Methods: add_products, calculate_total, checkout
    """
    def __init__(self, order_id, customer, payment_method, shipping_method):
        self.order_id = order_id
        self.customer = customer                    #   composition
        self.payment_method = payment_method        #   composition
        self.shipping_method = shipping_method      #   composition
        self.products = []                          #   composition
        self.status = OrderStatus()                 #   composition

    def add_product(self, product):
        self.products.append(product)
    
    def calculate_total(self):
        product_total = sum(p.price for p in self.products)
        return product_total + self.shipping_method.cost    # product cost + shipping cost
    
    def checkout(self):
        total = self.calculate_total()
        payment_msg = self.payment_method.pay(total)
        shipping_msg = self.shipping_method.ship()
        self.status.update("Completed")
        return payment_msg, shipping_msg


# obj
# Products
p1 = Product("p101", "Laptop", 70000)
p2 = Product("p102", "Mouse", 1500)

# Customer
customer = Customer("c001", "Rahman", "rahimrahman@email.com")

# Payment & Shipping
payment = BkashPayment()
shipping = ShippingMethod("Home Delivery", 150)

# Create Order
order = Order("05001", customer, payment, shipping)

# Add products
order.add_product(p1)
order.add_product(p2)

# Checkout
payment_result, shipping_result = order.checkout()

print(payment_result)
print(shipping_result)
print("Order Status:", order.status.status)
