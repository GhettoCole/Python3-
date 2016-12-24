# Heads and Tails
# ----PROBLEM----
# Create a random list filled with characters H and T
# For heads and tails. Output the numbers of Hs and Ts
# Example Output
# Heads : 46
# Tails : 54
from random import choice


flips = []

for i in range(1,101):
	flips += choice(["H", "T"])

print("Heads: ", flips.count("H"))
print("Tails: ", flips.count("T"))


print("\nNumber of different types of genders in the world\n")

genders = []

for i in range(1,90000):
        genders += choice(["M", "F"])

print("Males: ", genders.count("M"))
print("Females: ", genders.count("F"))
