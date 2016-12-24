import re
# Regular expressions 

animals = "cat bat rat mat"
# matches anything that end with 'at' and anything that
# starts with one of the letters in the square brackets
all_animals = re.findall("[crmfp]at", animals)

for i in all_animals:
	print(i)

# Searches for a series of matches between lower case c-m 
# And upper case C-M and that end with 'at'

few_animals = re.findall("[c-mC-M]at", animals)

for i in few_animals:
	print(i)
# Finds any word that doesn't have J or j and ends with 'e'
people = "Jason jacob jakal GiveyGee GhettoCole Grizele"
persons = re.findall("[^Jj]e", people)

