# Notes
string = "   given once said \"Programming is like writing poetry, it soothes your mind\".    "
print(string)
string = string.lstrip() # Take out the space on the left, hence (l)strip 
string = string.rstrip() # Take out the space on the right, hence (r)strip
string = string.strip() # Takes out the white space on all sides
print(string.capitalize()) # Capitalizes the first letter
print(string.upper()) # Changes the string to uppercase
print(string.lower()) # Changes the string to lowercase

a_list = ["Programming","is","fun","and","productive!"]
print(a_list) # normal form
print(" ".join(a_list)) # converting the list into strings


another_list = string.split() # converting in a list
for i in another_list:
	print(i)

# print(list(string)) -> another way

print("This \'it\' occures {} times in the string".format(string.count("it")))
print("This \'like\' word occures at index {} in the string".format(string.find("like")))
print(string.replace("soothes ", "calms "))


z = "z"
num = "3"
space = " "
num_fl = "3.14"

print("Is {} a letter or number: ".format(z),z.isalnum())
print("Is {} a letter: ".format(z),z.isalpha())
print("Is {} a letter or number: ".format(num), num.isdigit())
print("Is {} a lowercase: ".format(z),z.islower())
print("Is {} a uppercase: ".format(z),z.isupper())
print("Is {} (space) a space: ".format(space),space.isspace())
# Function can be used to check for float if is a float
print("First method")
print("Is {} a float: ".format(num_fl),num_fl.isalnum())


def isFloat(str_value):
	try:
		float(str_value)
		return True
	except ValueError:
		return False
print("Second method")
print("Is {} a float: ".format(num_fl),isFloat(num_fl))
