# Instruction
# Create a program that displays a multidimensional table of a multiplication table


print("Activity - 14 (derek banas test)")
print("\nA Multiplication table")

multiplication = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        multiplication[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(multiplication[i][j], end=" ")
    print()