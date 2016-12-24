# Exceptions - means of breaking out of normal flow of control of a code block in order to handle errors
# or other exceptional conditions
# They occur when something goes wrong, due to incorrect input or incorrect code
try:
    num1 = 7
    num2 = 0
    print(num1/num2)
except ZeroDivisionError:
    print("A ZeroDivisionError Occured")

print('''Different exceptions are raised for different reasons
common exceptions:
ImportError: an import fails
IndexError: a list is indexed with an out-of-range number
NameError: an unknown variable is used
SyntaxError: the code can't be parsed properly
TypeError: a function is called on a value in an appropriate type
ValueError: a function is called on a value of correct type, but an inappropriate value
''')
# Python has several other built-in exceptions
# Such as ZeroDivisionError and OSError
# Third-party libraries also often define their own exceptions
