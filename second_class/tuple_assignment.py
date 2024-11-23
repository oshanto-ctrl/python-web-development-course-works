'''
Tuple assignment
'''
# All tuple methods without dunder
def tuple_methods():
    i = 0
    for method in dir(tuple):
        if '__' not in method:
            i += 1
            print(i, method, sep=": ")
# Call the tuple method
# tuple_methods()

# Creating a tuple
print("\n##### Creating Tuple #####\n")
tup1 = tuple([1, 2, 3, 4, 5, 2, 2, 3, 6])
tup2 = ()
tup3 = ('f',) # Can not create tuple with 1 item[It's string without comma(,)]
print(f"Type of tup1 = {type(tup1)} type of tup2 {type(tup2)} type of tup3 {type(tup3)}")

# 1: count
# Find number of time element is present in the tuple
print("\n##### Count Function #####\n")
# Find the occurence of 2 in tuple1
one_count = tup1.count(2)

# 2: index
# Giving the first occurence of an element (index)
# Raises an exception if element is not found in the tuple
print(f"Occurence of 5 in tuple at index = {tup1.index(5)}")

# Length of tuple
print("\n##### Length of Tuple #####\n")
print(f"Length of tup1 {len(tup1)}")

# Sorted() function
print("\n##### Sorted() function in Tuple #####\n")
my_tup = (1, 5, 3, 10, 9, 7, 6, 2)
print(f"Sorted tuple {sorted(my_tup)}. Type of output after sorting: {type(sorted(my_tup))}")

# sort() tuple in-place
list(tup1).sort(); print("In-place sort() of tup1: ", tup1)

# Maximum value at tuple
max_value = max(my_tup)
print("Maximum value ", max_value)

# Minimum value at tuple
min_value = min(my_tup)
print("Minimum value ", min_value)

# Accumulate value of tuple
sum_of_my_tup = sum(my_tup)
print("Sum of tuple ", sum_of_my_tup)

# my_tup = (1, 5, 3, 10, 9, 7, 6, 2)
print(my_tup)
first_element = my_tup[0]
last_element = my_tup[-1]
print(f"First Elem: {first_element}\nLast Elem: {last_element}")

# Slicing of a tuple
tup = (10, 20, 30, 40, 50, 60)
print("Slicing tup till mid : ", tup[:len(tup)//2])

print("Getting values with alternate element: ", tup[::2])
