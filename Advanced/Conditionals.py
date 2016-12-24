#  Given's way

print("Exercise - 5 (Derek banas test)\n")
print("Corrected")

# Write a program that calculates compounded interest over time give

money = input("How much to invest: ")
interest_rate = input("Interest Rate: ")

money = float(money)

interest_rate = float(interest_rate) * .01 # Producing a 2 decimal answer

for i in range(10):
	money = money + (money * interest_rate)

print("Investment after 10 years: {:.2f}".format(money))


print("Additional work")

age = 56
# if age is both greater than or equal to 1 and less than or equal to 18 Important
if (age >= 1) and (age <= 18):
	print("Important birthday!")
# if age is either 21 or 50 Important
elif (age == 21) or (age == 50):
	print("Important birthday!")
# We check if age is less than 65 and then convert true to false
elif not (age < 65):
	print("Important birthday!")
# All others -> Not important
else:
	print("Not important")

print("\n")
# Activity 2
'''
If age is 5, Go to kinder garden
Age of 6 through 17 goes to grades 1 through 12
If age is greater than 17, say go to college
challenge - complete with 10 or less lines of code
'''

age = eval(input("Enter age to determine proper grades: ")) # line 1
if age <=  5: # line 2
	print("Go to kinder garden!") # line 3
elif (age >= 6) and (age <= 17): # line 4
	print("Goes to grades of 1 through 12!") # line 5
elif (age > 17): # line 6
	print("Goes to college!") # line 7

# Different method/way

age = eval(input("Enter age: "))

if age < 5:
	print("Too young for school")
elif age == 5:
	print("Go to kinder garden")
elif (age > 5) and (age <= 17):
	grade = age - 5
	print("Go to grade {} ".format(grade))
else:
	print("Go to college")
