# Given's way

print("Activity - 17 (derek banas test)")


# Instructions
# Create a program that prints out the fibonacci numbers
# Of a passed in argument

# Hints
# Fn = Fn-1 + Fn-2
# If Fn = 0 and Fn = 1
# Return them else continue

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result


print(fib(5))
print(fib(6))
print(fib(7))
numFib = int(input("How many fibonacci numbers to display: "))
i = 0
while i < numFib:
    fibvalue = fib(i)
    print(fibvalue)
    i += 1

print("All done")
