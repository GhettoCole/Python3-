# Tuples are mutable

my_tuple = (1, 2, 3, 4, 5)
print("1st value in tuple: ", my_tuple[0])
print("1st to the 3rd: ", my_tuple[0:3])  # slicing
print("Tuple length: ", len(my_tuple))
moreFibs = my_tuple + (13, 21, 34)
print("34 in tuple: ", 34 in moreFibs)
for i in moreFibs:
    print("number: ", i)

alist = [56, 65, 67, 98, 99, 0]
atuple = tuple(alist)
alist = list(atuple)

print('Min; ', min(atuple))
print('Max; ', max(atuple))