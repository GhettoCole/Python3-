# In except blocks, the raise statement can be used without arguments to re-raise whatever exception

try:
    num = 5 / 0
except:
    print("An error occured")
    raise


# raise statement is used for raising exception
try:
    print(1)
    raise ValueError
    print(2)

# Need to specify the type the exception raised
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError

# Exceptions can be raised with arguments that give detail about them
finally:
    name = "123"
    raise NameError("Invalid name!")

num = input(":")
if float(num) < 0:
    raise ValueError("Negative")

