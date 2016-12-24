# Given's way 

print("Notes - Math functions")

import math

# method can be access by referencing the modules

print("ceil(4.4) = ",math.ceil(4.4))
print("floor(4.4) = ",math.floor(4.4))
print("fabs(-4.4) = ",math.fabs(-4.4))

# Factorial = 1 * 2 * 3 * 4 * ...
print("factorial(4) = ",math.factorial(4))

# Return remainder of a division
print("fmod(5,4) = ",math.fmod(5,4))

# Receive a float and return an integer
print("trunc(4.2) = ",math.trunc(4.2))

# Return x^y (exponentiation)
print("pow(4,4) = ",math.pow(4,4))

# Return the square root
print("sqrt(4) = ",math.sqrt(4))

# Special values
print("math.e = ",math.e)
print("math.pi = ",math.pi)

# Return e^x
print("exp(4) = ",math.exp(4))

# Return the natural logarithm of e * e * e ~= 20 so log(20)
# tells you that e ^ 3 ~= 20
print("log(20) = ",math.log(20))

# Can define thee base and the 10 ^ 3 = 1000
print("log(1000,10) = ",math.log(1000,10))

# Can also use the base 10 like
print("log10(1000) = ",math.log10(1000))

# Also the following trig functions
#  sin, cos, tan, asin, acos, atan, atan2,
# asinh, acosh, atanh, sinh, cosh, tanh

# Convert the radians to degrees and visa versa
print("degrees(1.5708) = ",math.degrees(1.5708))
print("radians(90) = ",math.radians(90))

# Different way of importing

from decimal import Decimal as D # creating an alias
sum = D(0)

sum += D("0.1") # incrementing for increase
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3") # decrementing to find the adequate difference

print("The sum = ",sum)

print(".1 + .1 + .1 - .3 = ",.1 + .1 + .1 - .3)

print("\nClassification of data types: \n")
print("String: ",type('GhettoCole'))
print("Integer: ",type(18))
print("Float: ",type(2.4535))
print("List: ",type(['GhettoCole',1]))
print("Tuple: ",type(("Given","Lepita")))
print("Dictionary: ",type({"Given":17}))
print("Boolean: ",type(True),"\n")

print("Strings")

string = "GhettoCole"

print("Last letter of {} is {}".format(string, string[-1]))
print("First letter of {} is {}".format(string, string[0]))
print("The length of {} is {}".format(string, len(string)))
print("Slice of {} from 0 to 6 is {}".format(string,string[0:6]))






