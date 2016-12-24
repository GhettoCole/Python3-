import re

# You need to split a string into fields, but the delimiters (and spacing around them) are'nt
# consistent throughout the string.

line = 'asdf fjdk; afed, fjek,asdf,        foo'
print(re.split(r"[;,\s]\s*", line))