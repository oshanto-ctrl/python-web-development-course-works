# File Handling in Python

# open file
# mode: r - read, w - write, a - append
# r+ - read and write, x - create

# write a file (Non-existant as firsthand)
with open('helloworld.txt', 'r') as file:
    # file.write("Hello world\n"*6)
    # print(file.read())
    # print(file.readline())
    # file.writelines('Hello my Pie')
    # file.writelines("Cutie")
    print(file.readlines())





