# Regular expressions

import re

# A period can be used is used to match any one character or a space
test = "I Am Given Lepita, I am 16 years old and I go to school at CSS\nThough sometime I don't enjoy because it is cold\n I may scold and be bold but I love to hold"



if re.search("old.", test):
	print("Matches")

all_olds = re.findall("old.", test)

if re.search("ape", "The ape was at the apex"):
	print("There is an ape")

allApes = re.findall("ape", "There is an ape in the corner"\
	"Another ape is hiding under my bed and lastly the ape named 'Giblo' is at the forest")

for i in allApes:
	print(i)

for i in all_olds:
        print(i)

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
	# Creating a tuple with span function/method
	locTuple = i.span()
	print(locTuple)
	print(theStr[locTuple[0]:locTuple[1]])