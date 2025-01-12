a = 10
s = [20, 30]
b = 40
f = [a, *s, b]
print(f)

print(f"{20 in s}") # True
print(f"{40 not in s}") # True
print(f"{not(30 in s)}") # False

ra = 0.3
rb = 0.4
rc = 0.1
rd = .7
RME = ra, rb, rc, rd # Make a tuple
print(RME, " type ", type(RME))

# Unpacking
# When unpacking values into locations, the number
# of locations on the left must exactly math the number
# of the items in the iterable on the right. 
name = "AWE"
a, b, c = name
print(name, f" {a} {b} {c}", end="")

# Nested unpacking
# two nested, 3-tuple
datetime = ((5, 19, 2008), (10, 30, 'am'))
(month, day, year), (hour, minute, am_pm) = datetime
print((
    f"\nIncident happend on the {month}th month of {year} at {hour}:{minute}{am_pm}"
))

# throw-away value
message = ("How", "Idiot", "Are", "You")
(a, _, b, c) =  message
print(f"{a} {b} {c}")

# Num of items being unpacked isn't known
# usue * varibale
items = [1, 10, 11, 20, 21, 30, 31, 40, 41, 50]
# a, b = items # 1, 10
# print(items) ValueError: too many values to unpack (expected 2)
a, b, *extra = items
print(f"{a} {b} {extra}") # a = 1, b = 10, extra = [...remainings]
# this *extra will always be a list.

# Different orders.
items = [1, 2, 3, 4]
a, *extra, b = items
print(f"{a}  {extra} {b}") # 1, [2, 3], 4
*extra, a, b = items
print(f"{extra} {a} {b}") # [1, 2], 3, 4

# Any iterables can be expanded when writing out
# list, tuple, and set literals.
# This is done with star(*).
items = [1, 2, 3]
a = [10, *items, 11] # This expands the list keeping single list
print(a, " type is ", {type(a)}) # list 
a = [10, items, 11] # this makes a list of list a[.., [items],..]
print(a)

b = (*items, 10, *items) # (1, 2, 3, 10, 1, 2, 3)
print(b, " type of b is ", type(b)) # tuple

c = {10, 2, *items} # 10, 1, 2, 3
print(c, " type of b is ", type(c)) # set

# checking dict
items = [1, 2, 3]
d = {
    'price': 2 * [*items], # List = [1 2 3 1 2 3]
    'time': "today"
}
print(d) 

# any()
'''
The method any(iterables) beahces like a series of OR operators
between each element of the iterable we passed.
It replace loops similar to this one.
for element in some_iterable:
    if element:
        return True
return False
'''
# Same result by any(some_iterable)
print(any([10 == 10, 10 == 1, 10 == 9])) # [True, False, False] = True
print(any((10==1, 9 != 9))) # (False, False) = False
"""
Using any() with dicts (Data type other than boolean)
it checks whether any of the keys evaluates to True, not values.
"""
d = {
    True: False,
    False: True
} # True
print(any(d)) # True
dc = {
    False: False,
    False: True
} # False
print(any(dc)) # False

# any() is often used in combination with the map() method and list comprehension
number_list = [2, 1, 3, 8, 10, 11, 13]
even_list = list(map(lambda x: x%2 == 0, number_list))
odd_list = [x%2 != 0 for x in number_list]
print(even_list)
print(odd_list)
print(f"Are there any elements even? {str(any(even_list))}")
print(f"Are there any elements odd? {str(any(odd_list))}")


# https://stackabuse.com/any-and-all-in-python-with-examples/

