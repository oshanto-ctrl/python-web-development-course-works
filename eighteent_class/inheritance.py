# Inheritance
inheritance = '''
Mechanism for creating a new class that specializes\n
or modifies the behavior of existing class.\n
The original class is called: base/super/parent class.\n
Then new class is called: sub/child/derived class.\n
Class created via inheritance it inherits attributes\n
defined by it's base class.\n
Derived/Clid class may redefine any of those attributes or\n
add new attributes of it's own.

'''
# print(f"What is inheritance?\n=> {inheritance}")

type_of_inheritance = '''
Type of inheritance.\n
# Single/Simple: Parent have only one child. (parent <-- child)\n
# Multiple: one child inherits from two or more parents (parent1 <-- child --> parent2)\n
# Multi-level: Child class also has it's sub-classes. (parent <-- child1 <-- child2)
parents, children, grand-childrens\n
# Hierarchical: Many child inherits from one parent. (child1 --> parent <--childN)
A parents have many childrens.\n
# Hybrid Inheritance: Mix of upper types of inheritances.
'''
# print(type_of_inheritance)


# Single/Simple Inheritance Example
class Parent:
    '''Parent Class'''
    def __inti__(self):
        print("Parent Class Constructor")
    
    def parent_method(self):
        print("From Parent Method.")


class Child(Parent):
    '''Child Class'''
    def __init__(self):
        print("Child Class Constructor")
    
    def child_method(self):
        print("From Child Method.")


# Objects
child = Child()
child.child_method()
child.parent_method() # From child, parent's method was invoked

parent = Parent()
parent.parent_method()
# Attribute Error
# parent.child_method() # Parent's object can not invoke any child's method here.


# Multiple Inheritance Example
# a child class has two or more parents to derived from.
'''
# Class Parent 1
class Parent1:
    pass

# Class Parent 2
class Parent2:
    pass

# Class child
class Child:
    # Extends parent1 & parent2
    pass

# Objects

'''
