# Printing out all contents of a file
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

# To read only a certain amount of a file
# Provide number as an argument to the read function
# More calls can be made to read on the same file

file = open("filename.txt", "r")
print(file.read(4))
print(file.read(6))
print(file.read())  # reads more of the file byte by byte
file.close()

file = open("filename.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()

# After all contents in a file have been read, any attempts to read further from that file will turn
# Into an empty string, because you are trying to read from a the end of the file
file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("finished")
file.close()

file = open("filename.txt","r") # open
str = file.read() # read contents
print("The read file has the length of: ",len(str)) # print file length
file.close()

# To retrievie each line in a file, you can use readlines method to return a list
# In which each element is a line in the file
file = open("filename.txt","r")
print(file.readlines())
file.close()

# for loops can be used to iterate through the lines in the file
file = open("filename.txt","r")

for line in file:
    """
    In the output the lines are separated by blank lines
    as the print function automatically adds a new line
    at the end of its out put
    """
    print(line)

file.close()

