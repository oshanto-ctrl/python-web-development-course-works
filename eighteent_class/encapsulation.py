# Encapsulation
# Demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):
        # protected member
        self._a = 2.00

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # calling construct of Base class
        Base.__init__(self)
        print("Calling protected member of Base class", self._a)

        # modify the protected variable
        self._a = 3.00
        print("Calling modified protected member outside class", self._a)

# obj
obj1 = Derived()
obj2 = Base()

# Calling protected member
# Can be accessed but should not be done due convention
print("Accessing protected member of obj1 (Derived)", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2 (Base)", obj2._a)
print(f"\n{'*'*15}\n")
ex1 = """
EX: This program simulates a patient management system 
for a medical clinic, where sensitive patient data 
(like medical history and diagnosis) is protected using
encapsulation. This allows access only 
through specific methods, ensuring that data
remains secure and cannot be accidentally modified.
"""
class Patient:
    def __init__(self, name, age, medical_history):
        self.name = name # public
        self.age = age # public
        self._medical_history = medical_history # protected
        self.__diagnosis = None # private
    
    # Method to access medical history
    def get_medical_history(self):
        return self._medical_history

    # Method to update medical history
    def add_medical_history(self, record):
        self._medical_history.append(record)
    
    # Method to set a diagnosis (only accessible within the class)
    def set_diagnosis(self, diagnosis):
        self.__diagnosis = diagnosis
    
    # Method to get the diagnosis (only accessible within class)
    @property
    def get_diagnosis(self):
        return self.__diagnosis
    
    # Display patient information
    def display_paitent_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print("Medical History:", self.get_medical_history())
        print("Diagnosis:", self.get_diagnosis) # use of @property: behave like attribute

# obj
# Simulating the medicial system

# Creating a patient with some initial medical history
p1 = Patient("John Karim", 45, ["High BP", "Diabetes Type2"])

# Accessing protected medical history via method
print("Patient Initial Medical history:", p1.get_medical_history())

# Adding a new record to the medical history
p1.add_medical_history("Cholesterol issue")

# Setting a diagnosis using the encapsulated method
p1.set_diagnosis("Stable Condition")

# Display patient info (using encapsulated isplay method)
p1.display_paitent_info()

# Accessing the private diagnosis directly (Should not be done)
# print(p1.__diagnosis) # This will raise an attributeError (private variable)



# ATM (Basic features)

class ATM:
    def __init__(self, account_number, pin, balance="2000"):
        self.account_number = account_number
        self.__pin = pin
        self.__balance = balance
    
    # Get balance method
    def get_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return self.__balance
        return "Invalid PIN. Try Again."

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return "Deposit Successful."
        return "Invalid Amount. Trye Again."
    
    # Withdraw money
    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:
            return "Invalid PIN."
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return "Withdrawl successful."











