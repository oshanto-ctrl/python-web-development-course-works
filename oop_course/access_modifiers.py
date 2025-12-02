access_modifiers = '''
Three type of acccess modifiers.
Public - Accessible from everywhere. Syntax: name
Protected - Internal use, but accessible if needed. Syntax: _name
Private - Strictly internal. Syntax: __name
'''

public_attr_methods = '''
Simple meaning:
Anyone can access and modify them from outside the class.
Real-life analogy:
A restaurant's phone number — publicly available.

When used in real software:
User profile fields
Product name, price
Public APIs of a class
'''

class User:
    '''Public access modifier usage'''
    def __init__(self, username, email):
        self.username = username # public 
        self.email = email # public

# obj
u = User('rejoan siddiky', 'rej@fmail.com')
print(f"username: {u.username}\nEmail: {u.email}")


protected_attr_methods = '''
Simple meaning:
"Don't touch from outside unless you really know what you're doing."
It’s just a convention, but used heavily in real code.
Real-life analogy:
A hospital has a “STAFF ONLY” zone — not illegal to enter but not recommended.
Software example:
Maybe you want to allow inheritance but discourage outside access.

When used in real software
To indicate “internal use”
When subclasses need access
In frameworks (Flask/Django internal variables)
'''
class BankAccount:
    '''Protected access modifier usage'''
    def __init__(self, balance):
        self._balance = balance # protected
    def deposit(self, amount):
        self._balance += amount

class SavingsAccount(BankAccount):
    '''Protected access modifier usage.
        Child class of BankAccount class.
    '''
    def add_interest(self):
        self._balance *= 1.5 # child class can access protected attributes

# obj
acc = SavingsAccount(100)
print(acc._balance) # Technically allowed, but discouraged.


private_attr_methods = '''
Simple meaning:
Can't be accessed directly outside the class.
Python converts:
__balance → _ClassName__balance
for safety.
Real-life analogy:
ATM PIN — not shareable, protected inside machine’s logic.

Why private is useful in real software?
Hiding sensitive data
Preventing accidental corruption
Protecting internal state
Real examples:
Password hashing
Database connection handlers
Cryptographic keys
'''
class Bank:
    '''
    Private access modifier usage
    '''
    def __init__(self, balance):
        self.__balance = balance # private
    def deposite(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance

# obj
b = Bank(4000)
# print(b.__balance) # Error: private attribute
print(b.get_balance()) # Correct way to get private value


# Real Projet-Level OOP (COMBINED EXAMPLE)
# UserAuth system showing all modifiers

class UserAuth:
    '''User authentication: UserAuth class
        username, password, entered password.

        Explanation:
        username: public → anyone can read
        _login_attempts: protected → used inside class or subclasses
        __password: private → sensitive
        __check_password(): private → core logic hidden
    '''
    def __init__(self, username, password):
        self.username = username        # public (Ok to show)
        self._login_attempts = 0        # protected (Internal)
        self.__password = password      # private (Strictly internal)
    
    def login(self, entered_password):
        if self.__check_password(entered_password):     # private method
            self._login_attempts = 0
            return "Login successful."
        else:
            self._login_attempts += 1
            return "Wrong Username or Password!"
    
    def __check_password(self, entered):
        return entered == self.__password       # private logic
    

# UserAuth usage
u = UserAuth("Hamza", "h123")

print(u.username)               # OK, as it's public
print(u._login_attempts)        # Discouraged, but OK
# print(u.__password)             # Will fail: as it's private (Attribute Error)
# This works? Mangle Names. This is to avoid accidental overriding in subclases.
# print(u._UserAuth__password) 

