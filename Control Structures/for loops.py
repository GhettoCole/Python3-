# Loops

# This iterates through all items in a list
# Accesses them through their indices and prints them with exclamation marks
names = ["GhettoCole", "Given", "GiveyG", "Lepita"]
counter = 0
max_index = len(names) - 1

while counter <= max_index:
    name = names[counter]
    print(name + "!")
    counter += 1

languages = ['Python', 'C++', 'JavaScript', 'C#', 'Swift', 'Android', 'Java', 'Ruby', 'ASP.net', 'VB.net']
count = 0
maximum = len(languages) - 1
while count <= maximum:
    language = languages[count]
    print("I program in", language)
    count += 1

#  Shortcut of iterating through a loop is with a for loop
cars = ["Porsche", "Ferrari", "Mercedes benz", "Polo GTI"]
for car in cars:
    print(car + "!")

letters = ['a', 'b','c']
for l in letters:
    print(l)

for i in range(10):
    print("Programming is fun!")

# Printing only even numbers in a range
for i in range(0, 20, 2):
    print(i)
