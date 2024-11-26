"""
String Methods
"""
# All string methods without dunder
def string_methods():
    i = 0
    for method in dir(str):
        if '__' not in method:
            i += 1
            print(i, method, sep=": ")
# Call the string method
# string_methods()

a = "Hello"
b = 'John'
my_comment = '''I like doing some problem solving.'''

# Matching two string: return boolean state
sa = "Hello"
sb = "hello"
sc = 'Hello'
sd = '''Hello'''

print(f"Is {sa} equal to {sb}: { sa == sb}")
print(f"Is {sa} equal to {sc}: {sa == sc}")
print(f"Is {sa} equal to {sd}: {sa == sd}")

# concatenation
f_name = "mohammad"; l_name = "john"
full_name = f_name + " " + l_name; print("\nFull name: ", full_name)


# 1: capitalize : Uppercase the first letter
print("fine".capitalize())

# 2: casefold : Returns a string converting a wider range of characters to lowercase
print("abCDEFgh".casefold())

# 3: center : Pads the input string to the center with the specified character

# 4: count : returns number of times value 'x' appears in the string
txt = "I like apples. green apple, blue apple. apple is good."
count_apples = txt.count("apple")
print("count function: ", count_apples)

# 5: encode

# 6: endswith
txt = "Hello, welcome to my world!"
print(f"Is {txt} ends with ! mark: {txt.endswith('!')}")
# check if text  ends with 'my world' in specific position
print(f"Is phrase 'my world' in range of 15 and 26 of {txt}? ans: {txt.endswith("my world!", 15, 26)}")

# 7: expandtabs : Set the tab size to 2 whitespaces
print(f"{txt.expandtabs(2)}")

# 8: find : finds the first occurence of the specified value
# if value not found, returns -1 [Kind of simillar to index()]
txt = "you you me you me"
you = txt.find("you") # 0
me = txt.find("me") # 8
print(f"'you' in index {you}\n'me' at index {me}")

# 9: format
# 10: format_map
# 11: index : same as find() but raises an exception
str1 = "Hello. welcome to pythong course."
str2 = "to"
resulting_index = str1.index(str2)
print("The index where substring str2 found: ", resulting_index)

# 12: isalnum : returns true if string has atleast 1 char and all char are alphanumeric, false otherwise.
# Other characters such as '!', '.', '/', etc.. are not alphanumeric characters
txt = "1JohnUpTheTree#"
only_num = '123abc'
print(f"Is {txt} alphanumeric? {txt.isalnum()}\nIs {only_num} alphanumeric? {only_num.isalnum()}")


# 13: isalpha : check whether the string consist of alphabets. otherwise return false.
txt = "Abcdefg"
print(f"Is {txt} all alphabet? {txt.isalpha()}") # False: '' space character.



# 14: isascii : Check whether all characters in a string is ASCII (Unicode 0-127)
txt = "Hello"
print(txt.isascii())


# 15: isdecimal


# 16: isdigit


# 17: isidentifier

# 18: islower

# 19: isnumeric

# 20: isprintable

# 21: isspace

# 22: istitle
# 23: isupper # check if the string is in uppercase.
# 24: join
# 25: ljust
# 26: lower : lowercase conversion of string.
# 27: lstrip
# 28: maketrans
# 29: partition
# 30: removeprefix
# 31: removesuffix
# 32: replace : replace substring found in string.
# 33: rfind
# 34: rindex
# 35: rjust
# 36: rpartition
# 37: rsplit
# 38: rstrip
# 39: split : splits all the words in a string
# sepearted by a separator. This separator can is a delimiter string,
# can be comma, full-stop, space char or anyother char pattern.
txt = "We Love Mangoes."
print(f"Split with space char: ", txt.split())

# 40: splitlines
# 41: startswith
# 42: strip
# 43: swapcase
# 44: title
txt = "usergame is gaming."
print(txt.title()) # Usergame Is Gaming.
# 45: translate
# 46: upper
txt = "username"
print(txt.upper()) # USERNAME
# 47: zfill




'''
Valuable recourse from tutorialspoint: https://www.tutorialspoint.com/python/python_string_methods.htm
'''
