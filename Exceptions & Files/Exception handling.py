# Exception handling - to handle exceptions and to call code when an exception occurs
# Use try/except statement
# The try block contains code that might throw an exception. If an exception occurs

try:
    num1 = 7
    num2 = 0
    print(num1 / 2) # Origin of an error
    print("Calculation done.")
except ZeroDivisionError: # Catching the error by name
    print("An error occurred\nThis is due to a zero division error")

# A try statement can have multiple different except blocks to handle different exceptions
# Multiple exceptions can be put into a single except block using parentheses
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("An error occurred due to a zero division")
except (ValueError, TypeError):
    print("An error occurred due to the data type and values provided")
    
# An except statement without any exception specified will catch all errors
try:
    word = "GhettoCole"
    print(word+10)
except:
    print('An error occurred')
    