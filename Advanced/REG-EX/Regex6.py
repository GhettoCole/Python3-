import re

text = 'cat cats'

regex = re.compile('[cat]+s?')

match = re.findall(regex, text)

print("Matches: ")
for i in match:
	print('-->', i)

med = "Doctor Doctors Doctor's"

regex = re.compile("[Doctor]+['s]*")

match = re.findall(regex, med)
print("Matches found: ")
for i in match:
	print('-->', i)

random_string = '''Just some words
and some more
and even more'''

regex = re.compile('[\w\s]+[\r]?\n')

matches = re.findall(regex, random_string)

for i in matches:
	print(i)

# Greedy matching

text = '<name>GhettoCole In The Hood</name><name>Hoods for Ass Goods<name/>'

# Greedy matching
regex = re.compile('<name>.*</name>')

matches = re.findall(regex, text)
for i in matches:
	print(i)


# Lazy matching

text = '<name>GhettoCole In The Hood</name><name>Hoods for Ass Goods<name/>'

# Lazy matching - matches smallest match possible
regex = re.compile('<name>.*?</name>')

matches = re.findall(regex, text)
for i in matches:
	print(i)

# Sub-expressions

text = '<name>GhettoCole In The Hood</name><name>Hoods for Ass Goods<name/>'

# Sub-expressions
regex = re.compile('<name>(.*?)</name>')

matches = re.findall(regex, text)
for i in matches:
	print(i)

# Word boundaries for matching desired number of matches using \b

words = 'ape at the apex'

regex = re.compile(r'\bape\b')
matches = re.findall(regex, words)
print("Match --> ", matches, end=' ')


sentence = 'Match everything up to @'
regex = re.compile(r'^.*[^@]')
match = re.findall(regex, sentence)
print('Match: ', match)

sentence = '@ Matched after me'
regex = re.compile(r'[^@\s].*$')
match = re.findall(regex, sentence)
print('Match: ', match)

wow = '''Ape is big
Turtle is slow
Cheetah is fast
Lion is King
'''

regex = re.compile(r'(?m)^.*?\s')

match = re.findall(regex, wow)
print('Matches: ', match, end='\n')

sentence = 'My number is 412-443-333'
regex = re.compile(r'412-(.*)')
match = re.findall(regex, sentence)
print('Match: ', match)