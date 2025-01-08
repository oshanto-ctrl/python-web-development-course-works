"""
Palindrome Checker

Problem Statement:
Determine whether a given string S is a palindrome. Ignore spaces, punctuation, and case.

Input Format:
A single string S.

Output Format:
Output "YES" if the string is a palindrome, otherwise output "NO".

Example:
 Input:
 A man, a plan, a canal, Panama
 Output:
 YES

Explanation:
Ignore spaces, punctuation, and case: "amanaplanacanalpanama".
Reverse of "amanaplanacanalpanama" is still "amanaplanacanalpanama", so the
string is a palindrome. 
"""
# Sanitize the text
def text_sanitizer(text):
    # Convert string to lowercase
    # Remove all non-alphanumeric chars(except spaces)
    # Replace spaces with empty string
    lowered_text = text.lower()
    cleaned_text = ''.join(ch for ch in lowered_text if ch.isalnum() or ch.isspace())
    sanitized_text = cleaned_text.replace(' ', '')
    return sanitized_text
    

# Check if given text is palindrome
def palindrome_checker(text):
    # Make the input text sanitized as requirement
    text = text_sanitizer(text)

    if len(text) < 2:
        print("YES")

    reversed_text = text[::-1]
    if reversed_text == text:
        print("YES")
    else:
        print("NO")

text  = "A man, a plan, a canal, Panama"

# Call palindrome checker with argument text
palindrome_checker(text)