''' Set Methods'''
def set_methods():
    i = 0
    for method in dir(set):
        if '__' not in method:
            i += 1
            print(i, method, sep=": ")

# Call the set methods
# set_methods()
my_set = {1, 2, 3}

# 1: add
my_set.add(4)
my_set.add(5.2)
my_set.add('a')
print(my_set)

# 2: copy : returns a shalow copy of set
your_set = my_set.copy()
print(your_set)

# 3: clear : remove all the element from a set
your_set.clear()
print(your_set)

# 4: difference : returns the difference of two or more set as a new set
# returns a new set containing elements that are present
# in the first set but not in any of the other sets provided as arguments.
set1 = {1, 2, 3, 4, 5, 6, 99}; set2 = {3, 4, 5, 6}
set3 = set1.difference(set2) # 1, 2
print("Set difference = ", set3)
# multiple sets
set4 = set1.difference(set2, set3)
print("Set difference (Multiple): ", set4)

# 5: difference_update  
# used to remove elements from the set that are also present
# in one or more specified sets by altering the original set
# modifies the original set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set3 = {3, 2}
# Update set1 by removing elements present in set2
set1.difference_update(set2, set3)
print(set1) # {1}

# update a set by removing elements present in an iterable list/tuple
set_a = {'a', 'b', 'c', 'd', 'e', 'f'}
list_a = ['b', 'd']
tuple_a = ('a', 'c')

set_a.difference_update(list_a, tuple_a)
print("Set a: ", set_a) # {'f', 'e'}

# 6: discard : remove an element from a list if it'a a member
# returns a new set. If element not present then raises a keyError
set_a.discard('f')
print("Discarded by discard() = ", set_a, " ", type(set_a))

# 7: intersection ; find the common elements between two or more sets.
# returns a new set containing only the elements that are present in all sets.
# Operator: &
set_a = {'I', 'L', 'Py'}
set_b = {'i', 'I', 'L'}
set_c = {'py', 'Py'}

# set_a intersection of set_b, set_c
set_a.intersection(set_b, set_c)
print("Set_a intersection set_b, set_c: ", set_a)


       
# 8: intersection_update
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

# Update set1 to keep only elements present in set2 and set3
set1.intersection_update(set2, set3)
print("set1 intersection_update set2, set3 ", set1) # 4 5 in all sets

# 9: isdisjoint : Check that two sets have no element in common
set_x = {'x', 'y'}
set_z = {'a', 'b'}
# returns a boolean
print("isdisjoint sample 1: ", set1.isdisjoint(set2)) # False
print("isdisjoint sample 2: ", set_x.isdisjoint(set_z)) # True


# 10: issubset : returns boolean value which is True if the given set 
# is a subset of the current set
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = set() # empty set 

# Check if set1 is a subset of set2
print(set1.issubset(set2))  # True
# Check if empty set is a subset of the non-empty set
print(set3.issubset(set1)) # True

# 11: issuperset
# The Python Set issuperset() method is used to determine if a set contains all elements of another set. 
# It returns True if the set calling the method contains every element of the set passed as an argument else False.

set1 = {1, 2, 3, 4}
set2 = {2, 4}
set3 = {1, 2}

result = set1.issuperset(set2) and set1.issuperset(set3)
print(result)  # True
set3 = {1, 6}
result2 = set1.issuperset(set3)
print(result2) # False

# 12: pop
# The Python Set pop() method is used to remove and return an arbitrary element from a set. If the set is empty it raises a 'KeyError'.
ss = {1, 2, 3, 4, 5}
popped = ss.pop()
print("Popped item: ", popped)
# popped = ss.pop()
# print("Popped item: ", popped)
# popped = ss.pop()
# print("Popped item: ", popped)


# 13: remove : removes a specified element from set, if not found then KeyError.
# discard doesn't raise keyerror.
ss.remove(4)
print("SS = ", ss) # 2 3 5

# 14: symmetric_difference
# 15: symmetric_difference_update

# 16: union : return a new set containing all the unique elements from the original set 
# and all specified sets. It combines the elements from multiple sets without including duplicates.
set1 = {1, 4, 5}
set2 = {2, 3, 6}
set3 = set1.union(set2) # {1, 2, 3, 4, 5, 6}
print(set3)

# 17: update : update method used to modify the set by adding 
# elements from another iterable(list, tuple etc.) or set.
# if any element in the iterale is already present in the set
# it won't be added again.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Update set1 with elements from set2
set1.update(set2)

print(set1)

# list of a tuple
# Define a set
my_set = {1, 2, 3}
my_iterable = [3, (4, 5), 6]

# Update the set with elements from the iterable
my_set.update(my_iterable)
print("Type of my_set: ", type(my_set))
print((4, 5) in my_set)
print(my_set) 

for x in my_set:
    print("x = ", x, " typ = ", type(x))


