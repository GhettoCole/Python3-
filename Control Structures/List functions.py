# List Functions
# A way of altering with lists
# The append method is used to add an item to the end of an existing list



nums = [1,2,3]
nums.append(4) # The dot before append is the because it is a method of the list class

print(nums)
# Method - like a function, but it runs "on" an object

words = ["GhettoCole"]
words.append("GiveyG")
print(words[1])

# To get the number of items in a list, the len function is used
# Function - a parameterized sequence of statements, It is written before the list it is being called on, without a dot.
nums = [1,2,3,4,5,6,7,8,9,10]
print(len(nums))

letters = ["a","b","c"]
letters.append("d")
print(len(letters))

# The insert method is used to insert a new item in a list at any position.
words = ["Python","fun"]
index = 1
words.insert(index, "is")
print(words)

nums = [9,8,7,6,5]
nums.append(4)
nums.insert(2,11)
print(nums)
print(len(nums))

# The index method is used to find the first occurence of a list item and returns its index.
# If the item isn't there, it raises  ValueError

letters = ['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))


nums = [1,2,3,4,5,6,7,8,9,10]
print(max(nums)) # Function that finds the maximum value in a list
print(min(nums)) # Function that finds the minimum value in a list
print(nums.count(7)) # Method used to count how many times an item occures in a list
nums.remove(10) # Method used to remove an item from a list
nums.reverse() # Method used to reverse objects in a list
print(nums)
