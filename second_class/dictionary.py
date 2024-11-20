# Dictionary

dict1 = {
    "key": "value",
    "name": "John",
    "age": 23
}

print(type(dict1))

# Accessing dictionary

# Print all the values only
# print(f"Dictionary values {dict1.values()} and type is {type(dict1.values())}")

# Print all the keys only
# print(f"Dictionary values {dict1.keys()} and type is {type(dict1.keys())}")

# access the dict1's name
n1 = dict1['name']
n2 = dict1.get('name')
print(f"Name {n1} and {n2}")

# Get all the key, value pairs 
# Returns list of tuples. It's iterable.
# [(a, b), (c, d), (e, f)]
print(dict1.items()) 
print(type(dict1.items())) # dict_items

# adding values in dictionary
dict1["address"] = "Dhaka"
dict1["roll"] = 1

dict1.update(
    {
        "phone": "017xxxxxxxxx",
        "email": 'john@doe.com'
    }
)

print(dict1)

# Remove the last item from dictionary

# Pop's the last item and returns it
email = dict1.popitem()
print(f"John's email is: {email}. type is {type(email)}") # Type if tuple
# we can use del/clear also
# d.clear()
# del d

# Length of dictionary
print(len(dict1))



