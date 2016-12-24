# Given's way

print("Activity - 12 (Derek banas test)")

# Instructions
# Make a program that looks for prime numbers
# From up to a gien point

# Hints - a prime is divisible by 1 and itself
# Use a for loop and check if the modulus == 0

def is_prime(num):
	for i in range(2,num):
		if (num % i) == 0:
			return False
	return True

def getPrimes(max_number):
	list_of_primes = []
	for num1 in range(2,max_number):
		if is_prime(num1):
			list_of_primes.append(num1)
	return list_of_primes

max_num_toCheck = int(input("Search for a prime from up to: "))

list_of_primes = getPrimes(max_num_toCheck)
print("\nPrimes present from up to {}\n".format(max_num_toCheck))
for prime in list_of_primes:
	print(prime)





