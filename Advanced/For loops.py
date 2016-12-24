#  Given's way

print("Exercise - 4 (Derek banas test)\n")

print("Printing Odd numbers (Solution 1)\n")
# Write a program that iterates through a loop 
# And prints out the odd numbers from 0 to 20
for i in range(20):
	if (i % 2) != 0:
		print("Odd number: ",i)
		i += i

print("\nPrinting Even numbers (Solution 1)\n")

# Write a program that iterates through a loop 
# And prints out the even numbers from 0 to 20
for i in range(20):
	if (i % 2) == 0:
		print("Even number: ",i)
		i += i


print("Printing Odd numbers (Solution 2)")

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
	if i % 2 != 0:
		print("Odd: ",i)
		i += i

print("Printing Even numbers (Solution 2)")

for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
	if i % 2 == 0:
		print("Even: ",i)
		i += i


float_ = float(input("Enter a float: "))
print("{:.2} - rounded to 2 decimal places".format(float_))
