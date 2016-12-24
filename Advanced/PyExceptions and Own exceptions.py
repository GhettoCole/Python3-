# Exception handling

try:
    aList = [1, 2, 3, 4, 5, 6, 7]
    print(aList[9])  # Catching an exception that in out of range in index
except IndexError:
    print("The index \'9\' doesn't exist")


# Catching an unknown error
# except:
#    print("An error has occurred")


# Self made exceptions

class DogNameError(Exception):  # Create a class and pass in the parameter of Exception
    def __init__(self, *args, **kwargs):  # Initialise init the *args and **kwargs

        Exception.__init__(self, *args, **kwargs)  # Initialise the class's parameter


try:
    dogName = input("What is your dog's name: ")  # Prompt the user for input

    if any(char.isdigit() for char in dogName):  # Check if any character in the dog's name is a digit
        raise DogNameError  # If so raise an exception(self-defined)
except DogNameError:  # pass in the response due to DogNameError
    print("Your dog's name can't contain a number!")

num1, num2 = input("Enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))
except (ZeroDivisionError, ValueError):
    print("An error occurred due to a Zero Division Attempt/Value Error")
else:
    print("You didn't cause an error(\'You didn't raise an exception\')")
finally:
    print("This is executed no matter if an exception is raise or not")


# More self made exceptions

class NetworkError(RuntimeError):
    def __init__(self, *args):
        self.args = args


try:
    raise NetworkError("Bad Hostname!")
except NetworkError as e:
    print(e.args)


class BadNameError(Exception):
    def __init__(self, *args, **kwargs):
        """
        INITIALISE THE ARGUMENTS AND KEYWORD ARGUMENTS
        """
        self.args = args
        self.kwargs = kwargs


name = str(input("Enter your name: "))
try:
    if any(char.isdigit() for char in name):
        raise BadNameError
except BadNameError:
    print("A normal human's name can't have digits in it")
