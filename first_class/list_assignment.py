''''
List copying methods.
'''
a = ['a', 'b', 'c', 'd']
# Copying with reference. Updating (b) elements also updates list a
b = a

# Testing:
b.append('E')
# print(f"List a: {a} \n List b: {b}")


# Copying without reference (Cloning)
c = a[:]

# Testing:
c.append('FF')
# print(f"List b: {b} \n List c: {c}")


'''
Testing different built-in list methods.
https://docs.python.org/3/tutorial/datastructures.html
'''

# All the list methods without dunder
def list_methods():
    i = 0

    for method in dir(list):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')

# Call the list_methods
# list_methods()

# 1: append
# Add an item to the end of the list.
print("\n###### APPEND ######\n")
l1 = ['cake', 'ice-cream']
l1.append('burger')
print(l1)

# 2: clear
print("\n###### CLEAR ######\n") 
# Removes all items from the list: Similar to del list[:]
# l1.clear()
# print(l1)

# 3: copy
print("\n###### COPY ######\n")
# Makes a shallow copy of the list. Similar to a[:]
# If list if multi dimension like: ['a', 'b', ['c', 'd']]
# then changing copy_l1 will change the original list
copy_l1 = l1.copy()
# print(copy_l1)
copy_l1.remove('ice-cream')
print(copy_l1)


# 4: count
# Returns the number of times value x appears in the list.
print("\n###### COUNT ######\n")
candidates = ['Mario', 'WhiteFang', 'Elon', 'Luigi', 'Elon', 'Bill']
elons = candidates.count('Elon'); print(elons)

# 5: extend
# Extend the list by appending all the items from the iterable. Simillar to a[len(a):] = iterable
print("\n###### EXTEND ######\n")
benched_candidates = ['Gai', 'Fujioshi', 'Hatake']
candidates.extend(benched_candidates)
print(candidates) # All the candidates newly added with old ones
# extend a list of retired candidates to candidate list as a list element.
retired_candidates = ['Apple', 'Lichi']
candidates.extend([retired_candidates])
print(candidates) # [a, b, c, d, [e, f, g]]

# 6: index
# Location of a certain value/element x at a list
print("\n###### INDEX ######\n")
print(f"Gai at position: {candidates.index('Gai')}")

# If value is missing in the list py3 will give a ValueError
# value X not in the list. Be careful to handle that.
if 'naruto' not in candidates:
    print("Naruto not in the list. Adding him now.")
    candidates.append('Naruto')
    print(f"New list: {candidates}")
else:
    print("Naruto is in the list.")


# 7: insert
print("\n###### INSERT ######\n")
# Insert an item at a given position. First argument is the index of the element
# which to insert, so a.insert(0, x) inserts x at the front of the list, and
# a.insert(len(a), x) is equivalent to a.append(x), last element in the list.
candidates.insert(3, 'Rock Lee')
print(candidates)

#  insert at an index that doesn't exist yet in the list, Python will append 'Tenten' to the end of the list.
benched_candidates.insert(5, 'Tenten')
print(benched_candidates)

# Insert with negative index.
# Insert 'paw' at the position that is one before the last element.
abcs = ['a', 'b', 'c', 'd', 'e']
abcs.insert(-1, 'paw')
# Insert 'gixx' at the last position.
abcs.insert(len(abcs), 'gixx')
print(abcs)

# 8: pop   
# Remove the item at the given position in the list, and return it.
# If no index specified, a.pop() removes and returns the last item
# in the list. It raises a indexError if the list is empty or index is 
# outside the list range.
print("\n###### POP ######\n")
lg = candidates.pop() 
# pop's the last element
legendary = [lg]
print(legendary)
print(f"New candidates list: {candidates}")

# pop from a certain index
candidates.append('Gaara')
retired_candidates_popped = candidates.pop(10)
print(f"Retired candidate list that popped: {retired_candidates_popped}\nNew list: {candidates}")


# 9: remove
# Remove the first item from the list whose value is equal to x.
# It raises a ValueError if there is no such item.
# What if multiple occurence of item x?
# Then it removes only the first occurence.
print("\n###### REMOVE ######\n")
candidates.remove('Elon')
print(candidates)

# 10: reverse
# Reverse the elements of the list in place

print("\n###### REVERSE ######\n")
legendary.append('kakashi'); legendary.append('Might Gai'); legendary.append('Bee')
legendary.append('Jiraiya')
print(f"Original list: {legendary}")
legendary.reverse()
print(f"After sort {legendary}")

# 11: sort
# Sort the items of the list in place (the arguments can be used for sort customization)
# Sort in alphabetical order. If no key provide then it sort first Upper then lowercase words
# 
print("\n###### SORT ######\n")
retired_candidates.append('hinata')
print(retired_candidates)

# Normal sorting
retired_candidates.sort()
print(f"Normal sorting {retired_candidates}")

# Making it lower.
retired_candidates.sort(key=lambda name: name.lower())
print(f"Lowercase sorting {retired_candidates}")

# Sort the values by their length
retired_candidates.sort(key=lambda name: len(name))
print(f"Sorted by length of values {retired_candidates}")

# Sort using reverse = True
retired_candidates.sort(key=lambda name: len(name), reverse=True)
print(f"Sorted by length of values using reverse=True {retired_candidates}")




