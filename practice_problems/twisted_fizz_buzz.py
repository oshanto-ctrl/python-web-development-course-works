"""
Fizz Buzz with a Twist

Problem Statement:
Print numbers from 1 to N with the following rules:
• If a number is divisible by 3, print "Fizz".
• If a number is divisible by 5, print "Buzz".
• If a number is divisible by both 3 and 5, print "FizzBuzz".
• If the number is a prime, print "Prime".

Input Format:
A single integer N.

Output Format:
Output the required sequence, one item per line.

Example:
 Input:
 15

Output:
Prime
Prime
Fizz
Prime
Buzz
Fizz
Prime
Prime
Fizz
Buzz
Prime
Fizz
Prime
Prime
FizzBuzz

 Explanation:
1. Numbers like 2,3,5,7,11,132, 3, 5, 7, 11, 132,3,5,7,11,13 are prime, so print "Prime".
2. Numbers divisible by 3 (but not 5) print "Fizz": 3,6,9,123, 6, 9, 123,6,9,12.
3. Numbers divisible by 5 (but not 3) print "Buzz": 5,105, 105,10.
4. Numbers divisible by both 3 and 5 print "FizzBuzz": 151515.
"""


