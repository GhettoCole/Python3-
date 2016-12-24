import re

valid = "Given"
# checking if Given is a valid name
# If by law name must be within the length of 2 to 20

if re.search("\w{2,20}", valid):
    print("{} is a valid name".format(valid))
else:
    print("{} isn't a valid name".format(valid))

invalid = "K"
if re.search("\w{2,20}", invalid):
    print("{} is a valid name".format(invalid))
else:
    print("{} isn't a valid name".format(invalid))  # Working with white space
# \s : [\f\n\r\t\v] - matches white space any other special characters in the []
# \S : [^\f\n\r\t\v] - Disregards white space any other special characters in the []

# Searching if the first and last names are valid
name = 'Given Lepita'
if re.search("\w{2,20}\s\w{2,20}", name):
    print(name, "is a perfect name!")
else:
    print("Given and Lepita are rubbish names")
# + : matches one or more characters

print("MATCH: ", len(re.findall("a+", "a as ape bug")))
