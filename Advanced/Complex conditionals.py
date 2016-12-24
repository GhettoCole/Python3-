# Get the number of rows for the trre
tree_height = input("Enter the tree height: ")
# Conver into an integer
tree_height = int(tree_height)

# Get the starting spaces for the top of the tree
spaces = tree_height - 1
# There is one hash to start will be incremented
hashes = 1
# Save stum spaces till later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while  tree_height != 0:
	for i in range(spaces):
		print(" ", end="")
	for i in range(hashes):
		print("|", end="")
# Print the spaces
	print()
# Newlines after each row
	spaces -=1
# THe spaces decremented by 1 each time
	hashes += 2
	tree_height -= 1
# Decrement tree height each time to jum out of the loop

# Printthe spaces befor the stum and then the hash
for i in range(stump_spaces):
	print(" ", end="")
if tree_height % 2 != 0:
        print("#")
elif tree_height % 2 == 0:
        print("#")
