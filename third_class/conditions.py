''' Conditions '''
a = 10
# a = 5
# if a == 10 or a == 5:
#     print("A isn't crazy.")
# elif a > 10:
#     print("A is crazy!")
# else:
#     print("A is lost")

# Ternary operator (Structure)
# result if condition else result2 if condition2 else result3

# Nested if else
mangoes = 11
boxsize = 3

if mangoes <= 10:
    if boxsize > 2:
        print("Excess baggage cost. Reduce bagging.")
    else:
        print("Go for boxing the mangoes.")
else:
    if mangoes > 10:
        print("Use 3 or more bags.")
    elif mangoes > 20:
        print("Call Mango Man to handle Mango-business.")

    
# User input
# name = input("Enter your name:")
# print("Welcome to class, ", name.capitalize() , "!")

# fz = int(input("Enter a number: "))
# s = int(input("Enter a number again: "))

# print("Total= ", fz+s)

# Input 2 numbers by spliting comma (,)
a, b = input().split(',')
a = int(a); b = int(b)
print("A", a, " B ", b)


# **TASK**
# Calulator with Two number input.
# which operation to do? (Prompt)
# Do operation
# Give result
# Do it in creative way (Handle cases)


