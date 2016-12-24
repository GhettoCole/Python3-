import re

owl_food = "rat mat pat cat"
regex = re.compile("[cr]at")  # Compiles anything that starts
# with c or r and ends with 'at'

owl_food = regex.sub("owl ate me", owl_food)  # Sub replaces the matches

random = "Here is \\Given"  # Regex uses \\ slashes and so confuse python
# Example
print("Here is \\Given: ", re.search("\\Given", random))

# Correct way of matching \\Given
print("Here is \\Given: ", re.search("\\\\Given", random))

# Easier way with raw string
print("Here is \\Given: ", re.search(r"\\Given", random))  # Does the same shit

orgs = "F.B.I. I.R.S CIA"
print("\nSecret organisations: ", orgs)
# Matching anything that has a period(.)

print("Matches: ", len(re.findall(".\..\..\.", orgs)))

randStr = '''This is a long
string that goes
on for many line'''
# Replacing new lines with space
print(randStr)

regex = re.compile("\n")
randStr = regex.sub(" ", randStr)
print(randStr)

# \b : Backspace
# \f : Form feed
# \r : Carriage return
# \t : Tab
# \v : Vertical Tab

# \d : [0-9] Matches all numbers from 0-9
# \D : [^0-9] Disregards all numbers from 0-9
numbers = '0123456789'

print("Matches: ", len(re.findall("\d", numbers)))  # Matches any digits
print("Matches: ", len(re.findall("[0-9]", numbers)))  # Matches any digits
print("Matches: ", len(re.findall("\D", numbers)))  # Doesn't match any digits
print("Matches: ", len(re.findall("[^0-9]", numbers)))  # Doesn't match any digits

# Curly brackets match in multiple numbers
print("Matches: ", len(re.findall("\d{5}", numbers)))
print("Matches: ", len(re.findall("\d{2}", numbers)))

# Matching numbers that are within range

numStr = "123 12345 123456 1234567 12345678 123456789"
print("Numbers in range of 5-9: ", len(re.findall("\d{5,9}", numStr)))

# \w : [a-zA-Z0-9_] matches all case letters, numbers and underscores
# \W : [^a-zA-Z0-9_] Disregards all case letters, numbers and underscores


# Matching numbers 
phone_numbers = "412-555-1212"

print("Check if {} is a valid phone number!".format(phone_numbers))

if re.search("\w{3}-\w{3}-\w{4}", phone_numbers):
    print("{} is a valid phone number!".format(phone_numbers))

phone_numbers1 = "241-352-525"
print("Check if {} is a valid phone number".format(phone_numbers1))

if re.search("\w{3}-\w{3}-\w{4}-", phone_numbers1):
    print("{} is a valid phone number".format(phone_numbers1))
else:
    print("{} isn't a valid phone number!".format(phone_numbers1))
