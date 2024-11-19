'''
Today learnings:

list, tuple, set, variable, index, type
list [pop, remove, extend, clear]

**TASKs**
[See List All Properties]
[See different combinations, working with vars, lists, sets etc.]
'''

# List
list1 = [1, 2, 3, 4, 5]
# print(list1); print(list1[0]); print(list1[2:3])
# print(list1[::-1]) # List in descending order
# print(list1[::1]) # List in ascending order
# print(list1.index(3)) # 0, 1, 2

# Set to list conversion
myset = {1, 3, 5, 7}
print(f"Type of my list is ", type(myset))
myset = list(myset)
print(f"Now my list type is ", type(myset))

myset.insert(4, 9)
myset.append(11)
print(myset)

temp = [13, 15, 17, 19]

# print(myset + temp)
myset.extend(temp)
print(myset, '\n', temp)

# List pop
p = temp.pop(); print(f"Popped Value {p} \nnewlist {temp}")

# Loop
nums = [1, 2, 3, 11, 4, 5]
for i in nums:
    print(i, end='\n')

nums.sort(reverse=True) # Original list sorts in reverse.
print(nums)
nums.reverse() # Reverse sorted reversed again make it ascending.
print(nums)


