# Operator precedence - an extension of the mathematical idea of order of operations
# multiplication being perfomed before addition, ect.

# Precedence example

x = False == False or True
print(x)
y = False == (False or True)
print(y)
z = (False == False) or True

# Precedence using an if statement
if 1 + 1 * 3 == 6:
    print("yes")
else:
    print("no")

a = 4
b = 2
if not 1 + 1 == b or a == 4 and 7 == 8:
    print("Bravoo!!")
elif a > b:
    print("Excellent")
