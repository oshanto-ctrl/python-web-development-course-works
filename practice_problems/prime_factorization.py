"https://cp-algorithms.com/algebra/factorization.html"
# https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

"""
Prime Factorization

Problem Statement:
Given a positive integer X, find all its prime factors.

Input Format:
A single integer X.

Output Format:
Print all prime factors of X in ascending order, separated by spaces. Each factor must
appear as many times as it divides X.

Example:

Input:
 12

Output:
 2 2 3

Explanation:
• Prime factors of 12: 12÷2=6, 6÷2=3, and 3 is a prime number. 
"""
def prime_fractorizator(n):
    primes = []
    fractorization = []

    i = 0
    for i in range(2, int(n**0.5)+1):
        while(n%i == 0):
            fractorization.append(i)
            n //= i
    if n > 1:
        fractorization.append(n)
    return fractorization


# Take input
# n = 12
n = int(input())
# Call the function
answer = prime_fractorizator(n)
# Print the result like desired format.
print(' '.join(map(str, answer)))