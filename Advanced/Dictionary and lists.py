# Given's way

print("Activity - 16 (derek banas test)")

# Instructions
# Make a program that prompts the user for input
# Let the user enter a first name and last name
# until they are satisfied and then they can stop
# and then print out what they entered

values = []

while True:
	ask = input("Enter customer(Yes/No): ")
	ask = ask[0].lower()

	if ask == "n":
		break
	else:
		first_name, last_name = input("Enter custumer name: ").split()
		values.append({"First name": first_name, "Last name": last_name})
print("\nSaved customers\n")
for value in values:
	print(value["First name"],value["Last name"])


