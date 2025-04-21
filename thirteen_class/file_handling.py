# Open file
# mode: r - read, w - write, a - append, r+ - read and write
# mode: x - create, rb - read binaryfile (image data)

# r - reads from the file
# w - write in a file, creates a file when no files found
# a - add something to a file
# x - create a file, if a file created before of that name
#      then shows error

# Let's write/read in a file
with open('write_file.txt', 'r') as file:
    # file.writelines("\nMe1")
    # file.write("Hello World by write() function.")
    # print(file.read())
    # print(file.readline())
    # print(file.readlines()) #Gives as a list
    pass

# Create a file
with open("rejoan.txt", 'rb') as f:
    # f.write("Give me some sunshine.")
    # f.write("Give me some rain.")
    # f.write("Give me another chanche")
    # f.write("I wana grow up once again.")
    # f.close()
    f.seek(10)
    print(f.tell())
    print(f.read())

