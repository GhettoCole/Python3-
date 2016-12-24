# Working with files - making sure files are always closed after they have been used
# By using try/finally statement

try:
    """
    This ensures that the file is always closed
    even if an error occurs
    """
    f = open("filename.txt")
    print(f.readline())
finally:
    print("Done reading: Closing up the file")
    f.close()

try:
    f = open("new.txt")
    print(f.read())
finally:
    f.close()

# Alternative way of doing the above code, is by using with statements
# This creates a temporary variable( often called f) which is only accessible
# in the indented block of the with statement

with open("new.txt") as f:
    """
    This file is automatically closed at the end of the with statement
    Even if an exception occurs within it
    """
    print(f.read())
