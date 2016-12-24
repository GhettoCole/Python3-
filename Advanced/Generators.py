# Generators

def isprime(num):
	for i in range(2, num):
		if num % 2 == 0:
			return False
	return True

def prime_generator(max_number):
	for num1 in range(2, max_number):
		if isprime(num1):
			yield num1

try:
	prime = int(input("Generate prime numbers: "))
	primes = prime_generator(prime)


	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
	print("Prime number: ", next(primes))
except (ValueError, TypeError, StopIteration):
	print("An error occurred!!")


# Generator expressions

print("\nCreated using a generator expression\n")
double = (x * 2 for x in range(100))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))
print("Double: ", next(double))

for num in double:
	print(num)