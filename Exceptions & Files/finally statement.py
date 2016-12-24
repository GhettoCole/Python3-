# Finally - to ensure that code runs no matter what error occurs, use a finally statement
# The finally statement is placed at the bottom of a try/except statement
# Code within a finally statement always runs after execution of the code in the try
# And possibly in the except blocks

try:
    print("Making a ZeroDivisionError on purpose")
    print(1 / 0)
except ZeroDivisionError:
    print("A division error occurred")
finally:
    print("This code will run no matter what!")

# Code in a finally statement even runs after an uncaught exception occurs
# In one of the preceding blocks

try:
    print(10 / 0)
except ZeroDivisionError:
    print("A ZeroDivisionError occurred")
finally:
    print("This is executed last!")
