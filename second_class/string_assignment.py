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
txt = "12345"
print(f"Is {txt} decimal? {txt.isdecimal()}")

# 16: isdigit
txt = "12345"
print(f"Is {txt} digit? {txt.isdigit()}")

# 17: isidentifier
txt = "variable1"
print(f"Is {txt} a valid identifier? {txt.isidentifier()}")

# 18: islower
txt = "hello"
print(f"Is {txt} all lowercase? {txt.islower()}")

# 19: isnumeric
txt = "12345"
print(f"Is {txt} numeric? {txt.isnumeric()}")

# 20: isprintable
txt = "Hello, World!"
print(f"Is {txt} printable? {txt.isprintable()}")

# 21: isspace
txt = "   "
print(f"Is {txt} all whitespace? {txt.isspace()}")

# 22: istitle
txt = "Hello World"
print(f"Is {txt} title-cased? {txt.istitle()}")

# 23: isupper
txt = "HELLO"
print(f"Is {txt} all uppercase? {txt.isupper()}")

# 24: join
my_list = ['a', 'b', 'c']
print(f"Joined string: {'-'.join(my_list)}")

# 25: ljust
txt = "Hello"
print(f"Left justified: '{txt.ljust(10)}'")

# 26: lower
txt = "HELLO"
print(f"Lowercase: {txt.lower()}")

# 27: lstrip
txt = "   Hello"
print(f"Left stripped: '{txt.lstrip()}'")

# 28: maketrans
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
txt = "this is string example....wow!!!"
print(txt.translate(trantab))

# 29: partition
txt = "I could eat bananas all day"
print(txt.partition("bananas"))

# 30: removeprefix
txt = "HelloWorld"
print(txt.removeprefix("Hello"))

# 31: removesuffix
txt = "HelloWorld"
print(txt.removesuffix("World"))

# 32: replace
txt = "I like bananas"
print(txt.replace("bananas", "apples"))

# 33: rfind
txt = "Hello, welcome to my world."
print(txt.rfind("e"))

# 34: rindex
txt = "Hello, welcome to my world."
print(txt.rindex("e"))

# 35: rjust
txt = "Hello"
print(f"Right justified: '{txt.rjust(10)}'")

# 36: rpartition
txt = "I could eat bananas all day, bananas are my favorite fruit"
print(txt.rpartition("bananas"))

# 37: rsplit
txt = "apple, banana, cherry"
print(txt.rsplit(", "))

# 38: rstrip
txt = "Hello   "
print(f"Right stripped: '{txt.rstrip()}'")

# 39: split
txt = "We Love Mangoes."
print(f"Split with space char: {txt.split()}")

# 40: splitlines
txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())

# 41: startswith
txt = "Hello, welcome to my world."
print(txt.startswith("Hello"))

# 42: strip
txt = "   Hello   "
print(f"Stripped: '{txt.strip()}'")

# 43: swapcase
txt = "Hello World"
print(txt.swapcase())

# 44: title
txt = "usergame is gaming."
print(txt.title())

# 45: translate
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
txt = "this is string example....wow!!!"
print(txt.translate(trantab))

# 46: upper
txt = "username"
print(txt.upper())

# 47: zfill
txt = "42"
print(txt.zfill(5))




'''
Valuable recourse from tutorialspoint: https://www.tutorialspoint.com/python/python_string_methods.htm
'''
