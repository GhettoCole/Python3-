class Sum:
    # Staticmethod
    @staticmethod
    def getcalc(*args):
        calc = 0
        for i in args:
            calc += i

        return calc


def main():
    print("Sum: ", Sum.getcalc(1, 2, 45, 6, 4, 6, ))


main()


class Dog:
    # Class variable
    number_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        Dog.number_of_dogs += 1

    @staticmethod
    def get_number_of_dogs():
        print("There are currently {} dogs".format(Dog.number_of_dogs))


def main():
    spot = Dog("Spot")
    print("Now ", end="")
    spot.get_number_of_dogs()
    doug = Dog("Doug")
    print("Now ", end="")
    doug.get_number_of_dogs()
    spotty = Dog("Spotty")

    spotty.get_number_of_dogs()


main()
