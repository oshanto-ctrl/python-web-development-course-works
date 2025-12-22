problem_one = """
Problem 1: Secure Bank Account
Problem Statement:
You are required to implement a BankAccount class that securely manages an account balance.
Class Specifications:
o	Stores the account number.
o	Stores the balance amount.
o	Initializes the account number and balance.
o	Adds the given amount to the balance.
o	Withdraws the given amount if sufficient balance exists; otherwise, return "Insufficient funds".
o	Returns the current balance.
Input Format:
•	First, a string representing the account number.
•	Second, a float representing the initial balance.
•	Then, multiple queries in the format:
o	"D amount" (Deposit)
o	"W amount" (Withdraw)
o	"B" (Get Balance)
Output Format:
•	Print the balance after each "B" query.
•	Print "Insufficient funds" if a withdrawal fails.
"""
class BankAccount:
    def __init__(self, account_number="ACC12242", balance=1000.00):
        self.account_number = account_number
        self.__balance = balance # private for security
    
    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= withdraw_amount
    
    def get_balance(self):
        return self.__balance

# obj
print(f"Input acc number: ")
account_number = input().strip()
print("Inital Balance: ")
balance = float(input())

account = BankAccount(account_number, balance)

while True:
    try:
        query = input().strip()
        if query.startswith("D"):
            _, amt = query.split()
            account.deposit(float(amt))
        
        elif query.startswith("W"):
            _, amt = query.split()
            account.withdraw(float(amt))
        
        elif query == "B":
            print(account.get_balance())
    except EOFError:
        break



problem_2 = """
Problem 2: Employee Management System
Problem Statement:
You need to implement an Employee class that securely manages employee details.
Class Specifications:
•	Stores the employee ID as a string.
•	Stores the employee salary as a float.
•	Initializes the employee ID and salary.
•	Increases salary by a given percentage.
•	Gets the current salary.
Input Format:
•	First, a string representing the employee ID.
•	Second, a float representing the initial salary.
•	Then, multiple queries in the format:
o	"I percentage" → Increase salary by given percentage.
o	"S" → Get the current salary.
Output Format:
•	Print the updated salary after each "S" query.
Example:
Input:  
EMP001  
5000  
I 10  
S  
I 5  
S  

Output:  
5500.0  
5775.0  
"""
class Employee:
    def __init__(self, emp_id, emp_salary):
        self.emp_id = emp_id
        self.__emp_salary = emp_salary
    
    def increase_salary(self, percentage):
        self.__emp_salary += self.__emp_salary * (percentage/100.00)
    
    def get_salary(self):
        return self.__emp_salary

# obj
emp_id = input("Enter EMP ID").strip()
salary = float(input("Enter base salary: "))
employee = Employee(emp_id, salary)

while True:
    try:
        query = input("[I]->Percentange\n[S]->Salary").strip()
        if query.startswith("I"):
            _, percent = query.split()
            employee.increase_salary(float(percent))
        elif query == "S":
            print(employee.get_salary())
    except EOFError:
        break


problem_three = """
Problem 3: Smart Home System
Problem Statement:
You are required to implement a SmartHome system that securely manages different smart devices in a home.
Class Specifications:
•	Stores the device name.
•	Toggles the light between ON and OFF.
•	Stores the temperature and allows updates to it.
•	Stores a list of devices and allows adding new devices.
•	Controls a device (toggle lights or set thermostat temperature).
•	Lists all devices.
Input Format:
•	"Light name" → Create a light device.
•	"Thermostat name" → Create a thermostat device.
•	"Add name" → Add a device to the smart home.
•	"List" → List all added devices.
•	"Toggle name" → Toggle a light ON/OFF.
•	"SetTemp name value" → Set temperature for thermostat.
Output Format:
•	Print responses based on the command.
Example:
Input:  
Light LivingRoomLight  
Thermostat HomeThermostat  
Add LivingRoomLight  
Add HomeThermostat  
List  
Toggle LivingRoomLight  
SetTemp HomeThermostat 25  
Toggle LivingRoomLight  

Output:  
Devices: LivingRoomLight, HomeThermostat  
Light LivingRoomLight is now ON  
Thermostat HomeThermostat is set to 25°C  
Light LivingRoomLight is now OFF  
"""

# Device class
class Device:
    def __init__(self, name):
        self.name = name

class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on
        state = "ON" if self.is_on else "OFF"
        print(f"Light {self.name} is now {state}.")

class Thermostat(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temparature = None
    
    def set_temperature(self, value):
        self.temparature = value
        print(f"Thermostat {self.name} is set to {value} degree celcius.")

# Smart home class
class SmartHome:
    def __init__(self):
        self.devices = {}
    
    def add_device(self, device):
        self.devices[device.name] = device
    
    def list_devices(self):
        print("Devices: ", ", ".join(self.devices.keys()))
    
    def toggle_light(self, name):
        device = self.devices.get(name)
        if isinstance(device, Light):
            device.toggle()
    
    def set_temperature(self, name, value):
        device = self.devices.get(name)
        if isinstance(device, Thermostat):
            device.set_temperature(value)


# obj
home = SmartHome()
created_devices = {}

while True:
    try:
        command = input().strip()
        parts = command.split()

        if parts[0] == "Light":
            created_devices[parts[1]] = Light(parts[1])

        elif parts[0] == "Thermostat":
            created_devices[parts[1]] = Thermostat(parts[1])

        elif parts[0] == "Add":
            home.add_device(created_devices[parts[1]])

        elif parts[0] == "List":
            home.list_devices()

        elif parts[0] == "Toggle":
            home.toggle_light(parts[1])

        elif parts[0] == "SetTemp":
            home.set_temperature(parts[1], int(parts[2]))

    except EOFError:
        break

