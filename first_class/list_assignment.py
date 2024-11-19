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
'''






