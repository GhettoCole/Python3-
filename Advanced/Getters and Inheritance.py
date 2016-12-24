# Getters & Inheritance


class Animal:  # Create a class
    # Initialize it's parameters and set them to defaults
    def __init__(self, birthType="Unknown", appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # Magic method
    def __str__(self):
        return "A {} is {} it has {} and it is {}".format(type(self).__name__, self.birthType, self.appearance,
                                                          self.blooded)


class Mammal(Animal):
    def __init__(self, birthType="born alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # Overwriting __string
    def __str__(self):
        return super().__str__() + " and it is {} They nurse" \
                                   "their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthType="born in an egg", appearance="pale/dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)


def main():
    unknown = Animal("born alive")
    print(unknown.birthType)

    # print(unknown)

    elephant = Mammal()
    print(elephant)

    reptile = Reptile()

    # can call each attribute print(reptile.birthType)
    print(reptile)


main()
