# List Operations
# Certain item in a list can be reassigned

nums = [7,7,7,7,7]
print("Now the list is like: ",nums)
nums[2] = 5
print("Now the list is change to: ",nums)

nums = [1,2,3,4,5]
nums[3] = nums[1]
print(nums[3])

# Lists can be multiplied and added
nums = [1,2,3]
print(nums + [4,5,6,7])
print(nums * 3)

# To check if an item is in a list, the in operator can be used
# It returns True if the item occurs once or more and False if it doesn't

names = ["Given","Lepita","Lebohang","GhettoCole"]
print("GhettoCole" in names)
print("SHIT" in names)
print("Lepita" in names)

nums = [10,9,8,7,6,5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

# To check if an item is not the list, the not operator can be used.
nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(3 not in nums)
print(not 3 in nums)

letters = ["a","b","c","d","e"]
if "c" in letters:
    print("Programming is FUN")
