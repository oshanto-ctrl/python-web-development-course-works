'''What are we learning today!?'''

''' Recursion and recursion related errors handling '''

''' Recursions have base case and recursive case '''


def func():
    return "Hello."

print(func())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return (n * factorial(n - 1))
    
print(factorial(5))

# Two problems
# output upto nth term of fibonacci
# output what is the nth value of fibonacci
# find recursive case, find base case

def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

# interview question: gives a list, use recursion to summation of list
def addition(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + addition(nums[1:])

nums = [1, 3, 5, 7, 9]
print("Recursive summation = ", addition(nums))



''' map, filter, reduce '''

# map
# map iterates the function
def find_length(word):
    return len(word)
words = ['apple', 'mango', 'sausage']
print("Find length: ", find_length(words))

print("Using map")
l1 = list(map(find_length, words))
print("L1 ", l1)

l2 = list(map(lambda w: len(w), words))
print("L2 ", l2)

l3 = [len(word) for word in words]
print("L3 ", l3)

# any, all

# filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = filter(lambda n : n > 5, nums)
print(list(res))

# reduce, zip, min, max

# class after next class.
# QUIZZZZ and Problem Solving TASK!!!!