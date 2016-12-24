# ***else Statements***
# an else statement follows an if statement and contains a code that is called when the if statement evaluates to False
# The code inside should be indented

x = 4
if x == 5:
    print("Yes")
else:
    print("No")


if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("False")
    else:
        print("True")

# else and if statements can be chained together to determine which option in a series of possibilities is true

num = 7
if num == 5:
    print("Number is 5")
else:
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else:
            print("The number isn't one of them!")

x = 10
y = 20
if x > y:
    print("if statement")
else:
    print("else statement")

# elif statements (short of else if) - shortcut of chaining if and else statements
# A series of if elif statements can have a final else block - called when none of the if and elif statements are not True
