''' Looping '''
# for loop
# structure:
# for i in range(x):
#     print(i)
for i in "12345":
    print(i, end=" ")

for i in ['a', 'b', 'c', 'd']:
    print(i, end=" ")
print()
for i in "INNOVATIVE"[::-1]:
    print(i, sep="-", end=" ")

print()
# while loop
# while looping has to have a condition
s = "12345"
i = 0
while i < len(s):
    print(s[i])
    i += 1 # Not incrementing will cause infinite loop
print()

# Break
for i in "MYLAPTOP":
    if i == 'P':
        break # Breaks out of the loop
    print(i, end="")

print()
# Continue
# Skip the part where hits 'continue' then goes back to iteration of next element.
for i in "SIGHUP":
    if i == 'G':
        continue # Skip current iteration and jump to next one
    print(i, end="")


print()
# Pass
for i in "12345":
    if i == '3':
        pass # will do nothing and print 3
        print(i, end="") # will also print 3
    print(i, end="")
print()

# for loop with else statement
for i in range(1, 5):
    print(i, end="")
else:
    print("\nLoop Ended? Really!?")
print()

# List for loop
l = ["A", "B", "C"]
for i in l:
    print(i)
print()

# list for tuple
for i in ("earth", "fire", "wind", "water", "heart"):
    pass

# Dictionary for loop
dict1 = {
    "name":"john",
    "age":35,
}


# List comprehension
# [what i want to do -> for loop in 1 line -> if any conditions]
fruits = [ fruit for fruit in ("apple", "banana", "cherry", "strawberry") if fruit is not "strawberry"]
print(f"{fruits} \t type is {type(fruits)}")

# tested new thing! Got generator.
fruits = (fruit for fruit in ["apple", "banana", "cherry"]) # 
print(f"{fruits} \t type is {type(fruits)}")

abcs = ['a', 'x', 'y', 'z']
print("Initial abcs: ", abcs)
abcs = [letter for letter in abcs if letter != 'a']
print("New abcs: ", abcs)

# power of 2 list comprehension
power_of_twos = [x**2 for x in range(11) if x%2!=0]
print("Power of twos but odds only", power_of_twos)

# Nested for loop in comprehension (READ MORE ABOUT IT)
# fruits = (fruit for fruit in ["apple", "banana", "cherry"] for f in fruit) # 
# print(fruits)

# Dictionary comprehension
dict1 = {key:value for key,value in dict1.items()}
print(f"New D {dict1}\t Type d = {type(dict1)}")

# Enumerate
# It's needed two data
# Uses mostly in project. Tracking data based on it's index.

list1 = ["apple", "chery", "coconut"]
for i, j in enumerate(list1):
    # index then value (i, j)
    print(i, " ", j, " " ,end="")

print()
# zip
# zip merges two lists?
l1 = ['a', 'b', 'c']
l2 = ['0', '1', '2']
for ch, num in zip(l1, l2):
    print(ch, num, sep=" ")
print()

# next()
l = ["app", "web", "iot"]
print(next(iter(l)))

# generator only access data only if its passes forward.
# tuples saves all data then access it.
# generator used for very large amount of data. (Data science/ handling large data.)