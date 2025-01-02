"""Inheritence"""

class SoftwareEngineer:
    """A class represents different type of software engieers."""
    
    # Constructor Class
    def __init__(self, experience_level):
        self.experience_level = experience_level
    
    # Calculate the salary of a software engineer
    def calculate_salary(self):
        base_salary = 10000
        actual_salary =  (base_salary * self.experience_level)
        # return actual_salary
        print(actual_salary)

class Intern(SoftwareEngineer):
    pass

class Junior(SoftwareEngineer):
    pass

class Mid(SoftwareEngineer):
    pass

class Senior(SoftwareEngineer):
    pass


# Create an object of Software Enginner class
# sw = SoftwareEngineer(2)
# salary = sw.calculate_salary()
# print(f"Salary of a software engineer: {salary}\ntype {type(sw)}")

intern_object = Intern(1)
junior_object = Junior(2)
mid_object = Mid(3)
senior_object = Senior(4)

# Invoke the calculate_salary method
intern_object.calculate_salary()
junior_object.calculate_salary()
mid_object.calculate_salary()
senior_object.calculate_salary()



""" ### Types of inheritances ### """
# Four(4) types of inheritance
# Single, Multilevel, Hierarchical, Multiple

# Single inheritance
# One base class and one derived or child class.
class Employee:
    """A class that represents an employee."""
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_employee_info(self):
        print(f"Employee id: {self.emp_id}, Name: {self.name}")
    
# Derived class Accountant
class Accountant(Employee):
    """A class that represents an accountant."""
    pass # Accountant class inherits all the properties of Employee class.

# Creating an object of the classes.
emp1 = Employee("TOMMY", 102)
acc1 = Accountant("JERRY", 201)

# Display the employee inofrmations
print("---- Employee ----")
emp1.display_employee_info()

print("\n---- Accountant ----")
acc1.display_employee_info() # Inherits and uses display_employee_info method from Employee class.











