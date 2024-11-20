# String

name = "Hello World"
print(name)
print(f"{name[0]}, {name.index('o')}, {name[:5]}, {name.count('o')}")

# Format string
num = 3
# print(f" {name * num}\n")

# Escape sequencing

# Write: He said "I'am not good at python\c++."
print('He said, \"I\'m not good at python\\c++\".')

# Newline \n, Tab \t, Backspace \b,  

# Print Uppercase
print(name.lower())
# Print Lowercase
print(name.upper())
# Print Title
print(name.title())
# Print capitalized
print(name.capitalize())

# Striping the string
f = "                   ouch                    "
print(f.strip()) # Remove all the space character around actual info.

# Replace
print(f.replace(' ', '#'))

n = "Yummy Yummy ABCDs"
n = n.split(' ')
print(f"{n}, {type(n)}")

n = "Yummy Yummy ABCDs"
# Find where any sub str in string
print(n.find('ABCD')) # Starting index of the word.

# Length of string

print(len(n)) # 17





