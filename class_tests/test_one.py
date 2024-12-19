# which of the following list comprehension produces the list [0, 4, 16]
a = [x**2 for x in range(5) if x%2==0]
print(a)

# Which of the following statements about python functions are correct?
'''Functions can be called with named arguments'''

# What is the result of this code?
x = 'hello'
y = x.upper().replace('L', '1')
print(y) # HE110

# What is the result of this code-snippet?
x = (1, 2, 3)
# y = x, y += (4,)
print(x) # Error

# Which of the following operations is valid in Python?
#a myset = {[1, 2], [3, 4]}
#b my_dict = {1: [1, 2, 3]}
#c mydict = {{1, 2}: "value"}
#d my_set = {1, 2, 3}
#b and #d are correct

# What is the result of this slicing operation?
s = "abcdefgh"
print(s[1:6]) # bcdef
print(s[::-1]) # hgfedcba
print(s[1::-1]) # ba
print(s[:6:-1]) # h
p = s[1:6:-1]
print(len(p)) # 0
print(s[1:6:-1]) # ''

# What will be the result of the follwoing code?
a = {1, 2, 3}
# a.add([4, 5])
# a.update([4, 5]) # correct
print(a) # TypeError: unhashable type: 'list'


# What will be the following code output?
def compute(a, b=[]):
    b.append(a)
    # print("I am list B: ", b)
    return sum(b)

print(compute(3)) # 3 
print(compute(5)) # 8

# what will the following code output?
s = "Python"
print(s[s.find('t'):s.find('n')]) # tho


