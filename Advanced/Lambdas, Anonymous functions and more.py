import random

# Anonymous functions/ lambdas

sum_ = lambda x, y: x + y
print("10 + 85 = ", sum_(10, 85))

# Ternary operator to see if someone can vote

can_vote = lambda age: True if age >= 18 else False

usr = int(input("Enter age to see if your applicable for voting: "))
print("Can vote(True/False): ", can_vote(usr))

powerList = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
print("Powers of 4 to 2, 3 and 4")
for each in powerList:
    print(each(4))

# Using lambdas inside dictionaries

attack = {"Quick": (lambda: print("Quick Attack")), "Slow": (lambda: print("Slow Attack")),
          "Painful": (lambda: print("Painful Attack")), "Brain": (lambda: print("Brain Attack")),
          "Boring": (lambda: print("Boring Attack"))}

attackKey = random.choice(list(attack.keys()))

print(attack[attackKey]())
