# The bubble sort
# 1. An outer loop decrease in size each time
# 2. The goal is to have the largest number at the end
# of the list when the outer loop completes cycle 1
# 3. The inner loop starts comparing indexes at the
# beginning of the loop
# 4. Check if list[index] > list[index + 1]
# 5. Is so, swap the index values
# 6. When the inner loop completes the largest number
# at the end of the list
# 7. Decrement the outer loop by 1


import random
import math

numList = []  # Create an empty list/array

for i in range(5):  # for i in the range of 5 (Items)
    numList.append(random.randint(1, 10))  # add 5 random integers from 0 to 10

i = len(numList) - 1  # Minus 1 from the length of numList ( 5 - 1 = 4)

while i > 1:  # While i is bigger than 1 do as follows
    j = 0  # set j to 0
    while j < i:  # so long as 0(j) is smaller than i, do as follows
        print("\nIs {} > {}".format(numList[j], numList[j+1]))  # print index of j and another of j + 1
        if numList[j] > numList[j + 1]:  # If the index of j is bigger than index of j + 1
            print("Switch")  # print switch and do so
            temp = numList[j]  # Give a new variable the value of the numList[j] for switching purposes
            numList[j] = numList[j + 1]  # numList[j] is now numList[j + 1]
            numList[j + 1] = temp  # and now that numList[j + 1] is switched with temp(numList[j])
        else:
            print("Don't switch") # else if the numList[j] is < than numList[j + 1] then don switch

        j += 1  # increment j by 1 each time
        for k in numList:  # for k in numList
            print(k, end=", ")  # print k separated by a comma
        print()  # newline

    print("End of round!")  # end of the checking round
    i -= 1  # then decrement i

for k in numList:  # for k in numList - smaller to biggest
    print(k, end=", ")  # print k separated by a comma
print("\n")

# The bubble sort
# 1. An outer loop decrease in size each time
# 2. The goal is to have the largest number at the end
# of the list when the outer loop completes cycle 1
# 3. The inner loop starts comparing indexes at the
# beginning of the loop
# 4. Check if list[index] > list[index + 1]
# 5. Is so, swap the index values
# 6. When the inner loop completes the largest number
# at the end of the list
# 7. Decrement the outer loop by 1

print("\nSecond bubble sort\n")
numbers = [13, 3, 5, 2, 8, 2, 11, 45, 11, 88, 21, 90]

i = len(numbers) - 1

while i > 1:
    j = 0
    while j < i:
        print("\nIs {} > {}".format(numbers[j], numbers[j+1]))
        if numbers[j] > numbers[j+1]:
            print("Switch")
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
        else:
            print("Don't switch!")

        j += 1
        for k in numbers:
            print(k, end=" ")
        print()
    print("End of round\n")
    i -= 1

for k in numbers:
    print(k, end=' => ')
print("\n")


random_nums = [1, 1, 0, 33, 22, 11, 44, 55, 333, 888, 9, 999, 7]

random_nums.sort()  # Auto sorting values
print("Ascending sort: ", random_nums)
random_nums.reverse()  # Reverse sorting
print("Reverse sort: ", random_nums)

random_nums.insert(13, 1000)
print("New value added: ", random_nums)
random_nums.remove(888)
print("888 is removed: ", random_nums)
random_nums.pop(-1) # Removes the last value of the list by the -1 index
print("1000 is \'pop\'ed out: ",  random_nums)


# List comprehension
print("\nList Comprehension\n")
evens = [i*2 for i in range(10)]
for i in evens:
    print("Even number: ", i)

print("\n")

nums = [1, 2, 3, 4, 5]
values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4), math.pow(m, 5)]
          for m in nums]

for i in values:
    print(i)

multDlist = [[0] * 10 for i in range(10)]
multDlist[0][1] = 10
print(multDlist[0][1])

print("\nCreating a multidimensional list\n")

table = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        table[i][j] = "{} : {}".format(i, j)

for i in range(4):
    for j in range(4):
        print(table[i][j], end=' || ')
    print("\n")


# Recursive functions
# A function that refers to itself

# 4! = 4 * 3 * 2 * 1

def factorial(num):
    # When the number reaches 1 then stop factorial process
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

#  result = num * factorial(num - 1)
#  1st: result = 4 * factorial(3)
#  2nd: result = 3 * factorial(2)
#  3rd: result = 2 * factorial(1) // Then the factorial stops because 1 is reached

print("4! = ",factorial(5))
