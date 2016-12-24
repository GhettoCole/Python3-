# Given's way

print("Activity - 13 (Derek banas test)")

# Instructions
# Code a program that prompts the user to choose a shape
# Enter the variables needed to calculate area for the user

import math
def get_shape(shape):
	shape = shape.lower()

	if shape == "rectangle":
		rectangle_area()
	elif shape == "circle":
		circle_area()
	else:
		print("The only available choices are \'circle\' and \'rectangle\'")

def rectangle_area():
	length = float(input("Enter the length: "))
	width = float(input("Enter the width: "))

	area = length * width
	print("The area of the rectangle is: ",area)

def circle_area():
	radius = float(input("Enter the radius: "))

	area = math.pi * (math.pow(radius, 2))
	print("The area of the circle is: {:.2f}".format(area))

def main():
	shape_type = input("Get the area for what shape: ")

	get_shape(shape_type)

main()


