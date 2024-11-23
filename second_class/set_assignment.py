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
# 6: discard
# 7: intersection       
# 8: intersection_update
# 9: isdisjoint
# 10: issubset
# 11: issuperset
# 12: pop
# 13: remove
# 14: symmetric_difference
# 15: symmetric_difference_update
# 16: union
# 17: update




