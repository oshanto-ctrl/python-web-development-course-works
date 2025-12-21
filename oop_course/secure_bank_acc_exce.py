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
Problem 3: Employee Management System
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