'''
Dictionary methods
'''# All dictionary methods without dunder
def dictionary_methods():
    i = 0
    for method in dir(dict):
        if '__' not in method:
            i += 1
            print(i, method, sep=": ")
# Call the dictionary method
# dictionary_methods()

# 1: clear
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)  # Output: {}

# 2: copy   
original = {'x': 1, 'y': 2}
copied = original.copy()
print(copied)  # Output: {'x': 1, 'y': 2}

# Modifying the copied dictionary doesn't affect the original
copied['z'] = 3
print(original)  # Output: {'x': 1, 'y': 2}
print(copied)   # Output: {'x': 1, 'y': 2, 'z': 3}
   
# 3: fromkeys  
fruits = ['apple', 'banana', 'cherry']
fruit_dict = fruits.fromkeys(fruits, 'juice')
print(fruit_dict)
# Output: {'apple': 'juice', 'banana': 'juice', 'cherry': 'juice'}

# 4: get  
my_dict = {'a': 1, 'b': 2}
print(my_dict.get('a'))  # Output: 1
print(my_dict.get('d', 0))  # Output: 0 (default value)
     
# 5: items     
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# a: 1
# b: 2
# c: 3

# 6: keys  
# my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict.keys():
    print(key)
# Output:
# a
# b
# c
    
# 7: pop   
# my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_value = my_dict.pop('b')
print(popped_value)  # Output: 2
print(my_dict)       # Output: {'a': 1, 'c': 3}
    
# 8: popitem  
# my_dict = {'a': 1, 'b': 2, 'c': 3}
pair = my_dict.popitem()
print(pair)  # Output: ('a', 1)
print(type(pair))
print(my_dict)  # Output: {'b': 2, 'c': 3}
 
# 9: setdefault
my_dict = {'a': 1, 'b': 2}
print(my_dict.setdefault('a'))  # Output: 1
print(my_dict.setdefault('c', 3))  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 10: update
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 11: values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)
# Output:
# 1
# 2
# 3
