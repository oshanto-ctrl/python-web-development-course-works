operator_overloading = '''
Operator overlaoding lets your objects work
with your python operators
(+, -, ==, <, len(), in, etc)
Example:
3 + 5       #   calls 3.__add__(5)
obj1 + obj2 #   calls obj1.__add__(obj2)
'A' + 'b'   #   Joining -> "Ab" (Concatanation)
Same symbol, different behavior based on objects.
'''

common_magic_methods='''
Common Magic Methods (short list)
Operator	Method
+	__add__
-	__sub__
*	__mul__
==	__eq__
<	__lt__
<=	__le__
>	__gt__
>=	__ge__
len(x)	__len__
str(x)	__str__
repr(x)	__repr__
x in y	__contains__
x[key]	__getitem__
round(x)	__round__
'''
# Vector addition example of operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

# obj
v1 = Vector(2, 5)
v2 = Vector(7, 3)
print(v1 + v2)

# Money Class (Real Banking)
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Diffenet Currency")
        return Money(self.amount + other.amount, self.currency)
    def __str__(self):
        return f"{self.amount} {self.currency}"

# obj
m1 = Money(350, "BDT")
m2 = Money(160, "BDT")
print(m1 + m2) # 510 usd


# Filesize
class FileSize:
    def __init__(self, bytes_) -> None:
        self.bytes = bytes_
    def __add__(self, other):
        return FileSize(self.bytes + other.bytes)
    def __str__(self):
        return f"{self.bytes/1024:.2f} KB"

# obj
f1 = FileSize(2048)
f2 = FileSize(0)
print(f1 + f2) # 2 KB


# Comparison Overloading __lt__, __eq__
class Student:
    '''Compare student gpa'''
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    def __lt__(self, other):
        return self.gpa < other.gpa
    def __eq__(self, other):
        return self.gpa == other.gpa

# obj
s1 = Student("Rahim", 3.93)
s2 = Student("Karim", 3.97)
print(s1 < s2) # True
print(s1 == s2) # False