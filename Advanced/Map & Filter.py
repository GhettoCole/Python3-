# Map Functions - allows us to execute a function on each item in a list

one_to_10 = range(1, 11)


def double_number(number):
    return number * 2


print(list(map(double_number, one_to_10)))

print(list(map((lambda x: x * 3), one_to_10)))

aList = list(map((lambda x, y: x + y), [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))

print(aList)

# Filter selects an item from a list based off on a function

print(list(filter((lambda x: x % 2 == 0), range(1, 50))))
