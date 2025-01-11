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


