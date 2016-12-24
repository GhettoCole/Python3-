# Given's way

print("Activity - 11 (Derek banas test)")

# Instructions
# Code a program that solves for x
# X will always be the first value received
# And will only deal with addition


def solve_x():
	x, operator, number, equal, result = input("Enter the algebraic expression: ").split()
	print("Solve for x:\n")
	number = int(number)
	result = int(result)
	x = result - number
	print("x + {} = {}".format(number,result))
	print("x = {}".format(result - number))

solve_x()

# Derek banas way
def solve_eq(equation):
	x, add, num1, equal, num2 = equation.split()
	num1, num2 = int(num1), int(num2)

	return "x = " + str(num2 - num1) 


# print(solve_eq("x + 4 = 9"))

# HOMEWORK - Make the solving equation work for other operators
# * + - / // %


