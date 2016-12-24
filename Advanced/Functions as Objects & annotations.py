def multiply(number):
	return number * 2

times2 = multiply
print("10 * 2 =", times2(10))

# Passing a function into a function

def do_math(func, num):
	return func(num)

# func = multiply (_Which is equal to * 2)

print("8 * 2 =",do_math(multiply, 8))

def function_multiplied(number):
	def multiply_by(value):
		return number * value

	return multiply_by

generated = function_multiplied(5)
print("5 * 10 =", generated(10))

listOfFunctions = [times2, generated]
print("5 * 9 =",listOfFunctions[1](9))

# ------PROBLEM---------
# Create a funciton that receives a list and a function
# The function passed will return True or False if a list value is odd
# THe surrounding function will return a list of odd numbers
def is_it_odd(num):
	if num % 2 == 0:
		return False
	else:
		return True

def change_list(list, func):
	oddList = []

	for i in list:
		if func(i):
			oddList.append(i)

	return oddList

aList = range(1,20)

print(change_list(aList, is_it_odd))

# Function annotations

def random_func(name: str, age: int, weight: float) -> str:
	print("Name: ",name)
	print("Age: ",age)
	print("Weight: ",weight)

	return "{} is {} years old and weighs {} pounds".format(name, age, weight)

print(random_func("Given", 17, 65.5))
# Will not get an error if unmatched data types are passed inside
print(random_func(89, "Derek", "Turtle"))
print(random_func.__annotations__)
