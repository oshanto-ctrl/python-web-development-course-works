''' Functions in python '''

# function structure
def function_name():
    pass # something to do

# arguments vs parameters
'''
def f(parameters...):
    pass

# call f()
f(arguments...)
'''
def my_name():
    return "MD Rejoan Siddiky"

name = my_name()
print(f"Your name is {name} and has {len(name)} characters in it!")


# arg = "arguments"

def my_function(*a):
    s = sum(a)
    print(f"Values of *a = {a}\ntype is {type(a)}") # constructs tuple
    return s

var = my_function(1, 10, 11)
print(var)

print("\n")

# kwargs = "keyword arguments" # Passing arguments with keywords

def my_function(**kwargs):
    
    for key, value in kwargs.items():
        print(key, value)
    
    # print(f"Values of **kwargs {kwargs}\ntype is: {type(kwargs)}")
    return kwargs

var = my_function(name="John", age=22, location="dhaka, bgd", acctype="premium")
print(var)

# args and kwargs together
# *args will go first as parameter
# **kwargs will go second as parameter when using both.
def fishy(*args, **kwargs):
    print("Printing from inside fishy func()")
    print(args)
    print(kwargs)
    return args, kwargs

# call fishy
fish = fishy(1, 2, 3, 4, 5, name="yummy", location="pond", level="middle")
# Unpack the fish information
fish_tup, fish_dict = fish
print(fish_tup) # tuple 1, 2, 3, 4, 5
print(fish_dict) # dict{}


# Default parameter
def users(name, age, location="BGD"):
    info = f"Name: {name} {age} years old located in {location}"
    return info

me = users("abc", 22, )
you = users("xyz", 23, "GB")
print(f"{me}\n{you}")