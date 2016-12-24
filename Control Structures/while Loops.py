# While loops
# While loops can be run more than once, the conditions inside it are repeatedly executed so long as the condition holds.
# Once it evaluates to false the next section of code is executed.

i = 1
while i <= 5:
    print(i)
    i = i + 1

print("The while loop is finished")
# The code in the body of the while loop is executed repeatedly - This is called **iteration**

a = 4
while a >= 0:
    print(a)
    a = a - 1

x = 0
while x <= 20:
    print(x)
    x += 2 # Increments the value of x by 2 and prints the even values

# The break statement can be used to end a while loop, prematurely
# When encountered inside a loop, the break statement causes the loop to finish immediately
b = 0
while 1 == 1:
    print(b)
    b = b + 1
    if b >= 5:
        print("Breaking the loop")
        break
    print("Program finished")
# Using the break statement outside a loop causes an error

y = 5
while True:
    print(y)
    y = y - 1
    if y <= 2:
        break

# The continue statement can be used to jumb to the top of the loop, rather than breaking it
# The continue statement breaks the curren iteration and continues with the next one

i = 0
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking the loop")
        break
    print(i)

print("Program finished")
# Using the continue statement outside of a loop causes an error

# Infinite loops - never stops running, its condition always remains True
while 1 == 1:
    print("Infinite Loop") # Can be stopped with Ctrl-C or by closing the program.

names = ["GhettoCole","Given","GiveyG","Lepita"]
counter = 0
max_index = len(names) - 1

while counter <= max_index:
    name = names[counter]
    print(name + "!")
    counter = counter + 1
