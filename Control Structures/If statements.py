# if Statements - used to run code if a certain condition holds
# if an expression evaluates to True, some statements are carried out. Otherwise they are'nt carried out
# The statement within an if statement should be indented

if 10 > 5:
    print("10 is greater than 5")

print("Program ended")


# Another simple example

seven = 7
if seven > 5:
    print("FIVE")
if seven > 8:
    print("EIGHT")

# To perform more complex checks, if statements can be nested. One inside the other

num = 12
if num > 5:
    print("Twelve is bigger than five")
    if num <= 47:
        print("Between 5 and 47")

# Another simple example

numb = 7
if numb > 3:
    print("3 is smaller")
    if numb < 5:
        print("5 is bigger")
        if numb == 7:
            print("The number is 7")


