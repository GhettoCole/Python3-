# Exercise - 1 
# Given's way
print("Exercise - 1 (Derek banas tests)\n")

# Ask the user for two values and store them in the variables "num1" and "num2"

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


#  Add the numbers, subtract the numbers, perfom division on the numbers
# Multiply the numbers, Perform the modulus operation on the numbers
# Print results

_sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
print("{} + {} = {}".format(num1,num2,_sum))
print("{} - {} = {}".format(num1,num2,difference))
print("{} * {} = {}".format(num1,num2,product))
print("{} / {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,remainder))

# Derek Banas way

num1, num2 = input("Enter two numbers: ").split()

num1 = int(num1)
num2 = int(num2)


_sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
print("{} + {} = {}".format(num1,num2,_sum))
print("{} - {} = {}".format(num1,num2,difference))
print("{} * {} = {}".format(num1,num2,product))
print("{} / {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,remainder))

