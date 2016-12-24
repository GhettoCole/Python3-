# -----PROBLEM------
# Find the multiples of 9 from a random 100 value list with values 1 and 1000
# Tips
# Generate a random list with randint between 1 and 1000
# Use range to generate 100 values
# Use modulus to find the multiples of 9

from random import randint
randList = list(randint(1,1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), randList)))
