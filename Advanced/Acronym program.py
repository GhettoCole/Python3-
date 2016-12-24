# Given's way 

print("Exercise - 9 (Derek banas test)")


# Instructions
# Ask the user for input and make an acronym of their input
# And print out the results

string = input("Enter the initials: ") # Ask for user input
string = string.upper() # set user input to uppercase
the_list = string.split() # split user's input by space a make a list

for i in the_list: # for each word in the list 
	print(i[0].upper(), end="") # Print the first word's letter and separate them by nothing 

print("\nYou text has been acronym\'ised\'")

# Derek banas solution
orig_string = input("Convert to acronym: ")
orig_string = orig_string.upper()

list_of_words = orig_string.split()
for word in list_of_words:
        print(word[0], end="")

print() # Adding a new line

