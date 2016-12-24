#  EXAMPLES OF ITERATORS
sample = iter("Sample string")

print("Char: ", next(sample))
print("Char: ", next(sample))
print()
# CUSTOM CLASS ITERATORS 

print("Alphabets: ")
class Alphabet:

        def __init__(self):
                self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                self.index = -1

        def __iter__(self):
                return self

        def __next__(self):
                if self.index >= len(self.letters) - 1:
                        raise StopIteration
                self.index += 1
                return self.letters[self.index]

def main():
        alpha = Alphabet()

        for letter in alpha:
                print(letter)

main()

given = {"First name: ":"Given",
"Last Name: ":"Lepita"}

for key in given:
        print(key, given[key])

class Fibonacci:
        def __init__(self):
                self.first = 0
                self.second = 1

        def __iter__(self):
                return self

        def __next__(self):
                fibonacci = self.first + self.second
                self.first = self.second
                self.second = fibonacci
                return fibonacci

def main():
        fibSeq = Fibonacci()

        for i in range(10):
                print("Fibonacci number: ", next(fibSeq))

main()
