# List comprehensions

print(list(map((lambda x: x * 2), range(1, 11))))

# Using list comprehension to generate the same output
print([2 * x for x in range(1, 11)])

# Using the filter to output odd numbers
print(list(filter((lambda x: x % 2 != 0), range(1,31))))

# Using list comprehension to generate the same output
print([x for x in range(1,31) if x % 2 != 0])

# Generate 50 values
# Take each value to the power of 8
# Return multiples of 8

print([i ** 2 for i in range(50) if i % 8 == 0])


# Using multiple for loops in a list comprehension
print([x * y for x in range(1,4) for y in range(8, 15)])


# Generate a list of 10 values
# Multiply them by 2
# Return multiples of 8


print([x for x in [i * 2 for i in range(10)]])

# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9 using a list comprehension

from random import randint

print([x for x in [randint(1,1001) for i in range(50) if x % 9 == 0]])

multidemensional = [[1,2,3],[4,5,6],[7,8,9]]
print([col[1] for col in multidemensional])

print([multidemensional[i][i] for i in range(len(multidemensional))])