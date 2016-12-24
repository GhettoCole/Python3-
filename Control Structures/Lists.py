# Lists - Objects used to store an indexed list of items
# Lists are created using square brackets with commas
# Certain item in a list can be accessed using its index in square brackets

names = ["Given","Lepita","Lebohang"]
print(names[0]) # The first list item's index is 0 rather than 1
print(names[1])
print(names[2])

numbers = [5, 4, 3, 2, 1]
print(numbers[1]) # 4 will be indexed instead of 5

# Empty lists are created with an empty pair of square brackets
empty_list = []
print(empty_list)

# Lists can be nested to include different types of items

number = 3
things = ["Stuff",0,[1,2,number],4.56]
print(things[1])
print(things[2])
print(things[2][2])

# Indexing out of the bounds of possible list values causes an IndexError
# Indexing strings is possible but as for other types, like integers is not.
# Causes a TypeError

boom = "Hello World!"
print(boom[11])
