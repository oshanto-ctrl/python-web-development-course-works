# any loop starts from 0 by default
# any loop steps = 1 by default
# limit always n - 1. for example = 5-1 = 4 = (0, 1, 2,, 3, 4)

for i in range(5):
    print(i) # 0, 1, 2, 3, 4

for i in range(1, 5, 3):
    print("Value of i: ", i)

# Odd numbers from 1 to 11 (exclusive)
print("Odd number from 1 to 10:")
odd_sum = 0
for i in range(1, 11, 2):
    odd_sum += i
    print(i, end=" ")
print("Odd sum: ", odd_sum)

# Even numbers from 1 to 11 (exclusive)
even_sum = 0
print("\nEven number from 1 to 10: ")
for i in range(0, 11, 2):
    even_sum += i
    print(i, end=" ")
print("Even sum: ", even_sum)

print("Coordinate axis: ")
axises = ['x', 'y', 'z']
for axis in axises:
    print(axis)