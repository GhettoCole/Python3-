# OOP - Object Orientated Programming
class Dog:
    """
    Self allows a class object to refer to it self
    The other attributes are set to default so that
    the Dog object can be set to default if not set
    to nothing.
    """

    def __init__(self, name="Bossy", height=0, weight=0):
        self.name = name
        self.weight = weight
        self.height = height

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Spotty", 66, 26)

    spot.bark()
    spot.run()
    spot.eat()
    blessie = Dog()
    blessie.bark()


main()
