# Tuple

# Tuple allows duplicate but set doesn't

t = ('a', 'b', 'c', 'd', 'e', 'f', 'f')
print(type(t))

# Create with tuple() constructor
mylist = ['awesome', 'wonderful', 'nice']
tup = tuple(mylist)
print(type(tup))

vowel_tup = tuple(('a', 'e', 'i', 'o', 'u'))
print(type(vowel_tup))

# Access a tuple
print(f"{t[0]}\t{t.index('c')}\t{t[:4:1]}\t {t.count('f')}")

# tuple doesn't allows single argument.
mytup = ('a') # it's not a tuple until mytup = ('a',) use a comma


# Tuple remove
# del mytup

# Tuple Unpack
(c1, c2, c3) = tup
print(f"Complements {c1}, {c2}, {c3}.")
print(type(c2))

# all arguments (*)
tc = (1, 2, 3, 4, 5, 6, 6)

(a, b, *c) = tc

print(f"{a}, {b}, {c}")


