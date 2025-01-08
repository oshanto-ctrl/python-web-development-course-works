"""
Password Validator

Problem Statement:
You are given a string S representing a password. Determine if it is valid.

A password is valid if:
1. It is at least 8 characters long.
2. It contains at least one uppercase letter, one lowercase letter, and one digit.
3. It does not contain any spaces.

Input Format:
A single string S.

Output Format:
Output "VALID" if the password meets all criteria, otherwise output "INVALID".

Example:
 
 Input:
 Password123

 Output:
 VALID

 Explanation:
• Length: 11 characters (valid
• Contains at least one uppercase letter: "P
• Contains at least one lowercase letter: "assword"
• Contains at least one digit: "123"
• No spaces: "Password123"
"""

# Check required password length
def pass_length_checker(password):
    # 1. It is at least 8 characters long.
    return len(password) >= 8

def pass_case_checker(password):
    # 2. It contains at least one uppercase letter, one lowercase letter, and one digit.
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    return has_upper and has_lower and has_digit
    

def pass_space_checker(password):
    # 3. It does not contain any spaces.
    return ' ' not in password

# Passoword Validator Function
def password_validator(password):
    # if pass_length_checker(password) and pass_case_checker(password) and pass_space_checker(password):
    #     return True
    # else:
    #     return False
    return (
        pass_length_checker(password) and
        pass_case_checker(password) and
        pass_space_checker(password)
    )

# Input
# password = "password11FQS3#"
password = input()

# Validate password
if password_validator(password) == True:
    print("VALID")
else:
    print("INVALID")

