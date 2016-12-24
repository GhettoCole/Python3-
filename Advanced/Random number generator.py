# Given's way

# Instructions
# Make a program that generates random numbers as a list

print("Activity - 14 (derek banas test)")
print("\nA Random number generator!!!")

import random
import math

nums = []

for i in range(5):
    nums.append(random.randint(0, 9))

print(nums)
for i in nums:
    print("A Random number: ", i)


