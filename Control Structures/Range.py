# Range function - creates a sequential list of numbers

numbers = list(range(10))
print(numbers)

nums = list(range(5))
print(nums[4])

# If range is called with one argument, it produces an object with values from 0 to that argument
# Argument - a value passed to a function (or method) when calling it
# If it is called with two arguments, it produces values from the first to the second

nums = list(range(3,8))
print(nums)

print(range(20) == range(0,20))

nums = list(range(5,8))
print(len(nums))

# Range can have a third argument, which determines the interval of the sequence produced
# The third argument must be a integer

numbers = list(range(5,20,2))
print(numbers)

nums = list(range(3,15,3))
print(nums[2])
