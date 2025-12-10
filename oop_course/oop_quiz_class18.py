# oop quiz (RANDOM) Class 18

#1. What does __init__ do
'''
The python __init__ method is declared within a
class and is used to initialize the attributes 
of an object as soon as the object is formed. 
While giving the definition for an __init__(self) method, 
a default parameter, named 'self' is always passed in its argument. 
This self represents the object of the class itself.
'''

#2. Output tracing
class Account:
    interest_rate = 0.05 # Class variable

    def __init__(self, balance):
        self.balance = balance
    def apply_interest(self):
        self.balance += self.balance * Account.interest_rate
    def set_interest(self, rate):
        self.interest_rate = rate

# obj
#a) 1100.0 #b) Attribute Error #c)1050.0 #d) 1000.0
savings = Account(1000)
savings.set_interest(0.1) # set interest called but it's intance var, Class preceeds Instance var
savings.apply_interest()    # 
print(savings.balance) # result: 1050.0


#3. Output trace
class Test:
    def __init__(self):
        self.x = 10
# obj
obj = Test()
print(obj.x) # 10

#4. Output trace
class Delta:
    def __init__(self):
        self.__sigma = "hidden" # private var

class Gamma(Delta):
    def reveal(self):
        return self.__sigma

# obj
# obj = Gamma()
# print(obj.reveal()) # AttributeError
d = Delta()
d.__sigma = "exposed"
print(d._Delta__sigma) # type: ignore # hidden.  
print(d.__sigma) # exposed. 





