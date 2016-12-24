import random

my_dict = {
	"Base-2 number system" : "binary",
	"Number system that uses characters 0-F" : "hexidecimal",
	"7-bit text encoding standard" : "ascii",
	"16-bit text encoding standard" : "unicode",
	"A number that is bigger than the maximum number that can be stored" : "overflow",
	"8 bits" : "byte",
	"1024 bytes" : "kilobytes",
	"The smallest component of a bitmapped image" : "pixel",
	"A continuosly changing wave, such as sound" : "analogue",
	"The number of times per second that a wave is measured" : "simple rate",
	"A binary representation of a program" : "machine code"
}

print("Computing Revision Quiz - Given Lepita")
print("==============================================")
print("This is for reference purposes and tests!!")
print("==============================================")


playing = True
while playing == True:
	score = 0
	num = int(input("\nHow many questions would you like: "))

	for i in range(num):
		question = (random.choice(list(my_dict.keys())))
		answer = my_dict[question]

		print("\nQuestion " + str(i+1))
		print(question + "?")

		guess = input("answer: ")
		
		if guess.lower() == answer.lower():
			print("Correct!!")
			score += 1
		else:
			print("Wrong answer!")

	print("\nYour final score is " + str(score))

	again = input("Enter any key to play again, or \'q\' to quit!")
	if again.lower() == 'q':
		playing = False
