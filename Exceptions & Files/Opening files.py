# Texts are the easiest to manipulate, before a file can be edited
# It must be opened using the open function

"""
example - myfile = open("filename.txt")
"""
# The argument of the open function is the path to the file
# If the file is in the same directory as the program you can only specify its name

# You can specify a mode used to open a file by applying a second argument to the open function

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

# once a file has been open and used, you can/should close it
# This is done with the close method of the file object
file = open("filename.txt", "w")

# do stuff to that file
file.close()
