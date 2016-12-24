class Time:
    """
    Initialise the parameters and make
    magic methods for the parameters passed in
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Defining a magic method
    # A magic method that returns a string
    def __str__(self):
        # Making sure the {:02d} returns a zero before each value
        # even if it is a single value, zero will be passed in first
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    # A magic method that represents the functionality of +
    def __add__(self, other_time):
        new_time = Time()  # the variable is set as a class

        # Add seconds and correct if the sum > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second
        # Add minutes and correct if the sum > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.minute = self.minute - other_time.minute

        # Add hours and correct if the sum > 24
        if (self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time1 = Time(1, 20, 30)
    print(time1)

    time2 = Time(24, 41, 30)
    print(time1 + time2)

    time3 = Time(2, 40, 30)
    print(time3 + time1)
main()


class GiveyG:
    name = "Given"
    age = 17
    address = "Wonderkop 56 revenue"

    def __init__(self, money=0, personality="Lovely", dream="a Programmer"):
        self.money = money
        self.personality = personality
        self.dream = dream

    def __str__(self):
        return "The personality of {} is {} and he has a goal of being a {}".format(self.name, self.personality,
                                                                                    self.dream)


def main():
    given = GiveyG(1000000, "Lovely", "Programmer & Professional Hacker")
    print(given)

main()
