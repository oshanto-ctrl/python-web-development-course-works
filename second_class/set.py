# Set
# Set is an unordered collection of unique objects.
# Sets are used to find distinct values

s = {'a', 'b', 'c'}
s.add('d')
print(f"Set {s}. Type {type(s)}")

s1 = ['e', 'f', 'g', 'a']
s.update(s1)

print(f"{s}")

# ** interview question **
# list of values given, remove duplicate.
temp = ['a', 'a', 'a', 'b']
temp_set = set(temp)
temp = list(temp_set)

print(temp)

# Remove

# remove(item), discard(item), pop(), clear(), del
temp.remove('b')
print(temp)
# temp.discard('a')
print(temp)

# We can make set operations (Union, Intersection, Complement etc.)
u1 = {1, 2, 3}
u2 = {2, 1}
u3 = u1.union(u2)
print(u3)
u4 = u1.intersection(u2)
print(u4)
# difference?






