# Exercise 2 
#  Given's way

print("Exercise - 3 (Derek banas test)\n")

# Store the user input of two numbers and the operator 
num1, operator, num2 = input("Enter calculation: ").split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# Provide output of the result based off on the user's choice of the operator
# Print the result
if operator == "+":
	print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
	print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
	print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
	print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
	print("{} % {} = {}".format(num1, num2, num1 % num2))
elif operator == "//":
	print("{} // {} = {}".format(num1, num2, num1 // num2))
else:
	print("An error occured!")




print("Additional work")

age = eval(input("Enter your age: "))

if ((age >= 1) and (age <= 18)):
	print("Your birthday is important")
elif (age == 21) or (age == 50):
	print("Your birthday is important")
elif not (age < 65):
	print("Your birthday is important")
else:
	print("Your birthday is not important")
