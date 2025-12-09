# Method overloading and method overriding
# Examples, Solutions, Sample interview solution.

method_overloading = '''
Method overloadin is a fefature in OOP that
allows a class to have multiple methods with
the same name but different parameter lists.

Real world use:
APIs often accepts:
- simple values
- complex values
- optional parameters
python handles it via *args, **kwargs

✔ Then how do we do "overloading" in Python?
We do it using:
Default parameters
Variable arguments (*args, **kwargs)
Type checking
✔ Real-life analogy
A cashier can handle different customers:
1 product
10 products
weight-based products
But its the same person, just flexible.
✔ Practical Example (SWE scenario)
Lets build a flexible Logger class:
'''
class Logger:
    def log(self, *messages):
        if len(messages) == 1:
            print(f"[INFO] {messages[0]}")
        else:
            for msg in messages:
                print(f"[INFO] {msg}")

# obj
l = Logger()
l.log('Server started.')    # Single log
l.log('XamSungh logged in.', 
      'Request $139.75 receieved.') # Multiple logs

# Common overloading patterns

class CommonOverloadingPatterns:
    def __init__(self):
        pass

    # Default arguments example
    def greet(self, name="Guest"):
        print("Hello ", name, ".\n")

    # Type-based overloading (Rectangle area calculation)
    def area(self, value):
        if isinstance(value, (int, float)):     # if value integer/float
            return value * value    # square the values to get area
        if isinstance(value, tuple):
            a, b = value    #   unpack the tuple var
            return a * b    #   square the unpacked values to get area
    
# obj
cop = CommonOverloadingPatterns()
cop.greet()     #   Hello, Guest.
cop.greet('Rahim')      # Hello Rahim.
x = cop.area(4)     #   value-> int = 16
y = cop.area(7.07)  #   value-> float = 49.9
z = cop.area((13,2)) #   value-> tuple = 26
# print(f"{x}\n{y}\n{z}")



method_overriding = '''
Child class replaces the parent class method
with the same name.

Real-life analogy:
parent say "go to bed at 10 PM"
kids goes to bed at 10 PM
Teenager overrides "I go to bed 12 AM"

SWE example:
Base class defines API, subclass customizes behavior.
'''

# Example of overriding 
# Polymorphism: Same method name -> different behavior. 
class PaymentGateway:
    def pay(self, amount):
        return f"Paying {amount} using default gateway."

class Bkash(PaymentGateway):
    def pay(self, amount):
        return f"Paying {amount} via bkash Mobile Payment."

class Stripe(PaymentGateway):
    def pay(self, amount):
        return f"Paying {amount} via Stripe Credit Card."

# obj
gateways = [Bkash(), Stripe()]
for gateway in gateways:
    print(gateway.pay(570))


"""
Problem:
Create a class FileUploader with a single method upload 
that acts overloaded:
Requirements:
if passed a string → treat as file path
if passed a list → upload multiple files
if passed bytes → treat as raw file content
"""
class FileUploader:
    def __init__(self):
        pass

    def uplaod(self, file):
        if isinstance(file, str):
            print(f"Uploading file from path : {file}")
        elif isinstance(file, list):
            for f in file:
                print(f"Uploding file: {f}")
        elif isinstance(file, bytes):
            print(f"Uploading raw data of size {len(file)} bytes.")
        else:
            print("Unsupported file type.")

# obj
fu = FileUploader()
fu.uplaod("TEST.jpeg")
fu.uplaod(["3x9ab.png", "me_you.webp"])
fu.uplaod(b"RAW_IMG_DATA")


"""
Real-World OOP Scenario (Advanced Interview Level)

Task:
You are building a notification system with 3 channels:
Email
SMS
Push
Base class: Notifier.send(message)
Each subclass overrides send.
Also, the base send() should support overloading-style calls:
send("hello")
send("hello", priority="high")

Solution Shows:
Overloading (variable arguments)
Overriding (unique channels)
Polymorphism (loop over same interface)
"""
class Notifier:
    def __init__(self):
        pass

    def send(self, message, **options):
        priority = options.get("priority", "normal")
        return f"Sending '{message}' with priority {priority}"

class EmailNotifier(Notifier):
    def send(self, message, **options):
        base = super().send(message, **options)     #   reuse logic of base class
        return f"[Email] {base}"
    
class PushNotifier(Notifier):
    def send(self, message, **options):
        base = super().send(message, **options)
        return f"[PUSH] {base}"

# class SMSNotifier(PushNotifier):
#     def send(self, message, **options):
#         base = super().send(message, **options) # Just learning purpose
#         return f"[SMS] {base}"

class SMSNotifier(Notifier):
    def send(self, message, **options):
        base = super().send(message, **options)
        return f"[SMS] {base}"


# obj
notifier_channels = [EmailNotifier(), PushNotifier(), SMSNotifier()]
for notifier in notifier_channels:
    print(notifier.send("Server is UP: 200", priority="high"))


'''
Real world coffee order, coffee making: barista
example show how **kwargs handles various options with
default customizations.
'''

class CoffeeOrder:
    """Represents a customer's coffee order with various options"""
    def __init__(self, drink_type="coffee", **options):
        self.drink_type = drink_type
        self.options = options
    
    def __str__(self):
        return f"{self.drink_type.title()} order with options: {self.options}"

class Barista:
    """The coffee exper who prepares order with
        default and custom options
    """
    def __init__(self):
        # Default coffee options: A dictionary
        self.default_options = {
            "size": "medium",
            "milk": "whole",
            "sugar": 0,
            "extra_shot": False,
            "to_go": False,
            "temparature": "hot",
        }
    
    def prepare_order(self, order):
        """Prepares a coffee order with all options handled"""
        # Merge default options with customer's custom options
        all_options = {**self.default_options, **order.options}
        # Build the preparation steps
        steps = []
        # Size selection
        steps.append(f"Grab a {all_options['size']} cup")
        # Base drink
        steps.append(f"Add {all_options['size']} portion of {order.drink_type}")
        # Extra shot
        if all_options["extra_shot"]:
            steps.append("Add an extra shot of espresso")
        # Milk
        if all_options["milk"] != "none":
            steps.append(f"Add {all_options['milk']} milk")
        # Sugar
        if all_options["sugar"] > 0:
            steps.append(f"Add {all_options["sugar"]} sugar packet(s)")
        # Temparature
        if all_options["temparature"] == "iced":
            steps.append("Add ice")
        elif all_options["temparature"] == "extra_hot":
            steps.append("Steam to extra hot temparature")
        # To go or dine-in
        if all_options["to_go"]:
            steps.append("Put a lid on it")
        else:
            steps.append("Serve in a ceramic mug")
        
        # Handle any special requests (Unknown options)
        special_requests = [k for k in order.options.keys() if k not in self.default_options] 
        if special_requests:
            steps.append(f"Special requests: {', '.join(f'{k}={v}' for k, v in order.options.items() if k in special_requests)}")

        return "\n".join(steps)
    

# obj
barista = Barista()

order1 = CoffeeOrder("coffee")
print("+++ Order 1: Basic Coffee +++")
print(barista.prepare_order(order1))
print("\n" + "="*50 + "\n")

# customized order
order2 = CoffeeOrder("latte", size="large", milk="oat",
                     sugar=2, extra_shot=True)
print("+++ Order 2: Customized Latte +++")
print(barista.prepare_order(order2))
print("\n" + "="*50 + "\n")

# Iced cappuccino with a special request
order3 = CoffeeOrder(
    "cappuccino",
    temparature="iced",
    to_go=True,
    milk="almond",
    foam="extra", # This one is special request.
)
print("+++ Order 3: Cappuccino with request of extra foam +++")
print(barista.prepare_order(order3))
print("\n" + "="*50 + "\n")

# Complex order with many options
order4 = CoffeeOrder(
    "mocha",
    size="small",
    milk="skim",
    sugar=1,
    extra_shot=True,
    temparature="extra_hot",
    to_go=True,
    whipped_cream=True, # Extra option
    sprinkles="chocolate", # Extra option
)
print("+++ Order 4: Complex Order : Mocha coffee +++")
print(barista.prepare_order(order4))
print("\n" + "="*50 + "\n")



