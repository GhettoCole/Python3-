# Boolean Logic
# Used to make more complicated conditions for if statements that rely on more than one condition
# and, or, not - are boolean operators


# using 'and' operator
x = (1 == 1 and 2 == 2)  # the and operator takes two arguments and evaluates as
#  True if and only if both arguments are True
y = (1 == 1 and 2 == 3)
z = (1 > 2 and 2 < 1)
print(x)
print(y)
print(z)

# ARGUMENT - A value passed to a function, when calling it.
# Simple example using Boolean operator

if (1 == 1) and (2 + 2 > 3):
    print('The passed in argument is true')
else:
    print('FALSE')

# Boolean Or operator
# The or operator takes two arguments evaluates to True if either (or both) of its arguments are True.
# Evaluates to False if both arguments are False

a = (1 == 1) or (2 == 2)
b = (1 == 1) or (2 == 3)
c = (2 < 1) or (3 > 6)
print(a)
print(b)
print(c)

# Simple example using the Boolean operator

age = 15
money = 500
if age > 18 or money > 100:
    print("BOOLEAN")

# Boolean Not operator
# Only takes 1 argument and inverts it

a = (not 1 == 1)
print(a)
b = (not 1 > 7)
print(b)

# Simple example using the Boolean operator

if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")
