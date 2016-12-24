# Using reduce

from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 6)))
print(reduce((lambda x, y: x + y), range(1, 100)))
